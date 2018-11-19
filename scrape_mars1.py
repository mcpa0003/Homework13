from splinter import Browser
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd


def init_browser():
   
    executable_path = {"executable_path": 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    listings = {}

    tw_url = 'https://twitter.com/marswxreport?lang=en'
    url_nasa = 'https://mars.nasa.gov/news/'
    url_facts = 'https://space-facts.com/mars/'

    urlm1 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    urlm2 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    urlm3 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    urlm4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # tables = pd.read_html(url)
    # df = tables[0]
    # df.columns = ["Description", "Values"]
    # df.set_index('Description', inplace=True)
    # listings["html_table"] = df.to_html

    response_tw = requests.get(tw_url)
    response_nasa = requests.get(url_nasa)
    responsem1 = requests.get(urlm1)
    responsem2 = requests.get(urlm2)
    responsem3 = requests.get(urlm3)
    responsem4 = requests.get(urlm4)

    soupm1 = BeautifulSoup(responsem1.text, 'html.parser')
    soupm2 = BeautifulSoup(responsem2.text, 'html.parser')
    soupm3 = BeautifulSoup(responsem3.text, 'html.parser')
    soupm4 = BeautifulSoup(responsem4.text, 'html.parser')
    soup_tw = BeautifulSoup(response_tw.text, 'html.parser')
    soup_nasa = BeautifulSoup(response_nasa.text, 'html.parser')

    htmlm1 = soupm1.body.find_all('img', class_='wide-image')
    htmlm2 = soupm2.body.find_all('img', class_='wide-image')
    htmlm3 = soupm3.body.find_all('img', class_='wide-image')
    htmlm4 = soupm4.body.find_all('img', class_='wide-image')

    for w in htmlm1:
        (w['src'])
    for x in htmlm2:
        (x['src'])        
    for y in htmlm3:
        (y['src'])
    for z in htmlm4:
        (z['src'])

    listings["hem1"] = soupm1.body.find('h2', class_='title').text
    listings["hem2"] = soupm2.body.find('h2', class_='title').text
    listings["hem3"] = soupm3.body.find('h2', class_='title').text
    listings["hem4"] = soupm4.body.find('h2', class_='title').text

    listings["img_hem1"] = "https://astrogeology.usgs.gov{}".format((w['src']))
    listings["img_hem2"] = "https://astrogeology.usgs.gov{}".format((x['src']))
    listings["img_hem3"] = "https://astrogeology.usgs.gov{}".format((y['src']))
    listings["img_hem4"] = "https://astrogeology.usgs.gov{}".format((z['src']))

    listings["nasa_text"] = soup_nasa.body.find('div', class_='rollover_description_inner').text.strip()
    listings["nasa_title"] = soup_nasa.body.find('div', class_='content_title').text.strip()

    time.sleep(5)

    for x in range(1, 2):
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        articles = soup.find('footer')
        path = articles.a.attrs['data-fancybox-href']

    browser.click_link_by_partial_text('FULL IMAGE')

    listings["jpl"] = "https://www.jpl.nasa.gov{}".format(path)


    listings["tweet"] = soup_tw.body.find_all('p')[4].get_text()
    #listings["jpl"] = featured_img
    # listings["hood"] = soup.find("span", class_="result-hood").get_text()

    return listings
