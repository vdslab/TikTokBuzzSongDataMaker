from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from .formated import format_data
import pickle
import pandas as pd
from .common import ALL_FEATRUE, MUSIC_FEATURE


def logistic_classifier_maker(data):

    df = format_data(data)

    # TODO:関数か
    # 標準化インスタンス (平均=0, 標準偏差=1)
    standard_sc = StandardScaler()

    # 01じゃないものを標準化
    X = df.loc[:, ALL_FEATRUE]
    X = standard_sc.fit_transform(X)

    # 標準化後のデータ出力
    df.loc[:, ALL_FEATRUE] = X

    # 説明変数
    X = df[MUSIC_FEATURE]

    # 目的変数
    y = df["rank"]

    # ロジスティック回帰のインスタンス
    model = LogisticRegression(penalty='l2',          # 正則化項(L1正則化 or L2正則化が選択可能)
                               dual=False,            # Dual or primal
                               tol=0.0001,            # 計算を停止するための基準値
                               C=1.0,                 # 正則化の強さ
                               fit_intercept=True,    # バイアス項の計算要否
                               intercept_scaling=1,   # solver=‘liblinear’の際に有効なスケーリング基準値
                               class_weight=None,     # クラスに付与された重み
                               random_state=None,     # 乱数シード
                               solver='lbfgs',        # ハイパーパラメータ探索アルゴリズム
                               max_iter=100,          # 最大イテレーション数
                               multi_class='auto',    # クラスラベルの分類問題（2値問題の場合'auto'を指定）
                               verbose=0,             # liblinearおよびlbfgsがsolverに指定されている場合、冗長性のためにverboseを任意の正の数に設定
                               warm_start=False,      # Trueの場合、モデル学習の初期化に前の呼出情報を利用
                               n_jobs=None,           # 学習時に並列して動かすスレッドの数
                               # L1/L2正則化比率(penaltyでElastic Netを指定した場合のみ)
                               l1_ratio=None
                               )

    # モデル学習
    model.fit(X, y)

    # 学習モデルの保存(path：classifierMaker.pyの所からの相対パス)
    with open('./classifier/analysis/models/logistic.pickle', mode='wb') as f:
        pickle.dump(model, f, protocol=2)

    """
    #結果の出力
    df_model = pd.DataFrame(
        index=["tempo", "danceability", "energy", "mode", "loudness", "acousticness", "speechiness", "instrumentalness", "liveness", "key", "valence", "duration_ms", "time_signature", "total_rhyme_score", "total_positive_score"])

    df_model["偏回帰係数"] = model.coef_[0]

    print("intercept: ", model.intercept_)
    """


# TODO:現状引数にリストを渡さないといけないので、オブジェクト1つでもできるように
# サイズ１の[{hogehoge}]が渡されてくることを想定
def classify_data_by_logistic(data):
    # モデルのオープン
    with open('./classifier/analysis/models/logistic.pickle', mode='rb') as f:
        model = pickle.load(f)

    df = pd.DataFrame(data)

    # 標準化インスタンス (平均=0, 標準偏差=1)
    standard_sc = StandardScaler()

    # 01じゃないものを標準化
    X = df.loc[:, ALL_FEATRUE]
    X = standard_sc.fit_transform(X)

    # 標準化後のデータ出力
    df.loc[:, ALL_FEATRUE] = X

    # 説明変数
    X = df[MUSIC_FEATURE]

    result = model.predict(X)

    if result[0]:
        return 1
    else:
        return 0
