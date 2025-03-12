def main(digit: int = 3):
    assert digit >= 1, f"Digit must greater or equal then 1, not {digit}"
    memo = []
    starts = 1 if digit == 1 else 10**(digit-1)
    ends = 10**digit
    
    for i in range(starts, ends):
        for j in range(starts, ends):
            result = i * j
            str_result = str(result)
            if str_result == str_result[::-1]:
                memo.append(result)
    
    return max(memo)
    
if __name__ == "__main__":
    result = main(3)
    print(f"Result: {result}")  #  Result: 906609
