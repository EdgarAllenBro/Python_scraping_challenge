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

        #create a class for book objects to store each set of data
        class Book:
            def __init__(self,title,price,avail):
                self.title = title
                self.price = price
                self.avail = avail
        shelf = []

        #use xpath to grab the title price and availability from html
        titles = content.xpath("//h3/a/@title")
        prices = content.xpath("//p[@class='price_color']/text()")
        avail = content.xpath("//div[@class='product_price']/p[last()]/@class")


        #loop through title price and avail lists to create my book objects
        for i in range(len(titles)):
            newBook = Book(titles[i],prices[i],avail[i])
            shelf.append(newBook)
        #write each object as a row in the csv file
        for i in range(len(titles)):
            writer.writerow([titles[i],prices[i],avail[i]])

#file is closed at the end of the with open()