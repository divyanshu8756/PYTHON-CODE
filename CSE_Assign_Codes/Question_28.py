import time
import tracemalloc


def collatz_length(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


if __name__ == "__main__":
    try:
        user_input = int(input("Enter a positive integer: "))

        tracemalloc.start()
        start_time = time.perf_counter_ns()

        result = collatz_length(user_input)

        end_time = time.perf_counter_ns()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"Collatz Sequence Length: {result}")
        print(f"Execution Time: {end_time - start_time} nanoseconds")
        print(f"Memory Utilisation: {peak} bytes")

    except ValueError:
        print("Please enter a valid integer.")
