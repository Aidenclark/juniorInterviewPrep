def sum_even_numbers(numbers):
    """
    Function to find the sum of all even numbers in a given list.

    Args:
    numbers (list): List of integers.

    Returns:
    int: Sum of all even numbers in the list.
    """
    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
    return sum_even

# Example usage
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_numbers(numbers_list)
print("Sum of even numbers:", result)
