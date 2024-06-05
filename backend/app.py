from flask import Flask, jsonify
from YoutubeData import fetchAllComments
from SentimentAnalysis import AnalyzeSentiment
import pandas as pd
import json

app = Flask(__name__)


@app.route('/api/analyzecomments/<video_id>')
def analyze_youtube_comments(video_id):

    comments = fetchAllComments(video_id)
    youtube_comments_analysis_results = AnalyzeSentiment(comments)
    

    return jsonify(youtube_comments_analysis_results)


if __name__ == "__main__":
    app.run(debug=True)
