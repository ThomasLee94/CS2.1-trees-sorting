#!python3

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of complete words inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self) -> bool:
        """Return True if this prefix tree is empty (contains no strings)."""

        if self.size == 0:
            return True
        return False

    def contains(self, word: str) -> bool:
        """Return True if this prefix tree contains the given string."""

        node, _ = self._find_node(word)

        if node is not None and node.terminal:
            return True

        return False

    def insert(self, word: str):
        """Insert the given string into this prefix tree."""

        node, _ = self._find_node(word)

        # case: node already exists & is a terminal
        if node and node.terminal:
            return

        node = self.root

        for letter in word:
            # case: if the letter does not exist as a child from current node
            if letter not in node.children:
                # add child node to current node
                new_child_node = PrefixTreeNode(letter)
                node.add_child(letter, new_child_node)
            # traverse down
            node = node.children[letter]
        # set node terminal to True at the end of word iteration
        node.terminal = True

        self.size += 1

    def _find_node(self, word: str) -> (object, int):
        """Return a tuple containing the node that terminates the given string
        in this prefix tree and the node's depth, or if the given string is not
        completely found, return None and the depth of the last matching node.
        Search is done iteratively with a loop starting from the root node."""

        depth = 0
        node = self.root

        # Match the empty string
        if len(word) == 0:
            return node, depth

        for char in word:
            if char in node.children:
                node = node.children[char]
                depth += 1
            else:
                node = None
                break
        return node, depth

    def complete(self, word_or_prefix: str) -> [str]:
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""

        # Create a list of completions in prefix tree
        completions = []

        # init node & depth
        node, _ = self._find_node(word_or_prefix)

        # case: prefix does not exist
        if node is None:
            return completions

        # case: word_or_string is already a completed word
        if node.is_terminal():
            completions.append(word_or_prefix)

        # traverse through prefix tree & append all terminal words
        for child in node.children.values():
            self._traverse(child, word_or_prefix +
                           child.character, completions.append)

        return completions

    def strings(self) -> [str]:
        """Return a list of all strings stored in this prefix tree."""

        all_strings = list()

        for child in self.root.children.values():
            if child is not None:
                self._traverse(child, child.character, all_strings.append)
        return all_strings

    def _traverse(self, node: object, prefix: str, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node and visit each node with the given function."""

        # execute visit if it is terminal
        if node.is_terminal():
            # visit(prefix + node.character)
            visit(prefix)

        for child_node in node.children.values():
            # concat chars
            self._traverse(child_node, prefix + child_node.character, visit)


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


if __name__ == '__main__':
    # Create a dictionary of tongue-twisters with similar words to test with
    tongue_twisters = {
        'Seashells': 'Shelly sells seashells by the sea shore'.split(),
        # 'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
        # 'Woodchuck': ('How much wood would a wood chuck chuck'
        #                ' if a wood chuck could chuck wood').split()
    }
    # Create a prefix tree with the similar words in each tongue-twister
    for name, strings in tongue_twisters.items():
        print('\n' + '='*80 + '\n')
        print(f'{name} tongue-twister:')
        create_prefix_tree(strings)
