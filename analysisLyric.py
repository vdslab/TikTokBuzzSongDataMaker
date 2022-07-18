
from calcRhymeScore import calc_section_rhyme_score
import math


def analysis_lyric(lyric_text):
    line_feature = []
    total_rhyme_score = 0
    total_positive_score = 0
    for section in lyric_text:
        rhyme_score = calc_section_rhyme_score(section)
        positive_score = 0
        obj = {
            "text": section,
            "rhyme_score":  rhyme_score,
            "positive_score": 0
        }
        line_feature.append(obj)
        total_rhyme_score += rhyme_score
        total_positive_score += positive_score

    lyric_feature = {
        "lyrics_list": line_feature,
        "total_rhyme_score": math.floor(total_rhyme_score/len(lyric_text)),
        "total_positive_score": math.floor(total_positive_score/len(lyric_text)),
        "word_cloud_data": {},
    }

    return lyric_feature
