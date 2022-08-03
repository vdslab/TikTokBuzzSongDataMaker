import requests
import os
import re
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('MUSIXMATCH_API_KEY')


# REVIEW:全体的にエラーハンドリングが必要。どんな不足データが返ってくるか考えること。
def get_lyric(title, artist):
    track_request_url = 'http://api.musixmatch.com/ws/1.1/track.search'
    track_request_params = {'apikey': API_KEY,
                            'q_track': title, 'q_artist': artist}
    track_response = requests.get(
        track_request_url, params=track_request_params)
    track_info = track_response.json()
    # エラーハンドリング
    if track_info["message"]["header"]["status_code"] != 200:
        return None
    if len(track_info["message"]["body"]["track_list"]) == 0:
        return None
    track_id = track_info["message"]["body"]["track_list"][0]["track"]["track_id"]

    lyric_request_url = 'http://api.musixmatch.com/ws/1.1/track.lyrics.get'
    lyric_request_params = {'apikey': API_KEY, 'track_id': track_id}
    lyric_response = requests.get(lyric_request_url, lyric_request_params)
    # エラーハンドリング
    lyric_info = lyric_response.json()
    if lyric_info["message"]["header"]["status_code"] != 200:
        return None
    lyric = lyric_info["message"]["body"]["lyrics"]["lyrics_body"]

    return lyric


def get_line_splitlyric(title, artist):
    lyric = get_lyric(title, artist)
    if lyric is None:
        return None
    lyric_section_div = re.split('\n\n', lyric)
    # MUST：有料APIにしたら削除する(無料枠ではここまでと文字が出力されているため)
    lyric_section_div.pop(-1)
    return lyric_section_div


def get_formated_lyric(title, artist):
    lyric_section_div = get_line_splitlyric(title, artist)
    if lyric_section_div is None:
        return None
    lyric_sp = [[] for i in range(len(lyric_section_div))]
    for i in range(len(lyric_section_div)):
        lyric_sp[i] = lyric_section_div[i].replace('.', ' ').split()
    # MUST：有料APIにしたら削除する(無料枠ではここまでと文字が出力されているため)
    if len(lyric_sp) > 0:
        lyric_sp.pop(-1)
    return lyric_sp
