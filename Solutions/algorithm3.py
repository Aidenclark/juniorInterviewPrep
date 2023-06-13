def find_second_smallest(numbers):
    if len(numbers) < 2:
        return None

    smallest = float('inf')
    second_smallest = float('inf')

    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest

# Example usage
numbers = [5, 2, 8, 3, 9, 2, 1, 6]
result = find_second_smallest(numbers)
print("Second smallest number:", result)
