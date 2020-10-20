import time
import datetime

t = time.time() #获取当前时间戳

#要打印的时间戳列表，毫秒级时间戳格式：时间戳/100
timestamp_list = [
    t,
    1602756899636/1000,
    1602756899652/1000,
    1602756899667/1000
]
data_time_list = [
    '2020-10-16 18:39:10.652213',
    '2020-10-15 18:14:59.636000'
]

timestr = '2019-01-14 15:22:18.123'
datetime_obj = datetime.datetime.strptime(timestr,"%Y-%m-%d %H:%M:%S.%f")
obj_stamp = int(time.mktime(datetime_obj.timetuple()) * 1000.0 + datetime_obj.microsecond / 1000.0)
print(obj_stamp)

def print_frame_time(timestamp_list):
    print('格式化输出年月日时分秒毫秒：')
    cnt = 1
    for timestamp in timestamp_list:
        frame_time = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S.%f")
        print("【%d】%s    "%(cnt,timestamp),frame_time)
        cnt += 1

def print_timestamp(data_time_list):
    print('输出某时刻的时间戳(毫秒/微秒)：')
    cnt = 1
    for date_time in data_time_list:
        date_time_obj = datetime.datetime.strptime(date_time,"%Y-%m-%d %H:%M:%S.%f")
        timestamp = int(time.mktime(date_time_obj.timetuple()) * 1000000.0 + int(date_time.split(".")[1]))
        print("【%d】%s    " %(cnt,date_time), timestamp)
        cnt += 1

if __name__ == "__main__":
    print_frame_time(timestamp_list)
    print_timestamp(data_time_list)

