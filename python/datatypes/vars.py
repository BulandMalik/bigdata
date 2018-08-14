'''----------------------------------- Variables
A Python variable is a reserved memory location to store values. In other words, a variable 
in a python program gives data to the computer for processing.

Every value in Python has a datatype. Different data types in Python are Numbers, List, Tuple, 
Strings, Dictionary, etc. Variables can be declared by any name or even alphabets like x, xyz etc. 

You can decalre and re-declare the variable even after you have declared and initialized it.
'''

#decalre var1 plus also initialize it
var1 = 900
print(var1)

#re-declare var1 with diff type
var1 = "Buland"
print(var1)

'''----------------------------------- Concatenate Variables
Unlike Java, which concatenates number with string without declaring number as string, 
Python requires declaring the number as string otherwise it will show a TypeError
'''
#print("My Name is Buland and my age is "+35) #Error as diff types cannot be combined

#Once the integer is declared as string, it can concatenate both
print("My Name is Buland and my age is "+str(35))

''' ----------------------------------- Local & Global Variables
Variables can have Global vs Local scope (defined within fucntions/modules)
'''
# Declare a variable and initialize it
age = 35
print age
# Global vs. local variables in functions
def someFunction():
# global age #it means use the global age var
    age = 40
    print age #oprint local age variable that is 40
someFunction()
print age #back to global value that is 35


'''----------------------------------- Deleting Variables
use 'del' command
'''
name = "My Name is Buland";
print(name)
del name
print(name)

'''----------------------------------- Summary
Variables are referred to "envelop" or "buckets" where information can be maintained and 
referenced.
'''