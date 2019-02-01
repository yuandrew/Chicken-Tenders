"""
    Author: Andrew Yuan
    Date: Jan 30, 2019
    Purpose: To eat more chicken tenders
"""
from __future__ import print_function
from urllib.request import urlopen
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/calendar.events',
]
CALENDAR_EVENTS = []
ADD_CALENDAR = 0
bursley = 'https://dining.umich.edu/menus-locations/dining-halls/bursley/'
mojo = 'https://dining.umich.edu/menus-locations/dining-halls/mosher-jordan/'
nq = 'https://dining.umich.edu/menus-locations/dining-halls/north-quad/'
sq = 'https://dining.umich.edu/menus-locations/dining-halls/south-quad/'

letterMonth = [
    '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',
    'August', 'September', 'October', 'November', 'December'
]


def search(dining_url, hall, day, month, year, num):
    global CALENDAR_EVENTS
    dining_url += '?menuDate={}-{}-{}'.format(year, month, day)
    page = urlopen(dining_url).read().decode('utf-8')
    if "No menu available." in page:
        return False
    # if "Chicken Tenders" in soup:
    if "Chicken Tenders" in page:
        print("Chicken Tenders found at {} on {} {}.".format(hall, letterMonth[num], day))
        if ADD_CALENDAR == 'yes':
            CALENDAR_EVENTS.append(
                {
                    'summary': 'Chicken Tenders at {}'.format(hall),
                    'start': {
                        'date': '{}-{}-{}'.format(year, month, day),
                        'timeZone': 'America/New_York'
                    },
                    'end': {
                        'date': '{}-{}-{}'.format(year, month, day),
                        'timeZone': 'America/New_York',
                    },
                }
            )
    return True


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    global ADD_CALENDAR
    ADD_CALENDAR = input("Would you like to add the dates to your google calendar? yes/no ")

    while ADD_CALENDAR != 'yes' and ADD_CALENDAR != 'no':
        ADD_CALENDAR = input("Sorry, invalid response. Would you like to add the dates to your google calendar? yes/no ")
    if ADD_CALENDAR == 'yes':
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year


    for i in range(30):
        if day > 31:
            month += 1
            day = 1
        if day < 10:
            strDay = '0' + str(day)
        else:
            strDay = str(day)
        if month < 10:
            strMonth = '0' + str(month)
        else:
            strMonth = str(month)
        if not search(bursley, "Bursley", strDay, strMonth, str(year), month):
            break
        if not search(mojo, "Mojo", strDay, strMonth, str(year), month):
            break
        if not search(nq, "North Quad", strDay, strMonth, str(year), month):
            break
        if not search(sq, "South Quad", strDay, strMonth, str(year), month):
            break

        day += 1
    for item in CALENDAR_EVENTS:
        print("item: ")
        print(item)
        event = service.events().insert(calendarId='primary', body=item).execute()
    print(CALENDAR_EVENTS)

if __name__ == '__main__':
    main()
