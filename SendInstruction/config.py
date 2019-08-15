import json

class Config(object):
    def __init__(self, server, user, passwd, output_folder, db_file, dev_name, local_db_file_path):
        self.server = server
        self.user = user
        self.passwd = passwd
        self.output_folder = output_folder
        self.db_file = db_file
        self.dev_name = dev_name
        self.local_db_file_path = local_db_file_path

def read():
    # read config file
    with open('config.json') as f:
        conf = Config(**json.loads(f.read()))
    return conf


# Serialize example
#conf = Config( to_ip = '192.168.1.20', dev_name = '/dev/ttyACM0')
#with open('config.json', mode='w') as f:
#    f.write(json.dumps(conf.__dict__))
