#var1 = range(8)
#print var1
import time
import calendar


#dict = {'hello':'hi', 'age':22}
#text = type(dict)
#print text



tm = time.asctime(time.localtime(time.time()))
print tm


cal = calendar.calendar(2018,w=2,l=1,c=6)
print cal
