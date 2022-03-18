import json
import seaborn as sns
import matplotlib.pyplot as plt

# category class
class category:

    def __init__(self, name):
        self.name = name
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.time = 0

    # adds time
    def add_time(self, time_duration):
        s = self.seconds  + time_duration[2]
        m = self.minutes + time_duration[1] + s//60
        h = self.hours + time_duration[0] + m//60

        self.hours = h
        self.minutes = m%60
        self.seconds = s%60
        self.time = self.hours*3600 + self.minutes*60 + self.seconds

# sub_category

class sub_category(category):

    def __init__(self, name, sub_name):
        self.name = name
        self.sub_name = sub_name
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.time = 0


class utilities:

    # converts string to time
    def convert_time(time):
        t = list(map(int,time.split(":")))
        return t
    
    # finds time the application is used
    def time_duration(start_time, end_time):
        
        start_time = utilities.convert_time(start_time)
        end_time = utilities.convert_time(end_time)

        s = start_time[0]*60*60 + start_time[1]*60 + start_time[2]
        e = end_time[0]*60*60 + end_time[1]*60 + end_time[2]

        time_diff = e-s

        s = time_diff % 60
        m = int(time_diff/60) % 60
        h = int(time_diff/3600)

        return [h,m,s]

    def get_names_and_time(categories_list):
        for i in categories_list:
            name = i.name
            h, m, s = i.hours, i.minutes, i.seconds
            print(name, h, m, s)

    def get_names_and_time_sub(categories_list):
        for i in categories_list:
            name = i.name
            sub_name = i.sub_name
            h, m, s = i.hours, i.minutes, i.seconds
            print(name, sub_name, h, m, s)

    # add time for hour data
    def add_hms(time, new_time):
        s = (new_time[2] + time[2])
        m = (new_time[1] + time[1] + s//60)
        h = (new_time[0] + time[0 + m//60])

        return [h, m%60, s%60]

    # get top categories
    def get_top_categories(categories_list, number):
        arr = sorted(categories_list, key = lambda x:x.time, reverse=True)

        utilities.get_names_and_time(arr[:number])
    
    def get_top_sub_categories(sub_categories_list, number):
        arr = sorted(sub_categories_list, key = lambda x:x.time, reverse=True)

        utilities.get_names_and_time_sub(arr[:number])

    def usage_hour(date, hour):
        data = json.load(open('activity_time.json',))
        if(date not in data):
            print('No data on '+date)
        else:
            hours = data[date].keys()
            if(hour not in data[date]):
                print('No data on this hour')
            else:
                categories_list = []
                sub_categories_list = []
                categories = data[date][hour].keys()
                
                for c in categories:
                    categories_list.append(category(c))
                    

                for i in range(len(categories_list)):
                    name = categories_list[i].name
                    sub_categories = data[date][hour][name].keys()
                    for sub in sub_categories:
                        sub_categories_list.append(sub_category(name, sub))
                        [h,m,s] = [0,0,0]
                        for j in range(len(data[date][hour][name][sub])):
                            [h,m,s] = utilities.add_hms([h,m,s], data[date][hour][name][sub][j])
                        
                        sub_categories_list[-1].add_time([h,m,s])
                        categories_list[i].add_time([h,m,s])
        
                return categories_list, sub_categories_list


    def data_by_hour(date, hour):
        print('ja')
        c, sub_categories = utilities.usage_hour(date, hour)

        file = open('activity_each_hour.json','r+')
        file_data = json.load(file)
                
        for sc in sub_categories:
            if(sc.name in file_data):
                if(sc.sub_name in file_data[sc.name]):
                    file_data[sc.name][sc.sub_name][int(hour)-1] = sc.time
                else:
                    file_data[sc.name][sc.sub_name] = [0]*24
                    file_data[sc.name][sc.sub_name][int(hour)-1] = sc.time
            else:
                file_data[sc.name] = {sc.sub_name : [0]*24}
                file_data[sc.name][sc.sub_name][int(hour)-1] = sc.time

        file.seek(0)
        json.dump(file_data, file, indent=5)


if __name__=="__main__":

    categories_list = []
    sub_categories_list = []

    data = json.load(open('activity.json',))

    categories = data.keys()

    print(categories)

    # each category
    for c in categories:
        categories_list.append(category(c))
    

    for i in range(len(categories_list)):
        name = categories_list[i].name
        l = len(sub_categories_list)        
        for sub_name in data[name].keys():
            sub_categories_list.append(sub_category(name, sub_name))

            for j in range(len(data[name][sub_name])):

                start_time = data[name][sub_name][j]['start']
                end_time = data[name][sub_name][j]['end']

                time_duration = utilities.time_duration(start_time, end_time)

                sub_categories_list[-1].add_time(time_duration)
                categories_list[i].add_time(time_duration)
        
    
    #utilities.get_top_categories(categories_list, 3)
    
    # each sub category
    #utilities.get_top_sub_categories(sub_categories_list, 10)
    

    # categories in a hour
    c,sc = utilities.usage_hour("04:02:22", "11")
    utilities.get_top_categories(c, 3)

    utilities.data_by_hour("04:02:22", "12")
    # different categories all together like social media, streaming stuff, code, email, study


