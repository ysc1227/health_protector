
import os
import joblib
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from dataset import Dataset
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
from sklearn.feature_selection import RFECV
import pandas as pd
from classifier import ClassifierSelector
from plot_utils import create_folder, plot_cross_validation, plot_feature_importances
import warnings
from columns import FEATURE_LIST, INSURANCE_FEATURES
import torch


torch.set_float32_matmul_precision('high')

font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
[fm.FontProperties(fname=font).get_name() for font in font_list if 'Nanum' in font]
plt.rc('font', family='NanumGothicCoding')
mpl.rcParams['axes.unicode_minus'] = False
warnings.filterwarnings("ignore", category=UserWarning, message=".*Falling back to prediction using DMatrix.*")

def main(config, file_path):
    print(f'----------타겟 변수: {config[0]}, 선정 강도: {config[1]}, 모델: {config[2]}----------------')
    
    dataset = Dataset(data_path='dataset/KNHANES.csv')
    create_folder(config)
    
    X, y = dataset.get_feature_and_label(
        feature_list=(INSURANCE_FEATURES if config[3] else FEATURE_LIST) + [config[0]],
        label=config[0],
        preprocess=False,
        clean=False,
        config=config
    )
    
    model = ClassifierSelector(config=config)
    
    print(f'\n클래스 개수: {y.value_counts()}')
    
    columns = X.columns
    max_features = 10
    
    if os.path.exists(f'rfecv/{"insurance" if config[3] else "survey"}/{config[2]}/{config[1]}/{config[0]}.pkl'):
        rfecv = joblib.load(f'rfecv/{"insurance" if config[3] else "survey"}/{config[2]}/{config[1]}/{config[0]}.pkl')
    else:
        rfecv = RFECV(estimator=model.model, step=1, cv=5, scoring='accuracy')
        rfecv.fit(X, y)
        joblib.dump(rfecv, f'rfecv/{"insurance" if config[3] else "survey"}/{config[2]}/{config[1]}/{config[0]}.pkl')
    columns = columns[rfecv.support_]
    importance = rfecv.estimator_.feature_importances_
    if len(columns) > max_features:
        columns = columns[(-importance).argsort()]
        columns = columns[:max_features]
        
    columns = columns if isinstance(columns, list) else columns.tolist()

    plot_cross_validation(rfecv, config)
    plot_feature_importances(rfecv, config, INSURANCE_FEATURES if config[3] else FEATURE_LIST, max_features)
    
    print(f'\n선택된 피쳐: {columns}')

    X = X[columns]
    
    report, acc = model(X, y)
    
    # 평가 결과 출력
    print("\nAccuracy: \n\n", acc)

    # pandas DataFrame으로 변환
    report_df = pd.DataFrame(report).transpose()

    result_df = pd.DataFrame({
        'label': [config[0]],
        'strength': [config[1]],
        'model': [config[2]],
        'accuracy': [round(acc, 2)]
    })

    # 각 클래스의 precision, recall, f1-score 추가
    for class_label in report_df.index[:-3]:  # 마지막 'accuracy', 'macro avg', 'weighted avg' 제외
        result_df[f'{class_label}_precision'] = round(report_df.loc[class_label, 'precision'], 2)
        result_df[f'{class_label}_recall'] = round(report_df.loc[class_label, 'recall'], 2)
        result_df[f'{class_label}_f1'] = round(report_df.loc[class_label, 'f1-score'], 2)
    
    if config[2] != 'tabular':
        result_df['features'] = [columns] if isinstance(columns, list) else [columns.tolist()]
    else:
        result_df['features'] = 'all'

    # 파일 경로가 존재하면 기존 데이터를 읽어옴
    if os.path.exists(file_path):
        existing_df = pd.read_csv(file_path)

        # 기존 데이터에 'label', 'strength', 'model' 값이 동일한 행이 있는지 확인
        if not any((existing_df['label'] == config[0]) & 
                (existing_df['strength'] == config[1]) & 
                (existing_df['model'] == config[2])):
            # 중복이 없다면 파일에 추가
            result_df.to_csv(file_path, index=False, mode='a', header=False)
    else:
        # 파일이 없으면 새로 생성
        result_df.to_csv(file_path, index=False, mode='w')

    joblib.dump(model.model, f'checkpoints/{"insurance" if config[3] else "survey"}/{config[2]}/{config[1]}/{config[0]}.joblib')

if __name__ == '__main__':
    inference_strength = ['strong', 'week']
    model_type = ['lgbm']
    label_list = ['HE_obe', 'HE_HCHOL', 'HE_HTG', 'HE_anem', 'HE_HP', 'HE_DM_HbA1c']
    isinsurance = False
    
    for a in label_list:
        for b in inference_strength:
            for c in model_type:
                config = [a, b, c, isinsurance]
                main(config, f'result/{"insurance_lgbm" if isinsurance else "survey_lgbm"}.csv')
    