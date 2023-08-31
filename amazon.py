# importing bs4 and requests
from bs4 import BeautifulSoup
import requests
import time

def main(URL):
    CSVFILE = open("output.csv", "a") # creates my output file with the finished data


# don't fully understand this, added it because helps with websites not flagging as spam ? (look into it)
    HEADERS = ({"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"})

    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")

# getting title of product
    try:
        title = soup.find("span", {"id": 'productTitle'})
 
        # Inner NavigableString Object
        title_value = title.string
 
        # Title as a string value
        title_string = title_value.strip().replace(',', '')
        time.sleep(2)

    except AttributeError:
        title_string = "NA" # in case its not there
        print("product Title = ", title_string)

    CSVFILE.write(f"{title_string},") # outputing found data to the csv file

# now doing for price
    try:
        price = soup.find("span", {'class': 'a-offscreen'}).string.strip().replace(',', '')
        time.sleep(2)
    except AttributeError:
        price = "NA" # if its not there
        print("Products price = ", price)

 
    # saving
    CSVFILE.write(f"{price},")

# closing csv (done at the end)
    CSVFILE.close();

if __name__ == "__main__":
    file = open("urls.txt", "r")

    for links in file.readlines():
        main(links)