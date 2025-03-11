import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve, auc


def plot_cross_validation(rfecv, config):
    mean_test_scores = rfecv.cv_results_['mean_test_score']
    std_test_scores = rfecv.cv_results_['std_test_score']

    # 시각화
    plt.figure(figsize=(10, 6))
    plt.title("Feature Selection with RFECV", fontsize=16)
    plt.xlabel("Number of features selected", fontsize=12)
    plt.ylabel("Cross-validation score (accuracy)", fontsize=12)

    # 평균 점수와 표준 편차 시각화
    plt.plot(range(1, len(mean_test_scores) + 1), mean_test_scores, marker='o', label='Mean CV Score')
    plt.fill_between(
        range(1, len(mean_test_scores) + 1),
        mean_test_scores - std_test_scores,
        mean_test_scores + std_test_scores,
        color='lightblue', alpha=0.5, label='± 1 Std Dev'
    )
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig(f'figure/{"insurance" if config[3] else "survey"}/{config[2]}/{config[1]}/{config[0]}/RFECV_cross_validation.png')
    plt.close()

def plot_feature_importances(rfecv, config, feature_list, max_features=10):
    # 최종 선택된 특징의 중요도
    feature_importances = rfecv.estimator_.feature_importances_
    
    # 선택된 특징의 원래 인덱스
    indexes = np.where(rfecv.support_)[0]

    selected_features = [feature_list[i] for i in indexes]
    
    top_indices = np.argsort(feature_importances)[::-1][:max_features]
    top_features = [selected_features[i] for i in top_indices]
    top_importances = feature_importances[top_indices]

    # 시각화
    plt.figure(figsize=(12, 6))
    plt.bar(range(len(top_importances)), top_importances, color='skyblue')
    plt.xticks(range(len(top_features)), top_features, rotation=45)
    plt.title("Feature Importance of Selected Features", fontsize=16)
    plt.xlabel("Feature Index", fontsize=12)
    plt.ylabel("Importance", fontsize=12)
    plt.grid()
    plt.tight_layout()
    plt.savefig(f'figure/{"insurance" if config[3] else "survey"}/{config[2]}/{config[1]}/{config[0]}/RFECV_feature_importance.png')
    plt.close()

def plot_auc_curve(y_pred_prob, y_test, config):
    # ROC 커브 계산
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
    roc_auc = auc(fpr, tpr)
    
    # ROC 커브 그리기
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='blue', label=f'ROC curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')
    # 저장 및 출력
    plt.tight_layout()
    plt.savefig(f'figure/{"insurance" if config[3] else "survey"}/{config[2]}/{config[1]}/{config[0]}/AUC_curve.png')
    plt.close()

    return roc_auc

def create_folder(config):
    # 파일 경로가 존재하면 기존 데이터를 읽어옴
    if not os.path.exists(f'figure/{"insurance" if config[3] else "survey"}/{config[2]}/{config[1]}/{config[0]}'):
        os.makedirs(f'figure/{"insurance" if config[3] else "survey"}/{config[2]}/{config[1]}/{config[0]}')
        
    if not os.path.exists(f'checkpoints/{"insurance" if config[3] else "survey"}/{config[2]}/{config[1]}'):
        os.makedirs(f'checkpoints/{"insurance" if config[3] else "survey"}/{config[2]}/{config[1]}')
    
    if not os.path.exists(f'rfecv/{"insurance" if config[3] else "survey"}/{config[2]}/{config[1]}'):
        os.makedirs(f'rfecv/{"insurance" if config[3] else "survey"}/{config[2]}/{config[1]}')
        
    if not os.path.exists(f'result'):
        os.makedirs(f'result')