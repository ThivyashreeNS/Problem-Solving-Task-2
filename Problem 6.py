""" Problem 6: Write a Program that takes two strings and returns the longest common substring between them """


# Get input from user for str1 and str2
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Initialize variables to store the length of longest common substring and its ending index
max_len = 0
end_index = 0

# Lengths of the input strings
len1 = len(str1)
len2 = len(str2)

# Iterate through each character of str1
for i in range(len1):
    for j in range(len2):       
        length = 0 
        
        # Check for common substrings starting at str1[i] and str2[j]
        while (i + length < len1 and j + length < len2 and str1[i + length] == str2[j + length]):
            length += 1         # length variable increments if the while condition True
            
        # Update max_len and end_index if we found a longer common substring
        if length > max_len:
            max_len = length
            end_index = i + length

# Extract the range of the longest common substring
substring = str1[end_index - max_len:end_index]

# Print the substring
print("Longest common Substring:", substring)
