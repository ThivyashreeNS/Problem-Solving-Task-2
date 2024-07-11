""" Problem 7: Write a program that takes a string and
               returns the most frequent character in it."""


# Take input string from the user
string = input("Enter a string: ")

# Initialize variables to store the most frequent character and its count
max_char = ''
max_count = 0

# Iterate through each character in the string
for i in string:
    # Count occurrences of the current character in the string
    count = string.count(i)
    
    # Update max_char and max_count if we find a character with a higher count
    if count > max_count:
        max_char = i
        max_count = count

# Print the most frequent character
print("Most frequent character:", max_char)
