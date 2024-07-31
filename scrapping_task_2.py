import requests, os, time, csv
from bs4 import BeautifulSoup

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
clear_terminal()

print('Scrapping "Books to Scrape" in progress... please wait...')

complete_list = []

mainUrl = 'https://books.toscrape.com/'



#  ++++ First page process  ++++ 
response = requests.get(mainUrl)
beautifulResponse = BeautifulSoup(response.content, 'html.parser')

olTagData = beautifulResponse.find('ol', class_='row')
liFromOlTagData = olTagData.find_all('li')

for element in liFromOlTagData:
    complete_list.append(element.find('h3').find('a').string)
    
pageTwoAddr = beautifulResponse.find('li', class_='next').find('a').attrs['href']
pageTwoURL = mainUrl + pageTwoAddr




#  ++++ Second page process  ++++ 
response = requests.get(pageTwoURL)
beautifulResponse = BeautifulSoup(response.content, 'html.parser')

olTagData = beautifulResponse.find('ol', class_='row')
liFromOlTagData = olTagData.find_all('li')

for element in liFromOlTagData:
    complete_list.append(element.find('h3').find('a').string)

pageThreeAddr = beautifulResponse.find('li', class_='next').find('a').attrs['href']
pageThreeURL = mainUrl + 'catalogue/' + pageThreeAddr




#  ++++ Third page process  ++++ 
response = requests.get(pageThreeURL)
beautifulResponse = BeautifulSoup(response.content, 'html.parser')

olTagData = beautifulResponse.find('ol', class_='row')
liFromOlTagData = olTagData.find_all('li')

for element in liFromOlTagData:
    complete_list.append(element.find('h3').find('a').string)

# pageTwoAddr = beautifulResponse.find('li', class_='next').find('a').attrs['href']
# pageTwoURL = mainUrl + pageTwoAddr




clear_terminal()
print('Scrapping complete!')
time.sleep(1)
clear_terminal()

# Print the first 50 titles
for cont, element in enumerate(complete_list, start=1 ):
    if cont < 51:
        print(f'{cont} -',  element.text, end="\n\n")  