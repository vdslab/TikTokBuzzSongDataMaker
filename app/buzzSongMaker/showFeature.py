import sys
from pathlib import Path
# parent_file_path = str(Path('__file__').resolve().parent.parent)
# sys.path.append(parent_file_path)

from random import random
from classifier.analysis.randomForest import get_random_forest_importance, random_forest_classifier_maker
from classifier.analysis.logistic import get_logistic_importance
from collections import Counter
from common import MUSIC_FEATURE


# THINK:結局どうしよう

# TODO:正規化してたす
def get_show_feature():
    show_feature = []
    feature_count = Counter()
    importance_len = 4
    random_forest_importance = get_random_forest_importance()
    logistic_importance = get_logistic_importance()
    # print(random_forest_importance)
    # print(logistic_importance)
    while len(show_feature) < len(MUSIC_FEATURE):
        random_forest_importance_top = random_forest_importance[:importance_len]
        logistic_importance_top = logistic_importance[:importance_len]
        for i in range(importance_len):
            feature_count[random_forest_importance_top[i][0]] += 1
            feature_count[logistic_importance_top[i][0]] += 1
        for feature in feature_count:
            if feature_count[feature] == 2:
                show_feature.append(feature)
        importance_len += 1
        print("---------------------")
        print(random_forest_importance_top)
        print()
        print(logistic_importance_top)
        print()
        print(show_feature)

    return show_feature


get_show_feature()
