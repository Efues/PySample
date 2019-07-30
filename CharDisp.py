import smbus
import time

i2c = smbus.SMBus(1)  # 1 is bus number
addr02 = 0x3e  # lcd
_command = 0x00
_data = 0x40
_clear = 0x01
_home = 0x02
display_On = 0x0f
LCD_2ndline = 0x40 + 0x80

# LCD AQM0802/1602
def command(code):
    i2c.write_byte_data(addr02, _command, code)
    time.sleep(0.1)


def writeLCD(message):
    mojilist = []
    for moji in message:
        mojilist.append(ord(moji))
    i2c.write_i2c_block_data(addr02, _data, mojilist)
    time.sleep(0.1)


def init():
    command(0x38)
    command(0x39)
    command(0x14)
    command(0x73)
    command(0x56)
    command(0x6c)
    command(0x38)
    command(_clear)
    command(display_On)


# main
init()

command(_clear)
writeLCD("Hello   ")
command(LCD_2ndline)
writeLCD("World!  ")
time.sleep(2)

command(_clear)
writeLCD("This is ")
command(LCD_2ndline)
writeLCD("a pen   ")
