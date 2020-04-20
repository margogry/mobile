




































info = []

class dataCDR (object):
    def __init__(self, date = 0, time = 0, numFrom = 0, numTo = 0, duration = 0, sms = 0):
        self.time = time
        self.date = date
        self.numTo = numTo
        self.numFrom = numFrom
        self.duration = duration
        self.sms = sms


def inputData():
    F = open("data", "r")
    f = F.read().replace("\n", " ").split(" ")
    #print(f)

    for i in range ((int)(len(f)/6) - 1):
        info.append(dataCDR())
        info[i].data = f[i*6]
        info[i].time = f[i*6 + 1]
        info[i].numFrom = f[i*6 + 2]
        info[i].numTo = f[i*6 + 3]
        info[i].duration = f[i*6 + 4]
        info[i].sms = f[i*6 + 5]


def moreZero (a):
    if a < 0:
        return 0
    return a

def tarific():
    who = input('ведите номер абонента - ')
    outRing = input('Сколько для него стоят исходящие звонки? - ')
    inRing = input('Сколько стоят входящие звонки? - ')
    freeSMS = input('Сколько бесплатных СМС? - ')
    costSMS = input('Сколько стоят последующие СМС? - ')
    res = 0
    for i in range (len(info)):
        if info[i].numTo == who:
            res += (float)(info[i].duration) * (float)(inRing)
            #print(res, ' info[i].duration = ', info[i].duration, ' inRing = ', inRing)
        if info[i].numFrom == who:
            res += (float)(info[i].duration) * (float)(outRing)
            #print(res, ' info[i].duration = ', info[i].duration, ' outRing = ', outRing)
            res += (moreZero((int)(info[i].sms) - (int)(freeSMS))) * (int)(costSMS)
            #print(res, ' info[i].sms = ', info[i].sms, ' costSMS = ', costSMS)
    return res

inputData()
print('Тарификация услуг - ', tarific())

