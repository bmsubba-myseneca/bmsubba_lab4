#!/usr/bin/env python3

# Function to join two lists (union of two lists)
def join_lists(list1, list2):
    return list(set(list1) | set(list2))

# Function to match two lists (intersection of two lists)
def match_lists(list1, list2):
    return list(set(list1) & set(list2))

# Function to find the symmetric difference of two lists
def diff_lists(list1, list2):
    return list(set(list1) ^ set(list2))

if __name__ == "__main__":
    # Example test runs
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 1, 0, -1, -2]

    print("Join lists:", join_lists(list1, list2))  # Union of lists
    print("Match lists:", match_lists(list1, list2))  # Intersection of lists
    print("Diff lists:", diff_lists(list1, list2))  # Symmetric difference of lists
