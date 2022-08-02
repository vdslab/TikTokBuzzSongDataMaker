from filterPopularSong import filter_popular_song
from addFeatureAndFormatedData import add_feature_and_formated_data
from classifierData import classifier_data
from insertDb import insertDb

file_name = "./data/regional-jp-weekly-2022-07-07.csv"

# チャートの中からNEW, RE-ENTRY, up15のものに絞る
filterd_data = filter_popular_song(file_name)
date = file_name[-14:-4]
# 特徴量をとってくる(TODO:歌詞APIによるタイムアウトエラー)
added_future_data = add_feature_and_formated_data(filterd_data, date)
# 分類器にかける
classifiered_data = classifier_data(added_future_data)
# バズる予測が出たものをデータベースに追加する
insertDb(classifiered_data)

# 出力
print(len(classifiered_data))
for i in classifiered_data:
    print(i["title"], i["rank"])
