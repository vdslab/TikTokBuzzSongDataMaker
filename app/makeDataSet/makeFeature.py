import json
import time
import sys
import os
from os.path import dirname, abspath
file_path = dirname(dirname(abspath(__file__)))
sys.path.append(file_path)
sys.path.append("../buzzSongMaker")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from buzzSongMaker.getLyric import get_formated_lyric
from buzzSongMaker.analysisLyric import analysis_lyric
from buzzSongMaker.common import MUSIC_FEATURE



load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv('SPOTIFY_CLIENT_ID'), client_secret=os.getenv('SPOTIFY_CLIENT_SECRET_ID')), requests_timeout=5)
json_key_name = MUSIC_FEATURE


def add_feature_and_formated_data(data_list):
    formated_data_list = []
    for data in data_list:
        formated_data = dict()
        analysis_song_info = dict()

        id = data["id"]
        song_features = sp.audio_features(id)
        artists_info = sp.track(id)["artists"][0]
        preview_url = sp.track(id)["preview_url"]
        img_url = sp.track(id)["album"]["images"][0]["url"]

        formated_data["id"] = id
        formated_data["title"] = data["title"]
        formated_data["preview_url"] = preview_url
        formated_data["img_url"] = img_url
        formated_data["artist"] = artists_info["name"]
        formated_data["artist_uri"] = artists_info["uri"][15:]

        music_feuture = dict()
        for key in json_key_name:
            music_feuture[key] = song_features[0][key]
        formated_data["music_feature"] = music_feuture

        lyric_text = get_formated_lyric(
            data["title"], artists_info["name"])
        if lyric_text is None:
            lyrics_feature = None
        else:
            lyrics_feature = analysis_lyric(lyric_text)

        # TODO：歌詞分析
        formated_data["lyrics_feature"] = lyrics_feature

        artist_name = artists_info["name"]
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

        # 気休めでのタイムエラー対策
        time.sleep(1.0)

        print(formated_data)
    with open("./data/feature_data.json", 'w', encoding='utf-8') as f:
        json.dump(formated_data_list, f, indent=2, ensure_ascii=False)

    return formated_data_list


def get_song_info(id):
    formated_data = dict()
    analysis_song_info = dict()

    song_features = sp.audio_features(id)
    song_track = sp.track(id)
    artists_info = song_track["artists"][0]
    preview_url = song_track["preview_url"]
    img_url = song_track["album"]["images"][0]["url"]

    formated_data["id"] = id
    formated_data["title"] = song_track["name"]
    formated_data["preview_url"] = preview_url
    formated_data["img_url"] = img_url
    formated_data["artist"] = artists_info["name"]
    formated_data["artist_uri"] = artists_info["uri"][15:]

    music_feuture = dict()
    for key in json_key_name:
        music_feuture[key] = song_features[0][key]
    formated_data["music_feature"] = music_feuture

    lyric_text = get_formated_lyric(
        song_track["name"], artists_info["name"])
    if lyric_text is None:
        lyrics_feature = None
    else:
        lyrics_feature = analysis_lyric(lyric_text)

    # TODO：歌詞分析
    formated_data["lyrics_feature"] = lyrics_feature

    artist_name = artists_info["name"]
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

    return formated_data
