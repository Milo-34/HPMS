from .models import *
# utils.py
def quicksort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if key(x) < key(pivot)]
        right = [x for x in arr[1:] if key(x) >= key(pivot)]
        return quicksort(left, key) + [pivot] + quicksort(right, key)
    

def binary_search(sorted_list, target, field_name):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_item = sorted_list[mid]
        mid_value = getattr(mid_item, field_name) if hasattr(mid_item, field_name) else mid_item.get(field_name)
        mid_value = str(mid_value).lower()

        if mid_value == target.lower():
            return mid_item
        elif mid_value < target.lower():
            left = mid + 1
        else:
            right = mid - 1
    return None

