import math

def main(probs: list[int]) -> float:
    return sum(-i * math.log2(i) for i in probs)

if __name__ == "__main__":

    probs = [0.5, 0.3, 0.2]
    result = main(probs)
    print(result)  #  Result: 1.4854752972273344
