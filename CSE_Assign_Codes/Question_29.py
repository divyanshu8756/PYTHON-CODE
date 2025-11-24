import time
import tracemalloc


def polygonal_number(s, n):
    return ((s - 2) * (n ** 2) - (s - 4) * n) // 2


if __name__ == "__main__":
    try:
        s_in = int(input("Enter 's' (number of sides): "))
        n_in = int(input("Enter 'n' (position): "))

        tracemalloc.start()
        start_time = time.time_ns()

        result = polygonal_number(s_in, n_in)

        end_time = time.time_ns()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"Result: {result}")
        print(f"Memory utilisation: {peak} bytes")
        print(f"Execution time: {end_time - start_time} nanoseconds")

    except ValueError:
        print("Invalid input")
