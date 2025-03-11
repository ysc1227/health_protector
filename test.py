from lightgbm import LGBMClassifier
import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, accuracy_score

cat_type = [
    'sex', 'occp', 'D_1_1', 'D_2_1', 'educ', 'graduat', 
    'EC_pedu_1', 'EC_pedu_2', 'CH2_1', 'CH2_2',
    'EC1_1', 'EC_occp', 'EC_stt_1', 'EC_stt_2', 'EC_wht_0',
    'LS_VEG1', 'LS_VEG2', 'LS_FRUIT', 'LS_1YR', 'LK_EDU', 'LK_LB_CO', 'LK_LB_US', 'LK_LB_IT', 'LK_LB_EF',
    'BO1', 'BO1_1', 'BO1_2', 'BO1_3', 'BO2_1',
    'BO3_01', 'BO3_02', 'BO3_03', 'BO3_14', 'BO3_05', 'BO3_04', 'BO3_12', 'BO3_07', 'BO3_09', 'BO3_10',
    'BD1', 'BD2', 'BD1_11', 'BD2_1', 'BD2_31', 'BD2_32', 'BD7_4',
    'BD7_5', 'BD7_61', 'BD7_62', 'BD7_63', 'BD7_64', 'BD7_65', 'BD7_66', 'dr_month',
    'BP17_2', 'BP17_3', 'BP17_4',
    'BP1', 'BP5', 'BP6_10', 'BP6_2', 'BP6_31', 'BP7', 'mh_stress',
    'BS1_1', 'BS3_1', 'BS12_37', 'BS12_47', 'BS12_1', 'BS12_2',
    'BS12_31', 'BS12_32', 'BS12_33', 'BS12_34', 'BS12_35', 'BS12_36', 'BS12_41', 'BS12_42', 'BS12_43', 'BS12_44', 'BS12_45', 'BS12_46',
    'BS5_4', 'BS5', 'BS5_1', 'BS5_21', 'BS5_28', 'BS5_26', 'BS5_33', 'BS5_34', 'BS5_32', 'BS5_29', 'BS5_30',
    'BS8_2', 'BS9_2', 'BS13', 'BS10_1', 'sm_presnt', 'BE3_71', 'BE3_81', 'BE3_91', 'BE3_75', 'BE3_85', 
    'BE3_31', 'BE5_1', 'BE9', 'pa_aerobic', 'LW_ms', 'LW_pr', 'LW_mt', 'LW_br', 'LW_oc', 'HE_mens', 'HE_prg', 
    'HE_HPfh1', 'HE_HPfh2', 'HE_HPfh3', 'HE_HLfh1', 'HE_HLfh2', 'HE_HLfh3', 'HE_IHDfh1', 'HE_IHDfh2', 'HE_IHDfh3', 'HE_STRfh1', 'HE_STRfh2', 'HE_DMfh1', 'HE_DMfh2', 'HE_DMfh3',
]

data = pd.read_csv('dataset/NHIS_2017_labeled.csv')
model = joblib.load('checkpoints/HE_obe_strong_lgbm.joblib')

X = data[['신장(5Cm단위)', '체중(5Kg단위)']]
y = data['비만여부']

y_pred = model.model.predict(X)
accuracy = accuracy_score(y, y_pred)
report = classification_report(y, y_pred, output_dict=False)

print(f"Accuracy: {accuracy}")
print(f"\nReport: {report}")

"['age', 'occp', 'D_1_1', 'D_2_wk', 'HE_ht', 'HE_wt', 'HE_mens', 'LS_VEG1', 'LS_VEG2', 'LS_FRUIT', 'LS_1YR', 'LK_LB_US', 'LK_LB_IT', 'LK_LB_EF', 'BO1', 'BO1_1', 'BO1_2', 'BO1_3', 'BO2_1', 'BO3_01', 'BO3_03', 'BO3_14', 'BO3_04', 'BO3_07', 'BO3_09', 'BD2', 'BD1_11', 'BD2_1', 'BD2_14', 'BD2_31', 'BD2_32', 'BD7_4', 'BD7_61', 'dr_month', 'BP16_1', 'BP16_2', 'BP17_2', 'BP17_3', 'BP17_4', 'mh_PHQ_S', 'mh_GAD_S', 'BP1', 'BP7', 'mh_stress', 'BE3_72', 'BE3_74', 'BE3_82', 'BE3_84', 'BE3_92', 'BE3_93', 'BE3_94', 'BE3_76', 'BE3_78', 'BE3_86', 'BE3_87', 'BE3_88', 'BE8_1', 'BE8_2', 'BE3_31', 'BE3_32', 'BE3_33', 'BE5_1', 'pa_aerobic']"
X = data[['연령대코드(5세단위)', '신장(5Cm단위)', '체중(5Kg단위)']]
y = data['고콜레스테롤혈증여부']

model = joblib.load('checkpoints/HE_HCHOL_strong_lgbm.joblib')
X = X.copy()
X['연령대코드(5세단위)'] = X['연령대코드(5세단위)'].apply(lambda x: (x-1) * 5 + 2)

for i in ['occp', 'D_1_1', 'D_2_wk']:
    X.insert(1, i, np.nan)
    if i in cat_type:
        X = X.copy()
        X[i] = X[i].astype('category')

for i in ['HE_mens', 'LS_VEG1', 'LS_VEG2', 'LS_FRUIT', 'LS_1YR', 'LK_LB_US', 'LK_LB_IT', 'LK_LB_EF', 'BO1', 'BO1_1', 'BO1_2', 'BO1_3', 'BO2_1', 'BO3_01', 'BO3_03', 'BO3_14', 'BO3_04', 'BO3_07', 'BO3_09', 'BD2', 'BD1_11', 'BD2_1', 'BD2_14', 'BD2_31', 'BD2_32', 'BD7_4', 'BD7_61', 'dr_month', 'BP16_1', 'BP16_2', 'BP17_2', 'BP17_3', 'BP17_4', 'mh_PHQ_S', 'mh_GAD_S', 'BP1', 'BP7', 'mh_stress', 'BE3_72', 'BE3_74', 'BE3_82', 'BE3_84', 'BE3_92', 'BE3_93', 'BE3_94', 'BE3_76', 'BE3_78', 'BE3_86', 'BE3_87', 'BE3_88', 'BE8_1', 'BE8_2', 'BE3_31', 'BE3_32', 'BE3_33', 'BE5_1', 'pa_aerobic']:
    X.insert(6, i, np.nan)
    if i in cat_type:
        X = X.copy()
        X[i] = X[i].astype('category')

import ipdb
ipdb.set_trace()

y_pred = model.model.predict(X)
accuracy = accuracy_score(y, y_pred)
report = classification_report(y, y_pred, output_dict=False)

print(f"Accuracy: {accuracy}")
print(f"\nReport: {report}")