import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()

"""
TODO:共通化
"""


def getAllSongsId():
    url = "https://tsubame.hasura.app/api/rest/songs/id"
    headers = {
        "Content-Type": "application/json",
        "x-hasura-admin-secret": os.getenv('HASURA_ADMIN_SECRET'),
    }

    res = requests.get(url, headers=headers)
    data = res.json()
    songs_id = data["songs"]

    return songs_id


def post_past_songs_one(data):
    url = "https://tsubame.hasura.app/api/rest/insert/past_songs_one"
    headers = {
        "Content-Type": "application/json",
        "x-hasura-admin-secret": os.getenv('HASURA_ADMIN_SECRET'),
    }
    data = json.dumps({"object": data})
    res = requests.post(url, headers=headers, data=data)
    data = res.json()
    print(data)


def post_songs_one(data):
    url = "https://tsubame.hasura.app/api/rest/insert/songs_one"
    headers = {
        "Content-Type": "application/json",
        "x-hasura-admin-secret": os.getenv('HASURA_ADMIN_SECRET'),
    }
    data = json.dumps({"object": data})
    res = requests.post(url, headers=headers, data=data)
    data = res.json()
    print(data)


def post_buzz_songs_one(data):
    url = "https://tsubame.hasura.app/api/rest/insert/buzz_songs_one"
    headers = {
        "Content-Type": "application/json",
        "x-hasura-admin-secret": os.getenv('HASURA_ADMIN_SECRET'),
    }
    data = json.dumps({"object": data})
    res = requests.post(url, headers=headers, data=data)
    data = res.json()
    print(data)
