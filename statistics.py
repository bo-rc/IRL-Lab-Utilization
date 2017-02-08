#!/usr/local/bin/python

"""Simple command-line sample for the Calendar API.
Command-line application that retrieves the list of the user's calendars."""

import sys
import re

from oauth2client import client
from googleapiclient import sample_tools

import dateutil.parser


def main(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        argv, 'calendar', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/calendar.readonly')

    # project number pattern
    pnp = re.compile('[2016|2017]')

    PIs = {'Seth Hutchinson': 0}

    try:
        page_token = None
        while True:
            events = service.events().list(calendarId='irl1.uiuc@gmail.com', pageToken=page_token).execute()
            print(events['items'])

            for event in events['items']:
                for key, value in event.items():
                    if key == 'description':
                        if pnp.search(value):
                            if '2016-10-103-01' in value:
                                item = event['start']
                                start_time = dateutil.parser.parse(item['dateTime'])
                                item = event['end']
                                end_time = dateutil.parser.parse(item['dateTime'])
                                usage_time = end_time - start_time

                                print('Seth uses: {0}'.format(usage_time))
                                #PIs['Seth Hutchinson'] = PIs['Seth Hutchinson'] + usage_time

            page_token = events.get('nextPageToken')
            if not page_token:
                break

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run'
              'the application to re-authorize.')



if __name__ == '__main__':
    main(sys.argv)
