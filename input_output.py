import sys
import os

# fileOpen = open('foo.txt','wb')
# fileOpen.write('The should be some text in the file so what we could read it later! \nGot it! \n')
# fileOpen.close()



# fileOpen = open('foo.txt','r+')
# stri = fileOpen.read(10)
# print stri
#
# position = fileOpen.tell()
# print position
# position = fileOpen.seek(5,1)
# stri = fileOpen.read(10)
# print stri
#
# fileOpen.close()
#
#
# os.rename('foo.txt','bar.txt')
# os.remove('textFile')


try:
    fileOpen = open('foo.txt','r')
    try:
        fileOpen.write('Just some stuff')
    finally:
        #close
        fileOpen.close()
except IOError:
    print 'Error, in the opening of the file'
