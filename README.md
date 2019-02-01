#UMich Chicken Tenders

An application that tells you when there are chicken tenders in the dining hall
for the next few weeks. The application is a little slow, due to how it visits
each page to scrape the menu from the HTML.

To run: `python chicken.py`

To setup Google Calendar API:
    - Go to [Google Developers](https://developers.google.com/calendar/quickstart/python)
    - Click on `ENABLE THE GOOGLE CALENDAR API`
    - Click on `DOWNLOAD CLIENT CONFIGURATION` and save the credentials.json file into the same folder as chicken.py
    - You're all set to save chicken tender dates to your Google Calendar!