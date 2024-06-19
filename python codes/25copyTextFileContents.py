import os

source_filename = 'output.txt'
destination_filename = 'destination.txt'

if os.path.exists(source_filename):
    with open(source_filename, 'r') as source_file:
        with open(destination_filename, 'w') as destination_file:
            destination_file.write(source_file.read())
    print(f"Contents from '{source_filename}' copied to '{destination_filename}'.")
else:
    print(f"'{source_filename}' does not exist. Please create the file or provide a valid source file.")
