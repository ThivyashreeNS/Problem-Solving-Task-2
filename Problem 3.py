""" Problem 3: Write a Program that takes a string and returns a 
               new string with all the vowels removed """
               
string= input("Enter a String:")                              # get a string input from user
new_string=""                                                 # an empty string
for i in string:                                              # iterates through the string
    if (i!="a" and i!='e' and i!='i' and i!='o' and i!='u'):  # checks if the loop variable is not an vowel
        new_string=new_string+i                               # concatenate the consonants to the empty string
print("New String with all the vowels removed:",new_string)                                              
        