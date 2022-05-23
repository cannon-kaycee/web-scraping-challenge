{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "edbd3b67",
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup as bs\n",
    "import pandas as pd\n",
    "from splinter import Browser\n",
    "import os\n",
    "import requests\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1695597f",
   "metadata": {},
   "source": [
    "## NASA Mars News"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "99975120",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 101.0.4951\n",
      "Get LATEST chromedriver version for 101.0.4951 google-chrome\n",
      "There is no [mac64] chromedriver for browser  in cache\n",
      "Trying to download new driver from https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_mac64.zip\n",
      "Driver has been saved in cache [/Users/kayceecannon/.wdm/drivers/chromedriver/mac64/101.0.4951.41]\n"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "3c9c4ba2",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"https://redplanetscience.com/\"\n",
    "browser.visit(url)\n",
    "soup = bs(browser.html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "58f018e0",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"list_text\">\n",
       "<div class=\"list_date\">May 14, 2022</div>\n",
       "<div class=\"content_title\">NASA to Reveal Name of Its Next Mars Rover</div>\n",
       "<div class=\"article_teaser_body\">After a months-long contest among students to name NASA's newest Mars rover, the agency will reveal the winning name — and the winning student — this Thursday. </div>\n",
       "</div>"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result = soup.select_one('div.list_text')\n",
    "result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "81c52766",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA to Reveal Name of Its Next Mars Rover\n",
      "After a months-long contest among students to name NASA's newest Mars rover, the agency will reveal the winning name — and the winning student — this Thursday. \n"
     ]
    }
   ],
   "source": [
    "news_title=result.find('div',class_='content_title').get_text()\n",
    "news_par=result.find('div',class_='article_teaser_body').get_text()\n",
    "print(news_title)\n",
    "print(news_par)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f2b77913",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad390396",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "be5df3e4",
   "metadata": {},
   "source": [
    "# JPL Mars Space Images - Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "eb09a1b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 100.0.4896\n",
      "Get LATEST chromedriver version for 100.0.4896 google-chrome\n",
      "Trying to download new driver from https://chromedriver.storage.googleapis.com/100.0.4896.60/chromedriver_mac64.zip\n",
      "Driver has been saved in cache [/Users/kayceecannon/.wdm/drivers/chromedriver/mac64/100.0.4896.60]\n"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "2574005f",
   "metadata": {},
   "outputs": [],
   "source": [
    "url_2 = 'https://spaceimages-mars.com/'\n",
    "browser.visit(url_2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3be6dc4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "image/featured/mars1.jpg\n",
      "https://spaceimages-mars.com/image/featured/mars1.jpg\n"
     ]
    }
   ],
   "source": [
    "for x in range(1):\n",
    "\n",
    "    html = browser.html\n",
    "    soup_2 = bs(html, 'html.parser')\n",
    "\n",
    "    mars_image = soup_2.find('img', class_='headerimage')['src']\n",
    "    \n",
    "    print(mars_image)\n",
    "    \n",
    "featured_mars_image = url_2 + mars_image\n",
    "\n",
    "print(featured_mars_image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96aa8151",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "10e586eb",
   "metadata": {},
   "source": [
    "# Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c51fdc01",
   "metadata": {},
   "outputs": [],
   "source": [
    "url_3='https://galaxyfacts-mars.com/'\n",
    "reqs_3 = requests.get(url_3)\n",
    "soup_3 = bs(reqs_3.text, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f3edff78",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Mars Facts - Interesting facts about Planet Mars'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "title_3=soup_3.title.text\n",
    "title_3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "60cb194a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                         0                1                2\n",
       " 0  Mars - Earth Comparison             Mars            Earth\n",
       " 1                Diameter:         6,779 km        12,742 km\n",
       " 2                    Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       " 3                   Moons:                2                1\n",
       " 4       Distance from Sun:   227,943,824 km   149,598,262 km\n",
       " 5          Length of Year:   687 Earth days      365.24 days\n",
       " 6             Temperature:     -87 to -5 °C      -88 to 58°C,\n",
       "                       0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:          2 ( Phobos & Deimos )\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tables=pd.read_html(url_3)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "82343501",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Diameter:</td>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Distance from Sun:</td>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Length of Year:</td>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "0 Mars - Earth Comparison             Mars            Earth\n",
       "0               Diameter:         6,779 km        12,742 km\n",
       "1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "2                  Moons:                2                1\n",
       "3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       "4         Length of Year:   687 Earth days      365.24 days\n",
       "5            Temperature:     -87 to -5 °C      -88 to 58°C"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = tables[0]\n",
    "header_row=0\n",
    "df.columns=df.iloc[header_row]\n",
    "df=df.drop(header_row)\n",
    "df_mars=df.reset_index(drop=True)\n",
    "df_mars"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "8ba0bf9f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Mars - Earth Comparison</th>\\n      <th>Mars</th>\\n      <th>Earth</th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>0</th>\\n      <td>Diameter:</td>\\n      <td>6,779 km</td>\\n      <td>12,742 km</td>\\n    </tr>\\n    <tr>\\n      <th>1</th>\\n      <td>Mass:</td>\\n      <td>6.39 × 10^23 kg</td>\\n      <td>5.97 × 10^24 kg</td>\\n    </tr>\\n    <tr>\\n      <th>2</th>\\n      <td>Moons:</td>\\n      <td>2</td>\\n      <td>1</td>\\n    </tr>\\n    <tr>\\n      <th>3</th>\\n      <td>Distance from Sun:</td>\\n      <td>227,943,824 km</td>\\n      <td>149,598,262 km</td>\\n    </tr>\\n    <tr>\\n      <th>4</th>\\n      <td>Length of Year:</td>\\n      <td>687 Earth days</td>\\n      <td>365.24 days</td>\\n    </tr>\\n    <tr>\\n      <th>5</th>\\n      <td>Temperature:</td>\\n      <td>-87 to -5 °C</td>\\n      <td>-88 to 58°C</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "html_table=df_mars.to_html()\n",
    "html_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f2b87859",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">  <thead>    <tr style=\"text-align: right;\">      <th></th>      <th>Mars - Earth Comparison</th>      <th>Mars</th>      <th>Earth</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>Diameter:</td>      <td>6,779 km</td>      <td>12,742 km</td>    </tr>    <tr>      <th>1</th>      <td>Mass:</td>      <td>6.39 × 10^23 kg</td>      <td>5.97 × 10^24 kg</td>    </tr>    <tr>      <th>2</th>      <td>Moons:</td>      <td>2</td>      <td>1</td>    </tr>    <tr>      <th>3</th>      <td>Distance from Sun:</td>      <td>227,943,824 km</td>      <td>149,598,262 km</td>    </tr>    <tr>      <th>4</th>      <td>Length of Year:</td>      <td>687 Earth days</td>      <td>365.24 days</td>    </tr>    <tr>      <th>5</th>      <td>Temperature:</td>      <td>-87 to -5 °C</td>      <td>-88 to 58°C</td>    </tr>  </tbody></table>'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "html_table.replace('\\n','')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "9416d823",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_mars.to_html('table.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "0fffb49b",
   "metadata": {},
   "outputs": [],
   "source": [
    "!open table.html"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "82d29c1b",
   "metadata": {},
   "source": [
    "# Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "818ec9f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "url_4='https://marshemispheres.com/'\n",
    "reqs_4 = requests.get(url_4)\n",
    "soup_4 = bs(reqs_4.text, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "2405fc04",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Astropedia Search Results | GUSS Astrogeology Science Center'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "title_4=soup_4.title.text\n",
    "title_4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "db385437",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg\n",
      "https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg\n"
     ]
    }
   ],
   "source": [
    "url_cerb = 'https://marshemispheres.com/cerberus.html'\n",
    "\n",
    "def getdata(url_cerb): \n",
    "    r = requests.get(url_cerb) \n",
    "    return r.text \n",
    "    \n",
    "htmldata = getdata(\"https://marshemispheres.com/cerberus.html\") \n",
    "soup_5 = bs(htmldata, 'html.parser') \n",
    "for item in soup_5.find_all('img',class_='wide-image'):\n",
    "     print(item['src'])\n",
    "cerb_image= url_4 + item['src']\n",
    "print(cerb_image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "0e82745c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg\n",
      "https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg\n"
     ]
    }
   ],
   "source": [
    "url_schia = 'https://marshemispheres.com/schiaparelli.html'\n",
    "\n",
    "def getdata(url_schia): \n",
    "    r = requests.get(url_schia) \n",
    "    return r.text \n",
    "    \n",
    "htmldata_schia = getdata(url_schia) \n",
    "soup_schia = bs(htmldata_schia, 'html.parser') \n",
    "for item in soup_schia.find_all('img',class_='wide-image'):\n",
    "     print(item['src'])\n",
    "schia_image= url_4 + item['src']\n",
    "print(schia_image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "7e302cf4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg\n",
      "https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg\n"
     ]
    }
   ],
   "source": [
    "url_syrt = 'https://marshemispheres.com/syrtis.html'\n",
    "\n",
    "def getdata(url_syrt): \n",
    "    r = requests.get(url_syrt) \n",
    "    return r.text \n",
    "    \n",
    "htmldata_syrt = getdata(url_syrt) \n",
    "soup_syrt = bs(htmldata_syrt, 'html.parser') \n",
    "for item in soup_syrt.find_all('img',class_='wide-image'):\n",
    "     print(item['src'])\n",
    "syrt_image= url_4 + item['src']\n",
    "print(syrt_image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "58cd27c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg\n",
      "https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg\n"
     ]
    }
   ],
   "source": [
    "url_valles = 'https://marshemispheres.com/valles.html'\n",
    "\n",
    "def getdata(url_valles): \n",
    "    r = requests.get(url_valles) \n",
    "    return r.text \n",
    "    \n",
    "htmldata_valles = getdata(url_valles) \n",
    "soup_valles = bs(htmldata_valles, 'html.parser') \n",
    "for item in soup_valles.find_all('img',class_='wide-image'):\n",
    "     print(item['src'])\n",
    "valles_image= url_4 + item['src']\n",
    "print(valles_image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "a08e8ebd",
   "metadata": {},
   "outputs": [],
   "source": [
    "hemisphere_image_urls = [\n",
    "    {\"title\": \"Valles Marineris Hemisphere\", \"img_url\": valles_image},\n",
    "    {\"title\": \"Cerberus Hemisphere\", \"img_url\": cerb_image},\n",
    "    {\"title\": \"Schiaparelli Hemisphere\", \"img_url\": schia_image},\n",
    "    {\"title\": \"Syrtis Major Hemisphere\", \"img_url\": syrt_image},\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "bd58471e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Valles Marineris Hemisphere',\n",
       "  'img_url': 'https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'},\n",
       " {'title': 'Cerberus Hemisphere',\n",
       "  'img_url': 'https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere',\n",
       "  'img_url': 'https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere',\n",
       "  'img_url': 'https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'}]"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04e1a001",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
