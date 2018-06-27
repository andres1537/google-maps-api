# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 07:09:58 2018

@author: andres1537@gmail.com
"""

import places
import csv

num_lines = sum(1 for line in open('sources/MDE-IPI.csv'))
coord_num_line = int(num_lines / 100)

with open('sources/MDE-IPI.csv') as csvfile:
    reader  = csv.reader(csvfile, delimiter=';')
    file= open('salida.csv','w+')
    i = 1
    
    for coord in reader:
        if i == coord_num_line:
            formatted_address = places.reverse_geocode(coord)
            file.write(';'.join(coord) + ';' + formatted_address +'\n')
            i = 0
        i = i + 1
    file.close() 
print('Fin')