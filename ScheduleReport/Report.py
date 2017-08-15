import datetime, dateutil.parser

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import xlsxwriter

from dateutil.relativedelta import relativedelta
from oauth2client import client
from googleapiclient import sample_tools

from . PI import *

proj_to_PI = PI.get_proj_dict()
PI_dict = PI.get_PI_dict()

def crawl(start_date = datetime.date(2016,7,1), end_date = datetime.date.today()):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        ' ', 'calendar', 'v3', ' ', ' ',
        scope='https://www.googleapis.com/auth/calendar.readonly')
    page_token = None
    
    projs = {}
    days = {}
    
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
                                if num in projs.keys():                                    
                                    projs[num] += time_h
                                else:
                                    projs[num] = time_h
                                
                                # add to day-time
                                days_date = dateutil.parser.parse(event['start']['dateTime'])
                                days_key = str(days_date).split(' ')[0]
                                
                                if days_key in days.keys():
                                    days[days_key] += time_h
                                else:
                                    days[days_key] = time_h
                                
                    
        page_token = events.get('nextPageToken')
        if not page_token:
            break
            
    return projs, days

def fetch_range(start_date = datetime.date(2016,7,1), end_date = datetime.date.today()):
    return crawl(start_date, end_date)

def fetch_month(year = datetime.datetime.now().year, month = datetime.datetime.now().month):
    start_date = datetime.date(year,month,1)
    end_date = start_date + relativedelta(months = +1)
    return crawl(start_date, end_date)

def get_PI_app_hours_from_proj_hours(proj_hours):
    PI_hours = {}
    app_hours = {}
    
    for key, value in proj_hours.items():
        if key not in proj_to_PI.keys():
            raise RuntimeError("unknown project number from PI database, key = {}".format(key))
        
        name = proj_to_PI[key]
    
        if name not in PI_hours.keys():
            PI_hours[name] = value
        else:
            PI_hours[name] += value
    
        app_list = PI_dict[name].app
    
        for app in app_list:
            if app not in app_hours.keys():
                app_hours[app] = value
            else:
                app_hours[app] += value

    return PI_hours, app_hours

def get_PI_dept_hours_from_proj_hours(proj_hours):
    PI_hours = {}
    dept_hours = {}
    
    for key, value in proj_hours.items():
        if key not in proj_to_PI.keys():
            raise RuntimeError("unknown project number from PI database, key = {}".format(key))
        
        name = proj_to_PI[key]
    
        if name not in PI_hours.keys():
            PI_hours[name] = value
        else:
            PI_hours[name] += value
    
        dept = PI_dict[name].dept
    
        if dept not in dept_hours.keys():
            dept_hours[dept] = value
        else:
            dept_hours[dept] += value

    return PI_hours, dept_hours    


