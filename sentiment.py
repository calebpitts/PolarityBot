import csv
from nltk.sentiment import SentimentIntensityAnalyzer


class Sentiment():
    def __init__(self):
        self.sentiments = []

    # Utlizes nltk module to assign a sentiment or 'polarity score' for the text parameter.
    def generate_vader_instance(self, text):
        vader_analyzer = SentimentIntensityAnalyzer()
        text_sentiment = vader_analyzer.polarity_scores(text)
        text_sentiment["text"] = text
        self.sentiments.append(text_sentiment)

    # Writes sentiments to CSV file named polarity_[VIDEO_ID]
    def parse_sentiments(self, video_id):
        keys = self.sentiments[0].keys()
        filename = "polarity_" + video_id + ".csv"
        with open(filename, "w") as csvfile:
            writer = csv.DictWriter(csvfile, keys)
            writer.writeheader()
            writer.writerows(self.sentiments)
        return filename
