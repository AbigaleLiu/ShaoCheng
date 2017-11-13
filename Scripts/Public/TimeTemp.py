import datetime
class TimeTemp:
    def time_temp(self):
        """
        当前时间
        :return:
        """
        temp = datetime.datetime.now().strftime("%Y-%m-%d _%H_%M_%S")
        return temp

if __name__ == '__main__':
    TimeTemp().time_temp()