# UMich Chicken Tenders

An application that tells you when there are chicken tenders in the dining hall
for the next few weeks. The application is a little slow, due to how it visits
each page to scrape the menu from the HTML.

If you don't have pip installed, install [pip](https://pip.pypa.io/en/stable/installing/)

Then install Google Maps API `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

To setup Google Calendar API:
    - Go to [Google Developers](https://developers.google.com/calendar/quickstart/python)<br />
    - Click on `ENABLE THE GOOGLE CALENDAR API`<br />
    - Click on `DOWNLOAD CLIENT CONFIGURATION` and save the credentials.json file into the same folder as chicken.py<br />
    - You're all set to save chicken tender dates to your Google Calendar!<br />

To run: `python3 chicken.py`
