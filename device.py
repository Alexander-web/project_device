# -*- coding: utf-8 -*-

import sys
from sys import argv
import grove_gsr_sensor
from battery_check import *
value_list = []

def make_measure_GSR():
    sys.argv=[sys.argv[0],'0'] #Передача параметра в список аргументов командной строки, передаваемых сценарию Python. Пока не понятно зачем это сделано!
    measure = grove_gsr_sensor.main() #Вызов функции модуля, проводящей измерения.
    print(measure)
    
    
if __name__ == '__main__':
    try:
        #make_measure_GSR()
        ina219()
    except KeyboardInterrupt:
        print('Прервано!')
        #data_writer(measure)
