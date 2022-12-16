import requests
from config import polygon_key
from pprint import pprint
import pandas as pd
import json
from bs4 import BeautifulSoup
import time

##########################################################################################
### DEFINING FUNCTIONS ###################################################################
def ticker_details(tkr, key):
    # url to polygon.io data REST API
    url = f'https://api.polygon.io/v2/aggs/ticker/{tkr}/range/1/day/2021-12-12/2022-12-10?adjusted=true&sort=asc&limit=10000&apiKey={key}'
    response = requests.get(url)
    json_data = response.json()
    # time.sleep(13)
    return json_data

def create_list(list_of_tickers, key):
    performance_list = []
    for tkr in list_of_tickers:
        performance_list.append(ticker_details(tkr, key))
        print(f'\nticker #{list_of_tickers.index(tkr)} extracted\n\n')
    return performance_list
##########################################################################################
##########################################################################################


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


##########################################################################################
### CALL FUNCTIONS TO CREATE JSON FILE ###################################################
ticker_data = create_list(tickers, polygon_key)
with open("ticker_performance.json", "w") as file:
    json.dump(ticker_data , file)
##########################################################################################
##########################################################################################