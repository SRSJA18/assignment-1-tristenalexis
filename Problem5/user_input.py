"""Assignment 1: Problem 5 - User Input"""
'''
In this exercise, we will ask the user for his/her first and last name and date of birth and print them out formatted.
Recall that you can get input from the user using the command input("text").

Example Output:

Enter your first name: Chuck
Enter your last name: Norris
Enter your date of birth:
Month? March
Day? 10
Year? 1940
Chuck Norris was born on March 10, 1940.

To print a string and a number in one line, you just need to separate the arguments with a comma (this works for
any two types within a print statement). The comma adds a space between the two arguments. For example, the
lines:

mo = 'October'
day = '20'
year = '1977'
print mo, day, year

will have the output:

October 20 1977
'''

# TODO 1. Ask for the first name and store it in a variable
a = input("What is your first name?")
# TODO 2. Ask for the last name and store it in a variable
b = input("What is your last name?")
# TODO 3. Print "Enter your date of birth:"
print("Enter your date of birth")
# TODO 4. Ask for the Month and store it in a variable
c = input("Month?")
# TODO 5. Ask for the day and store it in a variable
d = input("Day?")
# TODO 6. Ask for the year and store it in a variable
e = input("Year?")
# TODO 7. Print the name with the date of birth as shown above.
print ("%s %s you were born on %s %s, %s. " %(a, b, c, d, e))