import datetime
import requests
from bs4 import BeautifulSoup
import json
import search_spotify
import time

'''
tiktokのランキング情報を取得（spotifyの情報は不足）
'''


def create_tiktok_rank_data(year, month, day):
    url = 'https://www.billboard-japan.com/charts/detail?a=tiktok&year=' + \
        str(year) + '&month=' + str(month) + '&day=' + str(day)
    response = requests.get(url)
    text_html = response.text
    soup = BeautifulSoup(text_html, 'html.parser')
    ranking = soup.select('td.rank_td.pc_obj')
    music_title = soup.select('p.musuc_title')
    artists = soup.select('p.artist_name')
    ranking_data = []
    for r, title, artist in zip(ranking, music_title, artists):
        r = r.select_one('span')
        ranking_info = {}
        ranking_info['rank'] = r.text
        ranking_info['title'] = title.text
        ranking_info['artist'] = artist.text
        ranking_info['id'] = search_spotify.search_spotify_url(title.text)
        if ranking_info['id'] == None:
            ranking_info['url'] = None
        elif ranking_info['id'] == "404":
            ranking_info['url'] = "404"
        else:
            ranking_info['url'] = "https://open.spotify.com/track/" + \
                ranking_info['id']
        ranking_info['date'] = str(year) + '/' + str(month) + '/' + str(day)
        ranking_data.append(ranking_info)
        time.sleep(1)
    return ranking_data


def main():
    tiktok_ranking_data = []
    # date = datetime.date(2021, 12, 13)
    # end = datetime.date(2022, 5, 16)
    date = datetime.date(2022, 10, 31)
    end = datetime.date(2022, 11, 17)
    while date <= end:
        print(date)
        year = date.year
        month = date.month
        day = date.day
        ranking_data = create_tiktok_rank_data(year, month, day)
        tiktok_ranking_data.extend(ranking_data)
        date += datetime.timedelta(days=7)
    path = './data/tiktok_ranking_data.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(tiktok_ranking_data, f, indent=2, ensure_ascii=False)

    return tiktok_ranking_data


if __name__ == '__main__':
    main()
