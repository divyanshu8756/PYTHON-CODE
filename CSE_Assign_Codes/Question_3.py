import sys
import time
import tracemalloc


def mean_of_digits(n):
    n_str = str(abs(n))
    digit_sum = 0
    for digit in n_str:
        digit_sum += int(digit)
    return digit_sum / len(n_str)


if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number: "))

        tracemalloc.start()
        start_time = time.perf_counter_ns()

        result = mean_of_digits(user_input)

        end_time = time.perf_counter_ns()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"Mean of digits: {result}")
        print(f"Memory utilisation: {peak} bytes")
        print(f"Execution time: {end_time - start_time} nanoseconds")

    except ValueError:
        print("Invalid input. Please enter an integer.")
