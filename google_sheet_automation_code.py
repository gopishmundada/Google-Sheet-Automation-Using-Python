import pygsheets
import gspread
import mysql.connector
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import psycopg2 as pg


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('your_credentials_file_name.json', scope)
client = gspread.authorize(creds)
gc = pygsheets.authorize(service_file='your_credentials_file_name.json')
sh = gc.open('You_google_sheet_name')
wks = sh[4] 			#tab number
wks.clear()				#will clear all the data in that sheet

## Postgres-sql
connection1 = pg.connect(
user = "**",
password="**",
host="**",
port="**",
database="**"
)


#My-sql
connection = mysql.connector.connect(
  host="**",
  database='**',
  user="**",
  passwd="**"
)



df = pd.read_sql_query('''
select ______________''', connection)
wks.set_dataframe(df,(1,1)) # (row, col)



df = pd.read_sql_query('''
SELECT______________''', connection1)
wks.set_dataframe(df,(1,5)) # (row, col)


