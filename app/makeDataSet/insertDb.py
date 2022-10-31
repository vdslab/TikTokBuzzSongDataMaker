import api
import time


def insertPastSongsTable(data):
    for song in data:
        post_data = {
            "id": song["id"],
            "rank": song["rank"],
            "date": song["date"],
        }
        api.post_past_songs_one(post_data)
        time.sleep(0.5)
    print("fin")


def insertSongsTable(data):
    for song in data:
        api.post_songs_one(song)
        time.sleep(0.5)
    print("fin")
