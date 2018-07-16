import matplotlib
import pandas as pd


class Analysis():
    def __init__(self, filename):
        self.filename = filename
        self.mean_sentiment = 0
        self.max_sentiment = 0
        self.min_sentiment = 0
        self.counts = None

    # Opens the CSV file and gathers shape of the dataframe.
    def parse_file(self):
        df = pd.read_csv(self.filename)
        num_comments = df.shape[0] - 1
        df = self.clean_df(df)
        return df, num_comments

    # Removes all rows with a compound score of 0. A polarity score of 0
    # indicates that the nltk sentiment analysis could not determine the
    # polarity for that comment. Thus, I remove it to mitigate the impact
    # on determined polarity scores that are not 0.
    def clean_df(self, df):
        df = df[df["compound"] != 0]
        return df

    # Stores compound mean, frequency counts, and other interesting information.
    def investigate_file(self):
        ranges = [-1.0, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.0]

        df, num_comments = self.parse_file()

        # Collects the mean, max, and min sentiment from the dataframe.
        self.mean_sentiment = df["compound"].mean()
        self.max_sentiment = df["compound"].max()
        self.min_sentiment = df["compound"].min()

        # Groups the count of values based on where the fall within the ranges declared above.
        self.counts = df.groupby(pd.cut(df["compound"], ranges))["compound"].count()

    # Displays results found in 'investigate_file' to the console.
    def display_results(self):
        print("MEAN Sentiment:", "%.2f" % self.mean_sentiment)
        print("MAX  Sentiment:", self.max_sentiment)
        print("MIN  Sentiment:", self.min_sentiment)
        print("\nDistribution of Sentiment Counts:")
        print(self.counts.to_string(header=None))
