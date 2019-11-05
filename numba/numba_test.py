from numba import jit
import random

@jit(nopython=True)
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

def monte_carlo_pi_slow(nsamples):
    acc = 0
    for i in range(nsamples):
         x = random.random()
         y = random.random()
         if (x ** 2 + y ** 2) < 1.0:
             acc += 1
    return 4.0 * acc / nsamples

@jit(nopython=True, parallel=True)
def simulator(out):
    # iterate loop in parallel
    for i in prange(out.shape[0]):
        out[i] = run_sim()

import time
import sys
start_time = time.time()
monte_carlo_pi(int(sys.argv[1]))
stop_time = time.time()
elapsed_time = stop_time - start_time
print("Running %d loops with Numba: %f s" % (int(sys.argv[1]), elapsed_time))


start_time = time.time()
monte_carlo_pi_slow(int(sys.argv[1]))
stop_time = time.time()
elapsed_time = stop_time - start_time
print("Running %d loops without Numba: %f s" % (int(sys.argv[1]), elapsed_time))
