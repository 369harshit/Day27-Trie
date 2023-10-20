class Node:
    def __init__(self):
        self.links = [None] * 26

    def contains_key(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node
        
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]


def count_distinct_substrings(s):
    root = Node()
    count = 0
    n = len(s)
    
    for i in range(n):
        node = root
        for j in range(i, n):
            if not node.contains_key(s[j]):
                node.put(s[j], Node())
                count += 1
            node = node.get(s[j])

    return count + 1

if __name__ == "__main__":
    s1 = "ababa"
    print("Total number of distinct substrings:", count_distinct_substrings(s1))

    s2 = "ccfdf"
    print("Total number of distinct substrings:", count_distinct_substrings(s2))
    
    