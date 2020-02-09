import serial

ser = serial.Serial('/dev/tty1');
print(ser.name);
ser.close();
