from tkinter import *
from serial import Serial
import time


ser = Serial('COM4', baudrate=9600)
time.sleep(2)

params = [0, 0, 0] # скорость, угол, направление

def Speed_up():
    if 0 <= params[0] < 1000:
        params[0] += 1
    labelSpeed['text'] = 'Скорость = %s' % params[0]

def Speed_dn():
    if 0 < params[0] <= 1000:
        params[0] -= 1
    labelSpeed['text'] = 'Скорость = %s' % params[0]


def Angle_up():
    if 0 <= params[1] < 180:
        params[1] += 1
    labelAngle['text'] = 'Угол = %s' % params[1]

def Angle_dn():
    if 0 < params[1] <= 180:
        params[1] -= 1
    labelAngle['text'] = 'Угол = %s' % params[1]


def Dir_up():
    if params[2] == 0:
        params[2] += 1
    labelDir['text'] = 'Направление = %s' % params[2]


def Dir_dn():
    if params[2] == 1:
        params[2] -= 1
    labelDir['text'] = 'Направление = %s' % params[2]


def arduino_send():
   ser.reset_input_buffer()
   ser.write('$')
   ser.write(params[0])
   ser.write(' ')
   ser.write(params[1])
   ser.write(' ')
   ser.write(params[2])
   ser.write(';')
   root.after(500, arduino_send)


def arduino_read():
    print(ser.read_until('<').decode('ascii'))
    root.after(500, arduino_read)



root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)

labelSpeed = Label(frame1, text='Скорость = %s' % params[0])
labelSpeed.pack(side='left')

buttonSpeed_up = Button(frame1, text='+', command=Speed_up)
buttonSpeed_up.pack(side='right')
buttonSpeed_dn = Button(frame1, text='-', command=Speed_dn)
buttonSpeed_dn.pack(side='right')

labelAngle = Label(frame2, text='Угол = %s' % params[1])
labelAngle.pack(side='left')

buttonAngle_up = Button(frame2, text='+', command=Angle_up)
buttonAngle_up.pack(side='right')
buttonAngle_dn = Button(frame2, text='-', command=Angle_dn)
buttonAngle_dn.pack(side='right')

labelDir = Label(frame3, text='Направление = %s' % params[2])
labelDir.pack(side='left')

buttonDir_up = Button(frame3, text='+', command=Dir_up)
buttonDir_up.pack(side='right')
buttonDir_dn = Button(frame3, text='-', command=Dir_dn)
buttonDir_dn.pack(side='right')


frame1.pack()
frame2.pack()
frame3.pack()
root.after(500, arduino_send)
root.after(500, arduino_read)
root.mainloop()
