
import joblib
import pandas as pd
from columns import FEATURE_LIST, INSURANCE_FEATURES, LABEL, FEATURE_DICT, INT_TYPE, FLOAT_TYPE, CAT_LIST, LABEL_DICT
import torch
import argparse
from dataset import Dataset


torch.set_float32_matmul_precision('high')

def main(args):
    ans = input('건강검진 정보를 알고 계신가요? (y/n) ')
    while not (ans == 'n' or ans == 'N' or ans == 'Y' or ans == 'y'):
        ans = input('건강검진 정보를 알고 계신가요? (y/n) ')
    
    isinsurance = False if (ans == 'n' or ans == 'N') else True
    
    model_maps = {}
    input_features = set()
    for target in LABEL:
        model_maps[target] = {
            'strong': joblib.load(f'checkpoints/{"insurance" if isinsurance else "survey"}/{args.model}/strong/{target}.joblib'),
            'week': joblib.load(f'checkpoints/{"insurance" if isinsurance else "survey"}/{args.model}/week/{target}.joblib')
        }
        if args.model == "cat":
            input_features = input_features | set(model_maps[target]['strong'].feature_names_) | set(model_maps[target]['week'].feature_names_) | set(['age', 'sex'])
        if args.model == "lgbm":
            input_features = input_features | set(model_maps[target]['strong'].feature_name_) | set(model_maps[target]['week'].feature_name_) | set(['age', 'sex'])

    input_features = list(input_features)
    

    dataset = Dataset(data_path='dataset/KNHANES.csv')
    
    input_data = pd.DataFrame()
    for i in input_features:
        while True:
            input_data[i] = [input(FEATURE_DICT[i])]
            
            if i in INT_TYPE or i in FLOAT_TYPE:
                try:
                    input_data[i] = [float(input_data[i].iloc[0])]
                    input_data[i] = input_data[i].astype(float)
                    break
                except:
                    print("유효하지 않은 값입니다!")
                    continue
            else:
                try:
                    if int(input_data[i].iloc[0]) in CAT_LIST[i]:
                        input_data[i] = [int(input_data[i].iloc[0])]
                        input_data[i] = input_data[i].astype('category')
                        break
                    else:
                        print("유효하지 않은 값입니다!")
                        continue
                except:
                    print("유효하지 않은 값입니다!")
                    continue
    
    mean_value = {}

    for target in LABEL:
        X, _ = dataset.get_feature_and_label(
            feature_list=(INSURANCE_FEATURES if isinsurance else FEATURE_LIST) + [target],
            label=target,
            preprocess=False,
            clean=False,
            config=[target, 'strong'],
            sampling=False
        )

        strong_columns = None
        week_columns = None
        
        if args.model == 'cat':
            strong_columns = model_maps[target]['strong'].feature_names_
            week_columns = model_maps[target]['week'].feature_names_
        else:
            strong_columns = model_maps[target]['strong'].feature_name_
            week_columns = model_maps[target]['week'].feature_name_
        strong_result = model_maps[target]['strong'].predict_proba(X[strong_columns][(abs(X['age'] - input_data['age'].iloc[0]) < 5) & (X['sex'] == input_data['sex'].iloc[0])])
        week_result = model_maps[target]['week'].predict_proba(X[week_columns][(abs(X['age'] - input_data['age'].iloc[0]) < 5) & (X['sex'] == input_data['sex'].iloc[0])])
        mean_value[target] = (strong_result[:, 1].mean() + week_result[:, 1].mean())/2
    

    strong_result = {}
    week_result = {}
    for target in LABEL:
        strong_columns = None
        week_columns = None
        
        if args.model == 'cat':
            strong_columns = model_maps[target]['strong'].feature_names_
            week_columns = model_maps[target]['week'].feature_names_
        else:
            strong_columns = model_maps[target]['strong'].feature_name_
            week_columns = model_maps[target]['week'].feature_name_
        strong_result[target] = model_maps[target]['strong'].predict_proba(input_data[strong_columns])
        week_result[target] = model_maps[target]['week'].predict_proba(input_data[week_columns])
    
    health_type = {key: '위험' if items.argmax() == 1 else ('주의' if items.argmax() != week_result[key].argmax() else '안전') for (key, items) in strong_result.items()}
    danger_proba = {key: (week_result[key][0][1] + items[0][1])/2 for (key, items) in strong_result.items()}
    
    for key, items in health_type.items():
        print(f"{LABEL_DICT[key]} - 위험도: {items}, 확률: {round(danger_proba[key], 2)}, 평균 대비 발병 위험: {round((danger_proba[key] / mean_value[key]), 2)}배")
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model", choices=['cat', 'lgbm'], help="선택할 모델 - cat(CatBoost)/lgbm(LightGBM)", dest="model", action="store", default='lgbm')
    args = parser.parse_args()
    
    model_type = ['cat', 'lgbm']
    label_list = ['HE_obe', 'HE_HCHOL', 'HE_HTG', 'HE_anem', 'HE_HP', 'HE_DM_HbA1c']
    isinsurance = True
    
    main(args)