import requests
import os
import re
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('MUSIXMATCH_API_KEY')


def get_lyric(title, artist):
    track_request_url = 'http://api.musixmatch.com/ws/1.1/track.search'
    track_request_params = {'apikey': API_KEY,
                            'q_track': "Habit", 'q_artist': "SEKAI NO OWARI"}
    track_response = requests.get(
        track_request_url, params=track_request_params)
    track_info = track_response.json()
    track_id = track_info["message"]["body"]["track_list"][0]["track"]["track_id"]

    lyric_request_url = 'http://api.musixmatch.com/ws/1.1/track.lyrics.get'
    lyric_request_params = {'apikey': API_KEY, 'track_id': track_id}
    lyric_response = requests.get(lyric_request_url, lyric_request_params)
    lyric_info = lyric_response.json()
    lyric = lyric_info["message"]["body"]["lyrics"]["lyrics_body"]
    return lyric


def get_formated_lyric(title, artist):
    lyric = get_lyric(title, artist)
    lyric_section_div = re.split('\n\n', lyric)
    lyric_sp = [[] for i in range(len(lyric_section_div))]
    for i in range(len(lyric_section_div)):
        lyric_sp[i] = lyric_section_div[i].replace('.', ' ').split()
    # MUST：有料APIにしたら削除する(無料枠ではここまでと文字が出力されているため)
    lyric_sp.pop(-1)
