# data-structures
This will hold sample code for a number of classic data structures implemented in Python.

## linked_list
- push(val) will insert the value ‘val’ at the head of the list
- pop() will pop the first value off the head of the list and return it. Raises an exception with an appropriate message if there are no values to return.
- size() will return the length of the list
- search(val) will return the node containing ‘val’ in the list, if present, else None
- remove(node) will remove the given node from the list, wherever it might be (node must be an item in the list). If the node is not in the list, it should raise an exception with an appropriate message.
- display() will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”

- len(the_list) returns the size of the list
- print(the_list) returns what the display() method returns


## Stack
- push(value) - Adds a value to the stack. The parameter is the value to be added to the stack.
- pop() - Removes a value from the stack and returns that value. If the stack is empty, attempts to call pop should raise an appropriate Python exception with message.

## Doubly-Linked List

- push(val) will insert the value val at the head of the list
- append(val) will append the value val at the tail of the list
- pop() will pop the first value off the head of the list and return it. Raises an exception with an appropriate message if there are no values to return.
- shift() will remove the last value from the tail of the list and return it. Raises an exception with an appropriate message if there are no values to return.
- remove(val) will remove the first instance of val found in the list, starting from the head. If val is not present, it will raise an appropriate Python exception.

## Binary heap

- push(val): puts a new value into the heap, maintaining the heap property.
- pop(): removes the “top” value in the heap, maintaining the heap property.


## Graph

- g.nodes(): return a list of all nodes in the graph
- g.edges(): return a list of all edges in the graph
- g.add_node(val): adds a new node with value ‘n’ to the graph
- g.add_edge(val1, val2): adds a new edge to the graph connecting the node containing ‘val1’ and the node containing ‘val2’. If either val1 or val2 are not already present in the graph, they should be added. If an edge already exists, overwrite it.
- g.del_node(val): deletes the node containing ‘val’ from the graph; raises an error if no such node exists
- g.del_edge(val1, val2): deletes the edge connecting ‘val1’ and ‘val2’ from the graph; raises an error if no such edge exists
- g.has_node(val): True if node containing ‘val’ is contained in the graph, False if not.
- g.neighbors(val): returns the list of all nodes connected to the node containing ‘val’ by edges; raises an error if val is not in g
- g.adjacent(val1, val2): returns True if there is an edge connecting val1 and val2, False if not; raises an error if either of the supplied values are not in g
