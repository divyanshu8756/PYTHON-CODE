import time
import sys


def is_quadratic_residue(a, p):
    if a % p == 0:
        return True

    result = pow(a, (p - 1) // 2, p)
    return result == 1


if __name__ == "__main__":

    print("Enter integer 'a': ")
    a = int(sys.stdin.readline())

    print("Enter prime 'p': ")
    p = int(sys.stdin.readline())

    start_time = time.perf_counter_ns()

    result_bool = is_quadratic_residue(a, p)

    end_time = time.perf_counter_ns()

    execution_time_ns = end_time - start_time

    if result_bool:
        output_message = f"The congruence x^2 = {a} mod {p} has a solution."
    else:
        output_message = f"The congruence x^2 = {a} mod {p} does not have a solution."

    memory_utilization_bytes = sys.getsizeof(output_message)

    print(output_message)
    print(f"Memory Utilization: {memory_utilization_bytes} bytes")
    print(f"Execution Time: {execution_time_ns} nanoseconds")
