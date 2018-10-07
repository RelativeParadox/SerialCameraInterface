import serial
serialPort = serial.Serial('/dev/ttyS0')
while True:
    text = serialPort.readline()
    print(text)
