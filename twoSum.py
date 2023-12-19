def two_sum(nums, target):
    memo = {}
    for v, i in enumerate(nums):
        memo[v] = i

    for v, i in enumerate(nums):
        needed_number = target - v
        if needed_number in memo and memo[needed_number] != i:
            return True
        
    return False

print(two_sum([1,7,3],14))