#Assignment 1

#Request user to input a non-zero integer
#Ex. "Please enter an integer not equal to zero:"
#Store first user input as an integer variable
var1 = int(input('Please enter an integer not equal to zero: '))

#Request user to input a second non-zero integer
#Ex. "Please enter another integer not equal to zero:"
#Store second user input an an integer variable
var2 = int(input('Please enter another integer not equal to zero: '))


#Display the sum of variable1 and variable2
#Ex. variable1 "plus" variable2 "equals" sum
print(str(var1) + ' plus ' + str(var2) + ' equals ' + str(var1 + var2))
         
#Display the result of variable2 subtracted from variable1
#Ex. variable1 "minus" variable2 "equals" result
print(str(var1) + " minus " + str(var2) + " equals " + str(var1 - var2))

#Display the product of variable1 times variable2
#Ex. variable1 "times" variable2 "equals" product
print(str(var1) + " times " + str(var2) + " equals " + str(var1 * var2))

#Display the result of variable1 raised to the power of variable2
#Ex. variable1 "raised to the power of" variable2 "equals" result
print(str(var1) + " raised to the power of " + str(var2) +  " equals " + str(pow(var1,var2)))

#Display the result of variable1 integer divided by variable2, and the modulus of variable1 divided by variable2
#Ex. variable1 "divided by" variable2 "equals" result "with a remainder of" modulus
print(str(var1) + " divided by " + str(var2) + " equals " + str(var1//var2) + " with a remainder of " + str(var1%var2))