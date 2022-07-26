import csv


"""
ダウンロードしたデータのうちNEW, RE-ENTRY, up15のものに絞る
"""


def filter_popular_song(file_name):
    filterd_data = []
    with open(file_name, newline="") as f:
        dic_reader = csv.DictReader(f)
        for row in dic_reader:
            rank = int(row["\ufeffrank"])
            pre_rank = int(row["previous_rank"])
            # TODO:過去n位以内に入ったことがあるものは除くとかをしてもいいかもしれない
            if pre_rank == -1:
                filterd_data.append(row)
            elif -1*(rank-pre_rank) >= 15:
                filterd_data.append(row)
    return filterd_data
