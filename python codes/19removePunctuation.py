import string

input_str = input("Enter a string with punctuation: ")
output_str = input_str.translate(str.maketrans('', '', string.punctuation))
print(output_str)
