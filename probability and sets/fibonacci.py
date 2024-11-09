import sys

def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series

def main():
    if len(sys.argv) != 2:
        print("Usage: python fibonacci.py <number_of_terms>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n <= 0:
            raise ValueError("Number of terms must be positive")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    fib_series = fibonacci(n)
    print(f"Fibonacci series with {n} terms:")
    print(", ".join(map(str, fib_series)))

if __name__ == "__main__":
    main()