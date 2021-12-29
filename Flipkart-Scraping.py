import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
ai=0
url = "https://www.flipkart.com/beds/pr?sid=wwe,7p7&otracker=nmenu_sub_Home%20%26%20Furniture_0_Beds"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
page=requests.get(url, headers=headers)
content = BeautifulSoup(page.text, 'html.parser')
#print(content)
data = content.find_all('div', {'class': '_4ddWXP'})
links = []
phname = []
price=[]
for items in data:
    restlink=items.find('a')['href']
    name = items.find('a', {'class': 's1Q9rs'})['title']
    fp=items.find('div', {'class': '_30jeq3'})
    phname.append(name)
    #links.append(restlink)
    price.append(fp.text)
for i in range(len(phname)):
    print("Bed name::", phname[i])
    #print("https://www.flipkart.com"+links[i])
    print(price[i])
    print("<--------->")
df = pd.DataFrame({'Furniture Name': phname, 'Price': price})
df.to_csv('furnitureoutput.csv', index=False, encoding='utf-8')
exit()
