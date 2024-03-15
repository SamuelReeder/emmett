# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Emmett Wruk
# Student CCID: wruk
# Others:
#
# To avoid plagiarism, list the names of persons, Version 0 author(s)
# excluded, whose code, words, ideas, or data you used. To avoid
# cheating, list the names of persons, excluding the ENCMP 100 lab
# instructor and TAs, who gave you compositional assistance.
#
# After each name, including your own name, enter in parentheses an
# estimate of the person's contributions in percent. Without these
# numbers, adding to 100%, follow-up questions may be asked.
#
# For anonymous sources, enter pseudonyms in uppercase, e.g., SAURON,
# followed by percentages as above. Email a link to or a copy of the
# source to the lab instructor before the assignment is due.
#
import matplotlib.pyplot as plt
import numpy as np

print('Version 1')
# ------------Students edit/write their code below here--------------------------
# ------------Remove any code that is unnecessary--------------------------

iDeposit = 2000
mDeposit = 200
aInterest = 0.0625
mInterest = aInterest/12
years = 18
months = years*12
tuition = [5550, 6150, 6550] # Arts, Science, Engineering
avgTuitionIncrease = 0.07

savingsAccount = []
savingsAccount.append(iDeposit)
lifeSavings = []

## Saving Calculation
# The following section calculates the interest on the savings account every year until a specified year is met, at which point the savings is formatted and recorded. 

for index in range(1, months):
    accountBalance = savingsAccount[index-1] + (savingsAccount[index-1]*mInterest) + mDeposit
    savingsAccount.append(accountBalance)
    
savingsAccount = np.array(savingsAccount)
finalBalance = savingsAccount[-1]

## Tuition Calculation
# The following section adjusts the tuition cost, then calculates the yearly inflation, adjusting the tuition cost and then when the years specified are active adds together the tuition for the specified program

for program in tuition:
    adjustedTuition = program
    totalTuition = 0
    for index2 in range(1,23):
        newTuition = adjustedTuition + (adjustedTuition*avgTuitionIncrease)
        adjustedTuition = newTuition
        if index2 >= 18 and index2 <= 21:
            totalTuition += adjustedTuition
    lifeSavings.append(totalTuition)

lifeSavings = np.array(lifeSavings)

print(f"The savings amount is ${finalBalance:.2f}")
print(f"The cost of the arts program is ${lifeSavings[0]:.2f}")
print(f"The cost of the science program is ${lifeSavings[1]:.2f}")
print(f"The cost of the engg program is ${lifeSavings[2]:.2f}")

## PLot
# The following section creates labels, creates a curve for the annual savings, creates a plot, then creates the lines for tuition cost and then formats the graph accordingly and then displays the graph

labels = ["Arts", "Science", "Engineering"]
colors = ["orange", "green", "red"]
years = np.arange(0,19)

annualSavings = np.insert(savingsAccount[11::12], 0, iDeposit)

plt.plot(years, annualSavings, label="Saving Balance")

for index3 in range(len(lifeSavings)):
    plt.hlines(lifeSavings[index3], 0, 18, colors[index3], label=labels[index3])

plt.title("Savings vs Tuition")
plt.xlabel("Years")
xTicks = np.arange(0,19,1)
plt.xticks(ticks=xTicks)
plt.ylabel("Amount $")
plt.legend(loc = 'lower right')
plt.margins(x=0)
plt.ylim(0,100000)
plt.show()

## Version 2 Begins
#
while True:

    program = input("Enter a program 1.Arts, 2.Science, 3.Engineering : ")

    match program:

        case '1':
            iProgramCost = tuition[0]
            fProgramCost = lifeSavings[0]
            selection = 'arts'

        case '2':
            iProgramCost = tuition[1]
            fProgramCost = lifeSavings[1]
            selection = 'science'

        case '3':
            iProgramCost = tuition[2]
            fProgramCost = lifeSavings[2]
            selection = 'engineering'

        case _:
            iProgramCost = False
            print("Dumbass there are only 3 options, you ain't goin' to no university with reading comprehension like that.")
            continue
    
    match finalBalance:

        case yes if finalBalance >= fProgramCost:
            print("Congratulation!!! You have saved enough for the", selection, "program")

        case no if finalBalance <= fProgramCost:
            print("Unfortunately!!! You do not have enough saved for the", selection, "program")
    
    incrementalDeposit = 0
    incrementalAccountBalance = 2000
    iMDeposit = 1
    while incrementalAccountBalance < fProgramCost:
        for index4 in range(1, months):
            incrementalAccountBalance = incrementalAccountBalance + (incrementalAccountBalance*mInterest) + iMDeposit
            if incrementalAccountBalance < fProgramCost:
                iMDeposit = iMDeposit + 1
            elif incrementalAccountBalance > fProgramCost:
                print(f"The optimal monthly contribution amount is ${iMDeposit}:.f")
        break
    break