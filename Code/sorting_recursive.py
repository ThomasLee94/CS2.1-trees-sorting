#!python

from sorting_iterative import bubble_sort


def merge(items_1: [int], items_2: [int]) -> [int]:
    """
      Merge given lists of items, each assumed to already be in sorted order,
      and return a new list containing all items in sorted order. The 2 given
      given lists need not be the same length.

      Args:
          2 sorted lists of ints.
      Output:
          A merged list of sorted ints.
    """
    # Running time: O(n*m)
    # Memory usage: O(n+m)

    merged_items = list()

    # indicies for both lists
    i_1 = 0
    i_2 = 0

    while i_1 < len(items_1) and i_2 < len(items_2):
        # case: element at index i_1 in items_1 is less than element at index
        # i_2 in items_2
        if items_1[i_1] < items_2[i_2]:
            merged_items.append(items_1[i_1])
            # increment index
            i_1 += 1
        # vice versa
        else:
            merged_items.append(items_2[i_2])
            # increment index
            i_2 += 1

    # when we have reached the end of one of the lists (unequal lengths)
    if i_1 != len(items_1):
        # append remaining elemnts from index i_1 in items_1
        merged_items += items_1[i_1:]
    else:
        merged_items += items_2[i_2:]
    return merged_items


def split_sort_merge(items: [int]) -> [int]:
    """
        Sort given items by splitting list into two approximately equal halves,
        sorting each with an iterative sorting algorithm, and merging results
        into a list in sorted order.

        Args:
            list of ints
        Output:
            A list in ascending sorted order.

    """
    # Running time: ??? Why and under what conditions?
    # Memory usage: ??? Why and under what conditions?

    # split list into rough halves
    middle_index = len(items) // 2
    first_half = items[middle_index:]
    second_half = items[:middle_index]

    # sort both halves - sort alogrithm is replacable.
    first_half.bubble_sort()
    second_half.bubble_sort()

    # merge both halves
    merged_items = merge(first_half, second_half)
    return merged_items


def merge_sort(items: [int]) -> [int]:
    """
        Sort given items by splitting list into two approximately equal
        halves, sorting each recursively, and merging results into a list
        in sorted order.

        Args:
            An unsorted list of ints.

        Output:
            A sorted list of ints.
    """
    # Running time: ??? Why and under what conditions?
    # Memory usage: ??? Why and under what conditions?

    # base case: list is so small it's already sorted
    if len(items) <= 1:
        return items

    # split items list into approximately equal halves
    else:
        middle = len(items) // 2
        first_half = items[:middle]
        second_half = items[middle:]
        # Sort each half by recursively calling merge sort
        sorted_first_half = merge_sort(first_half)
        sorted_second_half = merge_sort(second_half)
        # Merge sorted halves into one list in sorted order
        return merge(sorted_first_half, sorted_second_half)


def partition(items: [int], low: int, high: int):
    """
        Return index `p` after in-place partitioning given items in range
        `[low...high]` by choosing a pivot (low) from that range, moving
        pivot into index `p`, items less than pivot into range
        `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.

        Args:
            items: list of ints.
            low: pivot.
            high: length of list.
        Output:
            list of ints sorted in relation to the pivot; any value is that is
            smaller than the pivot is placed on the left side in no sorted
            order. Vice versa for values higher than the pivot.

    """

    # TODO: Running time: ??? Why and under what conditions?
    # TODO: Memory usage: ??? Why and under what conditions?

    # "low" pivot value
    pivot_val = items[low]
    # index after pivot value
    first_index = low + 1
    # Loop through all items in range of first_index - high
    for i in range(first_index, high):
        # Move items less than pivot into front of range [low...p-1]
        if items[i] < pivot_val:
            # swap values
            items[first_index], items[i] = items[i], items[first_index]
            first_index += 1
    # Move pivot item into final position and return its position
    items[first_index - 1], items[low] = items[low], items[first_index - 1]
    # return the index of pivot
    return first_index - 1


def quick_sort(items: [int], low=None, high=None):
    """
        Sort given items in place by partitioning items in range `[low...high]`
        around a pivot item and recursively sorting each remaining sublist range.

        Arts:
            items: list of ints.
            low: pivot.
            high: length of list.

        Output:
            sorted list of ints in ascending order.

    """
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
