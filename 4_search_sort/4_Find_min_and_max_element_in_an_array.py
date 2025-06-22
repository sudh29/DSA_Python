def getMinMax(a: list, n: int) -> tuple:
    min_val = float('inf')  # Initialize to infinity
    max_val = float('-inf') # Initialize to negative infinity

    for i in range(n):
        if a[i] > max_val:
            max_val = a[i]
        if a[i] < min_val:
            min_val = a[i]

    return (min_val, max_val)

# Example usage:
# arr = [1, 2, 3, 4, 5]
# print(getMinMax(arr, len(arr)))  # Output: (1, 5)
