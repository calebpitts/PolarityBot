'''
Class that gathers comments from a given YouTube video id attribute.
Returns a list of comments stripped of HTML tags and entities.
'''
import json
from urllib.error import HTTPError
from urllib.request import urlopen
from html.parser import HTMLParser

BASE_REQUEST_URL = "https://www.googleapis.com/youtube/v3/commentThreads?"
PART = "part=snippet&videoId="


# Strips text of HTML tags
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


class Comment():
    def __init__(self, video_id, user_api_key):
        self.video_id = video_id
        self.user_api_key = user_api_key
        self.comment_list = []
        self.stripped_comments = []

    # Builds an initial url with a video id that collects the first page of comments
    def build_initial_url(self, search_query):
        return BASE_REQUEST_URL + PART + search_query + "&key=" + self.user_api_key

    # Builds a url with a video id's page token linking to the next page of comments
    def build_next_url(self, search_query, pageToken):
        return BASE_REQUEST_URL + "pageToken=" + pageToken + "&" + PART + search_query + "&key=" + self.user_api_key

    # Gets JSON response
    def get_result(self, url):
        response = None
        response = urlopen(url)
        json_txt = response.read().decode(encoding="utf-8")
        response.close()
        return json.loads(json_txt)

    # Accesses 'textDisplay' component of JSON output where the comment is stored
    def get_comments(self, json_result):
        page_comments = []
        for item in json_result['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            page_comments.append(comment)
        return page_comments

    # Strips HTML tags and entities
    def strip_tags(self, comment):
        s = MLStripper()
        s.feed(comment)
        return s.get_data()

    # Iteratively calls 'strip_tags' on each comment in 'comments'
    def strip_comments(self):
        for comment in self.comment_list:
            self.stripped_comments.append(self.strip_tags(comment))
        return self.stripped_comments

    def build_comment_list(self):
        pageToken = None
        try:
            # json_result is the response we get back from opening our custom url.
            json_result = self.get_result(self.build_initial_url(self.video_id))
            # 'get_comments' accesses all the comments on the current page.
            self.comment_list = self.comment_list + self.get_comments(json_result)
            try:
                pageToken = json_result['nextPageToken']
            except KeyError:
                print("MSG: No more results. Only one page of results.")
        except HTTPError:
            print("\nERROR: Failed to open url. Might be due to an invalid API key or video ID.\n")
        # Collects comments on the next pageToken until there is no pageToken present
        # pageToken exists when there is another page of comments.
        while pageToken != None:
            if len(self.comment_list) > 5000:
                print("Max comment count reached. Analyzing first 5000 comments...")
                break
            try:
                next_json_result = self.get_result(self.build_next_url(self.video_id, pageToken))
            except HTTPError:
                print("\nERROR: Failed to open pageToken url. Returning current list of comments..\n")
                break
            self.comment_list = self.comment_list + self.get_comments(next_json_result)
            try:
                pageToken = next_json_result['nextPageToken']
            except KeyError:
                print("MSG: Reached end of comments.")
                break
