class Trie:

    def __init__(self):
        self.isEnd = False
        self.neighbours = [None] * 26

    def insert(self, word: str) -> None:
        if not word:
            # self.neighbours[26] = Trie()
            self.isEnd = True
            return
        char = word[0]
        index = ord(char) - ord('a')
        next_node = self.neighbours[index]
        if next_node:
            return self.neighbours[index].insert(word[1:])
        else:
            self.neighbours[index] = Trie()
            return self.neighbours[index].insert(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            print(word, self.isEnd)
            return self.isEnd
        print(word, self.isEnd)
        char = word[0]
        index = ord(char) - ord("a")
        next_node = self.neighbours[index]
        if next_node:
            return self.neighbours[index].search(word[1:])
        return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        char = prefix[0]
        index = ord(char) - ord("a")
        next_node = self.neighbours[index]
        if next_node:
            return self.neighbours[index].startsWith(prefix[1:])
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)