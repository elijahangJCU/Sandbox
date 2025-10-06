#
# # Example 1
#
# valid_input = False
#
# names = ['Ada', 'Alan', 'Bill', 'John']
# print(', '.join(names))
#
# while not valid_input:
#     try:
#         name_to_remove = input("What do you want to remove? ")
#         names.remove(name_to_remove)
#         print(', '.join(names))
#         valid_input = True
#     except ValueError:
#         print("Please enter a valid name with the right capitalization")
#
#
# # Example 2
#
# file_name = input("Enter name of file to open: ")
#
# try:
#     file = open(file_name, "r")
#     contents = file.read()
#     print(contents)
# except FileNotFoundError:
#     print("Enter an existing file name.")
# else:
#     print("File opened successfully!")
# finally:
#     print("Checking done.")


# Example 3
data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]

name_width = max(len(data[0][0]) for pair in data)
score_with = max(len(data[0][1]) for pair in data)

pair = [pair for pair in data]

for pair in pair:
    x, y = pair
    print(f"{x:{name_width}} = {y:{score_with}}")

