## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.word_end = False
        
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
            
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        res = []
        for key in self.children:
            if self.children[key].word_end:
                res.append(suffix+key)
            res += self.children[key].suffixes(suffix+key)
        return res
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for c in word:
            current_node.insert(c)
            current_node = current_node.children[c]
        current_node.word_end = True
                

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        for c in prefix:
            if c in current_node.children:
                current_node = current_node.children[c]
            else:
                return None
        return current_node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)



prefixNode = MyTrie.find("")
print(prefixNode.suffixes())
#expected output: ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']
print('----------------------')

prefixNode = MyTrie.find("an")
print(prefixNode.suffixes())
#expected output: ['t', 'thology', 'tagonist', 'tonym']
print('----------------------')


prefixNode = MyTrie.find("ant")
print(prefixNode.suffixes())
#expected output: ['hology', 'agonist', 'onym']
print('----------------------')


prefixNode = MyTrie.find("f")
print(prefixNode.suffixes())
#expected output: ['un', 'unction', 'actory']
print('----------------------')

prefixNode = MyTrie.find("tripod")
print(prefixNode.suffixes())
#expected output: []
