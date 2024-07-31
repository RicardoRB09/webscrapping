import requests, os, time, csv
from bs4 import BeautifulSoup

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


clear_terminal()

print('Scrapping "Books to Scrape" in progress... please wait ⌛...')

complete_list = []
books = []

mainUrl = 'https://books.toscrape.com/'


class Book:
    def __init__(self, title = '', upc = '', price = '', imageAddress = '', description = ''):
        self.upc = upc
        self.price = price
        self.title = title
        self.imageAddress = imageAddress
        self.description = description


def scrapSubPages(subPageIndex):
    newBook = Book()
    response = requests.get(mainUrl+subPageIndex)
    beautifulResponse = BeautifulSoup(response.content, 'html.parser')
    
    newBook.upc = beautifulResponse.find_all("td")[0].text
    newBook.title = beautifulResponse.find('li', class_='active').text
    newBook.price = beautifulResponse.find('p', class_='price_color').text
    newBook.imageAddress = mainUrl + '/'.join(beautifulResponse.find("img").attrs['src'].split('/')[2:])
    newBook.description = beautifulResponse.find('article', class_='product_page').find('p', class_='').text

    books.append(newBook)
    # print('\n', 'UPC: ', newBook.upc ,'\n','Title: ', newBook.title,'\n','Price: ', newBook.price,'\n','Image: ', newBook.imageAddress, '\n','Description: ', newBook.description,'\n')




#  ++++ First page process  ++++
response = requests.get(mainUrl)
beautifulResponse = BeautifulSoup(response.content, 'html.parser')

olTagData = beautifulResponse.find('ol', class_='row')
liFromOlTagData = olTagData.find_all('li')

for book in liFromOlTagData:
    scrapSubPages(book.find('h3').find('a').attrs['href'])

pageTwoAddr = beautifulResponse.find('li', class_='next').find('a').attrs['href']
pageTwoURL = mainUrl + pageTwoAddr




#  ++++ Second page process  ++++
clear_terminal()
print('First page Scrapped! Second page in progress... Be patient please 🧐...')
response = requests.get(pageTwoURL)
beautifulResponse = BeautifulSoup(response.content, 'html.parser')

olTagData = beautifulResponse.find('ol', class_='row')
liFromOlTagData = olTagData.find_all('li')

for book in liFromOlTagData:
    scrapSubPages('catalogue/' + book.find('h3').find('a').attrs['href'])

pageThreeAddr = beautifulResponse.find('li', class_='next').find('a').attrs['href']
pageThreeURL = mainUrl + 'catalogue/' + pageThreeAddr




#  ++++ Third page process  ++++
clear_terminal()
print('Second page Scrapped! We are almost there!!... Just a sec 😎...')
response = requests.get(pageThreeURL)
beautifulResponse = BeautifulSoup(response.content, 'html.parser')

olTagData = beautifulResponse.find('ol', class_='row')
liFromOlTagData = olTagData.find_all('li')

for book in liFromOlTagData:
    scrapSubPages('catalogue/' + book.find('h3').find('a').attrs['href'])




clear_terminal()
print('👏👏 Scrapping complete successfully! 👏👏')
time.sleep(2)
clear_terminal()
# # print('📚📚📚 Books Scrapped 📚📚📚 \n')
# # # Print the first 50 books and its correspoding data
# # for cont, book in enumerate(books, start=1 ):
# #     if cont < 51:
# #         print(f'''{cont} - {book.title}
              
# # UPC: {book.upc}

# # Price: {book.price}

# # Image: {book.imageAddress}

# # Description: {book.description}


# #               ''')
        
        
# # # +++ Creating the CSV file +++
input('⚠️⚠️⚠️ Press any key to continue... ⚠️⚠️⚠️')
clear_terminal()
print('Creating a CSV file... hold on! Dont go! 🥹🥹')

with open('books.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    titles = ["Title", "UPC", "Price", 'Image', 'Description']
    
    writer.writerow(titles)
    
    for cont, book in  enumerate (books, start=1):
        if cont < 51:
            writer.writerow([book.title, book.upc, book.price, book.imageAddress, book.description])

clear_terminal()
print('Ready!✅ Your file is named "books.csv"')