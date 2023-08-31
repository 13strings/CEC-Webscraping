import requests
from bs4 import BeautifulSoup

#def main(URL):
#    CSVFILE = open("output.csv", "a") # creates my output file with the finished data

URL = "https://www.homedepot.com/p/Sylvania-85-Watt-Equivalent-BR40-Dimmable-LED-Light-Bulb-in-5000K-2-Pack-40787/315146217"

page = requests.get(URL)

#soup = BeautifulSoup(page.content, "html.parser")

#results = requests.find_all("div", class_ = "product-details__badge-title--wrapper")

#for result in results:
  #  title = result.find("h1", class_ ="sui-h4-bold sui-line-clamp-unset")

   # print(title)

with open('results.txt', 'w') as f:
    f.write('page.text')