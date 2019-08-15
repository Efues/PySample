import subprocess
import serial
import config
import form

from ftplib import *

def is_connectable(host):
    ping = subprocess.Popen(
        ["ping", "-c", "1", host],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
    ping.communicate()
    return ping.returncode == 0

#Main
try:
    conf = config.read()
    form = form.Form(conf=conf)

    print('Ping...')
    # send ping to host
    if(is_connectable(conf.server) is False):
        form.append_status(conf.server + " is disable")
    else:
        print('Enter FTP Process')
        # get db file from Server
        ftp = FTP(conf.server)
        ftp.login(conf.user, conf.passwd)
        #    print(ftp.nlst('.'))
        #    ftp.cwd('/')
        with open(conf.local_db_file_path, 'wb') as f:
            retr = 'RETR ' + conf.db_file
            ftp.retrbinary(retr, f.write)
        ftp.quit()
        print('DB file is downloaded')

    # open serial device
    form.serial = serial.Serial(conf.dev_name, timeout=0.1)
    form.append_status(text='serial port open')
    form.run()

except Exception as e:
    print(e)

finally:
    if form.serial is not None:
        form.serial.close()
        print('serial port is closed')
