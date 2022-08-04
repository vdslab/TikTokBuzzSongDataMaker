from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from .formated import format_data
import pickle
import pandas as pd
from .common import ALL_FEATRUE, MUSIC_FEATURE
import os

file_path = os.path.dirname(os.path.realpath(__file__))


def logistic_classifier_maker(data):

    df = format_data(data)

    # HACK
    # 標準化インスタンス (平均=0, 標準偏差=1)
    standard_sc = StandardScaler()

    # 01じゃないものを標準化
    X = df.loc[:, MUSIC_FEATURE]
    standard_sc.fit(X)
    X = standard_sc.transform(X)

    # 標準化後のデータ出力
    df.loc[:, MUSIC_FEATURE] = X

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
                               random_state=1234,     # 乱数シード
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
    with open(file_path+'/models/logistic.pickle', mode='wb') as f:
        pickle.dump(model, f, protocol=2)

    # 標準化関数の保存
    pickle.dump(standard_sc, open(
        file_path+"/models/logistic_sc.p", "wb"))

    # 結果の出力
    """
    df_model = pd.DataFrame(
        index=MUSIC_FEATURE)

    df_model["偏回帰係数"] = model.coef_[0]
    print(df_model)

    Y_pred = model.predict(X)
    print('confusion matrix = \n', confusion_matrix(y_true=y, y_pred=Y_pred))
    print('accuracy = ', accuracy_score(y_true=y, y_pred=Y_pred))
    print('precision = ', precision_score(y_true=y, y_pred=Y_pred))
    print('recall = ', recall_score(y_true=y, y_pred=Y_pred))
    print('f1 score = ', f1_score(y_true=y, y_pred=Y_pred))
    print("intercept: ", model.intercept_)
    """


# THINK:現状引数にリストを渡さないといけないので、オブジェクト1つでもできるように
# サイズ１の[{hogehoge}]が渡されてくることを想定
def classify_data_by_logistic(data):
    # モデルのオープン
    # with open('./models/logistic.pickle', mode='rb') as f:
    with open(file_path+'/models/logistic.pickle', mode='rb') as f:
        model = pickle.load(f)

    # 標準化インスタンス (平均=0, 標準偏差=1)
    standard_sc = pickle.load(
        open(file_path+'/models/logistic_sc.p', "rb"))

    df = pd.DataFrame(data)

    # 01じゃないものを標準化
    X = df.loc[:, MUSIC_FEATURE]
    X = standard_sc.transform(X)

    # 標準化後のデータ出力
    df.loc[:, MUSIC_FEATURE] = X

    # 説明変数
    X = df[MUSIC_FEATURE]

    result = model.predict(X)

    if result[0]:
        return 1
    else:
        return 0


def get_logistic_importance():
    with open(file_path+'/models/logistic.pickle', mode='rb') as f:
        model = pickle.load(f)

    fti = model.coef_[0]

    importance_abs_dic = dict()
    for i in range(len(fti)):
        importance_abs_dic[MUSIC_FEATURE[i]] = abs(fti[i])
    importance_abs_dic = sorted(
        importance_abs_dic.items(), key=lambda x: x[1], reverse=True)

    return importance_abs_dic
