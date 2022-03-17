from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import time
import csv

#request module
url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars '
page = requests.get(url, verify=False)

soup = bs(page.text,'html.parser')
time.sleep(10)
star_table = soup.find_all('table')

temp_list= []

table_rows = star_table[7].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

#empty list to store star's data from headers
Star_names = []
Distance =[]
Mass = []
Radius =[]


for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

bgs2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(bgs2)

bgs2.to_csv('brightest_stars.csv')
