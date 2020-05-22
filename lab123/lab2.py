import csv
import matplotlib.pyplot as plt
import datetime
import itertools
import numpy as np

FILENAME = "nfcapd.csv"


def tarific2():
    who = '217.15.20.194' #input('Ведите IP абонента - ')
    cost = 0.5 #(float)(input('Какой у него тариф? - '))

    rawData = []
    x = []
    y = []
    res = 0

    with open(FILENAME, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[3] == who or row[4] == who:
                res += (int)(row[12])
                currentRow = []

                currentRow.append(row[0][11:15] + '0')
                currentRow.append((int)(row[12]))

                rawData.append(currentRow)

        res *= cost
        rawData = np.array(rawData)
        rawData = sorted(rawData, key=lambda x: x[0])

        j = 0
        x.append(rawData[0][0])
        y.append((int)(rawData[0][1]))

        for i in range(1, len(rawData)):
            currentTime = rawData[i][0]
            if currentTime == x[j]:
                y[j] += (int)(rawData[i][1])
            else:
                x.append(currentTime)
                y.append((int)(rawData[i][1]))

                j += 1
        plt.plot(x, y)
    return res

#print('Тарификация услуг - ', tarific2())
#plt.show()
