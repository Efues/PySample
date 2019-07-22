import json

class Config(object):
    def __init__(self, to_ip, dev_name):
        self.to_ip = to_ip
        self.dev_name = dev_name




# Serialize example
#conf = Config( to_ip = '192.168.1.20', dev_name = '/dev/ttyACM0')
#with open('config.json', mode='w') as f:
#    f.write(json.dumps(conf.__dict__))
