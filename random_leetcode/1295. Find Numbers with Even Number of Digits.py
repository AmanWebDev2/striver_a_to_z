import math
def findNumbers(nums: list[int]) -> int:
    count = 0
    for num in nums:
        digits = math.floor(math.log10(num)+1)
        if digits % 2 == 0:
            count += 1
    return count

def findNumbers2(nums: list[int]) -> int:
    count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1
    return count
