introString = input("enter your introduction:-")
print(introString)
characterCount = 0
wordCount = 1
for i in introString:
        characterCount = characterCount+1
        print(characterCount)
        if(i ==" "):
            wordCount = wordCount+1

print("number of words in the string")
print(wordCount)
print("number of chracaters in the string")
print(characterCount)
