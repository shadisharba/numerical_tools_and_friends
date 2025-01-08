# from https://github.com/paulc160/PP-IP-Scraper/blob/main/PP%20Ip%20Scraper.ipynb
import requests
import json
from supabase import create_client
import json
import pandas as pd
from datetime import date
import datetime
from datetime import datetime
import time
import numpy as np
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

# Replace 'your_endpoint_url' with the actual URL you want to call
endpoint_url = 'https://apisms.paddypower.com/smspp/in-play/v4?_ak=vsd0Rm5ph2sS2uaK&betexRegion=IRL&capiJurisdiction=intl&comingUpTimeRange=360000&countryCode=IE&currencyCode=EUR&eventTypeId=1&exchangeLocale=en_GB&includeSeoContentSummaryCard=true&includeTabs=true&language=en&loggedIn=false&pageType=INPLAY&regionCode=IRE&timezone=Europe%2FDublin'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

# Make a GET request
response = requests.get(endpoint_url, headers=headers)
json_data = response.json()
event_ids = []
match_ids = []
fixtures = []
odds_matches = []
competitions = []
market_types = []
market_names = []
match_dates_and_time = []
time_scraped = []
data = json_data['attachments']['events']
for i in data:
    event_ids.append(i)
start_of_url = 'https://apisds.paddypower.com/sdspp/event-page/v5?_ak=vsd0Rm5ph2sS2uaK&betexRegion=GBR&capiJurisdiction=intl&countryCode=GB&currencyCode=GBP&eventId='
eventid = ''
end_of_url = '&exchangeLocale=en_GB&includeBettingOpportunities=true&includePrices=true&includeSeoCards=true&includeSeoFooter=true&language=en&loggedIn=false&priceHistory=1&regionCode=UK'
for i in event_ids:
    url = start_of_url + i + end_of_url
    print(url)
    match_response = requests.get(url, headers=headers)
    match_data = match_response.json()
    match_name = match_data['attachments']['events']
    competition_name = match_data['attachments']['competitions']
    keys_list = list(competition_name)
    competition_data = competition_name.get(keys_list[0], {})
    competition_name_new = competition_data.get('name', 'N/A')
    competition_id = competition_data.get('competitionId', 'N/A')
    keys_list = list(match_name)
    event_data = match_name.get(keys_list[0], {})  # Use get() to handle the case where the event ID is not present
    event_name = event_data.get('name', 'N/A')
    event_time = event_data.get('openDate', 'N/A')
    print(event_time)
    print(competition_name_new)
    print(competition_id)
    markets = match_data['attachments']['markets'].keys()
    for j in markets:
        markets_new = match_data['attachments']['markets'][j]['marketName']
        print(markets_new)
        selections = match_data['attachments']['markets'][j]['runners']
        for k in selections:
            fixtures.append(event_name)
            competitions.append(competition_name_new)
            market_types.append(markets_new)
            match_dates_and_time.append(event_time)
            match_ids.append(i)
            name = k['runnerName']
            market_names.append(name)
            current_time = datetime.now()
            time_scraped.append(current_time)
            print(name)
            try:
                odds = k['winRunnerOdds']['trueOdds']['decimalOdds']['decimalOdds']
            except:
                odds = 'Issue with Odds'
            print(odds)
            odds_matches.append(odds)
    
    print('----------------')
    
    
columns = ['Match ID','Fixture',"Match Time and Date","Competition","Market Type","Market Name","Market Odds","Time Scraped"]

# Initialize a new DataFrame with columns
new_dataframe = pd.DataFrame(columns=columns)

# Add arrays to columns
new_dataframe['Match ID'] = match_ids
new_dataframe['Fixture'] = fixtures
new_dataframe['Match Time and Date'] = match_dates_and_time
new_dataframe['Competition'] = competitions
new_dataframe['Market Type'] = market_types
new_dataframe['Market Name'] = market_names
new_dataframe['Market Odds'] = odds_matches
new_dataframe['Time Scraped'] = time_scraped

new_dataframe