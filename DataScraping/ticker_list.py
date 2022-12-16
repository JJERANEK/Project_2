import requests
from config import polygon_key
from pprint import pprint
import pandas as pd
import json
from bs4 import BeautifulSoup
import time

def ticker_details(tkr, key):
    # url to polygon.io data REST API
    url = f'https://api.polygon.io/v3/reference/tickers/{tkr}?apiKey={key}'
    response = requests.get(url)
    json_data = response.json()['results']
    time.sleep(13)
    return json_data

def create_list(list_of_tickers, key):
    detailed_list = []
    for tkr in list_of_tickers:
        detailed_list.append(ticker_details(tkr, key))
        print(f'\nticker #{list_of_tickers.index(tkr)} extracted\n\n')
    return detailed_list

##########################################################################################
### WEB SCRAPING FOR LIST OF TICKERS #####################################################
tickers_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
response = requests.get(tickers_url)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find('table')
tickers = []
for row in table.find_all("tr"):
    cells = row.find_all("td")
    if cells:
        tickers.append(cells[0].text.replace("\n", ""))
##########################################################################################
##########################################################################################

tickers = tickers[0:15]
ticker_data = create_list(tickers, polygon_key)
with open("stocks.json", "w") as file:
    json.dump(ticker_data , file)