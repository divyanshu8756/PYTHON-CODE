import time
import tracemalloc


def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


try:
    n = int(input("Enter a non-negative integer n: ").strip())
    if n < 0:
        print("Error: n must be non-negative")
        raise SystemExit
except:
    print("Invalid input")
    raise SystemExit
tracemalloc.start()
t0 = time.perf_counter_ns()
res = factorial(n)
t1 = time.perf_counter_ns()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(res)
print("Execution time (ns):", t1 - t0)
print("Memory peak (bytes):", peak)
