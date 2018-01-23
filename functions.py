import sys

# Required arguments *
def printtext(var):
    "This function takes text as input and prints it on the screen"
    print var
    return

printtext("hello")




# Passed by refernce *
def changeFunc (myList,yourList):
    myList.append([4,5,6])
    yourList = [4,5,6]
    print 'f_My list',myList
    print 'f_Your list',yourList

myList = [1,2,3]
yourList = [1,2,3]
changeFunc(myList,yourList)
print 'My list',myList
print 'Your list',yourList



# Keyword arguments *
def printinfo( name, age ):
   "This prints a passed info into this function"
   print "Name: ", name
   print "Age ", age
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )



# Default argument *
# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print "Name: ", name
   print "Age ", age
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )


# Variable length argument *

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in vartuple:
      print var+1
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )


# Anonymus function *
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print "Value of total : ", sum( 10, 20 )
print "Value of total : ", sum( 20, 20 )





# Return statement *
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   totalsum = arg1 + arg2
   print "Inside the function : ", totalsum
   return totalsum;

# Now you can call sum function
total = sum( 10, 20 );
print "Outside the function : ", total
