import re
txt = "i work for thunder soft india "
x = re.search("work",txt)
print (x)

if x :
    print ("match found")
else:
    print("not found")