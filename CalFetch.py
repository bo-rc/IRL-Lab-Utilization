import datetime, dateutil.parser
from dateutil.relativedelta import relativedelta
from oauth2client import client
from googleapiclient import sample_tools

def crawl(start_date = datetime.date(2017,1,1), end_date = datetime.date.today() ):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        ' ', 'calendar', 'v3', ' ', ' ',
        scope='https://www.googleapis.com/auth/calendar.readonly')
    page_token = None
    
    proj = {}
    while True:
        events = service.events().list(calendarId='irl1.uiuc@gmail.com', pageToken=page_token).execute()
        for event in events['items']:
            if 'start' in event.keys():
                e_date_str = event['start']['dateTime']
                e_date_str = e_date_str.split('T')[0].split('-')

                e_date = datetime.date(int(e_date_str[0]), int(e_date_str[1]), int(e_date_str[2]))
                                   
                if e_date >= start_date and e_date < end_date:
                    items = event.items()
                    for key, value in items:
                        if key == 'description':
                            pieces = value.split('PROJ:')
                            num = pieces[-1].strip()
                            if num[:3] == '201': # 2016, 2017, 201x
                                deltaTime = dateutil.parser.parse(event['end']['dateTime']) - dateutil.parser.parse(event['start']['dateTime'])
                                time_h = deltaTime.seconds/3600
                                if num in proj.keys():
                                    
                                    proj[num] += time_h
                                else:
                                    proj[num] = time_h
                    
        page_token = events.get('nextPageToken')
        if not page_token:
            break
            
    return proj

def fetch_month(year, month):
    start_date = datetime.date(year,month,1)
    end_date = start_date + relativedelta(months = +1)
    
    return crawl(start_date, end_date)
    
