# TODO 1. Open a file and read it
# file = open("my_file.txt")
# contents = file.read()  # saves the content in the file as a string
# print(contents)
# file.close()  # closes the file to save on computer memory resources

# TODO 2. Using With to automatically close a file
# with open("my_file.txt") as file:  # with keyword automatically closes the file
#     contents = file.read()
#     print(contents)

# TODO 3. Writing to file and changing other contents
# with open("my_file.txt", mode="w") as file:  # mode "w" writes to the file, but deletes other contents
#     file.write("Hello")
#
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# TODO 3. Writing to file and appending it to current file contents
# with open("my_file.txt", mode="a") as file:  # mode "a" writes to the file, appends to file at end
#     file.write(f"\nThat should work.")
#
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# TODO 4. Create and write a file at the same time.
with open("new_file.txt", mode="w") as file: # only works in Write mode and only when the file doesnt exist yet
    file.write("this is a new file")

with open("new_file.txt") as file:
    contents = file.read()
    print(contents)
