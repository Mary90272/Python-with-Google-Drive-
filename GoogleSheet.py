



import csv
#import requests doent need anymore 

import gspread
from oauth2client.service_account import ServiceAccountCredentials


file_path = 'test.csv'  # change on your file name 


# Parse CSV file
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    csv_data = list(csv_reader)




# Use Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('onemore.json', scope)  # Replace with your Google API key file onemore.json
client = gspread.authorize(creds)

# Open Google Sheets and get the first sheet
sheet = client.open('test').sheet1  # Replace 'test' with your Google Sheet name

# Write the CSV data to Google Sheets
for row in csv_data:
    sheet.append_row(row)


