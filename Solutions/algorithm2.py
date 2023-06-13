def count_unique_numbers(numbers):
    unique_numbers = set()
    duplicates = set()
    
    for num in numbers:
        if num not in duplicates:
            if num in unique_numbers:
                unique_numbers.remove(num)
                duplicates.add(num)
            else:
                unique_numbers.add(num)
    
    return len(unique_numbers)

# Example usage
numbers = [1, 2, 3, 4, 2, 3, 4, 5]
result = count_unique_numbers(numbers)
print(result)
