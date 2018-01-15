import sys

try:
    # open fle stream
    file_name = "textFile"
    file = open(file_name,"w");
except IOError:
    print ("There was an error writing to", file_name)
    sys.exit()
file_finish = "1"
file_text = ""
print ("Enter '",file_finish,"' When finished")
while file_text != file_finish:
    file_text = raw_input("Enter text: ")
    if file_text == file_finish:
        # close the file
        file.close
        break
    file.write(file_text)
    file.write("\n")
file.close()
filename = raw_input("Enter filename: ")
if len(filename) == 0:
    print ("Next time please enter something")
    sys.exit()
try:
    file = open(filename,"r")
except IOError:
    print ("There was an errir reading file")
    sys.exit()
file_text = file.read()
file.close
print (file_text)
