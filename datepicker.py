try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import datetime
import io
import serial
import subprocess
import platform
import threading
import psutil
import socket
import struct
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from tkinter import *
import spinningGIF
import pygatt
from pygatt.backends import BLEAddressType
from serial.tools import list_ports
from utilities import write_log_file,log_except
from PIL import Image, ImageTk
from fpdf import FPDF
import os
import csv
import requests
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import style
from pathlib import Path
from tkcalendar import Calendar

import logging
from subprocess import Popen
import json
import sqlite3
import report_generator
# from datetime import datetime

from ctypes import *
import time
from math import floor
import glob
entry5=""
entry4=""

root = parent = Tk()
root.title("Change font demo")
start=StringVar()
end=StringVar()
entry4 = Entry(root, textvariable=start, bd=3, width=51)
# entry4['validatecommand'] = (entry4.register(testVal), '%P', '%d')

entry4.place(x=360, y=200)
# entry4.insert(0,"DD-MM-YYYY")
entry4.focus()
# entry4.delete(0, END)
# print(entry4.get())


entry5 = Entry(root, textvariable=end, bd=3, width=51)
# entry5['validatecommand'] = (entry5.register(testVal), '%P', '%d')
# entry5.insert(0,"DD-MM-YYYY"
entry5.place(x=900, y=200)
entry5.focus()

# # entry5.delete(0, END)
#
# string_date = entry4.get()
# if string_date is not None:
#
# end_date=entry5.get()
# if end_date is not None:
#     datetime(end=end_date)
# a=None


def datetime_to_float(d):
    print(d.timestamp())
    return d.timestamp()

# print("starttime"+entry4.get())
# print("endtime"+entry5.get())
def dater(event):
    print("starttime" + entry4.get())
    print("endtime" + entry5.get())
    if entry4.get() !="" :
        val1=str(entry4.get())
        a=datetime.datetime.strptime(val1, "%d-%m-%Y")
        print(a)
        datetime_to_float(a)
    if entry5.get() !="":
        val2 =str(entry5.get())
        b = datetime.datetime.strptime(val2, "%d-%m-%Y")
        print(b)
        datetime_to_float(b)

def db_query():
    with open('Const/config.json') as i:
        json_const = json.load(i)

    device = json_const['DEVICE_FLAG']
    conn = sqlite3.connect(json_const['DB_NAME'])
    c = conn.cursor()
    D2="D2"
    data=[]
    # if device == "S":
    #     # c.execute("SELECT starttime,patientid FROM Exercisesession WHERE ID= 'D1'")
    c.execute("SELECT * FROM 'ExerciseSession' where StartTime>="+"'"+str(1557217912.1208632)+"'"+" and StartTime<="+"'"+str(1561465826.7702644)+"'"+" and patientid="+"'"+str(D2)+"'"+" and reps is not NULL")
    print(c.fetchall())
    for row in c.fetchall():
        # print(row)
        data.append(row)
        return row
    print(data)
db_query()
# if start.get() != "":
entry4.bind("<FocusOut>",dater)


entry5.bind("<FocusOut>",dater )
root.mainloop()