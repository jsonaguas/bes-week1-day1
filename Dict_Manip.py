def merge_dicts(dict_1, dict_2):
    merged_dict = dict_1.copy()  # O(n) time complexity
    merged_dict.update(dict_2)   # O(m) time complexity
    return merged_dict
#Total time complexity: O(n + m)

dict_1 = {
    'pie': 'apple',
    'ice_cream': 'moose tracks',
    'cobbler': 'peach',
    'cake': None
}

dict_2 = {
    'dinner': 'turkey',
    'ice_cream': 'vanilla',
    'appetizer': 'soup',
    'cobbler': 'peach'
}

merged = merge_dicts(dict_1, dict_2)
print(merged)
# Output: {'pie': 'apple', 'ice_cream': 'vanilla', 'cobbler': 'peach', 'cake': None, 
# 'dinner': 'turkey', 'appetizer': 'soup'}

#Task 2
def intersect_dicts(dict_1, dict_2):
    intersection = {}
    for key in dict_1:
        if key in dict_2 and dict_1[key] == dict_2[key]:
            intersection[key] = dict_1[key]
    return intersection

# Example dictionaries
dict_1 = {
    'pie': 'apple',
    'ice_cream': 'moose tracks',
    'cobbler': 'peach',
    'cake': None
}

dict_2 = {
    'dinner': 'turkey',
    'ice_cream': 'vanilla',
    'appetizer': 'soup',
    'cobbler': 'peach'
}

# Find intersection
intersection = intersect_dicts(dict_1, dict_2)
print(intersection)
# Output: {'cobbler': 'peach'}