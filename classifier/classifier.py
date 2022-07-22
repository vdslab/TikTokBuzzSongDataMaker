from api import getAllPastSongs
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
