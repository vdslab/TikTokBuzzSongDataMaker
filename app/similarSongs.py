import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from buzzSongMaker.addFeatureAndFormatedData import get_song_info, get_song_music_info
from buzzSongMaker.classifierData import classifier_data
import time


load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv('SPOTIFY_CLIENT_ID'), client_secret=os.getenv('SPOTIFY_CLIENT_SECRET_ID')), requests_timeout=5)


def get_similar_buzz_song_list(song_id):
    similar_songs = sp.recommendations(
        seed_tracks=[song_id], limit=10)
    similar_songs = similar_songs["tracks"]

    similar_feature_data_list = []
    for song in similar_songs:
        # song_info = get_song_info(song["id"])
        song_info = get_song_music_info(song["id"])
        similar_feature_data_list.append(song_info)
        time.sleep(0.5)

    classifiered_data = classifier_data(similar_feature_data_list)
    sorted_data = sorted(
        classifiered_data, key=lambda x: int(x["rank"]), reverse=True)

    return sorted_data
