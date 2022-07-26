from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from .formated import format_data
import pickle
import pandas as pd
from .common import ALL_FEATRUE, MUSIC_FEATURE


def svm_classifier_maker(data):
    df = format_data(data)

    # TODO:関数化
    # 標準化インスタンス (平均=0, 標準偏差=1)
    standard_sc = StandardScaler()

    # 01じゃないものを標準化
    X = df.loc[:, MUSIC_FEATURE]
    X = standard_sc.fit_transform(X)

    # 標準化後のデータ出力
    df.loc[:, MUSIC_FEATURE] = X

    # 説明変数
    X = df[MUSIC_FEATURE]

    # 目的変数
    y = df["rank"]

    model = SVC(kernel='linear', random_state=1234)
    model.fit(X, y)

    # 学習モデルの保存(path：classifierMaker.pyの所からの相対パス)
    with open('./classifier/analysis/models/svm.pickle', mode='wb') as f:
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
    with open('./classifier/analysis/models/svm.pickle', mode='rb') as f:
        model = pickle.load(f)

    df = pd.DataFrame(data)

    # 標準化インスタンス (平均=0, 標準偏差=1)
    standard_sc = StandardScaler()

    # 01じゃないものを標準化
    X = df.loc[:, MUSIC_FEATURE]
    X = standard_sc.fit_transform(X)

    # 標準化後のデータ出力
    df.loc[:, MUSIC_FEATURE] = X

    # 説明変数
    X = df[MUSIC_FEATURE]

    result = model.predict(X)

    if result[0]:
        return 1
    else:
        return 0
