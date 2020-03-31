## HTTPRouter using a Trie

\* PS: technically all operations in a dectionary can take O(n) in worst case because of collisions but in practice it's almost imposible, so that's why we'll use O(1) (the avg. case)

- ### RouteTrieNode:

  our RouteTrieNode has a children dictionary and a handler

  ### Efficiency

  - insert: time complexity O(1), space complexity O(n) where n is the length of the route.

- ### RouteTrie:

  a RouteTrie has a root RouteTrieNode, with insert and find functions

  ### Efficiency

  - insert: time complexity O(n), space complexity O(n)
  - find: time complexity O(N\*M) where N is the length of the part of the rout, M is the depth of the route.
    space complexity: O(1)

* ### Router:

  a Router has a root RouteTrie, with add_handler and lookup and split_path functions

  ### Efficiency

  - add_handler: time complexity O(n), space complexity O(n)
  - lookup: is efficiency of the RouteTrie find function.
  - split_path: time complexity O(n), space complexity O(n)
