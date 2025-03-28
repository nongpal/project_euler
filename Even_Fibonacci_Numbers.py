def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def main(limit=34):
    count = 0
    for i in range(1, limit):
        result = fibonacci(i)
        if result % 2 == 0:
            count += result
    return count

if __name__ == "__main__":
    result = main()
    print(f"Result: {result}")  #  Result: 4613732
