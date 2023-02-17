# was planning to use regex but opted for another simpler, and possible faster solution
import re
import os

os.system('cls')

# loading txt files into variables
fileOne = open("txt_files/tekstfil1.txt", "rt")
fileTwo = open("txt_files/tekstfil2.txt", "rt")
fileThree = open("txt_files/tekstfil3.txt", "rt")

# creating lists out of each of the lines of each txt file to search each one easier
fileOneList = fileOne.readlines()
fileTwoList = fileTwo.readlines()
fileThreeList = fileThree.readlines()

# creating a list containing the previous lists to easily parse through with a 'for'
listOfFileLists = [fileOneList, fileTwoList, fileThreeList]


# main function, the program loops back to this forever until you tell it to stop
def main():

    # i like having a clean and empty terminal
    os.system('cls')

    # recieve input from the user to search the files
    inputFromUser = input("""









Input word to search file or type 'quitNow' to exit
>>> """)
    print()
    
    # a check to see if the user wishes to stop the program or continue
    if inputFromUser == "quitNow":    
        os.system('cls')
        exit()
    else:
        checkIfWordIsInFile(inputFromUser, fileOneList)
        main()



# function to check where the instances of the 'inputFromUser' appears
def checkIfWordIsInFile(userInput, fileList):
    wordLocations = []

    # simple loop going through every line in every file
    for primaryListNumber in range(len(listOfFileLists)):
        for secondaryListNumber in range(len(listOfFileLists[primaryListNumber])):
            # using 'if x in y:' so that if the word is within another word it adds it as a hit
            # so if the input word is 'con' the word 'economy' will still be returned
            # this also prevents adding multiple instances of the same line as a hit
            if userInput.casefold() in listOfFileLists[primaryListNumber][secondaryListNumber].casefold():
                wordLocations.append([primaryListNumber, secondaryListNumber])








    # if the list is not empty then the word was found
    if wordLocations != []:
        viewAllHits = input(f"""The word '{userInput}' was found {len(wordLocations)} times. Print all hits? y/n
>>> """)
        print()
        # gives the user the option of viewing where the word was found and what it says
        if viewAllHits == "y":
            print(f"""------------------------------------

'{userInput}' was found in these places:

------------------------------------""")
            for occurrences in wordLocations:
                print()
                print(f"""
File {occurrences[0]+1}, line {occurrences[1]+1} which says:
{listOfFileLists[occurrences[0]][occurrences[1]]}

------------------------------------""")
            input("""
Hit 'ENTER' to continue
""")


    else:
        print(f"'{userInput}' was not found anywhere in the file")

        input("""
Hit 'ENTER' to continue
""")






main()