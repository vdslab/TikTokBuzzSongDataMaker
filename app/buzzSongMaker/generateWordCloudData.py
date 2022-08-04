from collections import Counter
import oseti
# from math import log
import MeCab
# from wordcloud import WordCloud

analyzer = oseti.Analyzer()

tagger = MeCab.Tagger('-Ochasen')
# define stop word
# stop_word_list = ['の', 'よう', 'それ', 'もの', 'ん', 'そこ', 'うち', 'さん', 'そう', 'ところ',
#                   'これ', '-', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
# これをどうにかしたい
# ストップワードは無くても動いた
stop_word_list = [
    '', 'てる', 'の', '(', ')', ' (', ')', "'", ',', '.', '、', '。', '!', '?', '！', '？']


def get_word_counter(lyric):
    # 2次元配列を1次元に
    text_lines = sum(lyric, [])
    word_counter = Counter()
    for text_line in text_lines:
        node = tagger.parseToNode(text_line)
        while node:
            word_type = node.feature.split(',')[0]
            if (word_type == '名詞') and (len(node.surface) != 0) and (not(node.surface in stop_word_list)):
                word_counter[node.surface] += 1
            # し、て、とかを省くために長さ1以上にしてみてるけどどうなのか
            if (word_type == '動詞') and (len(node.surface) > 1) and (not(node.surface in stop_word_list)):
                word_counter[node.surface] += 1
            if (word_type == '形容詞') and (len(node.surface) != 0) and (not(node.surface in stop_word_list)):
                word_counter[node.surface] += 1
            node = node.next
    return word_counter


def get_tf_dict(word_counter):
    tf_dict = {}
    word_total = sum(word_counter.values())
    for word, count in word_counter.items():
        tf_dict[word] = count/word_total
    return tf_dict

# TODO:idfの計算(past_songからデータを引っ張ってくる？)
# def get_idf_dict(file_word_counter, targetname):
#     word_list = file_word_counter[targetname].keys()
#     filename_list = file_word_counter.keys()
#     idf_dict = {}
#     for word in word_list:
#         word_count = 0
#         for filename in filename_list:
#             if word in file_word_counter[filename].keys():
#                 word_count += 1
#         idf_dict[word] = log(len(filename_list)/word_count)+1
#     return idf_dict


def add_negaposi_score(data):
    added_negaposi_data = []
    for word in data:
        negaposi = analyzer.analyze(word[0])
        if len(negaposi) > 0:
            obj = {
                "word": word[0],
                "score": word[1],
                "negaposi": negaposi[0]}
            added_negaposi_data.append(obj)
    return added_negaposi_data


def get_negaposi_tf_word_data(data):
    word_cnt_data = get_word_counter(data)
    tf_dict = get_tf_dict(word_cnt_data)
    sorted_tf_dict = sorted(tf_dict.items(), key=lambda x: x[1], reverse=True)
    added_negaposi_data = add_negaposi_score(sorted_tf_dict)
    return added_negaposi_data
