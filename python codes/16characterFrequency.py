def count_character_frequency(string):
    frequency = {}

    for char in string:
        if char in frequency:
            frequency[char] += 1

        else:
            frequency[char] = 1
    return frequency

user_input = input("Enter a string: ")
frequency_count = count_character_frequency(user_input)

print("\nCharacter frequencies: ")
for char, count in frequency_count.items():
    print(f"'{char}': {count}")