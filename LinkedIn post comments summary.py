import openai
Post_URN = input("input the post urn")
comment_count = 10
comments  = ""
from linkedin_api import Linkedin
api = Linkedin('******************', "**************")  ##linkedin account credentails

for j in  range(comment_count):
 comments = comments + api.get_post_comments(Post_URN, comment_count)[j]["comment"]["values"][0]["value"]


openai.api_key = "^^^^^^"  # you can get the openAi key from https://openai.com/api/
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=comments,
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
print ("\n")
