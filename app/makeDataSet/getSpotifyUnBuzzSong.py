from tkinter.tix import ROW
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import csv
import glob
import os


client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET_ID')

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret), requests_timeout=5)
json_key_name = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']


"""
シンプルにspotify chartの185位以下のデータを取得
"""


def create_spotify_un_buzz_song():
    analysis_song_data = []
    for filename in sorted(glob.glob("../buzzSongMaker/data/spotify_data/csv/regional-jp-weekly-*.csv")):
        print(filename)
        with open(filename, newline="") as f:
            dic_reader = csv.DictReader(f)
            for row in dic_reader:
                rank = row['\ufeffrank']
                if int(rank) < 185:
                    continue

                id = row["uri"][14:]
                date = filename[-14:-4]

                analysis_song_info = dict()
                analysis_song_info['id'] = id
                analysis_song_info['title'] = row['track_name']
                analysis_song_info['rank'] = rank
                analysis_song_info['date'] = date

                analysis_song_data.append(analysis_song_info)

    with open('./data/spotify_un_buzz_song.json', 'w', encoding='utf-8') as f:
        json.dump(analysis_song_data, f, indent=2, ensure_ascii=False)

    return analysis_song_data
