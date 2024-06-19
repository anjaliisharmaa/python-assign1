def are_anagrams(string1, string2):
    # Remove any spaces and convert both strings to lowercase
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are equal
    return sorted(string1) == sorted(string2)

# Ask the user for two strings
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Check if they are anagrams
if are_anagrams(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")