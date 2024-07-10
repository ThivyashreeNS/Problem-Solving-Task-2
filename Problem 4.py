""" Problem 4: Write a Program that takes a string and returns the
               number of Unique characters in it."""

string = input("Enter a String:")                                   # get a string input from user
unique_char = ""                                                    # an empty string
count = 0                                                           # variable to store the number of Unique char
for i in string:                                                    
    if i not in unique_char:                                        # checks if 'i' is present in the 'unique_char'
        unique_char = unique_char+i                                 # if condition is True, concatenate the unique char
        count += 1                                                  # increment the count value by 1
print("Unique characters in the String:",unique_char)
print("The Number of Unique characters in the String:",count)