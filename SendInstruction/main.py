import serial
import time
import json
import config


def read_config():
    # read config file
    with open('config.json') as f:
        conf = config.Config(**json.loads(f.read()))
    print('loaded config file is...')
    print('to_ip', conf.to_ip)
    print('dev_name', conf.dev_name)
    return conf

try:
    conf = read_config()

    # open serial device
    ser = serial.Serial(conf.dev_name, timeout=0.1)
    print('serial port is opened')

    # read from serial device
    while True:
        line = ser.readline()
        if line != "":
            print('read from device')
            print(line)

            # send ping to sending server

        else:
            time.sleep(0.1)

except KeyboardInterrupt as e:
    print('interrupted by ctrl+c')

except Exception as e:
    print(e)

finally:
    ser.close()
    print('serial port is closed')
