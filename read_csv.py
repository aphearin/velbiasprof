#!/usr/bin/env python

"""
Initial script used to turn csv data of 
queried halos and particles into hdf5 files.  
"""

import numpy as np 
import os, sys
import h5py
from time import time

def main(fname):

    basename = os.path.basename(fname)[0:-4]
    abspath = os.path.dirname(os.path.abspath(fname))
    output_fname = os.path.join(abspath, basename+'.hdf5')

    if 'mdr1_fofp_' in basename:
        print("\n...Reading particle data...\n")
        dt = np.dtype([('rowid', 'i8'), 
    ('x', 'f8'), ('y', 'f8'), ('z','f8'),
    ('vx', 'f8'), ('vy', 'f8'), ('vz','f8'), ('haloid', 'i8')]
    )
    else:
        print("\n...Reading halo data...\n")
        dt = np.dtype([('rowid', 'i8'), ('haloid', 'i8'), 
    ('x', 'f8'), ('y', 'f8'), ('z','f8'),
    ('vx', 'f8'), ('vy', 'f8'), ('vz','f8'), ('mass', 'f4'), ('size', 'f4')])

    start = time()
    data = read_csv(fname, dt)
    end = time()
    runtime = end-start
    print("Total time to read csv = %.1f seconds\n" % runtime)

    with h5py.File(output_fname,'w') as f:
        f['data'] = data

def file_len(fname):
    """ Compute the number of all rows in the raw halo catalog. 

    Parameters 
    ----------
    fname : string 

    Returns 
    -------
    Nrows : int
 
    """
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    Nrows = i + 1
    return Nrows


def read_csv(fname, dt):
    """ Function reads csv data stored in fname and returns the 
    data in the format of a numpy structured array of dtype dt. 

    Parameters 
    ----------
    fname : string

    dt : dtype object

    Returns 
    --------
    arr : array
    """

    nlines_tot = file_len(fname)
    print("Total number of lines in %s =  %i\n" % (fname, nlines_tot))
    iout = int(np.round(nlines_tot/10.))

    container = []
    for linenum, line in enumerate(open(fname)):
        if line[0] == '"':
            pass
        else:
            parsed_line = line.split(',')
            container.append(tuple(parsed_line)) 

        if linenum % iout == 0:
            percent_done = 100*linenum/float(nlines_tot)
            print("...%.0f%% done" % percent_done)

    print("\n...Converting data to structured numpy array...\n")
    arr = np.array(container, dtype = dt)

    return arr

###################################################################################################
# Trigger
###################################################################################################

if __name__ == "__main__":

    fname = sys.argv[1]
    main(fname)




