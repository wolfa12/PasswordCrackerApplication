import praw
# import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='qIv6ZQYkFNpvAQ', \
                     client_secret='IkWl2ulNzZrTpBjCQipQzskq-9A', \
                     user_agent='passwordcracker', \
                     username='pwcracker_throwaway', \
                     password='cse447112!')

# get URL for each comment
# allow user to click to view more
# print all results to the page

# https://www.reddit.com/user/thisisbillgates
print("Bill Gates's top comments of all time")
for comment in reddit.redditor('thisisbillgates').comments.new(limit=5):
    print(comment.body.split('\n', 1)[0][:79])

# top submissions
print("Bill Gates's top 10 submissions")
for topsub in reddit.redditor('thisisbillgates').submissions.top('all', limit=5):
    print(topsub.title)


# personal use script: PZ4WFNV5lz-rYQ
# secret	W1eGx-m9JL7MtwIh27MIJ1U9M3U
