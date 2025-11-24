import sys
import time


def mod_inverse(a, m):
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0
    a = a % m
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if a != 1:
        return None
    if x < 0:
        x = x + m0
    return x


a_input = int(input("Enter integer a: "))
m_input = int(input("Enter modulus m: "))

start_time_ns = time.perf_counter_ns()
result = mod_inverse(a_input, m_input)
end_time_ns = time.perf_counter_ns()

execution_time_ns = end_time_ns - start_time_ns

if result is None:
    print("Inverse does not exist (gcd(a, m) != 1)")
else:
    memory_bytes = sys.getsizeof(result)
    print(f"Modular Multiplicative Inverse (x): {result}")
    print(f"Memory Utilization (bytes): {memory_bytes}")
    print(f"Execution Time (nanoseconds): {execution_time_ns}")
