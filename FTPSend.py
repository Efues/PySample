from ftplib import *
import os

file_path='./test1.csv'
try:
    ftp = FTP('localhost')
    ftp.login('pi', 'password')
    ftp.cwd('/home/pi/scripts')
    ftemp = ftp.nlst('.')
    for file in ftemp:
        print(file)

    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            ftp.storlines('STOR /home/pi/share/sentByFTP.csv', f)
        print('file sent without error.')
    else:
        print ('selected file does not exist!')

    ftp.quit()
except Exception as e:
    print(e.message)

