""" Problem 1: Write a Python Program to calculate the total number of vowels and 
               count each of individual vowels in the string"""

vowels=['a','e','i','o','u','A','E','I','O','U']       # vowels in upper&lower case
str= "Guvi Geek Network Private Limited"               # given string

# To count the total number of vowels in the string:

total_vowels=0                                         # variable to store total no. of vowels in each iteration
for i in vowels:                                       # outer loop iterate through vowels
    for j in str:                                      # inner loop checks vowels in the string 
        if i==j:                                       # if condition to check the vowels and the 'char' in string is same.
            total_vowels=total_vowels+1
print("Total vowels in the String:",total_vowels)


# To count number of "a" or "A" in the given string:

a_count=0
for i in str:                                          # loops through the given string
    if i=='a' or i=='A':                               # condition to check the vowel 'a or A' in the string
        a_count+=1
print("Total 'a' in the given String:",a_count)        # prints the total number of 'a or A' in the string


# To count number of "e" or "E" in the given string:

e_count=0
for i in str:
    if i=='e' or i=='E':
        e_count+=1
print("Total 'e' in the given String:",e_count)    


# To count number of "i" or "I" in the given string:

i_count=0
for i in str:
    if i=='i' or i=='I':
        i_count+=1
print("Total 'i' in the given String:",i_count)     


# To count number of "o" or "O" in the given string:

o_count=0
for i in str:
    if i=='o' or i=='O':
        o_count+=1
print("Total 'o' in the given String:",o_count)     


# To count number of "u" or "U" in the given string:

u_count=0
for i in str:
    if i=='u' or i=='U':
        u_count+=1
print("Total 'u' in the given String:",u_count)     
        
        
        

            
