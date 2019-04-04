import facebook
import requests

token = 'EAAFymtofpnUBAEPAMB2XFYMdzdFZCPBexzOcKUX1d3JAKlULvlJjbSOjas5ZCSdQ0ylJu0V7gsa1gMEJK26IvudioCWPG32RWJh0B9I1KeAogW6Ebemsk7juA6WZAoha7nZCNoZAOOUyrs8ooa6ZBulifFtJh15rlbTqxSrl0sxAZDZD'
v3.2
graph = facebook.GraphAPI(access_token, version = 3.2)

# old version
# from urllib2 import urlopen
# urlopen(https://www.facebook.com/tara.bite.33)
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
#
# # write to a file (for testing)
# file = open("testfile.txt", "w")
# file.write(soup.prettify())
# file.close()
