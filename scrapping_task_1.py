
import requests, os, time
from bs4 import BeautifulSoup

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
clear_terminal()

print('Scrapping phrases in progress... please wait...')

complete_list = []

mainUrl = 'https://quotes.toscrape.com'

response = requests.get(mainUrl)
beautifulResponse = BeautifulSoup(response.content, 'html.parser')
# print(beautifulResponse.prettify())
# print(beautifulResponse.title.text)
# print(beautifulResponse.title.string)

first_list = beautifulResponse.find_all('span', class_= 'text')

# print(dir(title_list))
# element = title_list[0]
# print(dir(element))
# print(element.text)

# ++++ Add first page phrases ++++
for cont, element in enumerate(first_list, start=1):
    complete_list.append(element)




navContent = beautifulResponse.find('nav')
pageTwoIndex = navContent.find('a')['href']
pageTwoURL = mainUrl + pageTwoIndex

response = requests.get(pageTwoURL)
beautifulResponse = BeautifulSoup(response.content, 'html.parser')
second_list = (beautifulResponse.find_all('span', class_= 'text'))

# ++++ Add second page phrases ++++
for phrase in second_list:
    complete_list.append(phrase)
    
    
    
navContent = beautifulResponse.find('nav')
nextNavContent = navContent.find('li', class_='next')
pageThreeIndex = nextNavContent.find('a')['href']
pageThreeURL = mainUrl + pageThreeIndex
  
response = requests.get(pageThreeURL)
beautifulResponse = BeautifulSoup(response.content, 'html.parser')
third_list = (beautifulResponse.find_all('span', class_= 'text'))

# ++++ Add third page phrases ++++
for phrase in third_list:
    complete_list.append(phrase)
    
    
    
    
clear_terminal()
print('Scrapping complete!')
time.sleep(1)
clear_terminal()

# Print the first 25 phrases
for cont, element in enumerate(complete_list, start=1 ):
    if cont < 26:
        print(f'{cont} -',  element.text, end="\n\n")  





    
