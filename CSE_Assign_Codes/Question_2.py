import time
import tracemalloc


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    user_input = input("Enter a number: ")

    tracemalloc.start()
    start_time = time.time_ns()

    result = is_palindrome(user_input)

    end_time = time.time_ns()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Is Palindrome: {result}")
    print(f"Memory Utilisation: {peak} bytes")
    print(f"Execution Time: {end_time - start_time} nanoseconds")
