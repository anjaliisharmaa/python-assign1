text = input("Enter soem text: ")
with open('output.txt', 'w') as file:
    file.write(text)