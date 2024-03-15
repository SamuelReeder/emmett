from person import Person
import numpy as np
import matplotlib.pyplot as plt


iDeposit = 2000
mDeposit = 200
aInterest = 0.0625
mInterest = aInterest/12
years = 18
months = years*12
tuition = [5550, 6150, 6550] # Arts, Science, Engineering
avgTuitionIncrease = 0.07


class Main:

    def __init__(self, players):
        self.person = Person("name", iDeposit)
        
        
    def calculate_interest(self) -> None:
        for index in range(1, months):
            accountBalance = self.person.savingsAccount[index-1] + (self.person.savingsAccount[index-1]*mInterest) + mDeposit
            self.person.savingsAccount.append(accountBalance)
            
        self.person.lifeSavings = np.array(self.person.lifeSavings)
        self.person.finalBalance = self.person.savingsAccount[-1]
        
        
    def calculate_tuition(self) -> None:
        for program in tuition:
            adjustedTuition = program
            totalTuition = 0
            for index2 in range(1,23):
                newTuition = adjustedTuition + (adjustedTuition*avgTuitionIncrease)
                adjustedTuition = newTuition
                if index2 >= 18 and index2 <= 21:
                    totalTuition += adjustedTuition
            self.person.lifeSavings.append(totalTuition)
        
        self.person.lifeSavings = np.array(self.person.lifeSavings)


    def display(self) -> None:
        print(f"The savings amount is ${self.person.finalBalance:.2f}")
        print(f"The cost of the arts program is ${self.person.lifeSavings[0]:.2f}")
        print(f"The cost of the science program is ${self.person.lifeSavings[1]:.2f}")
        print(f"The cost of the engg program is ${self.person.lifeSavings[2]:.2f}")
        
        
    def plot(self) -> None:
        ## PLot
        # The following section creates labels, creates a curve for the annual savings, creates a plot, then creates the lines for tuition cost and then formats the graph accordingly and then displays the graph

        labels = ["Arts", "Science", "Engineering"]
        colors = ["orange", "green", "red"]
        years = np.arange(0,19)

        annualSavings = np.insert(self.person.savingsAccount[11::12], 0, iDeposit)

        plt.plot(years, annualSavings, label="Saving Balance")

        for index3 in range(len(lifeSavings)):
            plt.hlines(self.person.lifeSavings[index3], 0, 18, colors[index3], label=labels[index3])

        plt.title("Savings vs Tuition")
        plt.xlabel("Years")
        xTicks = np.arange(0,19,1)
        plt.xticks(ticks=xTicks)
        plt.ylabel("Amount $")
        plt.legend(loc = 'lower right')
        plt.margins(x=0)
        plt.ylim(0,100000)
        plt.show()
        
    
    def run(self) -> None:
        self.calculate_interest()
        self.calculate_tuition()
        self.display()
        self.plot()
        
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
        
        finalBalance = self.person.finalBalance
        
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
                
            