import os
import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd
from dotenv import load_dotenv  

load_dotenv()

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY
)


def fetchAllComments(video_id, pageToken=None):
    items = []
    maxCount = 100

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

    return items


# full link https://www.youtube.com/watch?v=4_UDm-nCjeA
video_id = "ddTV12hErTc"
items = fetchAllComments(video_id)



#output as df
comments = []

for item in items:
    comment = item['snippet']['topLevelComment']['snippet']
    comments.append([
        comment['authorDisplayName'],
        comment['publishedAt'],
        comment['updatedAt'],
        comment['likeCount'],
        comment['textDisplay']
    ])

df = pd.DataFrame(comments, columns=[
                  'author', 'published_at', 'updated_at', 'like_count', 'text'])

print(df)