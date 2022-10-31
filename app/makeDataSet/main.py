from shutil import get_unpack_formats
import getTiktokRank
import getSpotifyUnBuzzSong

tiktok_rank_data = getTiktokRank.main()
spotify_un_buzz_song = getSpotifyUnBuzzSong.create_spotify_un_buzz_song()

# spotify_idが取得できたもの、できてないものに分ける
# できていないものは、手動確認リストに入れる
tiktok_available_rank_data = []
tiktok_invalid_rank_data = []

# idがあるものはpast_songsに入れる
#tiktok_available_rank_data, spotify_un_buzz_songに対して

# songsテーブルにidがあるかを調べる
# idがなければ特徴データを作成
#tiktok_available_rank_data, spotify_un_buzz_songに対して