def report_range(start_year=2016, start_month=8, start_day=1, 
                 end_year=datetime.date.today().year, 
                 end_month=datetime.date.today().month, 
                 end_day=datetime.date.today().day):
    
    start_date = datetime.date(start_year, start_month, start_day)
    end_date = datetime.date(end_year, end_month, end_day)
    projs, days = fetch_range(start_date, end_date)

    # figure title
    title = ''
    if end_date <= start_date + relativedelta(months = +1):
        title = '{}-{}'.format(start_date.year, start_date.month)  
    else:
        title = '{} to {}'.format(start_date, end_date)
    print(title)
    
    writer = pd.ExcelWriter('./output/{}.xlsx'.format(title), engine='xlsxwriter')

    proj_hours, _ = fetch_range(start_date, end_date)
    
    pi_hours, dept_hours = get_PI_dept_hours_from_proj_hours(proj_hours)
    
    pi_df = pd.DataFrame(list(pi_hours.items()))
    pi_df.columns = ['name', 'hours']
    pi_df['percentage'] = 100 * pi_df['hours'] / pi_df['hours'].sum()
    pi_df = pi_df.sort_values('hours', ascending=False)
    pi_df.reset_index(drop=True, inplace=True)
    
    dept_list = []
    for index, row in pi_df.iterrows():
        key = row['name']
        dept = PI_dict[key].dept
        dept_list.append(dept)

    pi_df['dept'] = pd.Series(dept_list)

    dept_df = pd.DataFrame(list(dept_hours.items()))
    dept_df.columns = ['dept', 'hours']
    dept_df['percentage'] = 100 * dept_df['hours'] / dept_df['hours'].sum()
    dept_df = dept_df.sort_values('hours', ascending=False)
    dept_df.reset_index(drop=True, inplace=True)
    
    _, app_hours = get_PI_app_hours_from_proj_hours(proj_hours)

    app_list = []
    for index, row in pi_df.iterrows():
        key = row['name']
        app = PI_dict[key].app
        app_list.append(app)

    pi_df['app'] = pd.Series(app_list)

    app_df = pd.DataFrame(list(app_hours.items()))
    app_df.columns = ['unit(accumulative)', 'hours']
    app_df['percentage'] = 100 * app_df['hours'] / app_df['hours'].sum()
    app_df = app_df.sort_values('hours', ascending=False)
    app_df.reset_index(drop=True, inplace=True)

    # write to excel files
    pi_df.to_excel(writer, 'PI hours')
    dept_df.to_excel(writer, 'department hours')
    app_df.to_excel(writer, 'unit(accumulative) hours')
    writer.save()

    # calculating utilization
    days = (end_date - start_date).days
    total_hours = 8.0 * days
    used_hours = pi_df['hours'].sum()
    utilization_rate = used_hours / total_hours * 100
    
    plt.figure(figsize=(15,10))
    suptitle = ','.join([title, '(utilization = {:.{prec}f} %)'.format(utilization_rate, prec=1)])
    plt.suptitle(suptitle, y=1.0)
    sns.set_style("darkgrid")
    plt.subplot(1,3,1)

    ax1 = sns.barplot(x= pi_df['name'], y=pi_df['hours'], palette="muted")
    xlabels = []
    for index, row in pi_df.iterrows():
        xlabel = row['name'] + '\n' + '(' + ','.join(row['app']) + ')'
        xlabels.append(xlabel)
    ax1.set(xticklabels=xlabels)
    
    for patch, percentage in zip(ax1.patches, pi_df['percentage']):
        height = patch.get_height()
        ax1.text(patch.get_x()+patch.get_width()/2., height + height* 0.02, '{:2.1f}%'.format(percentage), ha="center") 

    plt.xticks(rotation=90)
    
    plt.subplot(1,3,2)
    ax2 = sns.barplot(x=dept_df['dept'], y=dept_df['hours'], palette="muted")
    
    for patch, percentage in zip(ax2.patches, dept_df['percentage']):
        height = patch.get_height()
        ax2.text(patch.get_x()+patch.get_width()/2., height + height * 0.02, '{:2.1f}%'.format(percentage), ha="center") 
   
    plt.subplot(1,3,3)
    ax3 = sns.barplot(x=app_df['unit(accumulative)'], y=app_df['hours'], palette="muted")
    
    for patch, percentage in zip(ax3.patches, app_df['percentage']):
        height = patch.get_height()
        ax3.text(patch.get_x()+patch.get_width()/2., height + height * 0.02, '{:2.1f}%'.format(percentage), ha="center") 
   
    #left, right, top, bottom = plt.axis()
    #plt.axis((left, right, top+0.5, bottom))
    #plt.tight_layout()
    plt.savefig('output/{}.jpg'.format(title))
    plt.show()
    

def report_month(year = datetime.datetime.now().year, month = datetime.datetime.now().month):
    start_date = datetime.date(year,month,1)
    end_date = start_date + relativedelta(months = +1)
    return report_range(start_date.year, start_date.month, start_date.day, end_date.year, end_date.month, end_date.day)


def get_days_record_range(start_year=2016, start_month=8, start_day=1, 
                 end_year=datetime.date.today().year, 
                 end_month=datetime.date.today().month, 
                 end_day=datetime.date.today().day):
    
    start_date = datetime.date(start_year, start_month, start_day)
    end_date = datetime.date(end_year, end_month, end_day)
    
    title = '{}-{}'.format(start_date, end_date)
    projs, days = fetch_range(start_date, end_date)

    days_df = pd.DataFrame(list(days.items()))
    days_df.columns = ['day', 'hours']
    days_df = days_df.sort_values('day')
    days_df.reset_index(drop=True, inplace=True)
    days_df['hours'] = days_df['hours'].astype(int)

    # write days record to files
    days_df.to_csv('./output/days-record-{}.txt'.format(title), sep=' ', header=['#day', 'hours'], index=False)

    projs_df = pd.DataFrame(list(projs.items()))
    projs_df.columns = ['num', 'hours']
    projs_df = projs_df.sort_values('hours', ascending=False)
    projs_df.reset_index(drop=True, inplace=True)

def get_days_record(start_year=2016, start_month=8, start_day=1):
    return get_days_record_range(start_year, start_month, start_day)