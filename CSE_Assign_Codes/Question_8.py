import time
import tracemalloc


def is_automorphic(n):
    square = n * n
    str_num = str(n)
    str_square = str(square)
    if str_square.endswith(str_num):
        return True
    return False


if __name__ == "__main__":
    num = int(input("Enter a number: "))

    tracemalloc.start()
    start_time = time.time_ns()

    result = is_automorphic(num)

    end_time = time.time_ns()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    if result:
        print(f"{num} is an Automorphic Number")
    else:
        print(f"{num} is not an Automorphic Number")

    print(f"Memory Utilisation: {peak} bytes")
    print(f"Execution Time: {end_time - start_time} nanoseconds")
