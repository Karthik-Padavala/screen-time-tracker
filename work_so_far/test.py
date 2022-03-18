# importing libraries
import psutil as psutil
import win32gui
import win32process
import datetime as dt
import json
from helper import helper as h
import time

# windows gui which takes the information from the screen
w = win32gui

# definig last and current activities

last_activity = None
last_subactivity = None
last_window = None
start_time = dt.datetime.now()

while(True):
    
    curr_window = w.GetWindowText(w.GetForegroundWindow())
    [curr_activity, curr_subactivity] = h.string_format(curr_window)
    
    # if the current window is different from the last window update 
    if(last_activity!='Task Switching' and curr_subactivity!=last_subactivity and last_activity!=None): 

        end_time = dt.datetime.now()
        print(last_activity, last_subactivity, last_window.split('-'))
        start_time = dt.datetime.now()

    last_activity = curr_activity
    last_subactivity = curr_subactivity
    last_window = curr_window
    

