cimport cython
import numpy as np
cimport numpy as np
from libc.math cimport sqrt


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
def pairwise_radial_velocity_no_pbc(np.ndarray[np.float64_t, ndim=1] x1,
                  np.ndarray[np.float64_t, ndim=1] y1,
                  np.ndarray[np.float64_t, ndim=1] z1,
                  np.ndarray[np.float64_t, ndim=1] vx1,
                  np.ndarray[np.float64_t, ndim=1] vy1,
                  np.ndarray[np.float64_t, ndim=1] vz1,
                  np.ndarray[np.float64_t, ndim=1] x2,
                  np.ndarray[np.float64_t, ndim=1] y2,
                  np.ndarray[np.float64_t, ndim=1] z2,
                  np.ndarray[np.float64_t, ndim=1] vx2,
                  np.ndarray[np.float64_t, ndim=1] vy2,
                  np.ndarray[np.float64_t, ndim=1] vz2):
    """
    """
    #c definitions
    cdef int Npts = len(x1)
    cdef np.ndarray[np.float64_t, ndim=1] radial_velocities = np.zeros((Npts,), dtype=np.float64)

    for i in range(Npts):
        radial_velocities[i] = radial_velocity_no_pbc(x1[i], y1[i], z1[i], \
            x2[i], y2[i], z2[i], \
            vx1[i], vy1[i], vz1[i], \
            vx2[i], vy2[i], vz2[i])

    return radial_velocities




cdef inline double radial_velocity_no_pbc(np.float64_t x1, np.float64_t y1, np.float64_t z1, \
    np.float64_t x2, np.float64_t y2, np.float64_t z2, \
    np.float64_t vx1, np.float64_t vy1, np.float64_t vz1, \
    np.float64_t vx2, np.float64_t vy2, np.float64_t vz2):
    """
    """
    cdef double dx, dy, dz, dvx, dvy, dvz

    dx = x2-x1
    dy = y2-y1
    dz = z2-z1
    dvx = vx2-vx1
    dvy = vy2-vy1
    dvz = vz2-vz1

    return ( dvx*dx + dvy*dy + dvz*dz ) / sqrt( dx*dx + dy*dy + dz*dz )

cdef inline double signed_periodic_square_distance_1d(np.float64_t x1,\
                                            np.float64_t x2,\
                                            np.float64_t Lbox):
    """
    Calculate the 3D square cartesian distance between two sets of points with periodic
    boundary conditions.
    """
    
    cdef double dx, dy, dz
    
    dx = x2-x1
    dx = fmin(dx, period[0] - dx)

    return 


def sgn(x, y):
    return (x < y) - (y < x)




