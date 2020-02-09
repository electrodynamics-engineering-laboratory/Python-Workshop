from tkinter import *
import serial,time, struct
import time
ser = serial.Serial()

ser.port = "COM4"

ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
#ser.timeout = None          #block read
ser.timeout = 1            #non-block read
#ser.timeout = 2              #timeout block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2     #timeout for write

root =Tk()

root.title("Seaweed")
root.geometry("600x600")
def digital_out(pin,value):
    ser.open()
    ser.write('D'.encode())
    time.sleep(1/1000000)
    ser.write(pin.encode())
    time.sleep(1/1000000)
    ser.write(value.encode())
    time.sleep(1/1000000)
    ser.close()

app = Frame(root)
app.grid()
def main():

    #OFF buttons
    button1 = Button(app, text ='OFF',command=lambda:digital_out('0','0'))
    button1.grid(row =0,column=0)
    button2 = Button(app, text='OFF', command=lambda: digital_out('1', '0'))
    button2.grid(row=1, column=0)
    button3 = Button(app, text='OFF', command=lambda: digital_out('2', '0'))
    button3.grid(row=2, column=0)
    button4 = Button(app, text='OFF', command=lambda: digital_out('3', '0'))
    button4.grid(row=3, column=0)
    button5 = Button(app, text='OFF', command=lambda: digital_out('4', '0'))
    button5.grid(row=4, column=0)
    button6 = Button(app, text='OFF', command=lambda: digital_out('5', '0'))
    button6.grid(row=5, column=0)
    button7 = Button(app, text='OFF', command=lambda: digital_out('6', '0'))
    button7.grid(row=6, column=0)
    button8 = Button(app, text='OFF', command=lambda: digital_out('7', '0'))
    button8.grid(row=7, column=0)

    #ON buttons
    button9 = Button(app, text ='ON',command=lambda:digital_out('0','1'))
    button9.grid(row =0,column=1)
    button10 = Button(app, text='ON', command=lambda: digital_out('1', '1'))
    button10.grid(row=1, column=1)
    button11 = Button(app, text='ON', command=lambda: digital_out('2', '1'))
    button11.grid(row=2, column=1)
    button12 = Button(app, text='ON', command=lambda: digital_out('3', '1'))
    button12.grid(row=3, column=1)
    button13 = Button(app, text='ON', command=lambda: digital_out('4', '1'))
    button13.grid(row=4, column=1)
    button14 = Button(app, text='ON', command=lambda: digital_out('5', '1'))
    button14.grid(row=5, column=1)
    button15 = Button(app, text='ON', command=lambda: digital_out('6', '1'))
    button15.grid(row=6, column=1)
    button16 = Button(app, text='ON', command=lambda: digital_out('7', '1'))
    button16.grid(row=7, column=1)

    #Labels
    Dig0 = Label(app, text="Digital 0")
    Dig0.grid(row=0, column=3)
    Dig1 = Label(app, text="Digital 1")
    Dig1.grid(row=1, column=3)
    Dig2 = Label(app, text="Digital 2")
    Dig2.grid(row=2, column=3)
    Dig3 = Label(app, text="Digital 3")
    Dig3.grid(row=3, column=3)
    Dig4 = Label(app, text="Digital 4")
    Dig4.grid(row=4, column=3)
    Dig5 = Label(app, text="Digital 5")
    Dig5.grid(row=5, column=3)
    Dig6 = Label(app, text="Digital 6")
    Dig6.grid(row=6, column=3)
    Dig7 = Label(app, text="Digital 7")
    Dig7.grid(row=7, column=3)
main()


app.mainloop()