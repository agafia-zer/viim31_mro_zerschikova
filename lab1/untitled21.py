# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 13:11:22 2023

@author: agafi
"""
import numpy as np
import matplotlib.pyplot as plt
from math import pi

class Circle:
    """Создает кргуи на основе предоставленных данных"""
    def __init__(self, x, y, r):
        self.x_batch = []
        self.y_batch = []
        self.x = x
        self.y = y
        self.r = r
        self.batch_size = 10
        self.gen_class()

    def gen_class(self): #Метод gen_class внутри класса Circle использует случайные параметры, 
                    #чтобы сгенерировать точки внутри круга
        for i in range(self.batch_size):
            theta = 2 * pi * np.random.uniform(0, 1)
            r = self.r * np.sqrt(np.random.uniform(0, 1))
            self.x_batch.append(self.x + r * np.cos(theta))
            self.y_batch.append(self.y + r * np.sin(theta))

    def get_batch_data(self):
        return self.x_batch, self.y_batch

    def get_circle_data(self):
        return self.x, self.y, self.r


classes = []
colors = ['orange', 'yellow', 'cyan', 'purple', 'red', 'blue']

try: #загрузка данных о кругах из файла class_data.txt. 
    with open('data/class_data.txt','r') as data:
        counter = 0
        for line in data:
            values=line.split(' ')
            values[len(values)-1]=values[len(values)-1].replace('\n',' ')
            x, y, r = [float(values[i]) for i in range(len(values))]
            classes.append(Circle(x,y,r))
            counter+=1

except FileNotFoundError: #Если этот файл не найден, программа запрашивает данные у пользователя вручную:
    print('File c_d not found! Manual data input...\n')
    counter = int(input('Class quantity = '))
    for i in range(counter):
        print('Class '.join(str(counter+1)).join('\n'))
        x = float(input('x = '))
        y = float(input('y = '))
        r = float(input('r = '))
        classes.append(Circle(x,y,r))


#программа записывает информацию о каждом круге и сгенерированных для них точках в файл data_datch.txt
# затем отображает их на графике:
result = open('data/data_datch.txt', 'w')
t = np.linspace(0, 2*pi, 100)
for i in range(counter):
    x_dat, y_dat = classes[i].get_batch_data()
    x,y,r = classes[i].get_circle_data()
    result.write("Class %s\n" % (i+1,))
    result.write("Class Info: %s, %s, %s\n" % (x,y,r))
    for j in range(len(x_dat)):
        result.write("%s, %s; " % (x_dat[j],y_dat[j]))
    result.write('\n')
    plt.scatter(x_dat, y_dat, c=colors[i])
    plt.plot(x+r*np.cos(t), y+r*np.sin(t), color=colors[i])

result.close()

plt.grid(color='lightgray', linestyle='--')
plt.show()