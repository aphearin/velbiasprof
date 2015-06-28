#!/usr/bin/env python

"""
Initial script used to turn csv data of 
queried halos and particles into hdf5 files.  
"""

from astropy.io.ascii import read
from astropy.table import Table
from read_csv import read_csv
import numpy as np

#halos_fname='DATA/mdr1_fof.csv'
#halos = read(halos_fname)
#halos.write('DATA/mdr1_fof.hdf5', path='data')



particles_0_0_0_fname='DATA/mdr1_fofp_0_0_0.csv'
particles_dtype = np.dtype([('rowid', 'i8'), 
	('x', 'f8'), ('y', 'f8'), ('z','f8'),
	('vx', 'f8'), ('vy', 'f8'), ('vz','f8'), ('haloid', 'i8')]
	)

p000 = read_csv(particles_0_0_0_fname, particles_dtype)
t = Table(p000)
print("Done reading data. Now saving hdf5 file. ")
t.write('DATA/mdr1_fofp_0_0_0.hdf5', path='data')







