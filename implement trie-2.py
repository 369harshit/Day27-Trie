class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word_count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.word_count += 1
        node.is_end_of_word = True

    def erase(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                # Word not found
                return
            node = node.children[char]
            node.word_count -= 1
        if node.is_end_of_word:
            node.is_end_of_word = False

    def count_words_equal_to(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.word_count if node.is_end_of_word else 0

    def count_words_starting_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.word_count


# Example usage:
trie = Trie()

# Insert operations
trie.insert("samsung")
trie.insert("samsung")
trie.insert("vivo")

# Erase operation
trie.erase("vivo")

# Count operations
result1 = trie.count_words_equal_to("samsung")
result2 = trie.count_words_starting_with("vi")

# Output results
print(result1)  # Output: 2
print(result2)  # Output: 0

