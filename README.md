# Python-with-Google-Drive

##  Description
This Python program facilitates the seamless transfer of data from a CSV file to a Google Sheets spreadsheet. It utilizes the csv module for reading CSV files and the gspread library to interact with the Google Sheets API. The primary purpose of this script is to automate the process of populating a Google Sheets worksheet with data from a specified CSV file.

## Prerequisites
Before running the program, ensure you have the following prerequisites in place:

CSV File: Prepare a CSV file containing the data you want to import into Google Sheets. Update the file_path variable with the correct path to your CSV file.

Google API Credentials: You'll need Google API credentials to authenticate your program with the Google Sheets API. Replace the onemore.json file in the ServiceAccountCredentials.from_json_keyfile_name() method with the path to your own JSON key file. This file should be obtained by setting up a project in the Google Developer Console and enabling the Google Sheets API.
Sharing Google Sheet After Role Creation.
Once you've completed the steps to create a role and obtain your Google API key file, you'll need to share the Google Sheet with the appropriate permissions to allow the program to write data to it. Here's how to do that:

Create a Role in Google Console: Follow the instructions in the Google Console to create a role and generate a JSON key file for authentication.

Copy the Email Address from the JSON Key File: Open the JSON key file you've generated. Inside the file, there should be an "email" field. Copy the email address associated with the JSON key.

Open Your Google Sheet: Navigate to the Google Sheet where you want to import the CSV data.

Share the Google Sheet:

Click on the "Share" button in the top right corner of the Google Sheet.
In the "Invite people" input field, paste the email address you copied from the JSON key file.
Select the desired permission level. To allow the program to edit the sheet, set the permission level to "Editor".




Google Sheet: Create a Google Sheet where you want the CSV data to be imported. Replace 'test' in the client.open('test').sheet1 line with the name of your target Google Sheet. Make sure the Google Sheet has at least one sheet (typically named 'Sheet1').

## Usage
Ensure you have the required modules installed. If not, you can install them using the following commands:

Copy code
pip install gspread
pip install oauth2client
Replace the placeholders in the script with your actual file paths and names:

file_path: Provide the path to your CSV file.
onemore.json: Replace this with the path to your Google API JSON key file.
'test': Change this to the name of your Google Sheet.
Run the script.

## Functionality
The program reads the data from the specified CSV file using the csv module and stores it as a list of lists in the csv_data variable.

It uses the Google Sheets API through the gspread library. The program authenticates with the Google API using the provided credentials.

The script accesses the specified Google Sheet (by name) and its first sheet (typically 'Sheet1').

The CSV data is iterated over, and each row is appended to the Google Sheet using the append_row() method.

