# Assignment One   

[<< Go back up a level](DataStructures.md)

## Assignment Overview

### Binary search of array elements in a sorted array

*Using 0-based indexing*

In this project, we want to efficiently search in a sorted array A[0..n − 1] for all its member elements whose values fall into a given value range [x..y]. For example, suppose the following sorted array A is given:

    A[ ] = {2,5,5,5,7,9,9,10,15,15,17,19}

*   Given a value range [x..y] = [6..12], the answer should be A[4..7], because every element in A[4..7]
has a value belonging to the range [6..12] and all the other array elements do not.
*   Given a value range [x..y] = [1..15], the answer should be A[0..9], because all elements from A[0..9]
have values belonging to [1..15], while all other array elements do not.
*   Given a value range [x..y] = [11..14], the answer should be null, because no array element has a
value belonging to this range.
*   Given a value range [x..y] = [22..35], the answer should be null, because no array element has a value belonging to this range.

[![Visual explanation of Binary Search algorithm]({https://www.youtube.com/watch?v=wz7XgKowJIg})]({"https://www.youtube.com/watch?v=wz7XgKowJIg"} "Visual explanation of Binary Search algorithm")

### Background

Note that in order to make the program overall efficient, the searches for both s and t need to be efficient and each search can take no more than O(log n) time, making the overall program to have a time cost of O(log n). It is your job to figure out how to efficiently modify the binary search to search for s and t. You will need to have two different modified versions of the binary search for the searchings of s and t efficiently.

Obviously, an exhaustive search in the array A with the value range [x..y] kept in mind will not be efficient, as it will take O(n) time in the worst case. You also need to know that the following idea is not efficient either and will spend O(n) time in the worst case and thus cannot be used: We modify the binary search, such that it can find the location of one of the smallest array elements that are ≥ x, then we do a walk starting from that location toward the left boundary of the array A to find the value of s. This procedure is not efficient, because the walk itself can cover the majority of the array A in the worst case. (Similar idea for finding t will not be efficient either. )


### Program Specifications

1. Your program should be named as: BinarySearchRange.py
2. The input and output of your program.
*   There are three inputs of your program. One is a text file, where each line is an integer number. All the numbers in the text file are already sorted in the ascending order. The file name should be supplied to your program as a command line parameter. The other two inputs are the integer values representing *x* and *y*, respectively, which should also be supplied to your program as command line parameters.

## Assignment Notes:

Before we do any complicated search procedure, we first will check all possible edges cases (Lines 1-8 below), all of which can be handled using constant amount of time.

1.  if A is empty OR x > y
2.  the answer is null
3.  elif y < A[0]
4.  the answer is null
5.  elif x > A[n-1]
6.  the answer is null
7.  elif x <= A[0] AND y >= A[n-1] 
8.  the answer is the whole array A[0..n-1]
9.  else
10. do a search that uses and modifies the binary search idea.
 
#### Getting Started

[data file](ass1_data.txt)
 
#### Questions for you to consider

1.	Why does it matter that you have an already sorted data file to search within?
 
### Sample Interactions:

For example, if we supply x = 10 and y = 20 and the given file named ass1_data.txt has the following content:

     2
     2
     5
     6
     8
     10
     10
     11
     21
     25
     26

Then, the command line you type would be:

    $python BinarySearchRange.py ass1_data.txt 10 20

and the output should be:

    $A[5..7]

For the same input text file, if x = 12 and y = 20, then the command line you type would be: 

    $python BinarySearchRange.py ass1_data.txt 12 20

and the output should be:

    $null

### Hints

[text description of simple solution](ass1_algorithm_description.txt)

### Solution

