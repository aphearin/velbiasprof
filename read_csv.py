#!/usr/bin/env python

import numpy as np 

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


def read_csv(f, dt):

    nlines_tot = file_len(f)
    iout = int(np.round(nlines_tot/100.))

    chunk = []
    for linenum, line in enumerate(open(f)):
        if line[0] == '"':
            pass
        else:
            parsed_line = line.split(',')
            chunk.append(tuple(parsed_line)) 
            if linenum == 10:
                print linenum, len(parsed_line) 

        if linenum % iout == 0:
            percent_done = 100*linenum/float(nlines_tot)
            print("...  %.1f percent done" % percent_done)

    arr = np.array(chunk, dtype = dt)

    return arr
