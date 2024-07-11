""" Problem 8: Write a Program that takes a string and returns True if it
               is an anagram of another string, false otherwise. """

# Get input from user for str1 and str2
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# convert both the strings into lowercase
str1 = str1.lower()
str2 = str2.lower()

# check if length are same
if(len(str1) == len(str2)):

    # sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # checks the sorted char are same
    if(sorted_str1 == sorted_str2):
        print("True") 
    else:
        print("False")

else:
    print("False")