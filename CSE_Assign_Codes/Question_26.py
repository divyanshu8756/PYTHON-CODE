import time
import tracemalloc


def lucas_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [2]
    if n == 2:
        return [2, 1]

    sequence = [2, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def main():
    try:
        n_input = int(input("Enter the number of terms: "))

        tracemalloc.start()
        start_time = time.time_ns()

        result = lucas_sequence(n_input)

        end_time = time.time_ns()
        _, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"Generated Sequence: {result}")
        print(f"Memory Utilisation: {peak_memory} bytes")
        print(f"Execution Time: {end_time - start_time} nanoseconds")

    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
