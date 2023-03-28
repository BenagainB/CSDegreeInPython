#Description: Program input is file and two integers.
#Program checks for index of first and last appearance of input ints using binary searches.
#Program prints out array indexes or null depending on inputs and file contents.
#Program is designed to run as O(logn) time complexity.
#This program is run from the command line.
#Assumptions: input file is a .txt file with one integer per line, in increasing sorted order.

import math
import sys
import csv

def main():
	#Check to see if initial arguments are valid
	filename = ""
	arg1 = 0
	arg2 = 0
	msg_IndexError = "Program requires 3 arguments: [filename.txt] [integer] [integer]"	
	try:
		if sys.argv[1] and sys.argv[2] and sys.argv[3]:
			filename = sys.argv[1]
			arg1 = int(sys.argv[2])
			arg2 = int(sys.argv[3])
	except IndexError:
		print(msg_IndexError)
	
	array = []

	#Check to see if file exists
	msg_FileNotFound = "Could not read file: "
	try:
		with open(filename, 'r') as f:
			reader = csv.reader(f)
			tempArr = []
			for row in reader:
				tempArr.extend(row)
		for item in tempArr:
			array.append(int(item))
	except IOError:
		print(msg_FileNotFound + filename)
	
	if checkPreconditions(array, arg1, arg2):
		if arg1 <= array[0] and arg2 >= array[len(array)-1]:
			print("A",array)
		else:
			startRange = binarySearchStartRange(array, arg1)
			endRange = binarySearchEndRange(array, arg2)
			
			if(startRange <= endRange):
				#ensure meaningful result is printed
				print("A[", startRange, "..", endRange, "]")
			if(startRange > endRange):
				print("null")
	else:
		print("null")

def checkPreconditions(array, arg1, arg2):
	if len(array) < 1:
		return False
	elif arg1 > arg2:
		return False
	elif arg2 < array[0]:
		return False
	elif arg1 > array[len(array)-1]:
		return False
	else:
		return True
		
def binarySearchStartRange(array, x):
	result = []
	low = 0
	high = len(array)-1
	while (low <= high):
		mid = int(math.floor((low + high)/2))
		if array[mid] == x:
			#hit the number we were looking for
			if (mid == 0):
				#leftmost position in the array hit
				return mid
			elif array[mid-1] == x:	
				#not the leftmost occurance of the number we were looking for
				high = mid-1
			else:
				#returns the leftmost occurance of the number we were looking for
				return mid
		elif array[mid] < x:
			#we are too far to the left
			low = mid + 1
		else:
			#we are to the right of x
			if mid == 0:
				#leftmost position in the array hit, should never hit b/c covered by first if statement
				return mid
			elif array[mid-1] < x:
				#! what if arr[mid-1] is less than arr[0]?
				#we are at the smallest number within the range we want
				return mid
			else:
				#we are too far to the right of x
				high = mid - 1
	#could not find the element we were searching for (should never hit this b/c preconditions)
	return -1
	#end binarySearchStartRange

def binarySearchEndRange(array, y):
	low = 0
	high = len(array)-1
	while (low <= high):
		mid = int(math.floor((low + high)/2))
		if (array[mid] == y):
			#hit the number we were looking for
			if mid == len(array)-1:
				#rightmost position in the array hit
				return len(array)-1
			elif array[mid+1] == y:	# ! what if arr[mid+1] is greater than arr.length-1?
				#not the rightmost occurance of the number we were looking for
				low = mid+1
			else:
				#returns the rightmost occurance of the number we were looking for
				return mid
		
		elif array[mid] > y:
			#we are too far to the right
			if (mid - 1 <= y):
				#we found the highest value within the range
				return mid - 1
			else:
				#restrict the search area to left of mid
				high = mid - 1
		else:
			#we are to the left of y, restrict the search area to the right of mid
			low = mid + 1
	#//could not find the element we were searching for (should never hit this b/c preconditions)
	return -1
#end binarySearchEndRange
    

if __name__ == "__main__":
    main()