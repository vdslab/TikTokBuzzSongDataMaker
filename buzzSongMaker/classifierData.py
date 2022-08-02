import sys
from pathlib import Path
parent_file_path = str(Path('__file__').resolve().parent)
sys.path.append(parent_file_path)

from classifier.analysis.logistic import classify_data_by_logistic
from classifier.analysis.randomForest import classify_data_by_random_forest
from classifier.analysis.svm import classify_data_by_svm
import math
from common import MUSIC_FEATURE


# TODO:このデータの整形をなしの形でapiからとってきたい
def formatData(data):
    music_feature_key = MUSIC_FEATURE
    s_data = []
    for d in data:
        obj = dict()
        obj["origin_data"] = d
        if d.get("music_feature"):
            for key in music_feature_key:
                obj[key] = d["music_feature"][key]
        else:
            continue
        # THINK:歌詞データがないのを省くでいいのかどうか（現状は省いている）
        # if d.get("lyrics_feature"):
        #     if d["lyrics_feature"]["total_rhyme_score"] is None:
        #         continue
        #     else:
        #         obj["total_rhyme_score"] = d["lyrics_feature"]["total_rhyme_score"]
        #     if d["lyrics_feature"]["total_positive_score"] is None:
        #         continue
        #     else:
        #         obj["total_positive_score"] = d["lyrics_feature"]["total_positive_score"]
        # else:
        #     continue
        s_data.append(obj)
    return s_data


def classifier_data(data):
    formated_data_for_classifier = formatData(data)
    classifiered_data = []
    for d in formated_data_for_classifier:
        logistic_result = classify_data_by_logistic([d])
        random_forest_resutl = classify_data_by_random_forest([d])
        svm_resutl = classify_data_by_svm([d])
        score = math.floor(
            (logistic_result + random_forest_resutl + svm_resutl)/3*100)
        if score > 0:
            d["rank"] = str(score)
            obj = d["origin_data"]
            obj["rank"] = str(score)
            classifiered_data.append(obj)
    return classifiered_data
