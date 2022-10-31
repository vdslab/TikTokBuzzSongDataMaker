from shutil import get_unpack_formats
import getTiktokRank
import getSpotifyUnBuzzSong
import separateUsableTiktokData
import json

# tiktok_rank_data = getTiktokRank.main()
# spotify_un_buzz_song = getSpotifyUnBuzzSong.create_spotify_un_buzz_song()
tiktok_rank_data_file = open('./data/tiktok_ranking_data.json')
spotify_un_buzz_song_file = open("./data/spotify_un_buzz_song.json")
tiktok_rank_data = json.load(tiktok_rank_data_file)
spotify_un_buzz_song = json.load(spotify_un_buzz_song_file)

# spotify_idが取得できたもの、できてないものに分ける
# できていないものは、手動確認リストに入れる
separated_data = separateUsableTiktokData.separateUsabaleData(tiktok_rank_data)
tiktok_available_rank_data = separated_data["available_rank_data"]
tiktok_invalid_rank_data = separated_data["invalid_rank_data"]

# idがあるものはpast_songsに入れる
#tiktok_available_rank_data, spotify_un_buzz_songに対して

# songsテーブルにidがあるかを調べる
# idがなければ特徴データを作成
#tiktok_available_rank_data, spotify_un_buzz_songに対して
