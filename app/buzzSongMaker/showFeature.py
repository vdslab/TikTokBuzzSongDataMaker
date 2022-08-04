import sys
from pathlib import Path
from random import random
from classifier.analysis.randomForest import get_random_forest_importance, random_forest_classifier_maker
from classifier.analysis.logistic import get_logistic_importance
from collections import Counter
from common import MUSIC_FEATURE
from sklearn import preprocessing
import json


# TODO:makerの中に組み込む
# THINK:結局どうしよう
def get_show_feature():
    random_forest_importance = get_random_forest_importance()
    logistic_importance = get_logistic_importance()
    random_forest_importance_value = list(random_forest_importance.values())
    logistic_importance_value = list(logistic_importance.values())
    random_forest_importance_value = list(preprocessing.minmax_scale(
        random_forest_importance_value))
    logistic_importance_value = list(preprocessing.minmax_scale(
        logistic_importance_value))

    sum_value = dict()
    for i in range(len(random_forest_importance_value)):
        p = random_forest_importance_value[i]+logistic_importance_value[i]
        sum_value[MUSIC_FEATURE[i]] = p

    sum_value = sorted(
        sum_value.items(), key=lambda x: x[1], reverse=True)

    priority_feature = []
    for i in range(len(sum_value)):
        obj = {sum_value[i][0]: sum_value[i][1]}
        priority_feature.append(obj)

    with open('./data/test/priority_feature.json', 'w', encoding='utf-8') as f:
        json.dump(json.dumps(priority_feature),
                  f, indent=2, ensure_ascii=False)


get_show_feature()
