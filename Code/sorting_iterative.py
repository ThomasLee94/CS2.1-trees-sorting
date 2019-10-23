#!python


def is_sorted(items: [int]) -> bool:
    """ 
        Return a boolean indicating whether given items are in sorted order. 

        Args:
            list of ints.
        Output:
            If given list is in ascending order, return True.
            If not, return False.
    """

    # runtime = O(n)
    # space = O(1)
    
    # -1 to account for index out of range
    for i in range(len(items)-1):
        # if current element is > than next
        if items[i] > items[i+1]:
            return False

    return True


def bubble_sort(items: [int]) -> [int]:
    """
        Sort given items by swapping adjacent items that are out of order, and
        repeating until all items are in sorted order.

        Args:
            list of ints.
        Output:
            ascending order list of ints.
    """

    # runtime = O(n^2)
    # space = O(1)

    for i in range(len(items)):
        if items[i] > items[i+1]:
            current = items[i]
            next = items[i+1]
            items[i] = next
            items[i+1] = current
            continue
    return items

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
