import api
import time


def insertPastSongsTable(data):
    for song in data:
        post_data = {
            "id": song["id"],
            "rank": song["rank"],
            "date": song["data"],
        }
        api.post_past_songs_one(post_data)
        time.sleep(0.5)
    print("fin")
