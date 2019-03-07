import serial
import time

ser = serial.Serial("com5")
ser.timeout = 3
# Please set the multimeter to use new "LF" aka. "\n"
print(ser.name)
ser.write(b'*idn?\n')
print(ser.readline())
ser.write(b'func volt:dc\n')
ser.write(b'volt:dc:rang:auto 1\n')

#Preceeding commands need time to finish, so we wait for a little while.
time.sleep(1)

ser.write(b'fetch?\n')
print(ser.readline())
ser.write(b'fetch?\n')
print(ser.readline())
