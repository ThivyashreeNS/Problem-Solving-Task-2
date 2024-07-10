""" Problem 2: Create a pyramid of numbers from 1 to 20 using for loop """

number = 1

for i in range(1, 7):               # Outer loop to iterate through rows
    for j in range(1, i+1):         # Inner loop print numbers in increasing order
        print(number, end=" ")      # Separated by space not in newline
        number += 1
        if number>20:               # To check the number is more than 20
            break                   # Stop the iteration to print numbers 1 to 20
    print()                         # Move to the next line after each row is printed