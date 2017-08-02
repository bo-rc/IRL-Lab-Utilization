from ScheduleReport import Report as rp

rp.get_days_record()

for i in range(6,13):
    rp.report_month(2016,i)

for i in range(1,8):
    rp.report_month(2017,i)