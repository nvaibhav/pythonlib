mysentence = input('Enter a sentence:')

wordslist = mysentence.split()
#print(f"workdslist={wordslist}")

mywordsrepeateddict = {}

for word in wordslist:
    if word in mywordsrepeateddict:
        mywordsrepeateddict[word] += 1
    else:
        mywordsrepeateddict[word] = 1

for key in mywordsrepeateddict.keys():
    value = mywordsrepeateddict[key]
    if value > 1:
        print(f"word {key} repeated {value} times")