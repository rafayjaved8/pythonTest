import sys


# If condition
var1 = 100
if var1:
    print ('We have got a true condition')
    print(var1)

var2 = 0
if var2:
    print ('We have got a true condition')
    print(var2)

print('end if')



# If-Else consition

var1 = 100
if var1:
    print ('\n \n We have got a true condition')
    print(var1)
else:
    print ('We have a false condition')
    print (var1)

var2 = 0
if var2:
    print ('We have got a true condition')
    print(var2)
elif var2 == 0:
    print ('We have a zero' + str(var2))
else:
    print ('We have a false condition')
    print (var2)

print('end if-else')


# Nested If

var1 = 170
if var1 < 300:
    print ('Its below 300')
    if var1 < 100:
        print ('Its below 100')
    if var1 < 200:
        print ('Its below 200')
else:
    print ('Its over 300')
