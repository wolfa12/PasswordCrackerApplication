# from urllib2 import urlopen
# urlopen(https://www.facebook.com/tara.bite.33)
import requests
from bs4 import BeautifulSoup

facebookpage_url = 'https://www.facebook.com/tara.bite.33'
response = requests.get(facebookpage_url)
html = response.content

soup = BeautifulSoup(html)
#print(soup.prettify())

# write to a file (for testing)
file = open("testfile.txt", "w")
file.write(soup.prettify())
file.close()
