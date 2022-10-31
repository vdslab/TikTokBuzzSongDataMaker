import json


def separateUsabaleData(data):
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
