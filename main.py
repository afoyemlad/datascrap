import pandas as pd
import requests
import schedule
import datetime
import time

from pandas import DataFrame

def fetch_data(day,time):
  apiKey = '6e6bfb2b24350ffd7ffc48c8b2fc3d6f6134a8d3'
  contract_name = 'dublin'
  url = 'https://api.jcdecaux.com/vls/v3/stations?contract='+ contract_name + '&apiKey=' + apiKey

  response = pd.read_json(url)
  df = DataFrame(response)
  csv_filename = f'{day}_Data_{time}.csv'
  df.to_csv(csv_filename)

def fetch_data_job():
    day = str(datetime.datetime.now().day)
    month = str(datetime.datetime.now().month)
    te = time.strftime("%H:%M:%S")
    date = month + '-'+ day
    fetch_data(date,te)

schedule.every().hours.at(':00').do(fetch_data_job)
while True:
    schedule.run_pending()
    time.sleep(3600)
