import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import PI, CalFetch

proj_number = PI.get_proj_list()
PIs = PI.get_PI_list()

proj = fetch_month(2017,4)

pi_hours = {}
dept_hours = {}

for key, value in proj.items():
    
    if key not in proj_number.keys():
        raise RuntimeError("unknown project number from PI database, key = {}".format(key))
        
    name = proj_number[key]
    
    if name not in pi_hours.keys():
        pi_hours[name] = value
    else:
        pi_hours[name] += value
    
    d = PIs[name].dept
    
    for i in d:
        if i not in dept_hours.keys():
            dept_hours[i] = value
        else:
            dept_hours[i] += value


pi_data = pd.DataFrame(list(pi_hours.items()))
pi_data.columns = ['name', 'hours']
pi_data = pi_data.sort_values('hours', ascending=False)
pi_data.reset_index(drop=True, inplace=True)

dept_list = []
for index, row in pi_data.iterrows():
    key = row['name']
    dept = PIs[key].dept
    dept_list.append(dept)

pi_data['dept'] = pd.Series(dept_list)

dept_data = pd.DataFrame(list(dept_hours.items()))
dept_data.columns = ['dept', 'hours']
dept_data = dept_data.sort_values('hours', ascending=False)
dept_data.reset_index(drop=True, inplace=True)

plt.suptitle("2017-4", y=1.0)
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

plt.tight_layout()
