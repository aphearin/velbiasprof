#!/usr/bin/env python

"""
Initial script used to turn queried halos and a single sub-volume of particles
into hdf5 files.  
"""

from astropy.io.ascii import read
from astropy.table import Table

#halos_fname='DATA/mdr1_fof.csv'
#halos = read(halos_fname)
#halos.write('DATA/mdr1_fof.hdf5', path='data')

particles_0_0_0_fname='DATA/mdr1_fofp_0_0_0.csv'
p000 = read(particles_0_0_0_fname)
p000.write('DATA/mdr1_fofp_0_0_0.hdf5', path='data')







