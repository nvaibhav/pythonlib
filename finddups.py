
#Create a list of integers
mylist = [4,5,1,2,0,45,2,6,0]

#Dup list
mydups = []

#Find dups in the list
for listitem in mylist:
    if listitem not in mydups and mylist.count(listitem) > 1:
        mydups.append(listitem)

print(f'Dups: {mydups}')