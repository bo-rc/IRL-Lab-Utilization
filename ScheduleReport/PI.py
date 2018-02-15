import collections, copy

class PI:
    
    PI_dict = collections.defaultdict()
    proj_dict = collections.defaultdict(str)
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.dept = kwargs.get('dept', '')
        self.app = kwargs.get('app', [])
        self.proj = kwargs.get('proj', {})
        # updating proj_list
        PI.update_proj_dict(self)
        
        # updating PI_list
        PI.update_PI_dict(self)
        
    
    def __repr__(self):
        return 'PI: {} '.format(self.name) + ' ' + self.dept + ' ' + ','.join(self.app) + ' ' + ','.join(self.proj)
    
    def add_app(self, s):
        self.app.append(s)
        
    def add_proj(self, proj_num, cfop):
        self.proj[proj_num] = cfop
        
    def update_proj_dict(self):
        for key in self.proj.keys():               
            if key not in PI.proj_dict.keys():
                PI.proj_dict[key] = self.name
            else:
                pass
            
    def update_PI_dict(self):
        if self.name not in PI.PI_dict.keys():
            PI.PI_dict[self.name] = copy.deepcopy(self)
        else:
            for key in self.proj.keys():
                if key not in PI.PI_dict[self.name].proj.keys():
                    PI.PI_dict[self.name].proj[key] = self.proj[key]
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

# Here starts the database
# You can modify this section for each PI, 
# or add PI entries to update the database.
LuiSha = PI(name='Lui Sha',dept='CS', app=['CS','CSL'],proj={'2016-08-100-02': 'cfop_SHA'})
RomitChoudhury = PI(name='Romit Roy Choudhury',dept='ECE', app=['ECE','CSL'],proj={'2017-06-100-01': 'cfop_CHOUDHURY'})
# yes, you can have duplicate, as long as the PI name is the same, they will merge as a same entry in the PI_dict
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
GeirDullerud = PI(name='Geir Dullerud', dept='ME', app=['ME', 'CS', 'CSL'], proj={'2017-09-101-01': 'cfop_DULLERUD'})
