from tkinter import *
from serial import Serial


ser = Serial('COM4', baudrate=9600, timeout=0.01)

links = [5]

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
    ser.write(links[0].to_bytes(1, byteorder='big', signed=0))

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
