numofwords = 0
numofletter = 0
numofdigit = 0

text = input("Enter your text: ")

for x in text:
    x.upper()
    if x>='a' and x<='z':
        numofletter += 1

    elif x>='0' and x<='9':
        numofdigit += 1

    elif x == ' ':
        numofwords +=1


print("Number of Letter: ", numofletter)
print("Number of digit:", numofdigit)
print("Number of words", numofwords)