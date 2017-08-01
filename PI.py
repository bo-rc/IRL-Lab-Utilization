import collections

class PI:
    PI_list = collections.defaultdict(list)
    proj_list = collections.defaultdict(str)
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.dept = kwargs.get('dept', [])
        self.proj = kwargs.get('proj', [])
        for p in self.proj:
            if not p in PI.PI_list[self.name]:
                PI.PI_list[self.name].append(p)
                
            if not p in PI.proj_list.keys():
                PI.proj_list[p] = self.name
    
    def __repr__(self):
        return 'PI: {} '.format(self.name) + ','.join(self.dept) + ' ' + ','.join(self.proj)
    
    def add_dept(s):
        self.dept.append(s)
        
    def add_proj(self, s):
        self.proj.append(s)
    
    @classmethod
    def get_PI_list(cls):
        return cls.PI_list
    
    @classmethod
    def get_proj_list(cls):
        return cls.proj_list

LuiSha = PI(name='Lui Sha',dept=['CS'],proj=['2016-08-100-02'])
RomitChoudhury = PI(name='Romit Roy Choudhury',dept=['ECE'],proj=['2017-06-100-01'])
SayanMitra = PI(name='Sayan Mitra',dept=['ECE'],proj=['2016-06-103-01'])
GirishKrishnan = PI(name='Girish Krishnan',dept=['ISE'],proj=['2017-03-106-01'])
SethHutchinson = PI(name='Seth Hutchinson', dept=['ECE'],proj=['2016-10-103-02', '2016-10-103-01'])
GraceGao = PI(name='Grace Gao', dept=['AE'], proj=['2016-11-103-01'])
MinhDo = PI(name='Minh Do', dept=['ECE'], proj=['2016-11-103-02'])
TimBretl = PI(name='Timothy Bretl', dept=['AE'], proj=['2017-02-103-02'])
MichaelSelig = PI(name='Michael Selig', dept=['AE'], proj=['2017-02-102-01'])
HwPark = PI(name='Hae-Won Park', dept=['ME'], proj=['2017-02-101-01'])
AimyWissa = PI(name='Aimy Wissa', dept=['ME'], proj=['2017-04-101-01'])
SayanMitra = PI(name='Sayan Mitra', dept=['ECE'], proj=['2017-03-103-01'])
PhilipAnsell = PI(name='Philip Ansell', dept=['AE'], proj=['2017-01-102-01'])
RomitRoyChoudhury = PI(name='Romit Roy Choudhury', dept=['ECE'], proj=['2016-08-100-01', '2017-02-100-01'])
GirishChowdhary = PI(name='Girish Chowdhary', dept=['ABE'], proj=['2016-11-105-01', '2016-10-105-01'])
AmyLaViers = PI(name='Amy LaViers', dept=['ME'], proj=['2016-12-101-01'])
NairaHovakimyan = PI(name='Naira Hovakimyan', dept=['ME'], proj=['2016-08-101-01'])
