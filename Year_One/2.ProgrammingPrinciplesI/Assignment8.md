# Assignment Eight - CodingPractice #1

[<< Go back up a level](ProgrammingPrinciplesI.md)

## Assignment Overview


Test #1
Due Oct 11 at 10:50am
Points 100 
Questions 9 
Time Limit 60 Minutes

Instructions
All submitted .java files must be compilable to be graded.  Please ask questions to instructor privately.  Academic fraud will be treated harshly...do your own work.

1.	Write a program that asks the user for three integers and prints the ones that are evenly divisible by 3.

2.	Write a program that is a for loop that prints the number from 100 to 202 (inclusive) by  threes.

3.	Write a which gets an integer input from the user, and print the number and whether it is odd or even.

4.	Write a program which will set the integer variable “class" to a single digit class.  Using a switch statement (and only a switch statement), print the variable, and the name of the class (1=Freshman, 2=Sophmore, 3=Junior, 4=Senior). If the variable is not 1-4, print "Graduate Student".

5.	Write a program which contains a while loop that prints the sum of the numbers between 2500 and 3500 inclusive.

6.	Write a program which gets a radius input from user and stores in an appropriate variable type. You will print the entered radius and the area of a circle with that radius (pi X radius2).

7.	Write a program which, using a do/while loop, prints the numbers between 10 and -10 by twos.

8.	Write a program that will take 4 numbers (floating point) as input. Print the smallest of the numbers.

9.	Write a program which contains a loop that prints numbers starting at one.  The loop will stop when the number is evenly divisible by 3, 5 and  7.  You must do this programatically (using code) and cannot use an if statement.


~~This assignment involves coding and testing of a program. ~~
 
~~The basic design of the first programs that you construct in this class consists of a prompt for information, receiving information, processing that information then producing a display of the results.~~

~~[Go To Pseudo Code](Assignment1_PseudoCode.txt)~~

~~[Go To Code](Assignment1.py)~~

### Background

~~This programming project will use the input and print functions along with some simple mathematics manipulation.~~
 
### Program Specifications

~~Your program will prompt the user for two non-zero integer numbers (numbers without decimal points).  It will next display the following output:~~
*   First line: the sum of the first and second number
*   Second line: the result of subtracting the second number from the first
*   Third line: the product of the first and the second number
*   Fourth line: the first number raised to the second number
*   Fifth line: the integer division of the first number by the second number, followed by the remainder from dividing the first number by the second number

## Assignment Notes:

~~To input the numbers it is necessary to use the input function. The input function takes a string, a sequence of characters between quotes, as a prompt to print to the user. It then waits until the user types a response, terminated by the user typing the Enter key. A string, again as a sequence of characters, is returned.~~
 
~~The returned string must be converted to a number. Since in this assignment we are strictly working with integers, a string is converted to an integer using the int function. The int function takes as an argument a single string and returns the integer the string represents. A typical interaction would be something like:~~
 
    numStr = input(‘Please enter a number: ‘)
    intVar = int(numStr)
 
print is a command that will print on the output window any combination of variables, values and strings. Each item to be printed must be separated from other items by a comma. All the items will be printed together, followed by a new line. For example:
 
    billsInt = 3
    print (‘The number ’,billsInt,‘ times two is ’, billsInt*2)
 
This command has 4 items to print: a string (‘The number ’), the value in the variable billsInt (3), another string (‘ times two is ’) and the result of an expression (6). What it will print is:
 
    The number 3 times two is 6
 
Once converted to numbers, the operations on these numbers are, respectively: + (sum), - (difference), * (product), , ** (exponent), // (division) and % (remainder). The last two deserve special comment.
 
In Python, if an integer is divided by another integer, the result is an integer. Thus the result of 6//4 is 1 (not 1.5).  That is, the “//” operation results in the integer quotient. The result of 6%4 is the integer remainder of the division, thus 2 (6 divided by 4 is 1 with a remainder of 2).  Play around with the quotient and remainder operators in the Python shell window until you get comfortable with how it works.
 
To clarify the problem specifications, we provide at the end of this document a snapshot of interaction with the already written program.
 
#### Getting Started

~~1.	Write up a pseudo code program for the assignment.~~
2.	Create a new program.
3.	Run the program
 
 
#### Questions for you to consider

~~1.	What happens when you try to divide by zero when you run your program?~~
2.	What happens when you multiply two VERY LARGE integers?
3.	What happens when you enter a letter instead of a number at the prompt?
 
### Sample Interactions:

~~```~~
~~Please enter an integer not equal to zero: 5~~
~~Please enter another integer not equal to zero: 2~~
5 plus 2 equals 7
5 minus 2 equals 3
5 multiplied by 2 equals 10
5 raised to the 2 equals 25
~~5 divided by 2 equals 2, with a remainder of 1~~
~~```~~

~~```~~
~~Please enter an integer not equal to zero: 109~~
Please enter another integer not equal to zero: 75
109 plus 75 equals 184
109 minus 75 equals 34
109 multiplied by 75 equals 8175
109 raised to the 75 equals 641190893321339203670626715036663652234223906598316420253822360900810232504714648526497415033069366991408148151773165107451222578274061290462826146705749
109 divided by 75 equals 1, with a remainder of 34.
~~```~~