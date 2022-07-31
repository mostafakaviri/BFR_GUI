import serial
import PySimpleGUI as sg
import os
data = []
ser = serial.Serial('com19', 9600)
layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]
sg.Window(title="Hello World", layout=layout, margins=(100, 50)).read()
while(len(data) <= 25) :
    line = ser.readline().decode('utf-8')   # read a '\n' terminated line
    print(line,end='')
    data.append(line)

writing_path = 'C:\\Users\\Mostafa\\Desktop\\test_data'
writing_path += f'\\{int(os.listdir(writing_path)[-1][:-4])+1}.csv'
os.makedirs(os.path.dirname(writing_path), exist_ok=True)
with open(writing_path, 'w') as f:
    f.write(''.join(data))