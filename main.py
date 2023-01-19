
limit = input("Enter the count of posts\n")
from openAi import *
from linkedinapi import *
from linkedin_api import Linkedin

# Authenticate using any Linkedin account credentials
limit = int(limit)
output  = feed_posts(limit) # Post_URN will specfic to the each linkedin post
#print(output)
if output == "":
    print("No feedposts on your profile")
else:
    for j in range(len(output)):
        print("Feed Post:" + str(j))
        content_summary = chatgpt_summary(output[j][0])
        comments_summary = chatgpt_summary(output[j][2])
        print(" 1) Here is the content summary of the feed post:\n")
        if content_summary == "":
            print("No content to this post")
        else:
            print(content_summary)
        print(" 2) Click here to navigate to the post " + str(output[j][1]))
        print("\n 3) Here is the comments summary of the feed post:\n")
        if comments_summary == "":
            print("No comments to this post")
        else:
            print(comments_summary)

# content summary can be checked specific key words like "microsoft", "Linkedin", "Amazon"  or "Google" if you want to segreagte the posts based on the content summary provided by the chatgpt
