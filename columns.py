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
    'BO3_01', 'BO3_02', 'BO3_03', 'BO3_14', 'BO3_05', 'BO3_04', 'BO3_12', 'BO3_07', 'BO3_09',
    # 음주 관련
    'BD1', 'BD2', 'BD1_11', 'BD2_1', 'BD2_14', 'BD2_31', 'BD2_32', 'BD7_4',
    'BD7_5', 'BD7_61', 'BD7_62', 'BD7_63', 'BD7_64', 'BD7_65', 'BD7_66', 'dr_month',
    # 수면 관련
    'BP16_1', 'BP16_2', 'BP17_2', 'BP17_3', 'BP17_4',
    
    # 정신건강 관련
    'BP1', 'BP5', 'BP6_10', 'BP6_2', 'BP6_31', 'BP7', 'mh_stress',
    # 흡연 관련
    'BS1_1', 'BS2_1', 'BS3_1', 'BS3_2', 'BS3_3', 'BS6_2', 'BS6_2_1', 'BS6_2_2', 'BS6_3', 'BS6_4', 'BS6_4_1', 'BS6_4_2',
    'BS12_37', 'BS12_47', 'BS12_47_1', 'BS12_47_2', 'BS12_1', 'BS12_2',
    'BS12_31', 'BS12_32', 'BS12_33', 'BS12_34', 'BS12_36', 'BS12_41', 'BS12_42', 'BS12_43', 'BS12_44', 'BS12_46',
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
    'HE_ht', 'HE_wt',
    
    # 건강검진 수치들
    'HE_HDL_st2', 'HE_LDL_drct', 'HE_wc',
    'HE_Upro', 'HE_crea', 'HE_ast', 'HE_alt'
]
FEATURE_LIST = [
    # 기본 정보
    'sex', 'age', 'occp', 'D_1_1', 'D_2_1', 'D_2_wk',
    # 신체 계측
    'HE_ht', 'HE_wt',
    # 검진 기본
    'HE_mens', 'HE_prg',
    # 식습관 관련
    'LS_VEG1', 'LS_VEG2', 'LS_FRUIT', 'LS_1YR', 'LK_EDU', 'LK_LB_CO', 'LK_LB_US', 'LK_LB_IT', 'LK_LB_EF',
    # 비만 관련
    'BO1', 'BO1_1', 'BO1_2', 'BO1_3', 'BO2_1',
    'BO3_01', 'BO3_02', 'BO3_03', 'BO3_14', 'BO3_05', 'BO3_04', 'BO3_12', 'BO3_07', 'BO3_09',
    'BD1', 'BD2', 'BD1_11', 'BD2_1', 'BD2_14', 'BD2_31', 'BD2_32', 'BD7_4',
    'BD7_5', 'BD7_61', 'BD7_62', 'BD7_63', 'BD7_64', 'BD7_65', 'BD7_66', 'dr_month',
    # 수면 관련
    'BP16_1', 'BP16_2', 'BP17_2', 'BP17_3', 'BP17_4',
    # 정신건강 관련
    'BP1', 'BP5', 'BP6_10', 'BP6_2', 'BP6_31', 'BP7', 'mh_stress',
    # 신체활동
    'BE3_71', 'BE3_72', 'BE3_73', 'BE3_74', 'BE3_81', 'BE3_82', 'BE3_83', 'BE3_84',
    'BE3_91', 'BE3_92', 'BE3_93', 'BE3_94', 'BE3_75', 'BE3_76', 'BE3_77', 'BE3_78', 'BE3_85', 'BE3_86', 'BE3_87', 'BE3_88', 'BE8_1', 'BE8_2',
    'BE3_31', 'BE3_32', 'BE3_33', 'BE5_1', 'BE9', 'pa_aerobic'
]
INT_TYPE = [
    'age', 'D_2_wk', 'EC_wht_23', 'BD2_14', 'BP16_1', 'BP16_2',
    'BS2_1', 'BS3_2', 'BS3_3', 'BS6_2', 'BS6_2_1', 'BS6_2_2', 'BS6_3', 'BS6_4', 'BS6_4_1', 'BS6_4_2',
    'BS12_47_1', 'BS12_47_2', 'BS2', 'BS10_2', 'BS10_3', 'BE3_72', 'BE3_73', 'BE3_74', 'BE3_82', 'BE3_83', 'BE3_84',
    'BE3_92', 'BE3_93', 'BE3_94', 'BE3_76', 'BE3_77', 'BE3_78', 'BE3_86', 'BE3_87', 'BE3_88', 'BE8_1', 'BE8_2',
    'BE3_32', 'BE3_33', 'LW_mp_a', 'LW_ms_a', 'LW_pr_1', 'LW_mt_a1', 'LW_mt_a2', 'LW_br_ch', 'LW_br_dur', 
    'LW_br_yy', 'LW_br_mm' 
]   
FLOAT_TYPE = [
    'HE_ht', 'HE_wt', 'HE_HDL_st2', 'HE_LDL_drct', 'HE_wc',
    'HE_Upro', 'HE_crea', 'HE_ast', 'HE_alt'
]
CAT_TYPE = [
    'sex', 'occp', 'D_1_1', 'D_2_1', 'educ', 'graduat', 
    'EC_pedu_1', 'EC_pedu_2', 'CH2_1', 'CH2_2',
    'EC1_1', 'EC_occp', 'EC_stt_1', 'EC_stt_2', 'EC_wht_0',
    'LS_VEG1', 'LS_VEG2', 'LS_FRUIT', 'LS_1YR', 'LK_EDU', 'LK_LB_CO', 'LK_LB_US', 'LK_LB_IT', 'LK_LB_EF',
    'BO1', 'BO1_1', 'BO1_2', 'BO1_3', 'BO2_1',
    'BO3_01', 'BO3_02', 'BO3_03', 'BO3_14', 'BO3_05', 'BO3_04', 'BO3_12', 'BO3_07', 'BO3_09',
    'BD1', 'BD2', 'BD1_11', 'BD2_1', 'BD2_31', 'BD2_32', 'BD7_4',
    'BD7_5', 'BD7_61', 'BD7_62', 'BD7_63', 'BD7_64', 'BD7_65', 'BD7_66', 'dr_month',
    'BP17_2', 'BP17_3', 'BP17_4',
    'BP1', 'BP5', 'BP6_10', 'BP6_2', 'BP6_31', 'BP7', 'mh_stress',
    'BS1_1', 'BS3_1', 'BS12_37', 'BS12_47', 'BS12_1', 'BS12_2',
    'BS12_31', 'BS12_32', 'BS12_33', 'BS12_34', 'BS12_36', 'BS12_41', 'BS12_42', 'BS12_43', 'BS12_44', 'BS12_46',
    'BS5_4', 'BS5', 'BS5_1', 'BS5_21', 'BS5_28', 'BS5_26', 'BS5_33', 'BS5_34', 'BS5_32', 'BS5_29', 'BS5_30',
    'BS8_2', 'BS9_2', 'BS13', 'BS10_1', 'sm_presnt', 'BE3_71', 'BE3_81', 'BE3_91', 'BE3_75', 'BE3_85', 
    'BE3_31', 'BE5_1', 'BE9', 'pa_aerobic', 'LW_ms', 'LW_pr', 'LW_mt', 'LW_br', 'LW_oc', 'HE_mens', 'HE_prg', 
    'HE_HPfh1', 'HE_HPfh2', 'HE_HPfh3', 'HE_HLfh1', 'HE_HLfh2', 'HE_HLfh3', 'HE_IHDfh1', 'HE_IHDfh2', 'HE_IHDfh3', 'HE_STRfh1', 'HE_STRfh2', 'HE_DMfh1', 'HE_DMfh2', 'HE_DMfh3',
]
LABEL = ['HE_obe', 'HE_HCHOL', 'HE_HTG', 'HE_anem', 'HE_HP', 'HE_DM_HbA1c']

