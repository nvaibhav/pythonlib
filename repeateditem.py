#having a list , identify how many times a element is repeated in the list
from ntpath import exists



mylist = [2,4,1,7,5,4,5,2,9,10,4]
mydict = {}

for item in mylist:
    if item in mydict:
        listitemcount = mydict[item]
        mydict[item] = listitemcount+1
    else:
        mydict[item] = 1

print(mydict)

