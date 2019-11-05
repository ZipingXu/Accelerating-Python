import numpy as np
import numba
from numba import jit
import random

# Serial version
@jit(nopython=True)
def monte_carlo_pi_serial(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

# Parallel version
@jit(nopython=True, parallel=True)
def monte_carlo_pi_parallel(nsamples):
    acc = 0
    # Only change is here
    for i in numba.prange(nsamples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

import time
import sys
start_time = time.time()
monte_carlo_pi_serial(int(sys.argv[1]))
stop_time = time.time()
elapsed_time = stop_time - start_time
print("Running %d loops without parallelization: %f s" % (int(sys.argv[1]), elapsed_time))


start_time = time.time()
monte_carlo_pi_parallel(int(sys.argv[1]))
stop_time = time.time()
elapsed_time = stop_time - start_time
print("Running %d loops with parallelization: %f s" % (int(sys.argv[1]), elapsed_time))
