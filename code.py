












































































































































































from tkinter import BROWSE
from urllib.request import Request
from bs4 import BeautifulSoup
import time
import csv

starturl="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser.get(starturl)
time.sleep(10)
r = Request.get("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars", verify=False)
def scrape():
    headers=["name","distance","mass","radius"]
    starrecord=[]
    for i in range(0,28):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for th_tag in soup.find_all("th",style={"background"}):
            tr_tag = th_tag.find_all("tr")
            temp_list=[]
            for index, tr_tag in enumerate(tr_tag):
                if index == 0:
                    temp_list.append(tr_tag.find all("p")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append("")
            starrecord.append(temp_list)
        BROWSE.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table/tbody/tr[8]').click()
    with open("scaper.csv","w") as f:
         writer =csv.writer(f)
        writer.writerow(headers)
        writer.writerows(starrecord)
scrape()




