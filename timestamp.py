import time
import datetime

t = time.time() #获取当前时间戳

#要打印的时间戳列表，毫秒级时间戳格式：时间戳/100
timestamp_list = [t,
                  1602756899636/1000,
                  1602756899652/1000,
                  1602756899667/1000
                  ]

print('格式化输出年月日时分秒毫秒：')
cnt = 1
for timestamp in timestamp_list:
    #frame_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
    frame_time = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S.%f")
    print("【%d】"%cnt,frame_time)
    cnt += 1



