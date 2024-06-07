from flask import Flask, jsonify
from YoutubeData import fetchAllComments
from SentimentAnalysis import AnalyzeSentiment
import pandas as pd
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/')
def Home():
    return '''<h3>Welcome, to analyze youtube comments just go to '/api/analyzecomments/<youtube_url>.</h3>
                Example: <a href="http://localhost:5000/api/analyzecomments/iwGVLiFL-Lw" >/api/analyzecomments/iwGVLiFL-Lw</a> '''

@app.route('/api/analyzecomments/<video_id>')
def analyze_youtube_comments(video_id):

    # video_id = extract_video_id(youtube_url=youtube_url)
    youtube_comments = fetchAllComments(video_id)
    youtube_comments_analysis_results = AnalyzeSentiment(youtube_comments)
    

    return jsonify(youtube_comments_analysis_results)


if __name__ == "__main__":
    app.run(debug=True)
