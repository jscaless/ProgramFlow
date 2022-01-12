# number = "9,223;372:036 854,775;007"
number = input('Please enter series of numbers using any separators: ')
separators = ""

for char in number:
    if not char.isnumeric(): #isnumeric, isalpha, isalnum (alphanumeric without symbols)
        separators += char # separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])