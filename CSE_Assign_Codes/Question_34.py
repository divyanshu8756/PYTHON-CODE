
import sys
import time
import tracemalloc


def partition_function(n):
    partitions = [0] * (n + 1)
    partitions[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]
    return partitions[n]


def main():
    try:
        user_input = input("Enter a number: ")
        n = int(user_input)

        tracemalloc.start()
        start_time = time.time_ns()

        result = partition_function(n)

        end_time = time.time_ns()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"Result: {result}")
        print(f"Memory Utilisation: {peak} bytes")
        print(f"Execution Time: {end_time - start_time} nanoseconds")

    except ValueError:
        print("Please enter a valid integer")


if __name__ == "__main__":
    main()
