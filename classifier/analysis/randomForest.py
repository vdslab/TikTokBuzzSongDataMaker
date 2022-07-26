from sklearn.metrics import mean_squared_error  # RMSE
from sklearn.metrics import r2_score            # 決定係数
from sklearn.ensemble import RandomForestClassifier
import pickle
from .formated import format_data
import pandas as pd
from .common import MUSIC_FEATURE


# RandomForestの分類器を作る
def random_forest_classifier_maker(data):
    df = format_data(data)

    X = df.loc[:, MUSIC_FEATURE].values
    y = df["rank"]

    # ランダムフォレスト回帰
    forest = RandomForestClassifier(random_state=1234)
    # モデル学習
    forest.fit(X, y)

    # 学習モデルの保存(path：classifierMaker.pyの所からの相対パス)
    with open('./classifier/analysis/models/randomForestModel.pickle', mode='wb') as f:
        pickle.dump(forest, f, protocol=2)

    """
    # 推論
    y_train_pred = forest.predict(X)

    # 平均平方二乗誤差(RMSE)
    print('RMSE 学習: %.2f' % (
        mean_squared_error(y, y_train_pred, squared=False)  # 学習
    ))
    # 決定係数(R^2)
    print('R^2 学習: %.2f' % (
        r2_score(y, y_train_pred)  # 学習
    ))

    # Feature Importance
    fti = forest.feature_importances_
    print(fti)
    """


# 実際にRandomForestで分類する
# THINK:現状引数にリストを渡さないといけないので、オブジェクト1つでもできるように
# サイズ１の[{hogehoge}]が渡されてくることを想定
def classify_data_by_random_forest(data):
    # モデルのオープン
    with open('./classifier/analysis/models/randomForestModel.pickle', mode='rb') as f:
        forest = pickle.load(f)

    df = pd.DataFrame(data)

    X = df.loc[:, MUSIC_FEATURE].values

    result = forest.predict(X)

    if result[0]:
        return 1
    else:
        return 0
