from ScheduleReport import PI
from ScheduleReport import CalFetch

proj_number = PI.PI.get_proj_list()
PIs = PI.PI.get_PI_list()

for i in range(6,13):
    CalFetch.get_monthly_report(2016,i,proj_number, PIs)

for i in range(1,8):
    CalFetch.get_monthly_report(2017,i,proj_number, PIs)

import numpy as np

day_data = pd.DataFrame(list(day.items()))
day_data.columns = ['day', 'hours']
day_data = day_data.sort_values('day')
day_data.reset_index(drop=True, inplace=True)
day_data['hours'] = day_data['hours'].astype(int)

# df.to_csv(r'c:\data\pandas.txt', header=None, index=None, sep=' ', mode='a')
day_data.to_csv(r'.\overall_days.txt', header=None, index=None, sep=' ', mode='a')

proj_data = pd.DataFrame(list(proj.items()))
proj_data.columns = ['num', 'hours']
proj_data = proj_data.sort_values('hours', ascending=False)
proj_data.reset_index(drop=True, inplace=True)

names = []
for num in proj_data['num']:
    names.append(PI.proj_list[num])

proj_data['num'] = names
proj_data.columns = ['name', 'hours']

proj_data = proj_data.groupby('name').sum()
proj_data = proj_data.reset_index()

plt.style.use('seaborn')

labels = list(proj_data['name'])
values = list(proj_data['hours'])
explode = np.zeros(len(values))

plt.pie(values, explode=explode, labels=labels, autopct='%2.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('overall percentage usage')
plt.savefig('overall_percentage.jpg')

proj_data.to_excel('overall_percentage.xlsx')