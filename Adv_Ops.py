#Task 1
def squares_list(n):
    return [i ** 2 for i in range(1, n + 1)]

# Example usage:
print(squares_list(5))  # Output: [1, 4, 9, 16, 25]
#The time complexity is (O(n)) because the function iterates through the range 
# of n and squares each element in the range.

#Task 2
def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

# Example usage:
list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(merge_sorted_lists(list1, list2))  # Output: [1, 2, 3, 4, 5, 6]
#The time complexity is (O(nlogn)) because the function merges the two lists
# and then sorts the merged list.