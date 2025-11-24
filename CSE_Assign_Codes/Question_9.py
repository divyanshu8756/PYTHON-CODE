import math
import time
import tracemalloc
import sys


def is_pronic(n):
    k = math.isqrt(n)
    return k * (k + 1) == n


try:
    n = int(input("Enter your number: "))
except:
    print("Invalid input")
    sys.exit()

tracemalloc.start()
start = time.perf_counter_ns()
ans = is_pronic(n)
end = time.perf_counter_ns()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("is_pronic:", ans)
print("memory utilisation(in bytes):", peak)
print("execution time(in nanoseconds):", end - start)
