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
			print("success")
			print(array)
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
		
def binarySearchAlgo(array, arg1, x):
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

    

if __name__ == "__main__":
    main()

"""
public class BinarySearchRange {

	public static void main(String[] args) {
		/** Data processing input */
		String fname = args[0]; //uses first argument entered as filename
		//String fname = "./src/data.txt"; //alternatively, use this line from IDE to import data from file
		File file = new File(fname);
		Scanner scan = null;
		try {
			scan = new Scanner(file);
		} catch (FileNotFoundException e1) {
			e1.printStackTrace();
		}
		
		if(!file.exists() && !file.canRead()) {
			fname = args[0]; //uses first argument entered as filename
			//fname = "./src/data.txt"; //alternatively, use this line from IDE to import data from file
			file = new File(fname);
		}
		
		int numOfLines = 0; //count the number of lines in the file
		while(scan.hasNextLine()) {
			scan.nextLine();
			numOfLines++;
		}
		scan.close(); //clear buffer
		
		String[] strArr = new String[numOfLines]; //build a string array to hold file contents
		
		try {
			Scanner fileRead = new Scanner(file);
			for (int ctr = 0; ctr <= strArr.length-1; ctr++) { //store each line of file in string array element
				strArr[ctr] = fileRead.nextLine();
			}
			fileRead.close();
		} catch(Exception e) {
			System.out.println(e.getMessage());
		}
		
		int[] arr = new int[strArr.length]; //build int array of same size as string array
		for (int ctr = 0; ctr <= strArr.length-1; ctr++) { //translate string array elements into int array elements
			   arr[ctr] = Integer.parseInt(strArr[ctr]);
		}
		
		int leftSearch = Integer.parseInt(args[1]); //take in second argument as string, parse as integer, pass to variable
		int rightSearch = Integer.parseInt(args[2]); //take in third argument as string, parse as integer, pass to variable
		
		
		if (arr.length < 1 || leftSearch > rightSearch) { // Check preconditions
			//array is empty or left and right search inputs are reversed
			System.out.println("null");
		}
		else if (leftSearch > arr[arr.length-1] || rightSearch < arr[0]) { // Check preconditions
			//left search is greater than the largest number and right search is less than the smallest number in array
			System.out.println("null");
		}
		else if (leftSearch <= arr[0] && rightSearch >= arr[arr.length-1]) { // Check preconditions
			//the entire array falls within the search terms
			System.out.println("A[" + 0 + ".." + (arr.length-1) + "]");
		}
		else { 
			//terms are acceptable and a fragment of the array will be searched for
			int startRange = binarySearchStartRange(arr, leftSearch);
			int endRange = binarySearchEndRange(arr, rightSearch);
			
			if(startRange <= endRange) {
				//ensure meaningful result is printed
				System.out.println("A[" + startRange + ".." + endRange + "]");
			}
			else {
				System.out.println("null");
			}
		}
	} //end main method
	
	public static int binarySearchStartRange(int[] arr, int x) {
		int low = 0, high = arr.length-1;
		while (low <= high) {
			int mid = (int) Math.floor((low + high)/2);
			if (arr[mid] == x) {
				//hit the number we were looking for
				if (mid == 0) {
					//leftmost position in the array hit
					return mid;
				}
				else if (arr[mid-1] == x) {	
					//not the leftmost occurance of the number we were looking for
					high = mid-1;
				}
				else {
					//returns the leftmost occurance of the number we were looking for
					return mid;
				}
			}
			else if (arr[mid] < x) {
				//we are too far to the left
				low = mid + 1;
			}
			else {
				//we are to the right of x
				if (mid == 0) {
					//leftmost position in the array hit, should never hit b/c covered by first if statement
					return mid;
				}
				else if (arr[mid-1] < x) { // ! what if arr[mid-1] is less than arr[0]?
					//we are at the smallest number within the range we want
					return mid;
				}
				else {
					//we are too far to the right of x
					high = mid - 1;
				}
			}
		}
		//could not find the element we were searching for (should never hit this b/c preconditions)
		return -1;
	} //end binarySearchStartRange
	
	public static int binarySearchEndRange(int[] arr, int y) {
		int low = 0, high = arr.length-1;
		while (low <= high) {
			int mid = (int) Math.floor((low + high)/2);
			if (arr[mid] == y) {
				//hit the number we were looking for
				if (mid == arr.length-1) {
					//rightmost position in the array hit
					return arr.length-1;
				}
				else if (arr[mid+1] == y) {	// ! what if arr[mid+1] is greater than arr.length-1?
					//not the rightmost occurance of the number we were looking for
					low = mid+1;
				}
				else {
					//returns the rightmost occurance of the number we were looking for
					return mid;
				}
			}
			else if (arr[mid] > y) {
				//we are too far to the right
				if (mid - 1 <= y) {
					//we found the highest value within the range
					return mid - 1;
				}
				else {
					//restrict the search area to left of mid
					high = mid - 1;
				}
			}
			else {
				//we are to the left of y, restrict the search area to the right of mid
				low = mid + 1;
			}
		}
		//could not find the element we were searching for (should never hit this b/c preconditions)
		return -1;
	} //end binarySearchEndRange
	/*
	public static int countLines(Scanner infs) { //method not used in this version of program, future improvement plan
		int count = 0;
		while(infs.hasNextLine()) {
			infs.nextLine();
			count++;
		}
		return count;
	} //end countLines method
	*/
} //end BinarySearchRange program
"""