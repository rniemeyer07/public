#!/usr/local/anaconda/bin/python

#script to enter a lat/lon and program will return lat/lon of grid cell that point resides in
# run the code like this:  ./rbm_find_grid_cell.py 35.011301 -85.697354  
import numpy as np
import os
import sys


def find_125_grid_Maurer(lat, lon):
   '''Find the 1/8 grid cell that a (lat, lon) point falls in
       (the 1/8 grid cells are Maurer's grids)    Input arguments: lat, lon (can be single number or np array)
   Return: lat_grid, lon_grid
   Module requred: import numpy as np
   '''
   lat_grid = np.around(8.0*lat-0.5)/8.0 + 0.0625
   lon_grid = np.around(8.0*lon-0.5)/8.0 + 0.0625
   return lat_grid, lon_grid


lat_lon = find_125_grid_Maurer(float(sys.argv[1]),float(sys.argv[2]))

print(lat_lon)

