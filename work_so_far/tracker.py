# importing libraries
import psutil as psutil
import win32gui
import win32process
import datetime as dt
import json
from helper import helper as h
from data_visualization import utilities as util
import time

# windows gui which takes the information from the screen
w = win32gui

# definig last and current activities

last_activity = None
last_subactivity = None
last_hour = None

start_time = dt.datetime.now()

while(True):
    
    curr_window = w.GetWindowText(w.GetForegroundWindow())
    [curr_activity, curr_subactivity] = h.string_format(curr_window)
    curr_hour = h.date_to_str(dt.datetime.now(), 'time')[:2]

    # if the current window is different from the last window update 
    if(last_activity!='Task Switching' and curr_subactivity!=last_subactivity and last_activity!=None): 

        end_time = dt.datetime.now()
        h.save_to_json('activity.json', last_activity, last_subactivity, start_time, end_time)
        h.save_to_json_time('activity_time.json', last_activity, last_subactivity, start_time, end_time)
        start_time = dt.datetime.now()

    if(curr_hour!=last_hour and last_hour!=None):
        date = h.date_to_str(dt.datetime.now(), None)
        util.data_by_hour(date, last_hour)

    last_activity = curr_activity
    last_subactivity = curr_subactivity
    last_hour = curr_hour
    

