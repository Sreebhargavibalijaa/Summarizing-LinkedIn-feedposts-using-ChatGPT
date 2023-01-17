import openai
limit = input("limit")
from linkedin_api import Linkedin

# Authenticate using any Linkedin account credentials
api = Linkedin('^^^^^^', "***********")  ##linkedin account credentails

# GET a profile
profile = api.get_profile('balija-sree-bhargavi-b7638517a')
# GET a profiles contact info
contact_info = api.get_profile_contact_info('billy-g')

# GET 1st degree connections of a given profile
connections = api.get_profile_connections('balija-sree-bhargavi-b761038517a')


#api.get_feed_posts to get feed posts based on limit specified
for j in range(limit):

    openai.api_key = "^^^^^^^^^^^"
    url = api.get_feed_posts(limit,offset=0, exclude_promoted_posts=True)[j]["url"]
    ask =   api.get_feed_posts(limit, offset=0, exclude_promoted_posts=True)[j]["content"]
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=ask,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )

    text = response['choices'][0]['text']

    print ('here is the summary:')
    print (text)
    print("Click here to view the post:")
    print(url)
    print ("\n")