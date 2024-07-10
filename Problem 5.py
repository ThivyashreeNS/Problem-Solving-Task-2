""" Problem 5: Write a Program that takes a string and returns True if it
               is a Palindrome, False otherwise"""


string = input("Enter a String:")      # get a string input from user
reverse_str = string[::-1]             # it reverse the string and saved in 'reverse_str' variable
if (string==reverse_str):              # checks the given string and the reversed string are equal
    print("True")                      # prints 'True' if the condition is true
else:                                   
    print("False")                     # prints 'False' if the condition is not true