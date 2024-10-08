#!/usr/bin/env python3

# Function to join two sets (union of two sets)
def join_sets(set1, set2):
    return set1 | set2

# Function to match two sets (intersection of two sets)
def match_sets(set1, set2):
    return set1 & set2

# Function to find the symmetric difference of two sets
def diff_sets(set1, set2):
    return set1 ^ set2

if __name__ == "__main__":
    # Example test runs
    set1 = {1, 2, 3, 4, 5}
    set2 = {2, 1, 0, -1, -2}

    print("Join sets:", join_sets(set1, set2))  # Union of sets
    print("Match sets:", match_sets(set1, set2))  # Intersection of sets
    print("Diff sets:", diff_sets(set1, set2))  # Symmetric difference of sets
