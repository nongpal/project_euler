def func1(nums: int = 1):
    return sum([i**2 for i in range(1, nums+1)])

def func2(nums: int = 1):
    return sum([i for i in range(1, nums+1)])**2
    
if __name__ == "__main__":
    nums = 100
    result = func2(nums) - func1(nums)
    print(f"Result: {result}")
