import serial

#Open Serial Port
serialPort = serial.Serial('/dev/ttyS0', timeout = 1)

#Open Txt File
output = open('data.txt', 'w')

i = 0
while i < 240:
    i = i + 1
    text = serialPort.readline()
    line = 'line: ' + str(i)
    print(line)
    output.write(line)
    print(text)
    output.write(text.decode('utf-8'))
output.close()
