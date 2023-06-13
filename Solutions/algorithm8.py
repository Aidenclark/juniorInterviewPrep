from sympy import symbols, Eq, solve

# Define the variables
x, y = symbols('x y')

# Define the equations
equation1 = Eq(2*x + 3*y, 12)
equation2 = Eq(4*x - y, 5)

# Solve the system of equations
solution = solve((equation1, equation2), (x, y))

# Extract the values of x and y from the solution
x_value = solution[x]
y_value = solution[y]

# Print the values of x and y
print("x =", x_value)
print("y =", y_value)
