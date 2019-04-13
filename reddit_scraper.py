
# old from facebook scraper 
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
