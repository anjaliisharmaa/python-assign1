def sum_of_numbers(numbers):
    return sum(numbers)

# Ask the user to input a list of numbers, separated by spaces
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of numbers
numbers_list = [float(number) for number in user_input.split()]

# Calculate the sum of the numbers
total_sum = sum_of_numbers(numbers_list)

# Print the result
print("The sum of the numbers is:", total_sum)