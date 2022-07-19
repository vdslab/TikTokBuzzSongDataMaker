import glob
from janome.tokenizer import Tokenizer

# 極性辞書の作成
dict_polarity = {}
with open('./data/dict/pn_ja.dic.txt', 'r', encoding='shift_jis') as f:
    line = f.read()
    lines = line.split('\n')
    print(dict_polarity)
    for i in range(len(lines)):
        line_components = lines[i].split(':')
        if len(line_components) >= 4:
            dict_polarity[line_components[0]] = line_components[3]


# ネガポジ分析用の関数の作成
# TODO:正規化
def judge_polarity(section):
    t = Tokenizer()
    pol_val = 0
    pos_cnt = 0
    for line in section:
        tokens = t.tokenize(line)
        for token in tokens:
            word = token.surface
            if word in dict_polarity:
                pol_val = pol_val + float(dict_polarity[word])
                pos_cnt += 1
    return pol_val


def calc_section_positive_score(section):
    score = judge_polarity(section)
    return score
