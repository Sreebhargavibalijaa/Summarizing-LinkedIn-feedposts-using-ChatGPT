
def feed_posts(self,limit):
    limit = int(limit)
    for j in range(limit):

        openai.api_key = "************"
        url = api.get_feed_posts(limit,offset=0, exclude_promoted_posts=True)[j]["url"]
        urn_index = url.index('activity') + len('activity')+1
        finish_index = len(url)


def post_comments(self):
    comment_count = 1
    comments = "you are a useful friendly summarizer. Summarise the following\n"
    from linkedin_api import Linkedin
    api = Linkedin('*************', "***************")  ##linkedin account credentails

    for j in  range(comment_count):
        comments = comments + api.get_post_comments(Post_URN, comment_count)[j]["comment"]["values"][0]["value"] #  uril useful 


    return comments
