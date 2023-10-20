def find_max_xor(nums):
    max_xor = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            max_xor = max(max_xor, nums[i] ^ nums[j])

    return max_xor

# Example usage
nums = [3, 10, 5, 25, 2, 8]
result = find_max_xor(nums)
print(result)
