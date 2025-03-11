from lightgbm import LGBMClassifier
from pandas import DataFrame, Series
from numpy import ndarray
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from plot_utils import plot_auc_curve
from columns import CAT_TYPE
from catboost import CatBoostClassifier


class ClassifierSelector():
    def __init__(
        self, 
        random_state: int = 42,
        config = []
    ):
        self.config=config
        if config[2] == 'lgbm':
            self.model = LGBMClassifier(
                objective='binary',
                is_unbalance=True,
                device='gpu',
                random_state=random_state,
                metric='auc',
                verbose=0
            )
        if config[2] == 'cat':
            self.model = CatBoostClassifier(
            iterations=1000,  # 최대 반복 수
            learning_rate=0.1,  # 학습률
            depth=6,  # 트리 깊이
            loss_function='MultiClass',  # 다중 클래스 분류
            verbose=0  # 출력 주기
        )
        
    def __call__(self, X: DataFrame | ndarray, y: Series):
        if isinstance(X, DataFrame):
            self.columns = X.columns
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.fit(X_train, y_train)
        return self.test(X_test, y_test)

    def fit(self, X: ndarray, y: ndarray):
        cat_features = list(set(X.columns) & set(CAT_TYPE))
        if isinstance(self.model, CatBoostClassifier):
            self.model.fit(X, y, cat_features=cat_features)
        else:
            self.model.fit(X, y)

    def test(self, X: ndarray, y: ndarray, plot_auc=True):
        y_pred = self.model.predict(X)
        accuracy = accuracy_score(y, y_pred)
        report = classification_report(y, y_pred, output_dict=True)

        if plot_auc:
            # 테스트 데이터에 대해 예측 확률
            y_pred_prob = self.model.predict_proba(X)[:, 1]  # 양성 클래스 확률
            plot_auc_curve(y_pred_prob, y, config=self.config)
        
        return report, accuracy