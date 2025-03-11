# %%
import pandas as pd

df = pd.read_csv('dataset/visual_acuity.csv')
df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns='성별').set_index('연령별')
df_male_left = df_male[df_male.columns[1:8].to_list()]

df_male_left.to_csv('dataset/processed/visual_acuity_left_male.csv')
# %%
df_male_right = df_male[df_male.columns[9:16].to_list()]

df_male_right.to_csv('dataset/processed/visual_acuity_right_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns='성별').set_index('연령별')
df_female_left = df_female[df_female.columns[1:8].to_list()]

df_female_left.to_csv('dataset/processed/visual_acuity_left_female.csv')

# %%
df_female_right = df_female[df_female.columns[9:16].to_list()]

df_female_right.to_csv('dataset/processed/visual_acuity_right_female.csv')

# %%
df = pd.read_csv('dataset/systolic_blood_pressure.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '계']).set_index('연령별')

df_male.to_csv('dataset/processed/systolic_blood_pressure_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '계']).set_index('연령별')

df_female.to_csv('dataset/processed/systolic_blood_pressure_female.csv')

# %%
df = pd.read_csv('dataset/diastolic_blood_pressure.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '계']).set_index('연령별')

df_male.to_csv('dataset/processed/diastolic_blood_pressure_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '계']).set_index('연령별')

df_female.to_csv('dataset/processed/diastolic_blood_pressure_female.csv')

# %%
df = pd.read_csv('dataset/FBG.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '계']).set_index('연령별')
df_male.to_csv('dataset/processed/FBG_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '계']).set_index('연령별')
df_female.to_csv('dataset/processed/FBG_female.csv')

# %%
df = pd.read_csv('dataset/total_cholesterol.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '계']).set_index('연령별')
df_male.to_csv('dataset/processed/total_cholesterol_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '계']).set_index('연령별')
df_female.to_csv('dataset/processed/total_cholesterol_female.csv')

# %%
df = pd.read_csv('dataset/triglyceride.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '계']).set_index('연령별')
df_male.to_csv('dataset/processed/triglyceride_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '계']).set_index('연령별')
df_female.to_csv('dataset/processed/triglyceride_female.csv')

# %%
df = pd.read_csv('dataset/HDL_cholesterol.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '계']).set_index('연령별')
df_male.to_csv('dataset/processed/HDL_cholesterol_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '계']).set_index('연령별')
df_female.to_csv('dataset/processed/HDL_cholesterol_female.csv')

# %%
df = pd.read_csv('dataset/LDL_cholesterol.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '계']).set_index('연령별')
df_male.to_csv('dataset/processed/LDL_cholesterol_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '계']).set_index('연령별')
df_female.to_csv('dataset/processed/LDL_cholesterol_female.csv')

# %%
df = pd.read_csv('dataset/hemoglobin.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '계']).set_index('연령별')
df_male.to_csv('dataset/processed/hemoglobin_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '계']).set_index('연령별')
df_female.to_csv('dataset/processed/hemoglobin_female.csv')

# %%
df = pd.read_csv('dataset/proteinuria.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '계']).set_index('연령별')
df_male.to_csv('dataset/processed/proteinuria_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '계']).set_index('연령별')
df_female.to_csv('dataset/processed/proteinuria_female.csv')

# %%
df = pd.read_csv('dataset/serum_creatinine.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '계']).set_index('연령별')
df_male.to_csv('dataset/processed/serum_creatinine_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '계']).set_index('연령별')
df_female.to_csv('dataset/processed/serum_creatinine_female.csv')

# %%
df = pd.read_csv('dataset/ALT_SGPT.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '계']).set_index('연령별')
df_male.to_csv('dataset/processed/ALT_SGPT_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '계']).set_index('연령별')
df_female.to_csv('dataset/processed/ALT_SGPT_female.csv')

# %%
df = pd.read_csv('dataset/gamma_GTP.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '계']).set_index('연령별')
df_male.to_csv('dataset/processed/gamma_GTP_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '계']).set_index('연령별')
df_female.to_csv('dataset/processed/gamma_GTP_female.csv')

# %%
df = pd.read_csv('dataset/e-cigarette_frequency.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '액상형_소계', '궐련형_소계']).set_index('연령별')
df_male.to_csv('dataset/processed/e-cigarette_frequency_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '액상형_소계', '궐련형_소계']).set_index('연령별')
df_female.to_csv('dataset/processed/e-cigarette_frequency_female.csv')

# %%
df = pd.read_csv('dataset/cigarette_frequency.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '평생 총 5갑이상 담배 흡연 여부_소계', '현재 흡연자 하루 평균 흡연량_소계']).set_index('연령별')
df_male.to_csv('dataset/processed/cigarette_frequency_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '평생 총 5갑이상 담배 흡연 여부_소계', '현재 흡연자 하루 평균 흡연량_소계']).set_index('연령별')
df_female.to_csv('dataset/processed/cigarette_frequency_female.csv')

# %%
df = pd.read_csv('dataset/drinking_frequency.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '합계']).set_index('연령별')
df_male.to_csv('dataset/processed/drinking_frequency_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '합계']).set_index('연령별')
df_female.to_csv('dataset/processed/drinking_frequency_female.csv')

# %%
df = pd.read_csv('dataset/normalB_details.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '실인원']).set_index('연령별')
df_male.to_csv('dataset/processed/normalB_details_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '실인원']).set_index('연령별')
df_female.to_csv('dataset/processed/normalB_details_female.csv')

# %%
df = pd.read_csv('dataset/overall.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '소계']).set_index('연령별')
df_male.to_csv('dataset/processed/overall_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '소계']).set_index('연령별')
df_female.to_csv('dataset/processed/overall_female.csv')

# %%
df = pd.read_csv('dataset/disease_details.csv')

df_male = df[df['성별'] == '남자'][df['연령별'] != '계']
df_male = df_male.drop(columns=['성별', '실인원']).set_index('연령별')
df_male.to_csv('dataset/processed/disease_details_male.csv')

# %%
df_female = df[df['성별'] == '여자'][df['연령별'] != '계']
df_female = df_female.drop(columns=['성별', '실인원']).set_index('연령별')
df_female.to_csv('dataset/processed/disease_details_female.csv')

# %%
import pandas as pd

df = pd.read_csv('../dataset/NHIS_OPEN_GJ_2017_100.csv')

df['비만여부'] = (df['체중(5Kg단위)'] / df['신장(5Cm단위)'].apply(lambda x: pow(x/100, 2))).apply(lambda x: 0 if x < 25 else 1)
df['비만위험여부'] = (df['체중(5Kg단위)'] / df['신장(5Cm단위)'].apply(lambda x: pow(x/100, 2))).apply(lambda x: 0 if x < 23 else 1)

df['고콜레스테롤혈증여부'] = df['총콜레스테롤'].apply(lambda x: 0 if x <= 250 else 1)

df['당뇨여부'] = df['식전혈당(공복혈당)'].apply(lambda x: 0 if x < 126 else 1)
df['당뇨의심여부'] = df['식전혈당(공복혈당)'].apply(lambda x: 0 if x < 100 else 1)

df['고혈압여부'] = ((df['수축기혈압'] >= 140 )| (df['이완기혈압'] >= 90)).apply(lambda x: 1 if x else 0)
df['고혈압의심여부'] = ((df['수축기혈압'] >= 120) | (df['이완기혈압'] >= 80)).apply(lambda x: 1 if x else 0)

df.to_csv('../dataset/NHIS_2017_labeled.csv', index=False)

# %%

from sas7bdat import SAS7BDAT

with SAS7BDAT('../dataset/hn19_all.sas7bdat') as file:
    df = file.to_data_frame()
    
df.to_csv('../dataset/KNHANES_2019.csv', index=False)

# %%
DEFAULT_COLUMNS = [
    'HE_obe', 'HE_HCHOL', 'HE_HTG', 'HE_anem', 'HE_HP', 'HE_DM_HbA1c',

    # 기본 정보
    'sex', 'age', 'age_month', 'occp', 'D_1_1', 'D_2_1', 'D_2_wk',
    # 설문조사들
    # 교육 수준
    'educ', 'graduat', 'EC_pedu_1', 'EC_pedu_2', 'CH2_1', 'CH2_2',
    # 경제활동
    'EC1_1', 'EC_occp', 'EC_stt_1', 'EC_stt_2', 'EC_wht_0', 'EC_wht_23',
    # 식습관
    'LS_VEG1', 'LS_VEG2', 'LS_FRUIT', 'LS_1YR', 'LK_EDU', 'LK_LB_CO', 'LK_LB_US', 'LK_LB_IT', 'LK_LB_EF',
    # 비만 관련
    'BO1', 'BO1_1', 'BO1_2', 'BO1_3', 'BO2_1',
    'BO3_01', 'BO3_02', 'BO3_03', 'BO3_14', 'BO3_05', 'BO3_04', 'BO3_12', 'BO3_07', 'BO3_09', 'BO3_10',
    # 음주 관련
    'BD1', 'BD2', 'BD1_11', 'BD2_1', 'BD2_14', 'BD2_31', 'BD2_32', 'BD7_4',
    'BD7_5', 'BD7_61', 'BD7_62', 'BD7_63', 'BD7_64', 'BD7_65', 'BD7_66', 'dr_month',
    # 수면 관련
    'BP16_1', 'BP16_2', 'BP17_2', 'BP17_3', 'BP17_4',
    # 정신건강 관련
    'mh_PHQ_S', 'mh_GAD_S',
    'BP1', 'BP5', 'BP6_10', 'BP6_2', 'BP6_31', 'BP7', 'mh_stress',
    # 흡연 관련
    'BS1_1', 'BS2_1', 'BS3_1', 'BS3_2', 'BS3_3', 'BS6_2', 'BS6_2_1', 'BS6_2_2', 'BS6_3', 'BS6_4', 'BS6_4_1', 'BS6_4_2',
    'BS12_37', 'BS12_47', 'BS12_47_1', 'BS12_47_2', 'BS12_1', 'BS12_2',
    'BS12_31', 'BS12_32', 'BS12_33', 'BS12_34', 'BS12_35', 'BS12_36', 'BS12_41', 'BS12_42', 'BS12_43', 'BS12_44', 'BS12_45', 'BS12_46',
    'BS5_4', 'BS5', 'BS5_1', 'BS5_21', 'BS5_28', 'BS5_26', 'BS5_33', 'BS5_34', 'BS5_32', 'BS5_29', 'BS5_30',
    'BS8_2', 'BS9_2', 'BS13', 'BS10_1', 'BS2', 'BS10_2', 'BS10_3', 'sm_presnt',
    # 신체활동
    'BE3_71', 'BE3_72', 'BE3_73', 'BE3_74', 'BE3_81', 'BE3_82', 'BE3_83', 'BE3_84',
    'BE3_91', 'BE3_92', 'BE3_93', 'BE3_94', 'BE3_75', 'BE3_76', 'BE3_77', 'BE3_78', 'BE3_85', 'BE3_86', 'BE3_87', 'BE3_88', 'BE8_1', 'BE8_2',
    'BE3_31', 'BE3_32', 'BE3_33', 'BE5_1', 'BE9', 'pa_aerobic',
    
    # 여성 건강
    'LW_ms', 'LW_mp_a', 'LW_ms_a', 'LW_pr', 'LW_pr_1', 'LW_mt', 'LW_mt_a1', 'LW_mt_a2', 'LW_br', 'LW_br_ch', 'LW_br_dur', 'LW_br_yy', 'LW_br_mm', 'LW_oc',
    
    # 검진 기본
    'HE_mens', 'HE_prg', 'HE_dprg',
    
    # 가족력
    'HE_HPfh1', 'HE_HPfh2', 'HE_HPfh3', 'HE_HLfh1', 'HE_HLfh2', 'HE_HLfh3', 'HE_IHDfh1', 'HE_IHDfh2', 'HE_IHDfh3', 'HE_STRfh1', 'HE_STRfh2', 'HE_DMfh1', 'HE_DMfh2', 'HE_DMfh3',
    
    # 신체 계측
    'HE_ht', 'HE_wt'
]



import pandas as pd
import numpy as np

knh_org = pd.read_csv('../dataset/KNHANES.csv')
knh_new = pd.read_csv('../dataset/KNHANES_2019.csv')
        
# df2와 df1의 컬럼 교집합만 선택
common_columns = knh_org.columns.intersection(knh_new.columns)

# df2의 컬럼 중 df1에 없는 컬럼 제거
knh_new = knh_new[common_columns]

# df1에 없는 컬럼을 NaN으로 채워서 df2의 컬럼 정렬
df2 = knh_new.reindex(columns=knh_org.columns, fill_value=np.nan)

# df1과 df2를 concat
result = pd.concat([knh_org, knh_new], ignore_index=True)

result.to_csv('../dataset/KNHANES.csv', index=False)