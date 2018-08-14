def main():
    ''' Step #1
    We declared the variable f to open a file named textfile.txt. Open takes 2 arguments, 
    the file that we want to open and a string that represents the kinds of permission or 
    operation we want to do on the file.
    
    Here we used "w" letter in our argument, which indicates write and the plus sign that means 
    it will create a file if it does not exist in library
    
    The available option beside "w" are "r" for read and "a" for append and plus sign means if 
    it is not there then create it
    '''
    f= open("./guru99.txt","w+")

    ''' Step #2
    We have a for loop that runs over a range of 10 numbers.
    Using the write function to enter data into the file.
    The output we want to iterate in the file is "this is line number", which we declare with write function and then percent d (displays integer)
    So basically we are putting in the line number that we are writing, then putting it in a carriage return and a new line character
    '''

    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))

    # This will close the instance of the file guru99.txt stored
    f.close()

'''
When Python interpreter reads a source file, it will execute all the code found in it.
When Python runs the "source file" as the main program, it sets the special variable 
(__name__) to have a value ("__main__").
When you execute the main function, it will then read the "if" statement and checks whether 
__name__ does equal to __main__.

One reason for doing this is that sometimes you write a module (a .py file) where it can be 
executed directly. Alternatively, it can also be imported and used in another module. By doing 
the main check, you can have that code only execute when you want to run the module as a program 
and not have it execute when someone just wants to import your module and call your functions 
themselves.
'''
if __name__ == "__main__":
    main()

print "I am done!!!"
