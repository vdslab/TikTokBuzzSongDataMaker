from api import getAllPastSongs
# 分類器のアップデート？をする


# TODO:このデータの整形をなしの形でapiからとってきたい
def formatData():
    music_feature_key = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                         'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']
    s_data = []
    for d in data:
        obj = dict()
        for key in music_feature_key:
            if d["detail"].get("music_feature"):
                obj[key] = d["detail"]["music_feature"][key]
        if d["detail"].get("lyrics_feature"):
            obj["total_rhyme_score"] = d["detail"]["lyrics_feature"]["total_rhyme_score"]
            obj["total_positive_score"] = d["detail"]["lyrics_feature"]["total_positive_score"]
        s_data.append(obj)


data = getAllPastSongs()
