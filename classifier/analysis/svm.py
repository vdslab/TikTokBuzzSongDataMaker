from analysis.formated import format_data
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from analysis.formated import format_data
import pickle


def svm_classifier_maker(data):
    df = format_data(data)

    # TODO:関数化
    # 標準化インスタンス (平均=0, 標準偏差=1)
    standard_sc = StandardScaler()

    # 01じゃないものを標準化
    X = df.loc[:, ["tempo", "danceability", "energy", "mode", "loudness", "acousticness", "speechiness", "instrumentalness",
                   "liveness", "key", "valence", "duration_ms", "time_signature", "total_rhyme_score", "total_positive_score"]]
    X = standard_sc.fit_transform(X)

    # 標準化後のデータ出力
    df.loc[:, ["tempo", "danceability", "energy", "mode", "loudness", "acousticness", "speechiness", "instrumentalness",
               "liveness", "key", "valence", "duration_ms", "time_signature", "total_rhyme_score", "total_positive_score"]] = X

    # 説明変数
    X = df[["tempo", "danceability", "energy", "mode", "loudness", "acousticness", "speechiness", "instrumentalness",
            "liveness", "key", "valence", "duration_ms", "time_signature", "total_rhyme_score", "total_positive_score"]]

    # 目的変数
    y = df["rank"]

    model = SVC(kernel='linear', random_state=None)
    model.fit(X, y)

    # 学習モデルの保存(path：classifierMaker.pyの所からの相対パス)
    with open('./analysis/models/svm.pickle', mode='wb') as f:
        pickle.dump(model, f, protocol=2)

    """
    # 出力
    y_train_pred = model.predict(X)
    accuracy_train = accuracy_score(y, y_train_pred)
    print('トレーニングデータに対する正解率： %.2f' % accuracy_train)
    """


# TODO:現状引数にリストを渡さないといけないので、オブジェクト1つでもできるように
# サイズ１の[{hogehoge}]が渡されてくることを想定
def classify_data_by_svm(data):
    # モデルのオープン
    with open('./analysis/models/svm.pickle', mode='rb') as f:
        model = pickle.load(f)

    df = format_data(data)

    # 標準化インスタンス (平均=0, 標準偏差=1)
    standard_sc = StandardScaler()

    # 01じゃないものを標準化
    X = df.loc[:, ["tempo", "danceability", "energy", "mode", "loudness", "acousticness", "speechiness", "instrumentalness",
                   "liveness", "key", "valence", "duration_ms", "time_signature", "total_rhyme_score", "total_positive_score"]]
    X = standard_sc.fit_transform(X)

    # 標準化後のデータ出力
    df.loc[:, ["tempo", "danceability", "energy", "mode", "loudness", "acousticness", "speechiness", "instrumentalness",
               "liveness", "key", "valence", "duration_ms", "time_signature", "total_rhyme_score", "total_positive_score"]] = X

    # 説明変数
    X = df[["tempo", "danceability", "energy", "mode", "loudness", "acousticness", "speechiness", "instrumentalness",
            "liveness", "key", "valence", "duration_ms", "time_signature", "total_rhyme_score", "total_positive_score"]]

    result = model.predict(X)

    if result[0]:
        return 1
    else:
        return 0
