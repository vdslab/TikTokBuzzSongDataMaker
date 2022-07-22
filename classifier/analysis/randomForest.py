from sklearn.metrics import mean_squared_error  # RMSE
from sklearn.metrics import r2_score            # 決定係数
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle


# tiktokランキングに入っているものが1, その他0
def ranking_convert(x):
    if int(x) <= 20:
        return 1
    else:
        return 0


def format_data(data):
    df = pd.DataFrame(data)
    # ランキングを01で
    df["rank"] = df["rank"].apply(ranking_convert)
    return df


# RandomForestの分類器を作る
def random_forest_classifier_maker(data):
    df = format_data(data)

    X = df.loc[:, ["tempo", "danceability", "energy", "mode", "loudness", "acousticness",
                   "speechiness", "instrumentalness", "liveness", "key", "valence", "duration_ms", "time_signature", "total_rhyme_score", "total_positive_score"]].values
    y = df["rank"]

    # ランダムフォレスト回帰
    forest = RandomForestClassifier()
    # モデル学習
    forest.fit(X, y)

    # 学習モデルの保存(path：classifierMaker.pyの所からの相対パス)
    with open('./analysis/models/randomForestModel.pickle', mode='wb') as f:
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
# TODO:現状引数にリストを渡さないといけないので、オブジェクト1つでもできるように
# サイズ１の[{hogehoge}]が渡されてくることを想定
def classify_data_by_random_forest(data):
    # モデルのオープン
    with open('./analysis/models/randomForestModel.pickle', mode='rb') as f:
        forest = pickle.load(f)

    df = format_data(data)

    X = df.loc[:, ["tempo", "danceability", "energy", "mode", "loudness", "acousticness",
                   "speechiness", "instrumentalness", "liveness", "key", "valence", "duration_ms", "time_signature", "total_rhyme_score", "total_positive_score"]].values

    result = forest.predict(X)

    if result[0]:
        return True
    else:
        return False
