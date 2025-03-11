def main(limit=1000):
    count = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            count += i
    return count

if __name__ == "__main__":
    result = main()
    print(f"Result: {result}")  #  Result: 233168
