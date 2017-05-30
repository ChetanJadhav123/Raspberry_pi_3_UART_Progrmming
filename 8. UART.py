'''
import serial

import os


ser = serial.Serial("/dev/ttyAMA0")

ser.baudrate=(9600)

data = ser.readline(10)

ser.write(data)

ser.close()




'''


import serial

port = serial.Serial ("/dev/ttyAMA0", baudrate-9600, timeout=0.2)

while True:
      rcv=port.redline()
      if len(rcv)>10:
          print(rcv)
