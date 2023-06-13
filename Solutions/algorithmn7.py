def sum_digits(n):
    # Base case: if n is a single digit, return n
    if n < 10:
        return n
    # Recursive case: add the last digit to the sum of the remaining digits
    else:
        last_digit = n % 10
        remaining_digits = n // 10
        return last_digit + sum_digits(remaining_digits)
      
print(sum_digits(123))  # Output: 6 (1 + 2 + 3)
print(sum_digits(9875))  # Output: 29 (9 + 8 + 7 + 5)
print(sum_digits(4))  # Output: 4
