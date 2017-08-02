import datetime, dateutil.parser, calendar
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
                            pieces = pieces[-1].split('\n')
                            num = pieces[0].strip()
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

def overall(start_date = datetime.date(2016,7,1), end_date = datetime.date.today() ):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        ' ', 'calendar', 'v3', ' ', ' ',
        scope='https://www.googleapis.com/auth/calendar.readonly')
    page_token = None
    
    proj = {}
    day = {}
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
                            pieces = pieces[-1].split('\n')
                            num = pieces[0].strip()
                            if num[:3] == '201': # 2016, 2017, 201x
                                deltaTime = dateutil.parser.parse(event['end']['dateTime']) - dateutil.parser.parse(event['start']['dateTime'])
                                time_h = deltaTime.seconds/3600
                                
                                # add to proj-time
                                if num in proj.keys():                                    
                                    proj[num] += time_h
                                else:
                                    proj[num] = time_h
                                
                                # add to day-time
                                day_date = dateutil.parser.parse(event['start']['dateTime'])
                                day_key = str(day_date).split(' ')[0]
                                
                                if day_key in day.keys():
                                    day[day_key] += time_h
                                else:
                                    day[day_key] = time_h
                                
                    
        page_token = events.get('nextPageToken')
        if not page_token:
            break
            
    return proj, day

def fetch_month(year, month):
    start_date = datetime.date(year,month,1)
    end_date = start_date + relativedelta(months = +1)
    fetch = crawl(start_date, end_date)
    return fetch

def get_hours(fetch, proj_number_PI_mapping):
    PI_hours = {}
    dept_hours = {}
    
    for key, value in fetch.items():
        if key not in proj_number_PI_mapping.keys():
            raise RuntimeError("unknown project number from PI database, key = {}".format(key))
        
        name = proj_number_PI_mapping[key]
    
        if name not in PI_hours.keys():
            PI_hours[name] = value
        else:
            PI_hours[name] += value
    
        d = PIs[name].dept
    
        for i in d:
            if i not in dept_hours.keys():
                dept_hours[i] = value
            else:
                dept_hours[i] += value

    return PI_hours, dept_hours

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def get_monthly_report(year, month, proj_number_PI_mapping, PI_list):

    title = '-'.join([str(year), str(month)])

    writer = pd.ExcelWriter('.'.join([title, 'xlsx']))

    pi_hours, dept_hours = get_hours(fetch_month(year, month), proj_number_PI_mapping)

    pi_data = pd.DataFrame(list(pi_hours.items()))
    pi_data.columns = ['name', 'hours']
    pi_data = pi_data.sort_values('hours', ascending=False)
    pi_data.reset_index(drop=True, inplace=True)

    dept_list = []
    for index, row in pi_data.iterrows():
        key = row['name']
        dept = PI_list[key].dept
        dept_list.append(dept)

    pi_data['dept'] = pd.Series(dept_list)

    dept_data = pd.DataFrame(list(dept_hours.items()))
    dept_data.columns = ['dept', 'hours']
    dept_data = dept_data.sort_values('hours', ascending=False)
    dept_data.reset_index(drop=True, inplace=True)

    # write to excel files
    pi_data.to_excel(writer, 'PI hours')
    dept_data.to_excel(writer, 'dept hours')
    writer.save()

    # calculating utilization
    days = calendar.monthrange(year, month)[1]
    total_hours = 8.0 * days
    used_hours = pi_data['hours'].sum()
    utilization_rate = used_hours / total_hours * 100
    
    suptitle = ','.join([title, '(utilization rate = {:.{prec}f} %)'.format(utilization_rate, prec=1)])
    plt.suptitle(suptitle, y=1.0)
    sns.set_style("darkgrid")
    plt.subplot(1,2,1)

    pi_plot = sns.barplot(x= pi_data['name'], y=pi_data['hours'], palette="muted")
    xlabels = []
    for index, row in pi_data.iterrows():
        xlabel = row['name'] + '\n' + '(' + ','.join(row['dept']) + ')'
        xlabels.append(xlabel)
    pi_plot.set(xticklabels=xlabels)

    plt.xticks(rotation=90)

    plt.subplot(1,2,2)
    dept_plot = sns.barplot(x=dept_data['dept'], y=dept_data['hours'], palette="muted")    
    
    #left, right, top, bottom = plt.axis()
    #plt.axis((left, right, top+0.5, bottom))
    plt.tight_layout()
    plt.savefig('.'.join([title, 'jpg']))

    def get_overall_report(start_date = datetime.date(2016,7,1), end_date = datetime.date.today(), proj_number_PI_mapping={}, PI_list={}):
        title = 'starting from {}'.format(start_date)
        
        