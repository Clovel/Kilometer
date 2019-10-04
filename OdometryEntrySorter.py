from datetime import datetime


def sort_odometry_entries(p_entries):
    n = len(p_entries)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already
        # in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if p_entries[j].date > p_entries[j + 1].date:
                p_entries[j], p_entries[j + 1] = p_entries[j + 1], p_entries[j]
                swapped = True

        # IF no two elements were swapped
        # by inner loop, then break
        if not swapped:
            break
