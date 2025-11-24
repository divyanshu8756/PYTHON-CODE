import time
import tracemalloc


def zeta_approx(s, terms):
    result = 0.0
    for n in range(1, terms + 1):
        result += 1 / (n ** s)
    return result


try:
    s_input = float(input("Enter value for s: "))
    terms_input = int(input("Enter number of terms: "))
    tracemalloc.start()
    start_time = time.time_ns()
    approximation = zeta_approx(s_input, terms_input)
    end_time = time.time_ns()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Approximation: {approximation}")
    print(f"Memory Utilisation: {peak} bytes")
    print(f"Execution Time: {end_time - start_time} nanoseconds")
except ValueError:
    print("Invalid input. Please enter a number for s and an integer for terms.")
