from ScheduleReport import PI
from ScheduleReport import CalFetch

proj_number = PI.PI.get_proj_list()
PIs = PI.PI.get_PI_list()

for i in range(6,13):
    CalFetch.get_monthly_report(2016,i,proj_number, PIs)

for i in range(1,8):
    CalFetch.get_monthly_report(2017,i,proj_number, PIs)
