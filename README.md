## Social Media Sentiment Analysis 

## Project setup

### Backend setup
`git clone <this repo>`
```
cd /backend
pip install -r requirements.txt
```

### Youtube Data API
1. Go on Google cloud console activate the Youtube Data api and then create a developer key. 
Tutorial: `https://www.youtube.com/watch?v=QY8dhl1EQfI&list=PL_cUvD4qzbkyZ_Q_P7W70rID0JkQ8rqic`

2. Create a `.env` file in the root directory and set a value `YOUTUBE_API_KEY="your key"`


### Using the API 
`http://localhost:5000/api/analyzecomments/<video_id>`

Youtube Video: (https://www.youtube.com/watch?v=8wYTDjQxxa8)
Its Id: `8wYTDjQxxa8`

##### The request: `http://localhost:5000/api/analyzecomments/8wYTDjQxxa8`

#### Results
```
[
    {
        "like_count": 39,
        "negative": 0.0032474733889102936,
        "neutral": 0.12740086019039154,
        "overall_sentiment": "positive",
        "positive": 0.8693516850471497,
        "published_at": "2024-06-01T02:16:10Z",
        "text": "Play War Thunder now with my link, and get a massive, free bonus pack including vehicles, boosters and more: \r<br><a href=\"https://playwt.link/jacksather24\">https://playwt.link/jacksather24</a>"
    },
    {
        "like_count": 0,
        "negative": 0.02853829227387905,
        "neutral": 0.18935763835906982,
        "overall_sentiment": "positive",
        "positive": 0.7821040749549866,
        "published_at": "2024-06-07T09:22:49Z",
        "text": "I got a third in my university course and I am in the industry, some people have honors and are still working for McDonalds. don&#39;t worry too much about the result, worry about how much better you can be"
    },
    {
        "like_count": 0,
        "negative": 0.2838704586029053,
        "neutral": 0.21036478877067566,
        "overall_sentiment": "positive",
        "positive": 0.5057647228240967,
        "published_at": "2024-06-07T06:08:26Z",
        "text": "I know this won&#39;t help and you don&#39;t wanna hear it, but – geez, those animations are so good and the idea that everything should move as your character is walking is great!"
    },
    ]
```


#### Development tasks
- [x] Youtube fetch post comments. 
- [x] Analyze comments endpoint from video_id.
- [ ] Add data cleaning to remove links and usernames from comments.
- [ ] Track youtube channel endpoint.
- [ ] Add instagram fetch post functionality.
- [ ] Analyze instagram post sentiment.
- [ ] Add reddit fetch post functionality.
- [ ] Analyze reddit post sentiment.
      
#### Frontend
- [X] Initialize React Native Project.
- [ ] Setup routing.
- [ ] Clerk Authentication.
