import os
from tkinter.tix import ROW
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from getLyric import get_formated_lyric
from analysisLyric import analysis_lyric

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv('SPOTIFY_CLIENT_ID'), client_secret=os.getenv('SPOTIFY_CLIENT_SECRET_ID')), requests_timeout=5)
json_key_name = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']


def add_feature_and_formated_data(data_list, date):
    formated_data_list = []
    for data in data_list:
        formated_data = dict()
        analysis_song_info = dict()

        id = data["uri"][14:]
        song_features = sp.audio_features(id)
        artists_info = sp.track(id)["artists"][0]
        preview_url = sp.track(id)["preview_url"]

        formated_data["id"] = id
        formated_data["title"] = data["track_name"]
        formated_data["date"] = date
        formated_data["preview_url"] = preview_url
        formated_data["artist"] = artists_info["name"]
        formated_data["artist_uri"] = artists_info["uri"][15:]

        music_feuture = dict()
        for key in json_key_name:
            music_feuture[key] = song_features[0][key]
        formated_data["music_feature"] = music_feuture

        lyric_text = get_formated_lyric(
            data["track_name"], artists_info["name"])
        if lyric_text is None:
            lyrics_feature = None
        else:
            lyrics_feature = analysis_lyric(lyric_text)

        # TODO：歌詞分析
        formated_data["lyrics_feature"] = lyrics_feature

        artist_name = data["artist_names"]
        artist_result = sp.search(
            q='artist:' + artist_name, type='artist')
        artist_info_list = artist_result["artists"]["items"]
        analysis_song_info["artist"] = artist_name

        # Noneにしておくことでspotify上で検索ができてないことが後から確認できるように
        if len(artist_info_list) == 0:
            analysis_song_info["artist_uri"] = None
            formated_data["genres"] = None

        if len(artist_info_list) > 0:
            analysis_song_info["artist_uri"] = artist_info_list[0]["uri"][15:]
            formated_data["genres"] = artist_info_list[0]["genres"]

        formated_data_list.append(formated_data)

    return formated_data_list
