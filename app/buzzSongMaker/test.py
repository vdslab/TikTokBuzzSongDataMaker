from filterPopularSong import filter_popular_song
from addFeatureAndFormatedData import add_feature_and_formated_data
import json
from classifierData import classifier_data
from memo import allSong
from insertDb import insertDb

file_name = "./data/regional-jp-weekly-2022-07-07.csv"

# filterd_data = filter_popular_song(file_name)
# date = file_name[-14:-4]
# added_future_data = add_feature_and_formated_data(filterd_data, date)
classifiered_data = classifier_data(allSong)
# insertDb(classifiered_data)
print(len(classifiered_data))
for i in classifiered_data:
    print(i["title"], i["rank"])


# with open('./data/test/pop.json', 'w', encoding='utf-8') as f:
#     json.dump(added_future_data, f, indent=2, ensure_ascii=False)
