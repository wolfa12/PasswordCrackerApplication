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

# write to a file (for testing)
file = open("testfile.txt", "w")
file.write(soup.prettify())
file.close()
