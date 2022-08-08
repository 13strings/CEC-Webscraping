# following this tutorial https://www.geeksforgeeks.org/scraping-amazon-product-information-using-beautiful-soup/

# importing bs4 and requests
from bs4 import BeautifulSoup
import requests

def main(URL):
    CSVFILE = open("output.csv", "a") # creates my output file with the finished data


# don't fully understand this, added it because helps with websites not flagging as spam ? (look into it)
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")

# Finding all the id's for the values we want

    # title id = "productTitle"
    # number of reviews id = "acrCustomerReviewText"
    # price class = a-offscreen / aria-hidden = "true" ????

    # Product Details
        # classes 
        # "a-color-secondary a-size-base prodDetSectionEntry" = "Wattage", "Color Temperature", "Color Rendering Index", "CRI", "Luminous Flux", "Shape", "Part Number", "Manufacturer", "Color", "Item model number"
            # "a-size-base prodDetAttrValue" = the value we want
        
        # for ASIN
            # "a-colr-secondary a-size-base prodDetSectionEntry" = ASIN
            # "a-sixe-base prodDetAttrValue" = what we want

# getting title of product
    try:
        title = soup.find("span",
                          attrs={"id": 'productTitle'})
 
        # Inner NavigableString Object
        title_value = title.string
 
        # Title as a string value
        title_string = title_value.strip().replace(',', '')

    except AttributeError:
        title_string = "NA" # in case its not there
        print("product Title = ", title_string)

    CSVFILE.write(f"{title_string},") # outputing found data to the csv file

    # now doing for price
    try:
        price = soup.find("span", 
                            attrs={'id': 'priceblock_ourprice'}).string.strip().replace(',', '')
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