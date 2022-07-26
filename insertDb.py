import json
from api import getAllSongsId
from api import post_buzz_songs_one, post_songs_one
import time


#songsデータと, past_songsデータに分ける
def div_data(data):
    songs = []
    buzz_songs = []

    ids = getAllSongsId()
    ids = [d["id"] for d in ids]

    for d in data:
        buzz_song = dict()
        buzz_song["id"] = d["id"]
        buzz_song["date"] = d["date"]
        buzz_song["rank"] = d["rank"]
        buzz_songs.append(buzz_song)

        hadId = d["id"] in (ids)
        if hadId:
            continue

        song = dict()
        song["id"] = d["id"]
        song["title"] = d["title"]
        song["preview_url"] = d["preview_url"]
        song["artist"] = d["artist"]
        song["artist_uri"] = d["artist_uri"]
        song["genres"] = json.dumps(d["genres"])
        song["music_feature"] = json.dumps(d["music_feature"])
        song["lyrics_feature"] = json.dumps(d["lyrics_feature"])

        songs.append(song)

    return {"songs": songs, "buzz_songs": buzz_songs}


# TODO:for文じゃなくて一括で行けるようなmutationを作る
def insertDb(data):
    divided_data = div_data(data)

    for d in divided_data["buzz_songs"]:
        post_buzz_songs_one(d)
        time.sleep(0.5)

    print("------------------")

    for d in divided_data["songs"]:
        post_songs_one(d)
        time.sleep(0.5)

    print("post all fin")
