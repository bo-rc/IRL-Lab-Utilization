import collections

class PI:
    PI_list = collections.defaultdict()
    proj_list = collections.defaultdict(str)
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.dept = kwargs.get('dept', [])
        self.proj = kwargs.get('proj', [])
        # updating proj_list
        PI.update_proj_list(self)
        
        # updating PI_list
        PI.update_PI_list(self)
        
    
    def __repr__(self):
        return 'PI: {} '.format(self.name) + ','.join(self.dept) + ' ' + ','.join(self.proj)
    
    def add_dept(self, s):
        self.dept.append(s)
        
    def add_proj(self, s):
        self.proj.append(s)
        
    def update_proj_list(self):
        for p in self.proj:               
            if p not in PI.proj_list.keys():
                PI.proj_list[p] = self.name
            else:
                pass
            
    def update_PI_list(self):
        if self.name not in PI.PI_list.keys():
            PI.PI_list[self.name] = self
        else:
            for p in self.proj:
                if p not in PI.PI_list[self.name].proj:
                    PI.PI_list[self.name].add_proj(p)
                else:
                    pass
            for dept in self.dept:
                if dept not in PI.PI_list[self.name].dept:
                    PI.PI_list[self.name].add_dept(dept)
                else:
                    pass
    
    @classmethod
    def get_PI_list(cls):
        return cls.PI_list
    
    @classmethod
    def get_proj_list(cls):
        return cls.proj_list

# constructing PIs
LuiSha = PI(name='Lui Sha',dept=['CS','CSL'],proj=['2016-08-100-02'])
RomitChoudhury = PI(name='Romit Roy Choudhury',dept=['ECE','CSL'],proj=['2017-06-100-01'])
SayanMitra = PI(name='Sayan Mitra',dept=['ECE','CSL'],proj=['2016-06-103-01'])
GirishKrishnan = PI(name='Girish Krishnan',dept=['ISE','CSL'],proj=['2017-03-106-01'])
SethHutchinson = PI(name='Seth Hutchinson', dept=['ECE', 'CSL'],proj=['2016-10-103-02', '2016-10-103-01'])
GraceGao = PI(name='Grace Gao', dept=['AE', 'CSL'], proj=['2016-11-103-01'])
MinhDo = PI(name='Minh Do', dept=['ECE', 'CSL'], proj=['2016-11-103-02'])
TimBretl = PI(name='Timothy Bretl', dept=['AE', 'CSL'], proj=['2017-02-103-02'])
MichaelSelig = PI(name='Michael Selig', dept=['AE'], proj=['2017-02-102-01'])
HwPark = PI(name='Hae-Won Park', dept=['ME', 'CSL'], proj=['2017-02-101-01'])
AimyWissa = PI(name='Aimy Wissa', dept=['ME'], proj=['2017-04-101-01'])
SayanMitra = PI(name='Sayan Mitra', dept=['ECE', 'CSL'], proj=['2017-03-103-01'])
PhilipAnsell = PI(name='Philip Ansell', dept=['AE'], proj=['2017-01-102-01'])
RomitRoyChoudhury = PI(name='Romit Roy Choudhury', dept=['ECE', 'CSL'], proj=['2016-08-100-01', '2017-02-100-01'])
GirishChowdhary = PI(name='Girish Chowdhary', dept=['ABE', 'CSL'], proj=['2016-11-105-01', '2016-10-105-01'])
AmyLaViers = PI(name='Amy LaViers', dept=['ME'], proj=['2016-12-101-01'])
NairaHovakimyan = PI(name='Naira Hovakimyan', dept=['ME','AE', 'CSL'], proj=['2016-08-101-01'])
PaulKwiat = PI(name='Paul G Kwiat', dept=['PHYS', 'ECE'], proj=['2016-08-104-01'])
DanWork = PI(name='Dan Work', dept=['CEE', 'CSL'], proj=['2017-06-107-01'])
