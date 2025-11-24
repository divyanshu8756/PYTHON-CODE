import time
import tracemalloc


def is_harshad(n):
    digit_sum = 0
    temp = n
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    return n % digit_sum == 0


def main():
    try:
        user_input = int(input("Enter a number: "))

        tracemalloc.start()
        start_time = time.perf_counter_ns()

        result = is_harshad(user_input)

        end_time = time.perf_counter_ns()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        if result:
            print(f"{user_input} is a Harshad number")
        else:
            print(f"{user_input} is not a Harshad number")

        print(f"Execution time: {end_time - start_time} nanoseconds")
        print(f"Memory utilisation: {peak} bytes")

    except ValueError:
        print("Invalid input")


if __name__ == "__main__":
    main()
