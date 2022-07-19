import random
import sys
import getopt,sys

#=====================================================#
#   Quiet mode, just show the number
#   Roll without the preceeding number? -r 1d20
#=====================================================#

full_cmd_arguments = sys.argv
arguments_list = full_cmd_arguments[1:]

helpInfo = "Args:\n -h -- help\n -r -- roll\n  -r (number of dice)d(type of dice)\n\nExamples:\n -r 1d20\n  (1 = number of dice)\n  (d = what sided dice to roll)"

def rollDice(numDie, dieType):

    print("Rolling " + str(numDie) + "d" + str(dieType))

    rolledDice = []
    rolls=0
    while rolls<numDie:
        if dieType == 0:
            Roll = 0
        else:
            Roll = random.randint(1,dieType)
        rolledDice.append(Roll)
        rolls+=1

    rollTotal = 0
    if rolls>1:
        for i in rolledDice:
            rollTotal+=i
    elif rolls == 1:
        rollTotal = Roll
    elif rolls == 0:
        print("Nothing was rolled")
    else:
        print("Error when counting rolls")

    if rollTotal!=0: print(rolledDice)
    print("Total: " + str(rollTotal))

    return rollTotal

def main(argv):
    short_options = "hr:"
    long_options = ["help","roll"]
    try:
        arguments, values = getopt.getopt(arguments_list, short_options, long_options)
    except getopt.error as err:
        print(str(err))
        sys.exit(2)
    for current_argument, current_value in arguments:
        if current_argument in ("-h","--help"):
            print(helpInfo)
            sys.exit(2)
        elif current_argument in ("-r", "--roll"):
            try:
                rollVal = current_value
            except:
                print("Error with input")
                sys.exit(2)

    for i in range(len(rollVal)):
        rolled = rollVal.split('d')

    for i in rolled:
        try:
            int(i)
        except:
            print("Invalid input, try -h or --help for examples of valid input")
            exit(2)
    if len(rolled)==2:
        numberOfDice = int(rolled[0])
        typeOfDice = int(rolled[1])
        rollDice(numberOfDice,typeOfDice)
    elif len(rolled)<2 or len(rolled)>2:
        print("Invalid input, try -h or --help for examples of valid input")
        exit(2)

if __name__ == '__main__':
    main(sys.argv[1:])
