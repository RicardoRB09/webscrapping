import requests, sys, os
from bs4 import BeautifulSoup
from lxml import etree


class MenuItem:
    def __init__(self, title = '', url = ''):
        self.title = title
        self.url = url


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

mainUrl = 'https://www.eltiempo.com'
menuItems = []

response = requests.get(mainUrl)

clear_terminal()

if response.status_code != 200:
    print('⚠️⚠️ Cannot continue with the execution... Try again! ⚠️⚠️\n')
    sys.exit()
    
beautifulResponse = BeautifulSoup(response.text, 'html.parser')
dom = etree.HTML(str(beautifulResponse))
scrappedTitles = dom.xpath('//ul[@class="c-subheader__nav__list"]/li/a')

for cont, scrappedTitle in enumerate (scrappedTitles, start=1):
    newMenuItem = MenuItem()
    newMenuItem.title = scrappedTitle.text
    
    if cont != 14:
        newMenuItem.url = mainUrl + scrappedTitle.attrib['href']
    else:
        newMenuItem.url = scrappedTitle.attrib['href']
    
    menuItems.append(newMenuItem)
    
    

for cont, menuItem in enumerate(menuItems, start=1):
    print(f'''{cont} -- {menuItem.title}
{menuItem.url}
''')
    



