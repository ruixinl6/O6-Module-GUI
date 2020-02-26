print('This code sends position commands through serial port to O=6 Module.')

import serial
import time


DEBUG_NO_SERIAL = 0
ser = serial.Serial(port = '/../../dev/ttyACM0', baudrate = '115200')


if DEBUG_NO_SERIAL == 0:
    ser.write('FFO\n')  # scan online modules
    msg = ser.readline()
    print('Scanned online modules: ' +msg)

start = time.time()
while True:
    time.sleep(0.1)
    ser.write('FFP29000R\n') # From Lu's Matlab version, it says that the encoder starts from 65535.
    # print('Position command sent.')
    end = time.time() 
    if end-start > 3:
        ser.close()
        exit()


