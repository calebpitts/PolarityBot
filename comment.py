################################
#  CommentAPI Project 6/30/18  #
################################
# Class that gathers comments from a given YouTube video id attribute.
# Returns a list of comments stripped of HTML tags and entities

import json
import sentiment
from urllib.error import HTTPError
from urllib.request import urlopen
from html.parser import HTMLParser

YOUTUBE_DATA_API_KEY = "AIzaSyAIyVr67OekIlgLvFVS_5N8sVFV5GVk3a4"
BASE_REQUEST_URL = "https://www.googleapis.com/youtube/v3/commentThreads?"
PART = "part=snippet&videoId="


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


'''
# Builds an initial url with a video id that collects the first page of comments
def build_initial_url(search_query):
    return BASE_REQUEST_URL + PART + search_query + "&key=" + YOUTUBE_DATA_API_KEY


# Builds a url with a video id's page token linking to the next page of comments
def build_next_url(search_query, pageToken):
    return BASE_REQUEST_URL + "pageToken=" + pageToken + "&" + PART + search_query + "&key=" + YOUTUBE_DATA_API_KEY


# Gets JSON response
def get_result(url):
    response = None
    response = urlopen(url)
    json_txt = response.read().decode(encoding="utf-8")
    return json.loads(json_txt)


# Accesses 'textDisplay' component of JSON output where the comment is stored
def get_comments(json_result):
    page_comments = []
    for item in json_result['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        page_comments.append(comment)
    return page_comments


# Strips HTML tags and entities
def strip_tags(comment):
    s = MLStripper()
    s.feed(comment)
    return s.get_data()


# Iteratively calls 'strip_tags' on each comment in 'comments'
def strip_comments(comments):
    stripped_comments = []
    for comment in comments:
        stripped_comments.append(strip_tags(comment))
    return stripped_comments


def main(video_id):
    pageToken = None
    # Get video module OR have Comment class and pass video_id in as a parameter
    # with unique list of comments as output specific to that video id
    video_id = "XEF1VHLlPWg"
    comments = []

    try:
        json_result = get_result(build_initial_url(video_id))
        comments = comments + get_comments(json_result)
        try:
            pageToken = json_result['nextPageToken']
        except KeyError:
            print("MSG: No more results. Only one page of results.\n")
    except HTTPError:
        print("\nERROR: Failed to open url\n")

    # Collects comments on the next pageToken until there is no pageToken present
    while pageToken != None:
        try:
            next_json_result = get_result(build_next_url(video_id, pageToken))
        except HTTPError:
            print("\nERROR: Failed to open pageToken url. Returning current list of comments..\n")
            break

        comments = comments + get_comments(next_json_result)

        try:
            pageToken = next_json_result['nextPageToken']
        except KeyError:
            print("MSG: No more results.\n")
            break

    stripped_comments = strip_comments(comments)
    print(stripped_comments)
    print("NUM OF COMMENTS: ", len(stripped_comments))
'''

if __name__ == '__main__':
    print("Please enter video id")
    video_id = input()
    print("Running...")
    main(video_id)
    print("DONE")
