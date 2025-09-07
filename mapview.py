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

def bt_on():
    thread_01 = Thread(target=play, daemon=True)
    thread_01.start()

def bt_exit():
    exit()

# чтение файла с записанными ранее координатами
def read_file():
    i = 0
    with open('gnss.txt', 'r') as f:
        nums = f.read().splitlines()
    len_nums = len(nums)
    while i < len_nums:
        num_csv = nums[i].split(',')
        label_time_UTC_now.configure(text='i')
        sleep(1)
        i += 1

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

label_time_UTC = ttk.Label(frame_tray, text='Дата и время UTC:', font=('Arial', 15))
label_time_UTC.place(x = 10, y = 100)

label_time_UTC_now = ttk.Label(frame_tray, text=' 0000.00.00 00:00:00 ', relief='groove', font=('Arial', 20))
label_time_UTC_now.place(x = 10, y = 130)

bt_exit = ttk.Button(frame_tray, text='ВЫХОД', width=15, command=bt_exit)
bt_exit.place(x = 175, y = 940)

bt_connect = ttk.Button(frame_tray, text='ПОДКЛЮЧИТЬ', width=15, command=bt_on)
bt_connect.place(x = 175, y = 980)

bt_connect = ttk.Button(frame_tray, text='ПРОИГРАТЬ', width=15, command=bt_on)
bt_connect.place(x = 175, y = 1020)

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
