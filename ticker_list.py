from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://stockanalysis.com/stocks/'
browser.visit(url)

x = True
for x in range(0,2):
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    stocks = soup.find_all('tr', class_='svelte-1xuuw1j')

    stocks_list = []
    for stock in stocks:
        data = pd.read_html(url)
        stocks_list.append(data)

    try:
        browser.links.find_by_partial_text('Next').click()
        url = browser.url

    except:
        x = False

for stock in stocks_list:
    print(stock.head())

# <button class="relative inline-flex items-center whitespace-nowrap rounded-md border border-gray-300 bg-white py-1.5 text-xs font-medium text-gray-700 hover:bg-gray-50 xs:py-2 bp:text-sm px-2 xs:pl-1 xs:pr-1.5 sm:pl-3 sm:pr-1 disabled:bg-gray-50"><span class="hidden sm:inline">Next</span> <svg class="-mb-px h-5 w-5 text-gray-600 bp:ml-1" viewBox="0 0 20 20" fill="currentColor" style="max-width:40px"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path></svg></button>
# <tr class="svelte-1xuuw1j"><td class="svelte-1xuuw1j"><a href="/stocks/a/">A</a></td><td class="svelte-1xuuw1j">Agilent Technologies</td><td class="svelte-1xuuw1j">Life Sciences Tools &amp; Services</td><td class="svelte-1xuuw1j">45.67B</td> </tr>