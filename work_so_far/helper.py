# importing libraries
import datetime as dt
import json
import uiautomation as ui
from data_visualization import utilities as utils
# helper class which does all the stuff
class helper:
    
    browsers = {'Brave', 'Google Chrome', 'Microsoft Edge'}
    
    # converts the datetime to date and time
    def date_to_str(datetime,d):
        if(d=='time'):
            return datetime.strftime('%H:%M:%S')
        return datetime.strftime('%d:%m:%y')
    
    # returns the application type (Browser or otherwise)
    def application_type(name):
        ans = ''
        j = 0
        for i in range(len(name)-1,-1,-1):
            if(name[i]=='-'):
                j = i
                break
            ans += name[i]

        return ans[::-1].lstrip(), j
    
    # to get hour
    def get_hour(start_time, end_time):
        start_hour = int(start_time[:2])
        end_hour = int(end_time[:2])

        if(start_hour == end_hour):
            time_duration = utils.time_duration(start_time, end_time)
            return [[str(start_hour), time_duration]]
        else:
            ans = []
            for i in range(start_hour, end_hour):
                if(i==start_hour):
                    start = start_time
                    end = str()+":00:00"
                elif(i==end_hour):
                    start_time = "{:02d}".format(i)+":00:00"
                    end_time = end_time
                else:
                    start_time = "{:02d}".format(i)+":00:00"
                    end_time = "{:02d}".format(i+1)+":00:00"

                time_duration = utils.time_duration(start_time, end_time)
                ans.append([str(i), time_duration])
            
            return ans

    # to get the url from the active browser window
    def get_url(browser):
        control = ui.GetFocusedControl()
        controlList = []
        while(control):
            controlList.insert(0, control)
            control = control.GetParentControl()
        if(len(controlList) == 1):
            control = controlList[0]
        else:
            control = controlList[1]
        try:
            url = ui.FindControl(control, lambda c, d: isinstance(c, ui.EditControl) and "Address and search bar" in c.Name)
        except Exception as exception:
            print(type(exception).__name__)
            url = None

        if(url==None):
            return 'None'
        #print(browser, "url: ", url.GetValuePattern().Value)
        return url.GetValuePattern().Value
    
    # convert the input from gui into necessary data
    def string_format(name):
        activity, j = helper.application_type(name)
        sub_activity = ''
        if(activity in helper.browsers):
            temp = helper.get_url(activity)
            for i in range(len(temp)):
                if(temp[i]=='.'):
                    break
                sub_activity += temp[i]
            return [activity, sub_activity]
        else:
            for i in range(j-2,-1,-1):
                if(name[i]=='-'):
                    break
                sub_activity += name[i]
            return [activity, sub_activity[::-1].lstrip()]

    # saving the data in to a json file
    def save_to_json(file_name, activity, sub_activity, start, end):
        
        if(activity!=""):
    
            time_line = {
                    'date':helper.date_to_str(start, None),
                    'start':helper.date_to_str(start,'time'),
                    'end':helper.date_to_str(end,'time')
                    }

            file = open(file_name, 'r+')
            file_data = json.load(file)
            
            if(activity in file_data):
                if(sub_activity in file_data[activity]):
                    file_data[activity][sub_activity].append(time_line)
                else:
                    file_data[activity][sub_activity] = [time_line]
            else:
                file_data[activity] = {sub_activity : [time_line]}
    
            file.seek(0)
            json.dump(file_data, file, indent=5)
    
    # saving the date hour wise
    def save_to_json_time(file_name, activity, sub_activity, start, end):

        if(activity!=""):
            
            file = open(file_name,'r+')
            file_data = json.load(file)
            
            start_time = helper.date_to_str(start, 'time')
            end_time = helper.date_to_str(end, 'time')
            date = helper.date_to_str(start, None)

            activity_duration = helper.get_hour(start_time, end_time)
            if(activity_duration!=[]):
                for i in range(len(activity_duration)):
                    ad = activity_duration[i]
                    
                    if(ad[1]==[0,0,0]):
                        continue
                    if(date in file_data):
                        if(ad[0] in file_data[date]):
                            if(activity in file_data[date][ad[0]]):
                                if(sub_activity in file_data[date][ad[0]][activity]):
                                    file_data[date][ad[0]][activity][sub_activity].append(ad[1])
                                else:
                                    file_data[date][ad[0]][activity][sub_activity] = [ad[1]]
                            else:
                                file_data[date][ad[0]][activity] = {sub_activity:[ad[1]]}
                        else:
                            file_data[date][ad[0]] = {activity:{sub_activity:[ad[1]]}}
                    else:
                        file_data[date] = {ad[0]: {activity:{sub_activity:[ad[1]]}}}
            
            file.seek(0)
            json.dump(file_data, file, indent=5)
    
    
    
         

