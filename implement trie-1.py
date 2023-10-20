class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage:
type_values = [1, 1, 2, 3, 2]
word_values = ["hello", "help", "help", "hel", "hel"]

trie = Trie()

for i in range(len(type_values)):
    if type_values[i] == 1:  # Insert operation
        trie.insert(word_values[i])
    elif type_values[i] == 2:  # Search operation
        result = trie.search(word_values[i])
        print(result)
    elif type_values[i] == 3:  # Starts with operation
        result = trie.startsWith(word_values[i])
        print(result)
