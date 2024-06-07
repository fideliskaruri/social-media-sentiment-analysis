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

2. Create a `.env` file in the `/backend` directory and set a value `YOUTUBE_API_KEY="your key"`


### Using the API 
`http://localhost:5000/api/analyzecomments/<video_id>`

Youtube Video: (https://www.youtube.com/watch?v=8wYTDjQxxa8)
Its Id: `8wYTDjQxxa8`

##### The request: `http://localhost:5000/api/analyzecomments/8wYTDjQxxa8`

#### Results
```

```

#### Development tasks
- [x] Analyze comments endpoint from video_id
- [x] Youtube fetch post comments 
- [ ] Track youtube channel endpoint
- [ ] Add instagram fetch post functionality
- [ ] Analyze instagram post sentiment
- [ ] Add reddit fetch post functionality
- [ ] Analyze reddit post sentiment
      
#### Frontend
- [ ] Initialize React Native Project
- [ ] Setup routing
- [ ] Clerk Authentication
