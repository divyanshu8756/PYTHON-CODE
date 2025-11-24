import time
import tracemalloc


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def twin_primes(limit):
    pairs = []
    for i in range(2, limit):
        if i + 2 <= limit:
            if is_prime(i) and is_prime(i + 2):
                pairs.append((i, i + 2))
    return pairs


if __name__ == "__main__":
    limit = int(input("Enter a number: "))

    tracemalloc.start()
    start_time = time.time_ns()

    result = twin_primes(limit)

    end_time = time.time_ns()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Twin Primes: {result}")
    print(f"Memory utilisation: {peak} bytes")
    print(f"Execution time: {end_time - start_time} nanoseconds")
