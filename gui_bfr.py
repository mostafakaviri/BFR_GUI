from faulthandler import disable
from tkinter.tix import Tree
from xml.etree.ElementTree import Element
from pandas import Series
import PySimpleGUI as sg
import serial
import os
import PySimpleGUI as sg
import threading
import serial.tools.list_ports
import math
import matplotlib.pyplot as plt

# Colors
back_ground_color = '#025d63' 
Connecting_text = 'red'
startDisabledButtonColor = '#424d40'
stopDisabledButtonColor = '#705858'
stopButtonColor = '#c40404'
startButtonColor = '#277c11'
texts_color = '#c5cdbd'
rescan_button_color = '#063136'
connect_button_color = '#063136'
serial_sit = '#f1c906'
serial_sit_g = '#7dda36'
save_button_color = '#063136'
conection_sit = '#7dda36'
# matplotlib.use("TkAgg")

# def draw_figure(canvas, figure):
#     figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
#     figure_canvas_agg.draw()
#     figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
#     return figure_canvas_agg

# Class to get datas

class serial_thread (threading.Thread):

    def __init__(self, input_ser, class_window):
      threading.Thread.__init__(self)
      self.input_ser = input_ser
      self.class_window = class_window
      self._stop = threading.Event()
     
    def run(self):
        self.get_data()
      
    def stop(self):
        self._stop.set()
 
    def stopped(self):
        return self._stop.isSet()

    def get_data(self):

        while(True):
            #line = "0"
            if self.stopped():
                break
            try:
                line = self.input_ser.readline().decode('utf-8')   # read a '\n' terminated line

                #line = line[:5]
                data.append(line)
                #data_int.append(int(line[:-2]))

                self.class_window["-CURRENT_PRESSURE_VALUE-"].update(f'Pressure Value:  {line[:5]}')


            except:
                #data.append(data[len(data)-1])
                pass
             
            
            
# def lop_calculator(data):

#     data_max = max(data)
#     data_max_index = data.index(data_max)
#     cutted_data = data[data_max_index : ]
#     mydata = [x for x in cutted_data if int(x) > 60]
#     plt.plot([x for x in range(len(mydata))], mydata)


#     puls_data = lop_pre_calculator(mydata)
#     max_data = max_finder(puls_data)
#     min_data = min_finder(puls_data,max_data)
#     length_data = length_finder(max_data,min_data)
#     maximum_puls = max(max_data[0])



# def move_mean(data, integer=75):
#     n = len(data)
#     output = []
#     for i in range(n - 2*integer):
#         sum = 0

#         for j in range(integer*2):
#             sum += data[i+j]
#         output.append(sum/(2*integer))

#     return output

# def lop_pre_calculator(data, integer=75):
#     trend_1 = move_mean(data, integer)
#     trand_2 = move_mean(trend_1, integer)
#     mydata = data[2*integer: len(data)-2*integer]
#     ali = []

#     for i in range(len(mydata)):
#         ali.append(mydata[i] - trand_2[i])
#     return ali

# def max_finder(data):
#     dist = 100
#     n = len(data)
#     counter = 0
#     output = [[],[]]
#     i = 0
#     while True:

#         if counter + dist > n :
#             break
        
#         assistive_array = [data[counter:counter + dist]]
#         temp_max = max(assistive_array)
#         temp_max_index = assistive_array.index(temp_max)

#         counter += temp_max_index
#         if counter + dist > n :
#             break
#         assistive_array = [data[counter:counter + dist]]
#         temp_max2 = max(assistive_array)
#         temp_max_index2 = assistive_array.index(temp_max)
#         if temp_max2 > temp_max:
#             counter += temp_max_index2-1
#             continue
#         counter += temp_max_index2
#         output[0][i] = temp_max
#         output[1][i] = counter
#         i += 1
#     return output

# def min_finder(data, max_data):
#     output = [[],[]]

#     for i in range(len(max_data[1]) - 1):
#         min_mammad = min(data[max_data[1][i] : max_data[1][i + 1]])
#         index_min_mammad = data[max_data[1][i] : max_data[1][i + 1]].index(min_mammad)
#         output[0][i] = min_mammad
#         output[1][i] = index_min_mammad
#     return output

# def length_finder(max_data,min_data):
#     output = [[],[]]
#     for i in range(len(max_data[1]) - 1):
#         output[0][i] = max_data[0][i] - min_data[0][i]
#         output[1][i] = (max_data[1][i] + min_data[1][i])/2
#     return output



def setup_start(ser):
    ser.write

def serial_connection(input_com):
    try:
        function_ser = serial.Serial(input_com, 9600)
        return function_ser
    except serial.SerialException:
        return serial_connection(com_port)


