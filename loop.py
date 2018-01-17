import sys

# While loop
var1 = 0
while var1 < 10:
    print 'Count is ',var1
    var1  += 1

print 'After while'

 # Else with while loop
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"



   # Infinite loop
var = 1
while var == 1 :  # This constructs an infinite loop
   var = raw_input("Enter a number  :")
   print "You entered: ", var

print "Good bye!"


# Single statements suits

flag = 1
#cswhile (flag): print 'Given flag is really true!'
print "Good bye!"




# For loop
for alphabets in 'Python':
    print 'Letter: ', alphabets
automobile = ['car','bike','truck']
for stuff in automobile:
    print 'Automobile: ',stuff

print 'End for loop'

# For loop with range

automobile = ['car','bike','truck']
for stuff in range(len(automobile)):
    print automobile[stuff]

# Nested for loop with range

var = range(10,20)
for num in var:
    for num1 in range(2,num):
        if(num%num1 == 0):
            num2 = num/num1
            print '%d * %d equals %d' % (num1,num2,num)
            break
        else:
            print '%d is prime' % (num)
            break
