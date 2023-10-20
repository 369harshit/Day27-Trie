def generate_subsequences(input_str, current="", index=0, subsequences=[]):
    if index == len(input_str):
        # Add the current subsequence to the list
        if current:
            subsequences.append(current)
        return

    # Include the current character in the subsequence
    generate_subsequences(input_str, current + input_str[index], index + 1, subsequences)

    # Exclude the current character from the subsequence
    generate_subsequences(input_str, current, index + 1, subsequences)

# Example usage
input_str = "abc"
subsequences = []
generate_subsequences(input_str, subsequences=subsequences)

# Sort and print the result lexicographically
subsequences.sort()
for subsequence in subsequences:
    print(subsequence, end=" ")
