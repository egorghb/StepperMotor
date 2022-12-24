from tkinter import *
from serial import Serial
import time


ser = Serial('COM4', baudrate=9600)
time.sleep(2)

params = [0, 0, 0] # скорость, угол, направление

def link_0_up():
    if 0 <= links[0] < 180:
        links[0] += 1
    label1['text'] = 'Скорость = %s' % links[0]

def link_0_dn():
    if 0 < links[0] <= 180:
        links[0] -= 1
    label1['text'] = 'Скорость = %s' % links[0]


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
print(root.children)

frame1 = Frame(root)

label1 = Label(frame1, text='Скорость = %s' % links[0])
label1.pack(side='left')

button0_up = Button(frame1, text='+', command=link_0_dn)
button0_up.pack(side='right')
button0_dn = Button(frame1, text='-', command=link_0_up)
button0_dn.pack(side='right')

frame1.pack()
root.after(500, arduino_send)
root.after(500, arduino_read)
root.mainloop()
