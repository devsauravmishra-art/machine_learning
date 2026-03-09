def fibonacci(n):
    """Return the nth Fibonacci number using an iterative approach."""
    if n <= 0:
        raise ValueError("n must be a positive integer")
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python fibonacci.py <n>")
        sys.exit(1)
    n = int(sys.argv[1])
    print(f"Fibonacci({n}) = {fibonacci(n)}")