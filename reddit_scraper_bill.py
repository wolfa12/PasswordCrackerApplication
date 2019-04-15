import praw
# import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='qIv6ZQYkFNpvAQ', \
                     client_secret='IkWl2ulNzZrTpBjCQipQzskq-9A', \
                     user_agent='passwordcracker', \
                     username='pwcracker_throwaway', \
                     password='cse447112!')
                     
# get URL for each comment

# https://www.reddit.com/user/thisisbillgates
print("Bill Gates's top comments of all time")
for comment in reddit.redditor('thisisbillgates').comments.new(limit=5):
    print(comment.body.split('\n', 1)[0][:79])

# top submissions
print("Bill Gates's top 10 submissions")
for topsub in reddit.redditor('thisisbillgates').submissions.top('all', limit=5):
    print(topsub.title)

# controversial
# for cont in reddit.redditor('thisisbillgates').controversial('all', limit=5):
#     print(cont.title)


# # old from facebook scraper
# import requests
# from bs4 import BeautifulSoup
#
# facebookpage_url = 'https://www.facebook.com/tara.bite.33'
# # need to do error handling here
# response = requests.get(facebookpage_url)
# html = response.content
#
# soup = BeautifulSoup(html, features="lxml")
# #print(soup.prettify())
# # do more here of course
#
# # get the titles
# # <ul class="uiList fbProfileEditExperiences _4kg _4ks"> - contains major and school
#
# # write to a file (for testing)
# file = open("testfile.txt", "w")
# file.write(soup.prettify())
# file.close()



# personal use script: PZ4WFNV5lz-rYQ
# secret	W1eGx-m9JL7MtwIh27MIJ1U9M3U
