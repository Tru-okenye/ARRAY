def find_missing_number(arr, n):
    # expected sum of numbers from 1 to n
    expected_sum = n * (n + 1) // 2
    # actual sum of the array
    actual_sum = sum(arr)
    # missing number is the difference
    return expected_sum - actual_sum

# Example Usage
n = 10  
arr = [1, 2, 3, 4, 5, 6, 8, 9, 10]  
missing_number = find_missing_number(arr, n)
print(f"The missing number is: {missing_number}")
