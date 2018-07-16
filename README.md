# PolarityBot
Calculates a "polarity score" and other notable stats on specific Youtube videos. The Polarity Score represents the overall viewer sentiment towards the video on a scale from -1 to 1 with one being the best sentiment and -1 being the worst.

## Installation of Libraries
You need python3 and pip installed to get these libraries.
Run:
```pip install nltk```

```pip install csv```

```pip install json```
    
You'll also need vader_lexicon.
Install vader_lexicon once you go into a python console:
    
    import nltk
    nltk.download('vader_lexicon')
## Setting up Youtube API Credentials
1. Go to https://console.developers.google.com/project and sign in to your google account
1. Click on Project -> Create Project
1. Select Youtube Data API
1. Click Enable and follow the prompted steps to get your credentials

## Select YouTube Video ID
To analyze a video, go on Youtube and get the video id found at the end of the url.
For example:
https://www.youtube.com/watch?v=YI3HD0HAz74
yields a video id of ```YI3HD0HAz74```. It's always found at the end of the url after ```v=```

## Running the Script
The script will save a CSV to the local directory so go to the directory you want to store the CSV file before running the script.
Run ```python3 main.py```


