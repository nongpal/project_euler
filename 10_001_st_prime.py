def main(limits: int = 10001):
    result = [2]
    attempt = 3
    while len(result) < limits:
        if all(attempt % prime != 0 for prime in result):
            result.append(attempt)
        attempt += 2
    return result[-1]

if __name__ == "__main__":
    result = main()
    print(f"Result: {result}")  #  Result: 104743
