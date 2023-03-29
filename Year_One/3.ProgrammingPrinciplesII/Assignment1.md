# Assignment One - 2D Multi-Dimensional Arrays

[<< Go back up a level](ProgrammingPrinciplesII.md)

## Assignment Overview

This assignment involves coding and testing of 4 programs:
1.  The first program will require you to perform simple arithmetic operations in multi-dimensional arrays.
2.  The second program will require you to re-write an existing program using a multi-dimensional array.
3.  The third program will require you to sum a multi-dimensional array by row and then sort by value.
4.  The fourth program will require you to write a method to sort a multi-dimensional array by rows.

### Details

Write 4 programs:
1.  code_Assignment1_SumArray.py
2.  code_Assignment1_SortStudentsArray.py
3.  code_Assignment1_WeeklyHoursArray.py
4.  code_Assignment1_SortRowsColumnsArray.py

### Program Specifications - SumArray:

*   Write a method that returns the sum of all the elements in a specified column in a m(Sum elements column by column) matrix.

~~public static double sumColumn(double[][] m, int columnIndex)~~

*   Write a test program that reads a 3-by-4 matrix and displays the sum of each column. 

Here is a sample run:
```
Enter a 3-by-4 matrix row by row:
1.5 2 3 4
5.5 6 7 8
9.5 1 3 1

Sum of the elements at column 0 is 16.5
Sum of the elements at colum 1 is 9.0
Sum of the elements at column 2 is 13.0
Sum of the elements at column 3 is 13.0
```

### Program Specifications - SortStudentsArray:

(SORT STUDENTS ON GRADES) Rewrite GradeExam.java, to display the students in increasing order of the number of correct answers.


```java
//* GradeExam.java */

public class GradeExam {
    /** Main method */
    public static void main(String[] args) {
        //Student' answers to the questions
        char[][] answers = {
            {'A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'},
            {'D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'},
            {'E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'},
            {'C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'},
            {'A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'},
            {'B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'},
            {'B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'},
            {'E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'}};
        
        //Key to the questions
        char[] keys = {'D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D'};

        //Grade all answers
        for (int i = 0; i < answers.length; i++){
            //Grade one student
            int correctCount = 0;
            for(int j = 0; j < answers[i].length; j++){
                if (answers[i][j] == keys[j])
                    correctCount++;
            }
        
            System.out.println("Student" + i + "'s correct count is " + correctCount);
        }
    }
}

```

### Program Specifications - WeeklyHoursArray:

(COMPUTE THE WEEKLY HOURS FOR EACH EMPLOYEE) Suppose the weekly hours for all employees are stored in a two-dimensional array. Each row records an employee’s seven-day work hours with seven columns. For example, the following array stores the work hours for eight employees. Write a program that displays employees and their total hours in decreasing order of the total hours.

 ||Su|M|T|W|Th|F|Sa|
 |-|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
 |Employee 0|2|4|3|4|5|8|8|
 |Employee 1|7|3|4|3|3|4|4|
 |Employee 2|3|3|4|4|3|2|2|
 |Employee 3|9|3|4|7|3|4|1|
 |Employee 4|3|5|4|3|6|3|8|
 |Employee 5|3|4|4|6|3|4|4|
 |Employee 6|3|7|4|8|3|8|4|
 |Employee 7|6|3|5|9|2|7|9|


### Program Specifications - SortRowsColumnsArray:

(SORT TWO-DIMENSIONAL ARRAY) Write a method to sort a two-dimensional array using the following header:

public static void sort(int m[][])

The method performs a primary sort on rows, and a secondary sort on columns. For example, the following array

{{4, 2},{1, 7},{4, 5},{1, 2},{1, 1},{4, 1}}

||||
|-|-|-|
|4||2|
|1||7|
|4||5|
|1||2|
|1||1|
|4||1|

will be sorted to

{{1, 1},{1, 2},{1, 7},{4, 1},{4, 2},{4, 5}}

||||
|-|-|-|
|1||1|
|1||2|
|1||7|
|4||1|
|4||2|
|4||5|


## Assignment Notes:

You only need to use the basic list and not a more advanced structure for the assignment.
 
#### Getting Started

1.	Write up a decomposition or pseudo code program for the assignment
2.	Create a new program
3.	Run the program
 
 
#### Questions for you to consider

~~1.	What type of data are you receiving from input?~~
~~2.	What happens when you try to print non-strings with strings in a single print statement?~~
~~3.  Should you do value conversions in your main function or in helper functions?~~
~~4.  Do you have to hard-code the value conversion or could you use something else? Have you read about libraries yet?~~

### Hints

[Go To SumArray Decomposition](Assignment1_SumArray.txt)

[Go To SortStudentsArray Decomposition](Assignment1_SortStudentsArray.txt)

[Go To WeeklyHoursArray Decomposition](Assignment1_WeeklyHoursArray.txt)

[Go To SortRowsColumnsArray Decomposition](Assignment1_SortRowsColumnsArray.txt)

### Solution

[Go To SumArray Code](code_Assignment1_SumArray.py)

[Go To SortStudentsArray Code](code_Assignment1_SortStudentsArray.py)

[Go To WeeklyHoursArray Code](code_Assignment1_WeeklyHoursArray.py)

[Go To SortRowsColumnsArray Code](code_Assignment1_SortRowsColumnsArray.py)