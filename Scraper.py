from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

# url = "https://www.amazon.com/s?k=iphone&ref=nb_sb_noss_2"
url = "https://www.amazon.com/s?k=dog+leash&crid=J1BUVMV43F9M&sprefix=dog+le%2Caps%2C218&ref=nb_sb_ss_i_1_6"
price = []
name = []
shipping = []

uClient = uReq(url)
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

for container in page_soup.find_all("div", { "class": "sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28"}):
    price_html = container.find("span", attrs={"class": "a-offscreen"})
    name_html = container.find("span", attrs={"class": "a-size-medium a-color-base a-text-normal"})
    # shipping_html = container.find("span", attrs={"dir": "auto"})

    if price_html is not None:
        price.append(price_html.text.strip())
    else:
        price.append("$0")

    if name_html is not None:
        name.append(name_html.text.strip())
    else:
        name.append("Unknown")

    # if shipping_html is not None:
    #     print(shipping_html)
    #     shipping.append(shipping_html.text.strip())
    # else:
    #     shipping.append("Unknown")

with open("products.csv", "r+") as file:
    file.write("Product,Price,Shipping \n")
    for i in range(len(name)):
        file.write(name[i].replace(",", " |") + ", " + price[i] + "\n")

