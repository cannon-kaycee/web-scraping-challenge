from flask import Flask, render_template
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pymongo
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import os
import requests

# Create an instance of our Flask app.
app = Flask(__name__)

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    scraped_data = {}

    url_1 = "https://redplanetscience.com/"
    browser.visit(url_1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    scraped_data["headline"] = soup.find('div', class_="content_title").get_text()
    scraped_data["teaser"] = soup.find("div", class_="article_teaser_body").get_text()
    
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    url_2 = "https://spaceimages-mars.com/"
    browser.visit(url_2)

    scraped_data["main_img"] = soup.find('img', class_="headerimage")['src'].get_text()
    
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    url_3 = "https://galaxyfacts-mars.com/"
    browser.visit(url_3)

    title_3=soup.title.text
    tables=pd.read_html(url_3)
    df = tables[0]
    header_row=0
    df.columns=df.iloc[header_row]
    df=df.drop(header_row)
    df_mars=df.reset_index(drop=True)
    html_table=df_mars.to_html()
    html_table.replace('\n','')

    scraped_data["table"] = df_mars

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    url_4 = "https://marshemispheres.com/"
    browser.visit(url_4)

    title_1=soup.title.text

    scraped_data["title_1"] = title_1

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    url_5 = "https://marshemispheres.com/cerberus.html"
    browser.visit(url_5)

    def getdata(url_5): 
        r = requests.get(url_5) 
        return r.text 
    
    htmldata = getdata("https://marshemispheres.com/cerberus.html") 
    soup_5 = bs(htmldata, 'html.parser') 
    for item in soup_5.find_all('img',class_='wide-image'):
        print(item['src'])
    cerb_image= url_4 + item['src']

    scraped_data["cerb"] = cerb_image

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    url_6 = "https://marshemispheres.com/syrtis.html"
    browser.visit(url_6)

    def getdata(url_syrt): 
        r = requests.get(url_syrt) 
        return r.text 
    
    htmldata_syrt = getdata(url_syrt) 
    soup_syrt = bs(htmldata_syrt, 'html.parser') 
    for item in soup_syrt.find_all('img',class_='wide-image'):
         print(item['src'])
    syrt_image= url_4 + item['src']

    scraped_data["syrt"] = syrt_image

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    url_7 = "https://marshemispheres.com/valles.html"
    browser.visit(url_7)

    def getdata(url_7): 
        r = requests.get(url_7) 
        return r.text 
    
    htmldata_valles = getdata(url_7) 
    soup_valles = bs(htmldata_valles, 'html.parser') 
    for item in soup_valles.find_all('img',class_='wide-image'):
         print(item['src'])
    valles_image= url_4 + item['src']
    
    scraped_data["valles"] = valles_image

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    url_8 = "https://marshemispheres.com/schiaparelli.html"
    browser.visit(url_8)


    def getdata(url_schia): 
        r = requests.get(url_schia) 
        return r.text 

    htmldata_schia = getdata(url_8) 
    soup_schia = bs(htmldata_schia, 'html.parser') 
    for item in soup_schia.find_all('img',class_='wide-image'):
         print(item['src'])
    schia_image= url_4 + item['src']
    print(schia_image)

    scraped_data["schia"] = schia_image


    # Quit the browser
    browser.quit()





    return scrape_mars

