import tkinter as tk
import datetime
from tkinter import ttk
from time import sleep
from random import uniform
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk
from thread import Thread

def get_time():
    while True:
        date_time = datetime.datetime.now()
        label_time_SYS_now.config(text = date_time.strftime(" %Y.%m.%d %H:%M:%S "))
        sleep(0.5)

def play():
    while True:
        lat_rnd = uniform(59, 61)
        long_rnd = uniform(29, 31)
        marker.set_position(lat_rnd, long_rnd)
        map_widget.set_position(lat_rnd, long_rnd)
        sleep(1)

# чтение файла с записанными ранее координатами
def read_file():
    i = 0
    with open('gnss.txt', 'r') as f:
        nums = f.read().splitlines()
    len_nums = len(nums)
    while i < len_nums:
        # чтение и формирование времени
        num_csv = nums[i].split(',')
        time_now = num_csv[1]
        time_now = time_now[2:8]
        time_now_hh = time_now[:2]
        time_now_mm = time_now[2:4]
        time_now_ss = time_now[4:6]
        time_file = time_now_hh + ':' + time_now_mm + ':' + time_now_ss

        # чтение и формирование даты
        date_now = num_csv[9]
        date_now = date_now[2:8]
        date_now_dd = date_now[:2]
        date_now_mm = date_now[2:4]
        date_now_gg = date_now[4:6]
        date_file = date_now_dd + '.' + date_now_mm + '.20' + date_now_gg
        # формирование строки даты и времени
        date_time_file = date_file + ' ' + time_file
        # преобразование строки даты и времени в объект datetime
        date_time_file_object = datetime.datetime.strptime(date_time_file, "%d.%m.%Y %H:%M:%S")
        #  выводим дату и время в label_time_UTC_now
        label_time_UTC_now.config(text = date_time_file_object.strftime(" %Y.%m.%d %H:%M:%S "))

        #  чтение и формирование координат (широта и долгота)
        lat_now = num_csv[3]
        lat_now = lat_now[2:15]
        lat_d = int(lat_now[0:2])
        lat_m = int(lat_now[2:4])
        lat_s = int(lat_now[5:9])

        latitude_file = lat_d + (lat_m / 60) + (lat_s / 3600)

        print(lat_d, ' ', lat_m, ' ', lat_s)
        print(latitude_file)

        sleep(1)
        i += 1

def bt_on():
    thread_01 = Thread(target=play, daemon=True)
    thread_01.start()

def bt_exit():
    exit()

def bt_play():
    thread_03 = Thread(target=read_file, daemon=True)
    thread_03.start()

database_path = 'file.db'

root = tk.Tk()
root.geometry('1920x1080')
root.attributes('-fullscreen', True)
root.resizable(False, False)

frame_root = tk.Frame(root, width=1600, height=1060, borderwidth=2, relief='groove')
frame_root.place(x=10, y=10)

frame_tray = tk.Frame(root, width=290, height=1060, borderwidth=2, relief='groove')
frame_tray.place(x=1620, y=10)


label_time_SYS = ttk.Label(frame_tray, text='Дата и Системное время:', font=('Arial', 15))
label_time_SYS.place(x = 10, y = 10)

label_time_SYS_now = ttk.Label(frame_tray, relief='groove', font=('Arial', 20))
label_time_SYS_now.place(x = 10, y = 40)

# поля проигрывания информации из файла
# дата и время
label_time_UTC = ttk.Label(frame_tray, text='Дата и время UTC:', font=('Arial', 15))
label_time_UTC.place(x = 10, y = 100)

label_time_UTC_now = ttk.Label(frame_tray, text=' 0000.00.00 00:00:00 ', relief='groove', font=('Arial', 20))
label_time_UTC_now.place(x = 10, y = 130)


bt_exit = ttk.Button(frame_tray, text='ВЫХОД', width=15, command=bt_exit)
bt_exit.place(x = 175, y = 940)

bt_connect = ttk.Button(frame_tray, text='ПОДКЛЮЧИТЬ', width=15, command=bt_on)
bt_connect.place(x = 175, y = 980)

bt_play = ttk.Button(frame_tray, text='ПРОИГРАТЬ', width=15, command=bt_play)
bt_play.place(x = 175, y = 1020)

frame_widget = tk.Frame(frame_root, width=1570, height=1000, borderwidth=2, relief='solid')
frame_widget.place(x=10, y=10)

initial_image = Image.open("flight_01.ico")
initial_icon = ImageTk.PhotoImage(initial_image)

map_widget = TkinterMapView(frame_widget, width=1570, height=1000, corner_radius=0, use_database_only=True,
                            max_zoom=14, database_path=database_path)
map_widget.pack(fill="both", expand=True)
map_widget.set_zoom(10)
map_widget.set_position(60.0743, 30.26)
marker = map_widget.set_marker(60.0743, 30.26, text = 'IL-114', icon = initial_icon)

thread_02 = Thread(target=get_time, daemon=True)
thread_02.start()

root.mainloop()
