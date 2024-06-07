from flask import Flask, jsonify
from YoutubeData import fetchAllComments
from SentimentAnalysis import AnalyzeSentiment
import pandas as pd
from flask_cors import CORS
import re
import json

app = Flask(__name__)
CORS(app)

import re

def extract_video_id(youtube_url):
    # Regular expression pattern to match YouTube video URLs
    pattern = r"(?<=v=|\\/videos\\/|embed\\/|youtu.be\\/|\\/v\\/|\\/e\\/|watch\\?v=|&v=|%2Fvideos%2F|%2Fv%2F|%2Fe%2F|%2Fwatch%3Fv%3D|%26v%3D)([\\w-]+)"
    
    # Search for the video ID in the URL
    match = re.search(pattern, youtube_url)
    if match:
        return match.group(1)
    else:
        return None


@app.route('/')
def Home():
    return '''<h3>Welcome, to analyze youtube comments just go to '/api/analyzecomments/<youtube_url>.</h3>
                Example: <a href="http://localhost:5000/api/analyzecomments/iwGVLiFL-Lw" >/api/analyzecomments/iwGVLiFL-Lw</a> '''

@app.route('/api/analyzecomments/<video_id>')
def analyze_youtube_comments(video_id):

    # video_id = extract_video_id(youtube_url=youtube_url)
    comments = fetchAllComments(video_id)
    youtube_comments_analysis_results = AnalyzeSentiment(comments)
    

    return jsonify(youtube_comments_analysis_results)


if __name__ == "__main__":
    app.run(debug=True)
