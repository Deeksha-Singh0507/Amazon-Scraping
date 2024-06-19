import requests
from bs4 import BeautifulSoup
import csv

def scrape_amazonlaptop_data():
    Product_names = []
    Prices = []
    Descriptions = []
    Reviews = []

    for page_num in range(1, 7):
        url = "https://www.flipkart.com/search?q=laptop+under+50000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_5_13_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_5_13_na_na_ps&as-pos=5&as-type=RECENT&suggestionId=laptop+under+50000&requestId=6fb41bd9-bf09-4224-b2b1-a64931db066d&as-searchtext=laptop+under+&page=" + str(page_num)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")

        names = soup.find_all("div", class_="KzDlHZ")
        for i in names:
            name = i.text.strip() # added strip() to remove leading/trailing whitespaces
            Product_names.append(name)

        prices = soup.find_all("div", class_="Nx9bqj _4b5DiR") 
        for i in prices:
            price = i.text.strip() # added strip() to remove leading/trailing whitespaces
            Prices.append(price)

        descriptions = soup.find_all("ul", class_="G4BRas") # assuming description is within a span tag
        for i in descriptions:
            description = i.text.strip() # added strip() to remove leading/trailing whitespaces
            Descriptions.append(description)

        reviews = soup.find_all("div", class_="XQDdHH")
        for i in reviews:
            review = i.text.strip() # added strip() to remove leading/trailing whitespaces
            Reviews.append(review)

    return Product_names, Prices, Descriptions, Reviews

def write_to_csv(product_names, prices, descriptions, reviews):   
    with open("Amazonlaptop _data.csv", "w", newline="", encoding="utf-8") as csvfile:
         writer = csv.writer(csvfile)
         writer.writerow(["Product Name", "Price", "Description", "Review"])
         for data in zip(product_names, prices, descriptions, reviews):
             writer.writerow(data)

if __name__ == "__main__":
    product_names, prices, descriptions, reviews = scrape_amazonlaptop_data()     
    write_to_csv(product_names, prices, descriptions, reviews)
    print("Data has been written to Amazonlaptop_data.csv")

    

