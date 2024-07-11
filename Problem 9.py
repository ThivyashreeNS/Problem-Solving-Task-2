""" Problem 9: Write a Program that takes a string and returns the number of words in it.  """

# Get input from user 
string = input("Enter a string: ")

# split function to split the string and store it in list
words=string.split()

# Counts the numbers of words in the list of strings
count=len(words)
print("The list of strings:",words)
print("The number of words in the string:",count)