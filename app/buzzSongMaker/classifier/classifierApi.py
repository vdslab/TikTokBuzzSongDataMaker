import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()


def getAllPastSongs():
    url = "https://tsubame.hasura.app/api/rest/all_past_songs"
    headers = {
        "Content-Type": "application/json",
        "x-hasura-admin-secret": os.getenv('HASURA_ADMIN_SECRET'),
    }

    res = requests.get(url, headers=headers)
    data = res.json()
    past_songs = data["past_songs"]

    return past_songs


def getPastSongsBeforeDate(date):
    print("date", date)
    url = "https://tsubame.hasura.app/api/rest/past_songs/before_date"
    headers = {
        "Content-Type": "application/json",
        "x-hasura-admin-secret": os.getenv('HASURA_ADMIN_SECRET'),
    }
    data = json.dumps({"date": date})
    res = requests.post(url, headers=headers, data=data)
    data = res.json()
    print(data)
    past_song = data["past_songs"]
    return past_song
