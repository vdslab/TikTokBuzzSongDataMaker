import pandas as pd


# tiktokランキングに入っているものが1, その他0
def ranking_convert(x):
    if int(x) <= 20:
        return 1
    else:
        return 0


def format_data(data):
    df = pd.DataFrame(data)
    # ランキングを01で
    df["rank"] = df["rank"].apply(ranking_convert)
    return df
