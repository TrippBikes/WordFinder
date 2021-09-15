from english_words import english_words_lower_alpha_set as englwords

# Variables
lowers = "abcdefghijklmnopqrstuvwxyz"
haveLetters = False
haveMustUse = False
foundInvalidLetter = False
letters = []
listOWords = []

# Collect letters from user, make sure letters are valid.
while not haveLetters:
    askForLetters = input("Available letters: ").lower()
    letters = list(askForLetters)
    for letterI in letters:
        if letterI not in lowers:
            print(f"Please only use letters, {letterI} is not a letter.")
            foundInvalidLetter = True
    if not foundInvalidLetter:
        haveLetters = True
    else:
        foundInvalidLetter = False

# Collect must use letter from user, make sure letter is in provided letters
while not haveMustUse:
    mustUse = input("Letter that must be used in each word: ").lower()
    if len(mustUse) == 1:
        if mustUse in askForLetters:
            haveMustUse = True
        else:
            print(f"Must be one of these letters: {askForLetters}")
    else:
        print("Can only have 1 must use letter.")


# Nested for loop tries every possible combination of every letter available against a dictionary and
# stores it in listOWords if it contains the must use letter. Only collects 4-9 letter words.
for letterI in letters:
    for letterII in letters:
        for letterIII in letters:
            for letterIV in letters:
                newWordI = letterI+letterII+letterIII+letterIV
                if mustUse in newWordI and newWordI in englwords:
                    listOWords.append(newWordI)
                for letterV in letters:
                    newWordII = newWordI+letterV
                    if mustUse in newWordII and newWordII in englwords:
                        listOWords.append(newWordII)
                    for letterVI in letters:
                        newWordIII = newWordII+letterVI
                        if mustUse in newWordIII and newWordIII in englwords:
                            listOWords.append(newWordIII)
                        for letterVII in letters:
                            newWordIV = newWordIII+letterVII
                            if mustUse in newWordIV and newWordIV in englwords:
                                listOWords.append(newWordIV)
                            for letterVIII in letters:
                                newWordV = newWordIV+letterVIII
                                if mustUse in newWordV and newWordV in englwords:
                                    listOWords.append(newWordV)
                                for letterIX in letters:
                                    newWordVI = newWordV+letterIX
                                    if mustUse in newWordVI and newWordVI in englwords:
                                        listOWords.append(newWordVI)

# Alphabetize and check if any words contain all provided letters
listOWords.sort()
for word in listOWords:
    containsAllLetters = True
    for letterI in letters:
        if letterI in word:
            continue
        else:
            containsAllLetters = False
    if containsAllLetters:
        listOWords.remove(word)
        listOWords.insert(0, f"***{word}***")

# Output words to terminal
print(f"All Possible 4-9 letter words that include the letter {mustUse}:")
for word in listOWords:
    print(word)

# Output words to a text file
with open("Text File of Words.txt", "w") as output:
    for word in listOWords:
        output.write(str(word + "\n"))
output.close()
