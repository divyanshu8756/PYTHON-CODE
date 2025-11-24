import time
import sys


def g(a, b):
    if a == 0:
        return b, 0, 1
    d, x1, y1 = g(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y


def i(a, m):
    d, x, y = g(a, m)
    if d != 1:
        raise ValueError(
            "The modular inverse does not exist (moduli might not be coprime).")
    return x % m


def c(r, m):
    M = 1
    for mi in m:
        M = M * mi

    x = 0
    for ri, mi in zip(r, m):
        Mi = M // mi
        yi = i(Mi, mi)
        x = x + ri * Mi * yi

    return x % M


def main():
    try:
        r_str = input("Enter remainders: ")
        m_str = input("Enter moduli: ")

        r = [int(n) for n in r_str.split()]
        m = [int(n) for n in m_str.split()]

        if len(r) != len(m) or not r:
            print(
                "Error: The number of remainders and moduli must be equal and non-zero.")
            return

        start = time.perf_counter_ns()

        solution = c(r, m)

        end = time.perf_counter_ns()

        mem = sys.getsizeof(solution)
        t = end - start

        print("\nSolution (x):", solution)
        print("Memory Utilisation (bytes):", mem)
        print("Execution Time (nanoseconds):", t)

    except ValueError as e:
        print("Error:", e)
        print("Please ensure your inputs are valid integers and your moduli are pairwise coprime.")
    except Exception as e:
        print("An unexpected error occurred:", e)


main()
