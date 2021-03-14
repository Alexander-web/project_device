# -*- coding: utf-8 -*-

import math
import sys
import time
import csv
from grove.adc import ADC

row=[]
value_list = []
point={}
sensor_is_on = True

class GroveGSRSensor:
 
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def GSR(self):
        value = self.adc.read(self.channel)
        return value
        #return {'value': value, 'value_list': value_list}
 
Grove = GroveGSRSensor
  
def main():
    if len(sys.argv) < 2:
        print('Используется: {} adc_channel'.format(sys.argv[0]))
        sys.exit(1)
 
    sensor = GroveGSRSensor(int(sys.argv[1]))
    
    print('Считывание...')
    while sensor_is_on:
        point=sensor.GSR
        value_list.append(point)
        l=value_list
        Human_Resistance = ((1024+2*point)*10000)/512
        print('Величина GSR: {0} Ом'.format(Human_Resistance))
        time.sleep(.1)
    return l
        
def data_writer(measure):
    csv_gsr = open('/home/pi/grove.py/grove/Project/data/GSR.csv', 'w')
    with csv_gsr:
        writer = csv.writer(csv_gsr)
        row.append(['Величина GSR: {0} Ом'.format(measure)])
        writer.writerows(row)
        
if __name__ == '__main__':
    main()
