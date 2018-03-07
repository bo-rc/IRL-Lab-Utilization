from .PI import PI

"""
Here starts the database
 -  You can modify this section for each PI, or add PI entries to update the database.
 -  PI.dept is the home department of the PI
 -  PI.app is the appointments of the PI, starting with the PI's home department
 - You may have duplicates, as long as the PI name is the same, they will merge as a same entry
"""
LuiSha = PI(name='Lui Sha',dept='CS', app=['CS','CSL'],proj={'2016-08-100-02': 'cfop_SHA'})
RomitChoudhury = PI(name='Romit Roy Choudhury',dept='ECE', app=['ECE','CSL'],proj={'2017-06-100-01': 'cfop_CHOUDHURY'})
# Yes, you may have duplicates, as long as the PI name is the same, they will merge as a same entry in the PI_dict
RomitRoyChoudhury = PI(name='Romit Roy Choudhury', dept='ECE', app=['ECE', 'CSL'], proj={'2016-08-100-01': 'cfop_RRC', '2017-02-100-01': 'cfop_RRC'})
SayanMitra = PI(name='Sayan Mitra',dept='ECE', app=['ECE','CSL'],proj={'2016-06-103-01': 'cfop_MITRA', '2017-03-103-01': 'cfop_MITRA'})
GirishKrishnan = PI(name='Girish Krishnan',dept='ISE', app=['ISE','CSL'],proj={'2017-03-106-01': 'cfop_KRISHNAN'})
SethHutchinson = PI(name='Seth Hutchinson', dept='ECE', app=['ECE', 'CSL'],proj={'2016-10-103-02': 'cfop_HUTCHINSON', '2016-10-103-01': 'cfop_HUTCHINSON'})
GraceGao = PI(name='Grace Gao', dept='AE', app=['AE', 'CSL'], proj={'2016-11-103-01': 'cfop_GAO'})
MinhDo = PI(name='Minh Do', dept='ECE', app=['ECE', 'CSL'], proj={'2016-11-103-02': 'cfop_DO'})
TimBretl = PI(name='Timothy Bretl', dept='AE', app=['AE', 'CSL'], proj={'2017-02-103-02': 'cfop_BRETL'})
MichaelSelig = PI(name='Michael Selig', dept='AE', app=['AE'], proj={'2017-02-102-01': 'cfop_SELIG'})
HwPark = PI(name='Hae-Won Park', dept='ME', app=['ME', 'CSL'], proj={'2017-02-101-01': 'cfop_PARK'})
AimyWissa = PI(name='Aimy Wissa', dept='ME', app=['ME'], proj={'2017-04-101-01': 'cfop_WISSA'})
PhilipAnsell = PI(name='Philip Ansell', dept='AE', app=['AE'], proj={'2017-01-102-01': 'cfop_ANSELL'})
GirishChowdhary = PI(name='Girish Chowdhary', dept='ABE', app=['ABE', 'CSL'], proj={'2016-11-105-01': 'cfop_GC', '2016-10-105-01': 'cfop_GC'})
AmyLaViers = PI(name='Amy LaViers', dept='ME', app=['ME'], proj={'2016-12-101-01': 'cfop_LAVIER'})
NairaHovakimyan = PI(name='Naira Hovakimyan', dept='ME', app=['ME','AE', 'CSL'], proj={'2016-08-101-01': 'cfop_NH'})
PaulKwiat = PI(name='Paul G Kwiat', dept='PHYS', app=['PHYS', 'ECE'], proj={'2016-08-104-01': 'cfop_KWIAT', '2018-01-104-01': 'cfop_KWIAT'})
DanWork = PI(name='Dan Work', dept='CEE', app=['CEE', 'CSL'], proj={'2017-06-107-01': 'cfop_WORK'})
SibinMohan = PI(name='Sibin Mohan', dept='CS', app=['CS', 'CSL'], proj={'2017-12-100-01': 'cfop_sibin'})
GeirDullerud = PI(name='Geir Dullerud', dept='ME', app=['ME', 'CS', 'CSL'], proj={'2017-09-101-01': 'cfop_DULLERUD', '2018-03-101-01': 'cfop_DULLERUD_1'})
