import csv

file_name = "./data/regional-jp-weekly-2022-07-07.csv"

"""
ダウンロードしたデータのうちNEW, RE-ENTRY, up15のものに絞る
"""
filterd_data = []
with open(file_name, newline="") as f:
    dic_reader = csv.DictReader(f)
    for row in dic_reader:
        rank = int(row["\ufeffrank"])
        pre_rank = int(row["previous_rank"])
        if pre_rank == -1:
            filterd_data.append(row)
        elif -1*(rank-pre_rank) >= 15:
            filterd_data.append(row)
