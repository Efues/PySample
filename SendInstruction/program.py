import subprocess

import serial
import time
import config
import form

from ftplib import *
import os


def is_connectable(host):
    ping = subprocess.Popen(
        ["ping", "-c", "1", host],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
    ping.communicate()
    return ping.returncode == 0

ser = None
db_file_path = 'item.db'
try:
    conf = config.read()
    form = form.Form(conf=conf)

    # send ping to host
    if(is_connectable(conf.server) is False):
        form.append_status(conf.server + " is disable")
    else:
        # get db file from Server
        ftp = FTP(conf.server)
        ftp.login(conf.user, conf.passwd)
        #    print(ftp.nlst('.'))
        #    ftp.cwd('/')
        with open(db_file_path, 'wb') as f:
            retr = 'RETR ' + conf.db_file
            ftp.retrbinary(retr, f.write)
        ftp.quit()

    # open serial device
    ser = serial.Serial(conf.dev_name, timeout=0.1)
    form.append_status(text = 'serial port open')

    form.do_mainloop()
    # read from serial device
#    while True:
#        line = ser.readline()
#        if line != "":
#            print('read from device')
#            print(line)

            # send ping to sending server

#        else:
#            time.sleep(0.1)
except Exception as e:
    print(e)

finally:
    if ser is not None:
        ser.close()
        print('serial port is closed')
