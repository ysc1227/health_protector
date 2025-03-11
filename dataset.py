import pandas as pd
from sklearn.preprocessing import StandardScaler
from pandas import DataFrame
from numpy import ndarray
import numpy as np
from sklearn.utils import resample
from columns import FLOAT_TYPE, INT_TYPE, CAT_TYPE, DEFAULT_COLUMNS, LABEL
from sklearn.impute import KNNImputer


def getLambda(config):
    funcs = {
        'HE_obe': {'strong': lambda x: 0 if x <=3 else 1, 'week': lambda x: 0 if x <=2 else 1},
        'HE_HCHOL': {'strong': lambda x: x, 'week': lambda x: x},
        'HE_HTG': {'strong': lambda x: x, 'week': lambda x: x},
        'HE_anem': {'strong': lambda x: x, 'week': lambda x: x},
        'HE_HP': {'strong': lambda x: 0 if x <=3 else 1, 'week': lambda x: 0 if x <=1 else 1},
        'HE_DM_HbA1c': {'strong': lambda x: 0 if x <=2 else 1, 'week': lambda x: 0 if x<=1 else 1},
    }
    
    return funcs[config[0]][config[1]]

one_digit = ['BE3_72', 'BE3_82', 'BE3_92', 'BE3_93', 'BE3_94', 'BE3_76', 'BE3_86', ]
two_digit = [
    'D_2_wk', 'BP16_1', 'BP16_2', 'BS3_3', 'BS6_2_1', 
    'BS6_2_2', 'BS6_4_1', 'BS6_4_2', 'BS2', 'BS10_2', 
    'BE3_73', 'BE3_74', 'BE3_83', 'BE3_84', 'BE3_77', 'BE3_78', 
    'BE3_87', 'BE3_88', 'BE8_1', 'BE8_2', 'BE3_32', 'BE3_33', 'LW_mp_a', 'LW_ms_a', 'LW_pr_1', 
    'LW_mt_a1', 'LW_mt_a2', 'LW_br_ch', 'LW_br_yy', 'LW_br_mm', 
]
three_digit = ['EC_wht_23', 'BD2', 'BD2_14', 'BS2_1', 'BS3_2',  'BS6_3', 'BS12_47_1', 'BS10_3', ]
four_digit= ['BS6_2', 'BS6_4', 'BS12_47_2', 'LW_br_dur', ]


class Dataset():
    def __init__(self, data_path: str):
        data = pd.read_csv(data_path, low_memory=False)
        
        data[INT_TYPE] = data[INT_TYPE].replace({' ': np.nan}).astype(float)
        data[FLOAT_TYPE] = data[FLOAT_TYPE].replace({' ': np.nan}).astype(float)
        
        data[one_digit] = data[one_digit].replace({8: 0, 9: np.nan})
        data[two_digit] = data[two_digit].replace({88: 0, 99: np.nan})
        data[three_digit] = data[three_digit].replace({888: 0, 999: np.nan})
        data[four_digit] = data[four_digit].replace({8888: 0, 9999: np.nan})
        
        data[CAT_TYPE] = data[CAT_TYPE].replace({' ': -1, np.nan: -1}).astype(float).astype(int).astype('category')
        
        for col in CAT_TYPE:
            if "NA" not in data[col].cat.categories:
                data[col] = data[col].cat.add_categories(["NA"])
            if 0 not in data[col].cat.categories:
                data[col] = data[col].cat.add_categories([0])

        data[LABEL] = data[LABEL].replace({' ': -1, np.nan: -1}).astype(float).astype(int).astype('category')
        
        self.data = data[DEFAULT_COLUMNS]

        self.scaler = StandardScaler()
        
    def _remove_missing(self, data: DataFrame, label: str) -> DataFrame:
        return data[data[label] != -1].reset_index(drop=True)
    
    def _preprocess(self, X: DataFrame) -> ndarray:
        X = self.scaler.fit_transform(X)
        X = self.pca.fit_transform(X)
        return X
    
    def get_feature_and_label(
        self,                               
        feature_list: list, 
        label: str,
        clean: bool = True,
        preprocess: bool = True,
        config = [],
        sampling = True,
    ):
        
        data = self.data[feature_list]
        data = self._remove_missing(data, label)
        
        if clean:
            int_list = list((set(INT_TYPE) | set(FLOAT_TYPE)) & set(feature_list))
 
            knn_imputer = KNNImputer(n_neighbors=5)
            knn_imputed = knn_imputer.fit_transform(data[int_list])
            
            # DataFrame으로 변환 및 병합
            knn_df = pd.DataFrame(knn_imputed, columns=int_list)

            # 기존 데이터프레임 업데이트
            data.loc[:, knn_df.columns] = knn_df
            
        data[label] = data[label].astype(float).astype(int)
        
        data[label] = data[label].apply(getLambda(config))
        
        if sampling:
            class_counts = data[label].value_counts()
            print("원본 데이터 크기:\n", class_counts)
            
            majority_class = class_counts.idxmax()  # 샘플 수가 가장 많은 클래스
            minority_class = class_counts.idxmin()  # 샘플 수가 가장 적은 클래스
            
            # 클래스별로 데이터 분리
            majority_data = data[data[label] == majority_class]
            minority_data = data[data[label] == minority_class]
            
                    # 다수 클래스(클래스 0)를 소수 클래스(클래스 1) 크기로 샘플링
            majority_data_undersampled = resample(majority_data,
                                            replace=False,  # 복원 샘플링 비활성화
                                            n_samples=len(minority_data),  # 소수 클래스 크기만큼 샘플링
                                            random_state=42)  # 재현성을 위한 랜덤 시드
            
            # 샘플링된 데이터 병합
            data = pd.concat([majority_data_undersampled, minority_data])

            # 언더샘플링된 데이터 크기 확인
            print("\n언더샘플링된 데이터 크기:\n", data[label].value_counts())
        
        X = data.drop(columns=[label])
        if preprocess:
            X = self._preprocess(X)
            
        y = data[label]
        
        self.X = X
        self.y = y
        return X, y