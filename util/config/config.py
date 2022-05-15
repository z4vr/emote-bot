import yaml

class Config:
    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            self.config = yaml.safe_load(f)
    
        self.token = self.config['token']
        self.prefix = self.config['prefix']