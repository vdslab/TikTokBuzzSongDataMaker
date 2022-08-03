import os
import sys
from pathlib import Path
parent_file_path = str(Path('__file__').resolve().parent)
sys.path.append(parent_file_path)

from similarSongs import get_similar_buzz_song_list
from buzzSongMaker.classifierData import get_classifier_score
from buzzSongMaker.addFeatureAndFormatedData import get_song_info
from flask_cors import CORS
from flask import Flask, jsonify


app = Flask(__name__)
cors = CORS(app)


@app.route("/song_info/<song_id>",  methods=['GET'])
def get_song_feature(song_id):
    song_featur = get_song_info(song_id)
    return jsonify(song_featur)


@app.route("/song_buzz_score/<song_id>",  methods=['GET'])
def get_song_score(song_id):
    song_info = get_song_info(song_id)
    song_featur = get_classifier_score(song_info)
    return jsonify(song_featur)


@app.route("/similar_buzz_songs/<song_id>", methods=['GET'])
def get_similar_buzz_songs(song_id):
    similar_buzz_songs = get_similar_buzz_song_list(song_id)
    print(len(similar_buzz_songs))
    return jsonify(similar_buzz_songs)


# 現在は未使用
@app.route("/buzz_song_info/<song_id>", methods=["GET"])
def get_buzz_song_info(song_id):
    song_info = get_song_info(song_id)
    song_featur = get_classifier_score(song_info)
    similar_buzz_songs = get_similar_buzz_song_list(song_info)
    return jsonify({"buzz_song_info": song_featur, "similar_buzz_songs": similar_buzz_songs})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',
            port=int(os.environ.get('PORT', 8080)))
