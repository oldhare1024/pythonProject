def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Define pi string
pi = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

# Convert pi string to list of integers
pi_list = [int(x) for x in pi]

# Sort pi list using quicksort
sorted_pi = quicksort(pi_list)

# Print sorted pi list
print(sorted_pi)