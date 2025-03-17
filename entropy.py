import math

array = [0.5, 0.3, 0.2]
result = 0
for i in range(len(array)):
    result += -array[i] * math.log2(array[i])

print(result)  #  Result 1.4854752972273344
