import datetime
import time
class TimeTemp:
    def time_temp(self):
        """
        当前时间
        :return:
        """
        temp = datetime.datetime.now().strftime("%Y-%m-%d _%H_%M_%S")
        return temp

    def mail_time(self):
        """
        获取当前周几\几点
        :return:
        """
        mail_time = {}
        weekday = time.strftime("%a")
        hour = time.strftime("%H")
        mail_time["weekday"] = weekday
        mail_time['hour'] = hour
        return mail_time

if __name__ == '__main__':
    TimeTemp().time_temp()
    print(TimeTemp().mail_time())