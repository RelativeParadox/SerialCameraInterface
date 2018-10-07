#Wakes Camera and Takes a Picture
import serial
import time

#Opens port
port = serial.Serial('/dev/ttyS0')

#Syncs Camera
syncCount = 0
while syncCount < 60:
        port.write(b'\xAA\x0D\x00\x00\x00\x00')
        syncCount = syncCount + 1
        port.write(b'\xAA\x0E\x0D\x00\x00\x00')

#Wait 2 Sec
time.sleep(2)

#Initalize Camera
port.write(b'\xAA\x01\x00\x08\x09\x07')

#Take Picture
port.write(b'\xAA\x04\x02\x00\x00\x00')

#Wait for Data
time.sleep(10)

#Thanks Camera
port.write(b'\xAA\x0E\x0D\x00\x00\x00')
