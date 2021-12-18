import serial
import time
import matplotlib.pyplot as plt
import csv
import pandas as pd

arduino = serial.Serial(port = 'COM4', baudrate = 9600, timeout = 0.1)

y = []
x = []
time.sleep(1.5)

for i in range(100):
    data = arduino.readline()
    #print(data)
    # y.append(data)
    print(int(data[0:len(data)-2]))

    y.append(int(data[0:len(data)-2]))
    x.append(i)

    time.sleep(0.1)

plt.plot(x,y, marker = 'o')
plt.show()

dictionary = {'time': x, 'voltage': y}
file = pd.DataFrame(dictionary)
file.to_csv('ecgvalues.csv', index = False)


