# PolarityBot
Calculates a "polarity score" and other notable stats on specific Youtube videos. The Polarity Score represents the overall viewer sentiment towards the video on a scale from -1 to 1 with one being the best sentiment and -1 being the worst.

## Installation of Libraries
You need python3 and pip installed to get these libraries.

Run:

```pip install nltk```

```pip install csv```

```pip install json```
    
You'll also need to install ```vader_lexicon```.
Go into a python console and run:
    
    import nltk
    nltk.download('vader_lexicon')
## Setting up Youtube API Credentials
1. Go to https://console.developers.google.com/project and sign in to your google account.
1. Click on Project -> Create Project
1. Select Youtube Data API.
1. Click Enable and follow the prompted steps to get your credentials.

## Select YouTube Video ID
To analyze a video, go on Youtube and get the video id found at the end of the url.
For example:
https://www.youtube.com/watch?v=YI3HD0HAz74
yields a video id of ```YI3HD0HAz74```. It's always found at the end of the url after ```v=```

## Running the Script
The script will save a CSV to the local directory so go to the directory you want to store the CSV file before running the script.
Run ```python3 main.py```

## Interpreting the Results
The script will output the mean polarity score of all the comments and the min, and max polarity score in that set of comments. It also gives a distribution of the number of comments within each polarity score interval. 

A CSV file with all the scores and comments will be saved in a CSV file named ```polarity_[VIDEO ID].csv```. You can manipulate those statistics however you like. 

Enjoy! Let me know if you find any bugs, want to contribute or just talk.
