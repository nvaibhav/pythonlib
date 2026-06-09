mylist = []

for r in range(100):
    mylist.append(r)

splitsize = (int)(input("Ente the split size for the list:"))
mylist[:splitsize]
noofsplits = (int)(100/splitsize)
print(f'noofsplits={noofsplits}')
for i in range(splitsize):
    print(f'i={i}')
    print(mylist[i*noofsplits:(i+1)*noofsplits])