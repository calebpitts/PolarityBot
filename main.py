import time
import comment
import sentiment
import analysis
from urllib.error import HTTPError


# Displays welcome message.
def welcome():
    print("------------------")
    print("|  POLARITY BOT  |")
    print("|  @version 1.0  |")
    print("| by Caleb Pitts |")
    print("------------------")
    print("Hi there! This is PolarityBot.")
    print("Ready to analyze the polarity of YouTube comments..")
    print("\nNOTES:\n  (1) Please look at the README.md file before running the script.")
    print("  (2) Sentiment analysis is measured on a scale of -1.0 to 1.0 with ")
    print("      -1.0 being the worst possible sentiment and 1.0 being the best.")
    print("  (3) A CSV file containing polarity scores for each comment will be ")
    print("      saved locally from wherever you run this script.")
    print("  (4) The query may take some time for videos with many comments. ")
    print("      This bot maxes out at 5000 comments (for the sake of time). ")


# Collects video id and user's API key.
def gather_user_input():
    print("\nPlease enter your valid YouTube API key: ", end="")
    user_api_key = input()

    print("Please enter the YouTube video id found at the end of the video's url: ", end="")
    video_id = input()

    while True:
        print("Proceed? (Y/N): ", end="")
        begin = input().strip().upper()
        if begin == "Y" or begin == "N":
            break
        else:
            print("Invalid Input.")

    return user_api_key, video_id, begin


# Collects all comments corresponding to the specified video id.
def collect_comments(video_id, user_api_key):
    c = comment.Comment(video_id, user_api_key)
    c.build_comment_list()

    # Strips comments of html tags, tabs, excessive spacing ect.
    return c.strip_comments()


# Asks the user if they would like to restart the script.
def pose_restart():
    while True:
        print("Would you like to quit or restart? (Q/R): ", end="")
        end = input().strip().upper()
        if end == "Q" or end == "R":
            break
        else:
            print("Invalid Input.")
    return end


if __name__ == '__main__':
    welcome()
    while True:
        user_api_key, video_id, begin = gather_user_input()

        if begin == "Y":
            start = time.time()
            print("\nCollecting Comments...")
            all_comments = collect_comments(video_id, user_api_key)

            if len(all_comments) == 0:  # Breaks if the url is broken or there are no comments to analyze.
                print("Please restart with a valid API key and video ID. Goodbye!")
                break

            print("Determining sentiments...")
            s = sentiment.Sentiment()
            for text in all_comments:
                s.generate_vader_instance(text)

            print("Writing sentiments to CSV file...")
            filename = s.parse_sentiments(video_id)

            end = time.time()
            print("DONE. That took", "%.2f" % (end - start), "seconds.\n")

            print("-" * 20)
            print("|     ANALYSIS     |")
            print("-" * 20)

            a = analysis.Analysis(filename)
            a.investigate_file()
            a.display_results()

            print("\nYou can view the CSV file locally from wherever you ran this script.")

            end = pose_restart()
            if end == "Q":
                print("Quitting PolarityBot... Goodbye!")
                break
            elif end == "R":
                print("Restarting...\n\n")
        elif begin == "N":
            end = pose_restart()
            if end == "Q":
                print("Quitting PolarityBot... Goodbye!")
                break
            elif end == "R":
                print("Restarting...\n\n")
