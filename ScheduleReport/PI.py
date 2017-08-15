import collections

class PI:
    
    PI_dict = collections.defaultdict()
    proj_dict = collections.defaultdict(str)
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.dept = kwargs.get('dept', '')
        self.app = kwargs.get('app', [])
        self.proj = kwargs.get('proj', [])
        # updating proj_list
        PI.update_proj_dict(self)
        
        # updating PI_list
        PI.update_PI_dict(self)
        
    
    def __repr__(self):
        return 'PI: {} '.format(self.name) + ' ' + self.dept + ' ' + ','.join(self.app) + ' ' + ','.join(self.proj)
    
    def add_app(self, s):
        self.app.append(s)
        
    def add_proj(self, s):
        self.proj.append(s)
        
    def update_proj_dict(self):
        for p in self.proj:               
            if p not in PI.proj_dict.keys():
                PI.proj_dict[p] = self.name
            else:
                pass
            
    def update_PI_dict(self):
        if self.name not in PI.PI_dict.keys():
            PI.PI_dict[self.name] = self
        else:
            for p in self.proj:
                if p not in PI.PI_dict[self.name].proj:
                    PI.PI_dict[self.name].add_proj(p)
                else:
                    pass
            for app in self.app:
                if app not in PI.PI_dict[self.name].app:
                    PI.PI_dict[self.name].add_app(app)
                else:
                    pass
    
    @classmethod
    def get_PI_dict(cls):
        return cls.PI_dict
    
    @classmethod
    def get_proj_dict(cls):
        return cls.proj_dict

LuiSha = PI(name='Lui Sha',dept='CS', app=['CS','CSL'],proj=['2016-08-100-02'])
RomitChoudhury = PI(name='Romit Roy Choudhury',dept='ECE', app=['ECE','CSL'],proj=['2017-06-100-01'])
SayanMitra = PI(name='Sayan Mitra',dept='ECE', app=['ECE','CSL'],proj=['2016-06-103-01'])
GirishKrishnan = PI(name='Girish Krishnan',dept='ISE', app=['ISE','CSL'],proj=['2017-03-106-01'])
SethHutchinson = PI(name='Seth Hutchinson', dept='ECE', app=['ECE', 'CSL'],proj=['2016-10-103-02', '2016-10-103-01'])
GraceGao = PI(name='Grace Gao', dept='AE', app=['AE', 'CSL'], proj=['2016-11-103-01'])
MinhDo = PI(name='Minh Do', dept='ECE', app=['ECE', 'CSL'], proj=['2016-11-103-02'])
TimBretl = PI(name='Timothy Bretl', dept='AE', app=['AE', 'CSL'], proj=['2017-02-103-02'])
MichaelSelig = PI(name='Michael Selig', dept='AE', app=['AE'], proj=['2017-02-102-01'])
HwPark = PI(name='Hae-Won Park', dept='ME', app=['ME', 'CSL'], proj=['2017-02-101-01'])
AimyWissa = PI(name='Aimy Wissa', dept='ME', app=['ME'], proj=['2017-04-101-01'])
SayanMitra = PI(name='Sayan Mitra', dept='ECE', app=['ECE', 'CSL'], proj=['2017-03-103-01'])
PhilipAnsell = PI(name='Philip Ansell', dept='AE', app=['AE'], proj=['2017-01-102-01'])
RomitRoyChoudhury = PI(name='Romit Roy Choudhury', dept='ECE', app=['ECE', 'CSL'], proj=['2016-08-100-01', '2017-02-100-01'])
GirishChowdhary = PI(name='Girish Chowdhary', dept='ABE', app=['ABE', 'CSL'], proj=['2016-11-105-01', '2016-10-105-01'])
AmyLaViers = PI(name='Amy LaViers', dept='ME', app=['ME'], proj=['2016-12-101-01'])
NairaHovakimyan = PI(name='Naira Hovakimyan', dept='ME', app=['ME','AE', 'CSL'], proj=['2016-08-101-01'])
PaulKwiat = PI(name='Paul G Kwiat', dept='PHYS', app=['PHYS', 'ECE'], proj=['2016-08-104-01'])
DanWork = PI(name='Dan Work', dept='CEE', app=['CEE', 'CSL'], proj=['2017-06-107-01'])