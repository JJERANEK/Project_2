# Project 2 Documentation
## S&P 500 1-Year Snapshot

### Data Sources with citations:
- [polygon.io](https://polygon.io/docs/stocks/getting-started)
- [NYTimesAPI](https://developer.nytimes.com/)
- [Wikipedia table of S&P 500 companies](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)

### Tools Used:
Mongo: Will load data into a non-realational Mongodb database.
Jupyter Notebooks and python files used for data scraping, cleaning, merging and uploading.

### Data Scraping:
We scraped 500 tickers from the S&P 500 wikipedia page (see citations). Ticker categorical data came from polygon.io (see citations) and was pulled with a python jupyter notebook. Ticker performance data came from polygon.io (see citations) and was pulled with a python jupyter notebook. Raw data for both categories and performance was saved in json files. 

See DataScraping folder for files associated with data scraping of categorical and performance data. 
See ArticleData folder for files associated with data scraping of stock article data.

### Data Cleaning:
Changing daily stock performance data to weekly stock value using pandas dataframe groupby and *datetime.isocalendar()* method. Categorical data came as dictionaries for each ticker. A list of dictionaries was created.

Article data cleaning dropped 16 keys from each stock ticker's dictionary, leaving behing three keys:
1. Headline
2. Abstract
3. Web URL

Article, categorical, and performance raw data all had ticker keys as part of the first hierarchy of each company's dictionary. The *dictionary.pop()* method was used on all three datasets to extract the ticker out (and for categorical data, also the company name) and make a new key on the first hierarchy. Then, the remaining dictionary keys for each of the three datasets was compiled into their own new keys, also on the first level of the main data hierarchy.

See DataCleaning folder for files associated with data cleaning. Cleaned data json files kept in CleanedData folder. Three cleaned json files were created in this folder.

### Data Merging:
Three json files from the CleanedData folder were combined.
Performance and categorical data were combined into one json file with for loops and construction dictionaries. The final merged data json file was created by pulling in the performance+categorical json and combining the article json file using Pandas.

See MergeData folder for files associated with data merging.

### Data Uploading:
An Atlas MongoDB free account was made and hosted through AWS. A connection was established using pymongo and a new db was created, called project2_db. One collection, called sp500_1year_snapshot, was created and holds one document for each of the 500 companies.

See MongoUpload folder for files associated with data uploading.