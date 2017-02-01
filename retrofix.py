#!/usr/local/bin/python

"""Simple command-line sample for the Calendar API.
Command-line application that retrieves the list of the user's calendars."""

import sys

from oauth2client import client
from googleapiclient import sample_tools

import dateutil.parser


def main(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        argv, 'calendar', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/calendar')

    try:
        page_token = None
        while True:
            events = service.events().list(calendarId='primary', pageToken=page_token).execute()
            print(events['items'])

            for event in events['items']:
                for key, value in event.items():
                    if key == 'description':
                        dstring = value
                        print(dstring)

                        if 'Drone Human Safety' in dstring:
                            event['description'] = dstring.replace('PROJ: Drone Human Safety', 'PROJ: 2016-08-101-01')
                            service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()
                            print("Old description: {0} changed to {1}".format(dstring, event['description']))

                    if key == 'start':
                        start_time = dateutil.parser.parse(value['dateTime'])
                    if key == 'end':
                        end_time = dateutil.parser.parse(value['dateTime'])

                usage_time = end_time - start_time
                # print("usage time: {0}".format(usage_time))

            page_token = events.get('nextPageToken')
            if not page_token:
                break

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run'
              'the application to re-authorize.')

if __name__ == '__main__':
    main(sys.argv)
