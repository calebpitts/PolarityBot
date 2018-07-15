import pandas as pd


class Analysis():
    def __init__(self, filename):
        self.filename = filename

    def parse_file(self):
        # PARSE FILE. REMOVE 0's for undetermined sentiments
        df = pd.read_csv(self.filename)
        return df

    def investigate_file(self):
        df = self.parse_file()
        mean = df["compound"].mean()
        print("MEAN COMPOUND SENTIMENT: ", "%.2f" % mean)

    def display_results(self):
        # Display bar graphs, pie charts, statistics, ect.
        pass
