## Autocomplete with Tries

\* PS: technically all operations in a dectionary can take O(n) in worst case because of collisions but in practice it's almost imposible, so that's why we'll use O(1) (the avg. case)

- ### TrieNode:

  our TrieNode needs to state wether it's a word end, and have a dictionary of children TrieNodes.

  ### Efficiency

  - insert: time complexity O(1), space complexity O(1)
  - suffixes: time complexity O(M\*N) where M is the number of children per Node, while N is the depth of the Trie tree
    space complexity: O(M\*N) with M being the length of a word (number of letters), and N the Number of words in the tree.

- ### Trie:

  a Trie has a root TrieNode, with insert and find functions

  ### Efficiency

  - insert: time complexity O(n), space complexity O(n)
  - find: time complexity O(n) where n is the length of the prefix.
    space complexity: O(1)
