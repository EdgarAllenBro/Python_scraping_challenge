from lxml import html #requires pip of lxml and requests
import requests
import csv

with open('./book.csv', 'w', newline='') as csvFile: #open csv file
    writer = csv.writer(csvFile)
    writer.writerow(['title','price','avail']) #create writer and create first row for column names
    #loop through each page of the site
    for i in range(1,51):
        page = requests.get('http://books.toscrape.com/catalogue/category/books_1/page-{}.html'.format(i))
        content = html.fromstring(page.content)

        #use xpath to grab the title price and availability from html
        titles = content.xpath("//h3/a/@title")
        prices = content.xpath("//p[@class='price_color']/text()")
        avail = content.xpath("//div[@class='product_price']/p[last()]/@class")

        #then loop thropugh these lists creating a row for each set of data.
        for i in range(len(titles)):
            writer.writerow([titles[i],prices[i],avail[i]])

#file is closed at the end of the with open()