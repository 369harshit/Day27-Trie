class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


def insert_word(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True


def longest_string_with_all_prefixes(root):
    result = [""]
    current_string = ""
    _longest_string_with_all_prefixes(root, current_string, result)
    return result[0]


def _longest_string_with_all_prefixes(node, current_string, result):
    # Check if the current node is the end of a word
    if node.is_end_of_word:
        # Update the result if the current string is longer
        if len(current_string) > len(result[0]):
            result[0] = current_string

    # Recursively explore all children
    for char, child_node in node.children.items():
        _longest_string_with_all_prefixes(child_node, current_string + char, result)


# Example usage:
words = ["n", "ni", "nin", "ninj", "ninja", "ninga"]
trie_root = TrieNode()

# Insert words into the trie
for word in words:
    insert_word(trie_root, word)

# Find the longest string with all prefixes
longest_string = longest_string_with_all_prefixes(trie_root)
print("Longest string with all prefixes:", longest_string)
