# following this tutorial https://www.geeksforgeeks.org/scraping-amazon-product-information-using-beautiful-soup/

# importing bs4 and requests
from bs4 import BeautifulSoup
import requests

CSVFILE = open("output.csv", "a") # my output file with the finished data


# don't fully understand this, added it because helps with websites not flagging as spam ? (look into it)
HEADERS = ({'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64)
                AppleWebKit/537.36 (KHTML, like Gecko)
                    Chrome/44.0.2403.157 Safari/537.36',
                           'Accept-Language': 'en-US, en;q=0.5'})
 
webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")

# Finding all the id's for the values we want

