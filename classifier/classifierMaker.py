from api import getAllPastSongs
from analysis.randomForest import random_forest_classifier_maker, classify_data_by_random_forest
# 分類器のアップデート？をする


# TODO:このデータの整形をなしの形でapiからとってきたい
def formatData(data):
    music_feature_key = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                         'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']
    s_data = []
    for d in data:
        obj = dict()
        obj["rank"] = d["rank"]
        if d["detail"].get("music_feature"):
            for key in music_feature_key:
                obj[key] = d["detail"]["music_feature"][key]
        else:
            continue
         # TODO:歌詞データがないのを省くでいいのかどうか（現状は省いている）
        if d["detail"].get("lyrics_feature"):
            if d["detail"]["lyrics_feature"]["total_rhyme_score"] is None:
                continue
            else:
                obj["total_rhyme_score"] = d["detail"]["lyrics_feature"]["total_rhyme_score"]
            if d["detail"]["lyrics_feature"]["total_positive_score"] is None:
                continue
            else:
                obj["total_positive_score"] = d["detail"]["lyrics_feature"]["total_positive_score"]
        else:
            continue
        s_data.append(obj)
    return s_data


data = getAllPastSongs()
formated_data = formatData(data)
print(len(formated_data))
# random_forest_classifier_maker(formated_data)
res = classify_data_by_random_forest(formated_data[0:1])

print(res)
