#!python3


class PrefixTreeNode:
    """PrefixTreeNode: A node for use in a prefix tree that stores a single
    character from a string and a structure of children nodes below it, which
    associates the next character in a string to the next node along its path from
    the tree's root node to a terminal node that marks the end of the string."""

    # Choose a type of data structure to store children nodes in
    # Hint: Choosing list or dict affects implementation of all child methods
    CHILDREN_TYPE = None

    def __init__(self, character=None):
        """Initialize this prefix tree node with the given character value, an
        empty structure of children nodes, and a boolean terminal property."""
        # Character that this node represents
        self.character = character
        # Data structure to associate character keys to children node values
        self.children = dict()
        # Marks if this node terminates a string in the prefix tree
        self.terminal = False

    def is_terminal(self) -> bool:
        """Return True if this prefix tree node terminates a string."""

        if len(self.children) == 0:
            return True
        return False

    def num_children(self) -> int:
        """Return the number of children nodes this prefix tree node has."""

        counter = 0

        if self.is_terminal():
            for key in self.children.keys():
                counter += 1

        return counter

    def has_child(self, character: str) -> bool:
        """Return True if this prefix tree node has a child node that
        represents the given character amongst its children."""

        for key, _ in self.children:
            if key == character:
                return True
        return False

    def get_child(self, character):
        """Return this prefix tree node's child node that represents the given
        character if it is amongst its children, or raise ValueError if not."""
        if self.has_child(character):
            # TODO: Find child node for given character in this node's children
        else:
            raise ValueError(f'No child exists for character {character!r}')

    def add_child(self, character, child_node):
        """Add the given character and child node as a child of this node, or
        raise ValueError if given character is amongst this node's children."""
        if not self.has_child(character):
            # TODO: Add given character and child node to this node's children
        else:
            raise ValueError(f'Child exists for character {character!r}')

    def __repr__(self):
        """Return a code representation of this prefix tree node."""
        return f'PrefixTreeNode({self.character!r})'

    def __str__(self):
        """Return a string view of this prefix tree node."""
        return f'({self.character})'
