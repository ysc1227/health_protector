import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
[fm.FontProperties(fname=font).get_name() for font in font_list if 'Nanum' in font]
\
import matplotlib.pyplot as plt
plt.rc('font', family='NanumGothicCoding')
\
import matplotlib as mpl
mpl.rcParams['axes.unicode_minus'] = False

def plot_height():
    df = pd.read_csv('dataset/height_adult.csv')
    
    df.plot(kind='bar', x='나이', y=['남자', '여자'])
    plt.xlabel('연령별', fontsize=14)
    plt.ylabel('신장', fontsize=14)
    plt.title('연령별 신장 분포', fontsize=16)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.savefig("plot/height_age.png")
    
def plot_weight():
    df = pd.read_csv('dataset/weight_adult.csv')
    
    df.plot(kind='bar', x='나이', y=['남자', '여자'])
    plt.xlabel('연령별', fontsize=14)
    plt.ylabel('몸무게', fontsize=14)
    plt.title('연령별 몸무게 분포', fontsize=16)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.savefig("plot/weight_age.png")
    
def plot_waist_circumference():
    df = pd.read_csv('dataset/waist_circumference.csv')
    df_m = df[df['연령별'] != '계'][df['성별'] == '남자'].T.reset_index()
    df_m.columns = df_m.iloc[0]
    df_m = df_m.drop(df.index[0:3])
    df_m = df_m.rename(columns={'연령별': "구간"})
    df_f = df[df['연령별'] != '계'][df['성별'] == '여자'].reset_index(drop=True)
    print(df_m)
    for k in ['19세 이하', '20 ~ 24세', '25 ~ 29세', '30 ~ 34세', '35 ~ 39세',
       '40 ~ 44세', '45 ~ 49세', '50 ~ 54세', '55 ~ 59세', '60 ~ 64세', '65 ~ 69세',
       '70 ~ 74세', '75 ~ 79세', '80 ~ 84세', '85세 이상']:
        
        df_m.plot(kind='bar', x='구간', y=[k])
        plt.xlabel('연령별', fontsize=14)
        plt.ylabel('허리둘레', fontsize=14)
        plt.title('연령별 허리둘레 분포', fontsize=16)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        plt.savefig(f"plot/waist_circumference/waist_circumference_{k}.png")

if __name__ == "__main__":
    # plot_height()
    # plot_weight()
    plot_waist_circumference()
    
# %%
import pandas as pd

df = pd.read_csv('output.csv')
for i in df.columns:
    print(i)
    
columns = [
    'ID', 'ID_fam',
    'DI1_pr', 'DI2_pr', 'DE1_pr', 'DN1_ag',
    'BD1', 'BD1_11',
    'BS1_1', 'BS3_1',
    'HE_ht', 'HE_wt', 'HE_BMI', 'HE_obe',
    'HE_sbp', 'HE_dbp', 'HE_HP',
    'HE_glu', 'HE_HbA1c', 'HE_DM_HbA1c',
    'HE_chol', 'HE_HDL_st2', 'HE_TG', 'HE_LDL_drct', 'HE_HCHOL', 'HE_HTG',
    'HE_ast', 'HE_alt', 'HE_hepaB', 'HE_hepaC',
    'HE_HB', 'HE_HCT', 'HE_anem',
    'HE_BUN', 'HE_crea',
    'HE_WBC', 'HE_RBC', 'HE_Bplt', 'HE_hsCRP', 'HE_Uacid',
    'HE_Uph', 'HE_Unitr', 'HE_Usg', 'HE_Upro', 'HE_Uglu', 'HE_Uket', 'HE_Ubil',
    'HE_Ubld', 'HE_Uro', 'HE_Ucrea', 'HE_UNa', 'HE_Ualb', 'HE_Ukal',
    'E_Cr_m', 'E_Cl_m', 'E_Cr_1', 'E_Cl_1'
]
    
df['HE_ht'][df['HE_ht'] != ' '].to_numpy(dtype='float32')