import time
import tracemalloc


def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


n = int(input("Enter a number: "))

tracemalloc.start()
start_time = time.time_ns()

result = count_divisors(n)

end_time = time.time_ns()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Number of divisors: {result}")
print(f"Memory utilisation: {peak} bytes")
print(f"Execution time: {end_time - start_time} nanoseconds")
