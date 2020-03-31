# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None
        
    def insert(self, route):
        # Insert the node as before
        if route not in self.children:
            self.children[route] = RouteTrieNode()

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, route, handler, current_node = None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        if not current_node:
            current_node = self.root

        if len(route) == 0:
            current_node.handler = handler
        elif len(route) == 1:
            current_node.insert(route[0])
            current_node.children[route[0]].handler = handler
        else:
            current_node.insert(route[0])
            self.insert(route[1:], handler, current_node.children[route[0]])

    def find(self, route, current_node = None):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if not current_node:
            current_node = self.root
    
        if len(route) == 0:
            return current_node.handler
        else:
            if route[0] in current_node.children:
                return self.find(route[1:], current_node.children[route[0]])
            else:
                return None

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.route_trie.insert(self.split_path(path), handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        handler =  self.route_trie.find(self.split_path(path))
        return handler if handler else self.not_found_handler


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        split_p = path.split('/')[1:]
        if len(split_p) == 0:
            return [] 
        if split_p[-1] == "":
            return split_p[:-1]
        return split_p

# Test cases
# create the router and add a route
router = Router("root handler", "404: not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/cart", "cart handler")  # add a route

print('------------------------------------------')
# some lookups with the expected output
print(router.lookup("")) 
# should print 'root handler'

print(router.lookup("/")) 
# should print 'root handler'

print(router.lookup("/home")) 
# should print '404: not found handler'

print(router.lookup("/home/about")) 
# should print 'about handler'

print(router.lookup("/home/about/")) 
# should print 'about handler' 

print(router.lookup("/home/about/me")) 
# should print '404: not found handler'

print(router.lookup("/cart")) 
# should print 'cart handler'

print(router.lookup("/cart/")) 
# should print 'cart handler'

print(router.lookup("/cart/saved")) 
# should print '404: not found handler'

print(router.lookup("/home/cart")) 
# should print '404: not found handler'