# Assignment One - MetricConversion

[<< Go back up a level](ProgrammingPrinciplesI.md)

## Assignment Overview

Write a python program that will prompt the user for their name,  height in inches, and weight in pounds.
You will then output that data using metric units.


### Background

This programming project will use the input and print functions along with some simple mathematics manipulation.
 
### Program Specifications

Your program will prompt the user for their name (a string), their height in inches (an int or float), and their weight in pounds (an int or float).  It will next display the following output:
*   First line: the program name
*   Second line: the user's name
*   Third line: the result of converting height to metric
*   Fourth line: the result of converting weight to metric

## Assignment Notes:

Consider yourself to be in 'Happy Python Land' where users input what you expect them to and data validation is not required.

#### **Simple Conversion Factors**

||**US/Imperial**|**Metric**|
|:-|:-:|:-|
|**Height**|inches|meters|
||1|0.0254|
|**Weight**|pounds|kilograms|
||1|0.4535|
 
#### Getting Started

1.	Write up a decomposition or pseudo code program for the assignment
2.	Create a new program
3.	Run the program
 
 
#### Questions for you to consider

1.	What type of data are you receiving from input?
2.	What happens when you try to print non-strings with strings in a single print statement?
3.  Should you do value conversions in your main function or in helper functions?
4.  Do you have to hard-code the value conversion or could you use something else? Have you read about libraries yet?
 
### Sample Interactions:

```
Enter your Name: $Brian
Enter Height in inches: $72
Enter Weight in pounds: $275

Metric Calculation
Name: Brian
Height: 1.8288 meters
Weight: 124.7125 kilograms
```

```
Enter your Name: $Fred
Enter Height in inches: $67
Enter Weight in pounds: $140

Metric Calculation
Name: Fred
Height: 1.7018 meters
Weight: 63.49 kilograms
```

### Hints

[Go To Decomposition](Assignment1.txt)

### Solution

[Go To Code](Assignment1.py)