my_ports = ['select']
flag = True
data = []
data_int = []
last_data = 0
com_port = ""

ports = serial.tools.list_ports.comports()
for port , desc , hwid in sorted(ports):
    my_ports.append(port)


#For show saved files
saved_test_list_column = [
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-SAVED TEST-"
        )
    ],
]

#To set a name for test resault
test_column = [
    [
        sg.Text("Pressure value:  0", font="Helvetica " + str(24), key = "-CURRENT_PRESSURE_VALUE-", text_color = texts_color, background_color = back_ground_color),
       # sg.Text("LOP: ",font="Helvetica " + str(24), key = "-CURRENT_PRESSURE_VALUE-", text_color = texts_color, background_color = back_ground_color, key = "-LOP_VALUE-" )
    ],
    [   
        sg.Text('Select COM', text_color = texts_color, background_color = back_ground_color),
        sg.Combo(my_ports, default_value=my_ports[0], key='com'),
        sg.Button('Rescan', key='-SCAN-', disabled = False, button_color = rescan_button_color),
        sg.Text("Connecting...", text_color = texts_color, key='statusC', background_color = back_ground_color)
    ],
    [
        
        sg.Button('CONNECT', key='cnct', button_color = connect_button_color),
        sg.Button("START",button_color = startButtonColor, disabled = True, disabled_button_color = startDisabledButtonColor, key = '-START_BUTTON-', use_ttk_buttons = True),
        
        sg.Button("STOP",button_color = stopButtonColor, disabled = True, disabled_button_color = stopDisabledButtonColor, key = '-STOP_BUTTON-', use_ttk_buttons = True),
    ], 
    [
        sg.Text("Choose Name:", text_color = texts_color, background_color = back_ground_color),
        sg.In(size=(25, 1), enable_events=True, key="-NAME-"),
        sg.Button("SAVE", button_color = save_button_color, key = "save"),
        sg.Text("Not saved", key = "-SITUATION-", text_color = texts_color, background_color = back_ground_color),
    ],
    [
        sg.Text("Serial data transfer has not began", key = "-SERIAL_SITUATION-", text_color = serial_sit, background_color = back_ground_color)
    ], 
   
]

layout_main = [
    [
        sg.Column(saved_test_list_column),
        sg.VSeperator(),
        sg.Column(test_column, element_justification = 'c', background_color = back_ground_color),
    ],
]

start_flag = False
window = sg.Window("BFR", layout_main, background_color = back_ground_color)

# Run the Event Loop

while True:

    event, values = window.read()

    if event == 'cnct':
        com_port = values["com"]
        window['statusC'].update("Connected", text_color  = conection_sit)
        print(com_port)
        window['-START_BUTTON-'].update(disabled = False)
        window['-STOP_BUTTON-'].update(disabled = False)
        
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    # Fill list of names

    try:

        file_list = os.listdir('.\\test_data')

    except:

        file_list = ["<File is empty>"]


    window["-SAVED TEST-"].update(file_list)

    # Start button

    if event == "-START_BUTTON-" and start_flag == False :
        
        start_flag = True
        ser = serial_connection(com_port)
        
        ser.write('1'.encode())
        my_thread = serial_thread(ser, window)
        
        my_thread.start() 
        
        window["-SERIAL_SITUATION-"].update("Seria data transer has began", text_color = serial_sit_g)
        window["-SCAN-"].update(disabled = True)
        window.Refresh()



    # Stop button

    if event =="-STOP_BUTTON-" and start_flag == True:
        #print("mammad")
        start_flag = False
        my_thread.stop()
        ser.write(bytes("0", 'utf-8'))
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        ser.close()
        #lop_calculator(data_int)
        window["-SERIAL_SITUATION-"].update("Serial data transfer has not began", text_color = 'red')
        window["-SCAN-"].update(disabled = False)
        window.Refresh()
    
    # Save button

    if event == "save" :
        #print(data)
        if(len(data) > 0) :
            name = values["-NAME-"]
            writing_path = '.\\test_data'
            writing_path += f'\\{name}.csv'
            os.makedirs(os.path.dirname(writing_path), exist_ok=True)
            with open(writing_path, 'w') as f:
                f.write(''.join(data))
            situation = "saved"
            window["-SITUATION-"].update("saved", text_color = 'green')
            #print(data)
            window.Refresh()
            data.clear()

        else:
            window["-SITUATION-"].update("There is nothing to save", text_color = 'yellow')
            window.Refresh()

    # if event == "-SCAN-":
    #     my_ports = ['select']
    #     ports = serial.tools.list_ports.comports()
    #     for port , desc , hwid in sorted(ports):
    #         my_ports.append(port)
    #     window["com"].update(my_ports, default_value= my_ports[0])
    #     window.Refresh()

window.close()
# bfr