def find_maximum(array):
    if not array:
        return None

    max_value = array[0]

    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]

    return max_value

# Example usage
arr = [12, 5, 17, 9, 21, 6]
print(find_maximum(arr))  # Output: 21
