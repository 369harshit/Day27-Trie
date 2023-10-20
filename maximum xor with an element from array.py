def max_xor(nums, queries):
    result = []
    for xi, mi in queries:
        max_xor = -1
        for num in nums:
            if num <= mi:
                max_xor = max(max_xor, num ^ xi)
        result.append(max_xor)
    return result

nums = [0, 1, 2, 3, 4]
queries = [[3, 1], [1, 3], [5, 6]]
output = max_xor(nums, queries)
print(output)
