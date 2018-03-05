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
