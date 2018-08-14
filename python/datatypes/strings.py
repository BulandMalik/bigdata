'''----------------------------------- Strings
In Python, Strings are immutable.

Python does not support a character type, these are treated as strings of length one, 
also considered as substring. 

[]	- Slice- it gives the letter from the given index
[ : ] -	Range slice-it gives the characters from the given range
in	- Membership-returns true if a letter exist in the given string 
not in	- Membership-returns true if a letter exist is not in the given string
% - Used for string format	-- %r - It insert the canonical string representation of the object 
(i.e., repr(o)) %s- It insert the presentation string representation of the object (i.e., str(o)) %d- it will format a number for display 

*	Repeat 
+	It concatenates 2 strings	
'''
hello = "Hello World!"
print(hello[:6]) # Slice ':6' or '0:6' has the same effect 
print(hello[0:6] + ", My Name is Buland")

repeat = "Hurrayyy.... "
print 2*repeat

name = 'My name is Buland Malik and age is '
age = 99
print'%s %d' % (name,age)	


'''----------------------------------- Replace method '''
oldstring = 'I like Python 2' 
print(oldstring)
newstring = oldstring.replace('2', '3')
print(newstring)

'''----------------------------------- Handling upper / lower case '''
text="python is GREAT"
print(text.upper())
print text.lower()
print text.capitalize()

'''----------------------------------- "join" function '''
#if you want to add a colon (:) after every character in the string "Python" you can use the 
# following code.
print(":".join("Python"))

'''----------------------------------- "reverse" function '''
phone="4090011120"
#print(''.join(reversed(phone)))
print(reversed(phone))

'''----------------------------------- "split" function '''
text="Python2 is simply great!"		
print(text.split(' '))
print(text.split('is'))

'''----------------------------------- Strings are immutable '''
name = "Buland"
name = name.replace("Buland","Buland Malik")
print(name)