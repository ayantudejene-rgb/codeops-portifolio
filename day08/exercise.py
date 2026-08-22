#Exercise 1: 
def total(nums):
    """Recursively sum a list of numbers."""
    if not nums:          
        return 0
    return nums[0] + total(nums[1:])

def count_down(n):
    """Recursively print from n down to 1."""
    if n < 1:
        return
    print(n)
    count_down(n - 1)

print("Sum of [1,2,3,4]:", total([1,2,3,4]))
print("Countdown from 3:")
count_down(3)

# Exercise 2: 
def binary_search(items, target):
    """Return index of target in sorted list, or -1 if not found."""
    lo, hi = 0, len(items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

balances = [100, 250, 400, 800, 1200, 1500]
print("Index of 400:", binary_search(balances, 400))
print("Index of 999:", binary_search(balances, 999))

#  Exercise 3:
def merge(left, right):
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)

import random
test = [random.randint(1, 100) for _ in range(10)]
print("Original:", test)
print("Merge sort:", merge_sort(test))
print("Python sorted:", sorted(test))
assert merge_sort(test) == sorted(test)

#  Exercise 4: 
people = [("Almaz", 1500), ("Dawit", 700), ("Hanna", 2000), ("Tigist", 1200)]
sorted_by_balance = sorted(people, key=lambda x: x[1], reverse=True)
print("Sorted by balance descending:", sorted_by_balance)

#Exercise 5:
def has_pair(nums, target):
    """Check if any two numbers in sorted list sum to target."""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        s = nums[lo] + nums[hi]
        if s == target:
            return True
        elif s < target:
            lo += 1
        else:
            hi -= 1
    return False
nums = [10, 20, 30, 40, 50]
print("Has pair sum 70?", has_pair(nums, 70))  
print("Has pair sum 100?", has_pair(nums, 100)) 