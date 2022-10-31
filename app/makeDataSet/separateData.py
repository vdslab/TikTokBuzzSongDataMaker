import json


def separateUsabaleTiktokData(data):
    available_rank_data = []
    invalid_rank_data = []
    for song in data:
        if song["id"] is None or song["id"] == "404":
            invalid_rank_data.append(song)
        else:
            available_rank_data.append(song)

    with open('./data/available_rank_data.json', 'w', encoding='utf-8') as f:
        json.dump(available_rank_data, f, indent=2, ensure_ascii=False)

    with open('./data/invalid_rank_data.json', 'w', encoding='utf-8') as f:
        json.dump(invalid_rank_data, f, indent=2, ensure_ascii=False)

    return {"available_rank_data": available_rank_data, "invalid_rank_data": invalid_rank_data}


def getRequiredFeatureList(song_ids, song_data):
    require_data = []
    for song in song_data:
        if not song["id"] in song_ids:
            require_data.append(song)

    with open('./data/feature_require_data.json', 'w', encoding='utf-8') as f:
        json.dump(require_data, f, indent=2, ensure_ascii=False)

    return require_data
