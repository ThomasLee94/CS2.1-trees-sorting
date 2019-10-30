#!python


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
        # increment both indicies
    # when we have reached the end of one of the lists (unequal lengths)
    if i_1 != len(items_1):
        merged_items += items_1[i_1:]
    else:
        merged_items += items_2[i_2:]
    return merged_items


def test_merge():
    a = [1, 3, 5]
    b = [2, 4, 6]
    ans = merge(a, b)
    print(ans)
    if ans == [1, 2, 3, 4, 5, 6]:
        print(True)
    else:
        print('False')


test_merge()


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
