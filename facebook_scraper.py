# import facebook
# import requests
#
# access_token = 'EAAFymtofpnUBAEPAMB2XFYMdzdFZCPBexzOcKUX1d3JAKlULvlJjbSOjas5ZCSdQ0ylJu0V7gsa1gMEJK26IvudioCWPG32RWJh0B9I1KeAogW6Ebemsk7juA6WZAoha7nZCNoZAOOUyrs8ooa6ZBulifFtJh15rlbTqxSrl0sxAZDZD'
#
# graph = facebook.GraphAPI(access_token)
# user = tara.bite.33
# profile = graph.get_object(user)
# posts = graph.get_connections(profile["id"], "posts")
#
# print(posts)

# post = graph.get_object(id='id', fields='message')
# print(post['message'])

# other version
# source = requests.get(https://www.facebook.com/tara.bite.33)
# old version
# from urllib2 import urlopen
# urlopen(https://www.facebook.com/tara.bite.33)
import requests
from bs4 import BeautifulSoup

facebookpage_url = 'https://www.facebook.com/tara.bite.33'
# need to do error handling here
response = requests.get(facebookpage_url)
html = response.content

soup = BeautifulSoup(html, features="lxml")
#print(soup.prettify())
# do more here of course

# get the titles
# <ul class="uiList fbProfileEditExperiences _4kg _4ks"> - contains major and school 

# write to a file (for testing)
file = open("testfile.txt", "w")
file.write(soup.prettify())
file.close()
