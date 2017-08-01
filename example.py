from ScheduleReport import *

proj_number = PI.get_proj_list()
PIs = PI.get_PI_list()

for i in range(6,13):
    get_monthly_report(2016,i,proj_number, PIs)

for i in range(1,8):
    get_monthly_report(2017,i,proj_number, PIs)
