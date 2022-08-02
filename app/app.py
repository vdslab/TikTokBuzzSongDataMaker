import os
import sys
from pathlib import Path
parent_file_path = str(Path('__file__').resolve().parent)
sys.path.append(parent_file_path)
from flask import Flask, jsonify
from flask_cors import CORS
from buzzSongMaker.addFeatureAndFormatedData import get_song_info
from buzzSongMaker.classifierData import get_classifier_score


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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',
            port=int(os.environ.get('PORT', 8080)))
