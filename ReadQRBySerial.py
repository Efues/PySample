import serial
import time

try:
    ser = serial.Serial('/dev/ttyACM0', timeout=0.1)
    print('serial port is opened')
    while True:
        line = ser.readline()
        if line != "":
            print (line)
        else:
            time.sleep(0.1)

except KeyboardInterrupt as e:
    print('interrupted by ctrl+c')
except Exception as e:
    print(e)
finally:
    ser.close()
    print('serial port is closed')
