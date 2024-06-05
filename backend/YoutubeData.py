import os
import googleapiclient.discovery
import googleapiclient.errors
# import pandas as pd
from dotenv import load_dotenv

load_dotenv()

api_service_name = "youtube"
api_version = "v3"
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=YOUTUBE_API_KEY
)


# fetch comments from a youtube video
def fetchAllComments(video_id, pageToken=None):
    items = []
    maxCount = 5000

    while True:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            pageToken=pageToken
        )

        response = request.execute()
        items.extend(response['items'])
        if len(items) >= maxCount:
            break
        if 'nextPageToken' in response:
            pageToken = response['nextPageToken']
        else:
            break

           # output as df
    comments = []

    for item in items:
        comment = item['snippet']['topLevelComment']['snippet']
        comment_info = {
            # comment['authorDisplayName'],
            'published_at': comment['publishedAt'],
            # comment['updatedAt'],
            'like_count': comment['likeCount'],
            'text': comment['textDisplay']
        }
        comments.append(comment_info)

    return comments


# full link https://www.youtube.com/watch?v=4_UDm-nCjeA
# video_id = "4_UDm-nCjeA"
# items = fetchAllComments(video_id)
