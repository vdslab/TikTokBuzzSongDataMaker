import requests
import os
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
