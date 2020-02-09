import serial
import binascii

def writeValues(Port,DataToWrite):
    return Port.write(DataToWrite);            

def readValues(Port, AmountToRead):
    return Port.read(AmountToRead);

def printSeparator():
    print("-----------------------------------------------")
    return;

def openPortV1():
    #Demonstration of a port being opened through setters

    #Create blank serial object
    OpenPort = serial.Serial();

    #Set the name of the port being used
    OpenPort.port = "/dev/ttyUSB0";

    #Set the baudrate for the port
    OpenPort.baudrate = 9600;

    #Set the amount of time for read()
    #to wait to receive a byte
    OpenPort.timeout = 1.0;

    #Set the number of bytes to be expected
    OpenPort.bytesize = serial.EIGHTBITS;

    #Set the parity to be used
    OpenPort.parity = serial.PARITY_EVEN;

    #Set the number of stop bits to be expected
    OpenPort.stopbits = serial.STOPBITS_ONE;
    
    return OpenPort;

def openPortV2():
    
    #Demonstration of a port being opened through constructor 
    OpenPort = serial.Serial("/dev/ttyUSB0", 9600, 
                             serial.EIGHTBITS, 
                             serial.PARITY_EVEN, 
                             serial.STOPBITS_ONE, 1.0);
    
    return OpenPort;

def main():
    OpenPort = openPortV2();

    print("Port: ",OpenPort.name)

    #if(OpenPort.is_open == False):
        #OpenPort.open();
    
    printSeparator();
    
    ValuesToWrite = [3, 7, 21, 15, 25, 23, 6, 255];

    #Demonstration of values being written to port and read
    print(ValuesToWrite[0:4])
    TempVal = ValuesToWrite[0:4];
    OpenPort.write(TempVal);
    print(OpenPort.read(len(TempVal)))

    printSeparator();
    
    #Demonstration of values being written to port, read, and saved as variable of certain type
    print(ValuesToWrite[4:8])
    writeValues(OpenPort,ValuesToWrite[4:8])
    ReadValues = readValues(OpenPort,4);
    print(ReadValues)

    printSeparator();

    #Demonstration of variable being typed
    print(type(ReadValues))

    printSeparator();

    #Demonstration of variable being converted from type to string
    IntValues = int(ReadValues.hex(),16);
    print(IntValues)

    printSeparator();
    
    #Demonstration of Individual Values being Converted
    for i in range(len(ReadValues)):
        print(ReadValues[i])

    printSeparator();

    for k in range(10):
        writeValues(OpenPort, [k]);
        print(int(readValues(OpenPort, 1).hex(), 16));
    
    #Demonstration of port being closed
    OpenPort.close();
    
    return;

main()

#use usb-devices to determine if the device is connected
#Changing to different bit modes will print differing values, could be used to print ASCII
