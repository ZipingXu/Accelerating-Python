import sys
import time
start_time = time.time()
map(lambda x: x+1, range(int(sys.argv[1])))
stop_time = time.time()
elapsed_time = stop_time - start_time
print("Running %d loops: %f s" % (int(sys.argv[1]), elapsed_time))