INSURANCE_FEATURES = [
    'age', 'sex', 'HE_ht', 'HE_wt',
    'HE_HDL_st2', 'HE_LDL_drct', 'HE_wc',
    'HE_Upro', 'HE_crea', 'HE_ast', 'HE_alt',
    'BS3_1', 'BS12_47', 'BS12_2', 'BD1_11'
]
KEY_FEATURES = ['HE_sbp', 'HE_dbp', 'HE_glu', 'HE_chol']

FEATURE_DICT = {
    'HE_alt': 'ALT 수치\n',
    'BD1_11': '1년간 음주빈도 \n 1. 최근 1년간 전혀 마시지 않았다 \n 2. 월 1회 미만 \n 3. 월 1회 정도 \n 4. 월 2-4회 \n 5. 주 2-3회 정도 \n 6. 주 4회 이상\n',
    'HE_LDL_drct': 'LDL-콜레스테롤 수치\n',
    'HE_ht': '신장(cm)\n',
    'HE_HDL_st2': 'HDL-콜레스테롤 수치\n',
    'HE_wt': '체중(kg)\n',
    'HE_crea': '혈중크레아티닌\n',
    'HE_wc': '허리둘레(?)\n',
    'age': '만나이\n',
    'HE_ast': 'AST 수치\n',
    'BE3_31': '1주일간 걷기 일수 \n 1. 전혀 하지 않음 \n 2. 1일 \n 3. 2일 \n 4. 3일 \n 5. 4일 \n 6. 5일 \n 7. 6일 \n 8. 7일 (매일)\n',
    'BD2_1': '한 번에 마시는 음주량 \n 1. 1-2잔 \n 2. 3-4잔 \n 3. 5-6잔 \n 4. 7-9잔 \n 5. 10잔 이상 \n 0. 마시지 않음\n' ,
    'BE8_1': '평소 하루 앉아서 보내는 시간 (시간)\n',
    "BD2": '음주 시작 연령 (만나이)\n',
    'BP5': '2주 이상 연속 우울감 여부 \n 1. 예 \n 2. 아니오 \n 0. 잘 모르겠음\n',
    'BP16_1': '주중(또는 일하는 날) 하루 평균 수면 시간 (시간)\n',
    'BP16_2': '주말(또는 일하지 않는 날, 일하지 않는 날 전날) 하루 평균 수면 시간 (시간)\n',
    'BO3_01': '운동을 통해 체중조절을 하고 있음 \n 0. 아니오 \n 1. 예\n',
    'BO3_14': '결식을 통해 체중조절을 하고 있음 \n 0. 아니오 \n 1. 예\n',
    'BO3_09': '원푸드다이어트 방식의 체중조절을 하고 있음 \n 0. 아니오 \n 1. 예\n',
    'BO3_12': '한약복용을 통해 체중조절을 하고 있음 \n 0. 아니오 \n 1. 예\n',
    'BO3_04': '처방받은 체중 감량제를 이용하여 체중조절을 하고 있음 \n 0. 아니오 \n 1. 예\n',
    'occp': '다음 중 어느 직종에 종사하고 있습니까? \n 1. 관리자, 전문가 및 관련 종사자 \n 2. 사무종사자 \n 3. 서비스 및 판매 종사자 \n 4. 농림어업 숙련 종사자 \n 5. 기능원, 장치, 기계조작 및 조립 종사자 \n 6. 단순노무종사자 \n 7. 무직(주부, 학생 등) \n',
    'sex': '성별 \n 1.남 2.여\n',
    'LS_FRUIT': '최근 1년 동안 평균 과일류 섭취 빈도 \n 1. 하루 3회 이상 \n 2. 하루 2회 \n 3. 하루 1회 \n 4. 주 5-6회 \n 5. 주 2-4회 \n 6. 주 1회 \n 7. 월 2-3회 \n 8. 월 1회 \n 9. 거의 먹지 않는다(월 1회 미만) \n 0. 잘 모르겠음\n',

}

LABEL_DICT = {
    'HE_obe': '비만',
    'HE_HP': '고혈압',
    'HE_HCHOL': '고콜레스테롤 혈증',
    'HE_HTG': '고지혈증',
    'HE_anem': '빈혈',
    'HE_DM_HbA1c': '당뇨'
}

CAT_LIST = {
    'BD1_11': [1, 2, 3, 4, 5, 6],
    'BE3_31': [1, 2, 3, 4, 5, 6, 7, 8],
    'BD2_1': [1, 2, 3, 4, 5, 0],
    'BO3_01': [0, 1],
    'BO3_14': [0, 1],
    'BO3_09': [0, 1],
    'BO3_12': [0, 1],
    'BO3_04': [0, 1],
    'BP5': [0, 1, 2,],
    'occp': [1, 2, 3, 4, 5, 6, 7],
    'BD2': [i for i in range(81)],
    'sex': [1, 2],
    'LS_FRUIT': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
}