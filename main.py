import time
import comment
import sentiment
import analysis


def collect_comments(video_id):
    # add platform functionality (reddit, youtube, twitter?)
    c = comment.Comment(video_id)
    c.build_comment_list()
    return c.strip_comments()


if __name__ == '__main__':
    # Gather user input and specifications (Seperate module????)
    video_id = "XEF1VHLlPWg"

    start = time.time()
    print("Collecting Comments...")
    all_comments = collect_comments(video_id)

    print("Determining sentiments...")
    s = sentiment.Sentiment()
    for text in all_comments:
        s.generate_vader_instance(text)

    print("Writing sentiments to CSV file...")
    filename = s.parse_sentiments(video_id)

    end = time.time()
    print("DONE. That took", "%.2f" % (end - start), "seconds.")

    print("ANALYSIS: ")
    a = analysis.Analysis(filename)
    a.investigate_file()
    a.display_results()
