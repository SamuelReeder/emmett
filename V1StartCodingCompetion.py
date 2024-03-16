from states import General, Village, Governor, WealthyMerchant, RandomPersonOffTheStreet, ReligiousFigure

## After selecting play this section should be activated affecting starting variables throughout the game
#

## Determine Player Age
# Ask the player for an integer age greater than 18 and chastises them for making incorrect selections before asking the player again. This age is then assigned to a general catogory for simplicity.

print()

while True:
    try:
        age = int(input("How many seasons have you weathered? "))
        if age < 18:
            print()
            print("They do not allow just anyone to become emperor. Please choose an age greater than 18.")
            print()
        else:
            break  # Exit the loop if the input is valid
    except ValueError:
        print()
        print("Adults count their age in integer numbers, Act your age!")
        print()
        

if age <= 27:
    genAge = "young"
    illchance = 0.005
    playerWealth = 50
elif 27 < age <= 47:
    genAge = "mature"
    illChance = 0.01
    playerWealth = 150
elif 47 < age:
    genAge = "wise"
    illChance = 0.09
    playerWealth = 450
    deathChance = 0.0001

## Determine PLayer Name
# Ask the player what they would like to be called while ensuring it is less than 12 character for formatting purposes.

print()
name = str(input(f"Greetings {genAge} Augustus, What shall you be called? "))

while len(name) > 12:
    print()
    print("Your courtiers will pass out from exhaustion if your name is greater than 8 characters, please choose a shorter name for the good of your people.")
    print()
    name = str(input(f"Greetings {genAge} Augustus, What shall you be called? "))

## Determine Background
# Ask the player which background they would like to select, assign buffs and debuffs accordingly.


class Game:
    
    self.dict = {
        '1': General(),
        '2': "none ",
        '3': 'Governor',
        '4': 'Wealthy Merchant',
        '5': 'Random person off of the street',
        '6': 'Religious Figure'
    }
    
    def __init__(self) -> None:
        # init player 
        self.player = Player()
        self.sure = False


    def sure(self) -> bool:
        choice = input("Are your sure? (Yes/No) ")
        self.sure = lower(choice) == 'yes'
        return self.sure
    
    def setup(self) -> None:
        while True:
            try:
                age = int(input("How many seasons have you weathered? "))
                if age < 18:
                    print()
                    print("They do not allow just anyone to become emperor. Please choose an age greater than 18.")
                    print()
                else:
                    break  # Exit the loop if the input is valid
            except ValueError:
                print()
                print("Adults count their age in integer numbers, Act your age!")
                print()
                

        if age <= 27:
            genAge = "young"
            illchance = 0.005
            playerWealth = 50
        elif 27 < age <= 47:
            genAge = "mature"
            illChance = 0.01
            playerWealth = 150
        elif 47 < age:
            genAge = "wise"
            illChance = 0.09
            playerWealth = 450
            deathChance = 0.0001

        ## Determine PLayer Name
        # Ask the player what they would like to be called while ensuring it is less than 12 character for formatting purposes.

        print()
        name = str(input(f"Greetings {genAge} Augustus, What shall you be called? "))

        while len(name) > 12:
            print()
            print("Your courtiers will pass out from exhaustion if your name is greater than 8 characters, please choose a shorter name for the good of your people.")
            print()
            name = str(input(f"Greetings {genAge} Augustus, What shall you be called? "))

        
    def run(self) -> None:
        while True:
            print()
            print("There are many ways to grow up in the empire of Rome.")
            print("You can live as: 1. General, 2. Wealthy Senator, 3. Governor, 4. Wealthy Merchant, 5. Random person off of the street, 6. Religious Figure.")
            background = input(f"How did you grow up {genAge} {name}? ")
            
            if not self.dict[background].run(self.player): break
            
            
            match background:
                case '1':
                    
                    self.sure = self.dict['1'].run(self.player)
                    if self.sure == True: continue
                    
                case '2':
                    lifePath = "Wealthy Senator"
                    print()
                    print(lifePath)
                    print("Difficulty: Easy")
                    print()
                    print(f"A life spent maneuvering the politics of the capital have provided you with the following perks {lifePath} {name}.")
                    print("The Senate is glad to have one of their own ruling the empire.")
                    senateOpinion = 75
                    print("The Army is reluctant to follow the orders of a career politician.")
                    armyOpinion = 25
                    print("Administering the empire comes easier to you.")
                    provinceActionModifier = 0.80
                    print("You have a large fortune at your disposal.")
                    playerWealth = playerWealth + 250
                    print()
                    choice = input("Are your self.sure? (Yes/No) ")
                    if choice == 'Yes' or 'yes':
                        self.sure = True
                    else :
                        self.sure = False
                case '3':
                    lifePath = "Governor"
                    print()
                    print(lifePath)
                    print("Difficulty: Easy")
                    print()
                    print(f"A life spent managing the provinces of the empire have left you well equipped to rule {lifePath} {name}.")
                    print("The Citizenry and Senate trust you to rule fairly.")
                    citizenOpinion = 75
                    senateOpinion = 75
                    print("Having foiled the attempts of Barbarian raiders they seek their chance to strike against you.")
                    barbarianOpinion = 25
                    print("Administering the empire comes easier to you.")
                    provinceActionModifier = 0.80
                    print()
                    choice = input("Are your self.sure? (Yes/No) ")
                    if choice == 'Yes' or 'yes':
                        self.sure = True
                    else :
                        self.sure = False
                case '4':
                    lifePath = "Wealthy Merchant"
                    print()
                    print(lifePath)
                    print("Difficulty: Medium")
                    print()
                    print(f"You have spent your years traveling the empire haggling and selling your wares, {lifePath} {name}.")
                    print("Both the Army and Senate view your rule as illegitimate.")
                    armyOpinion = 25
                    senateOpinion = 25
                    print("Your fair business dealings have endeared the Citizenry and Barbarians to your cause.")
                    citizenOpinion = 75
                    barbarianOpinion = 75
                    print("You have a large fortune at your disposal.")
                    playerWealth = playerWealth + 250
                    print()
                    choice = input("Are your self.sure? (Yes/No) ")
                    if choice == 'Yes' or 'yes':
                        self.sure = True
                    else :
                        self.sure = False
                case '5':
                    lifePath = "Random Guy off of the Street"
                    print()
                    print(lifePath)
                    print("Difficulty: Impossible")
                    print()
                    print(f"You don't really know how you got here, you just wandered into a big building and put a purple toga on.")
                    print("Everyone hates you for some reason, what did you even do?")
                    armyOpinion = 25
                    senateOpinion = 25
                    citizenOpinion = 25
                    eliteOpinion = 25
                    barbarianOpinion = 25
                    sassanidOpinion = 25
                    preatorianOpinion = 25
                    christianOpinion = 25
                    paganOpinion = 25
                    print("You are broke, at least the new robe is comfy even if the building you are squating in is quite drafty.")
                    playerWealth = 0
                    print()
                    choice = input("Are your self.sure? (Yes/No) ")
                    if choice == 'Yes' or 'yes':
                        self.sure = True
                    else :
                        self.sure = False
                case '6':
                    lifePath = "Religious Figure"
                    print()
                    print(lifePath)
                    print("Difficulty: Medium")
                    print()
                    print(f"You have rode a wave of religious fervor into the palace, the question is who elevated you {name}.")
                    endorsement = int(input("Was it the Pagans or Christians who brought you to power? (1 or 2) "))
                    while not (1 <= endorsement <= 2):
                        endorsement = int(input("Was it the Pagans or Christians who brought you to power? (1 or 2) "))
                    if endorsement == 1:
                        print("Your were lifted into power by the followers of Paganism")
                        religion = "Pagan"
                        christianOpinion = 25
                        paganOpinion = 75
                    elif endorsement == 2:
                        print("Your were lifted into power by the followers of Christianity")
                        religion = "Christian"
                        christianOpinion = 75
                        paganOpinion = 25
                    print(endorsement)
                    print("You often recieve personal donations from followers.")
                    #monthlyIncome = monthlyIncome + 25 # This currently does not work because the world variable does not exist
                    print("The Army and Senate believe that the church and state should remain seperate.")
                    armyOpinion = 25
                    senateOpinion = 25
                    print()
                    choice = input("Are your self.sure? (Yes/No) ")
                    if choice == 'Yes' or 'yes':
                        self.sure = True
                    else :
                        self.sure = False
                case _:
                    self.sure = False

## Give player some background information before bringing them to the main play area
#


# any code to be run for every state goes in here alongisde variables
class State:
    
    def __init__(self) -> None:
        pass
    
    def run(self, player: Player) -> bool:
        choice = input("Are your sure? (Yes/No) ")
        return lower(choice) == 'yes'
    

# create subclasses for each state and have specific code in run function 
class General(State):
    
    def __init__(self) -> None:
        pass
    
    def run(self, player: Player) -> bool:
        
        
        player.lifePath = "General"
        print()
        print(player.lifePath)
        print("Difficulty: Easy")
        print()
        print(f"A life spent in the army has provided you with the following perks {lifePath} {name}.")
        print("The Army is glad to have one of their own ruling the empire.")
        player.armyOpinion = 75
        print("Increased Likelihood of Success for Military Actions.")
        player.armyActionModifier = 1.20
        print("The Senate does not approve of Military leaders ruling the empire.")
        player.senateOpinion = 25
        print()
        return super().run(player)

class Player:
    
    # init variables
    def __init__(self) -> None:
        self.balance = 1000
        self.lifePath = "General"
        self.armyOpinion = 75
        self.senateOpinion = 25
        self.armyActionModifier = 1.20
        self.senateActionModifier = 0.80
        self.citizenOpinion = 50
        self.barbarianOpinion = 50
        self.eliteOpinion = 50
        self.sassanidOpinion = 50
        self.praetorianOpinion = 50
        self.christianOpinion = 50
        self.paganOpinion = 50
        self.monthlyIncome = 0
        self.playerWealth = playerWealth
        self.illChance = illChance
        self.deathChance = deathChance
        self.sure = False
    
    
    
print("The year is 235 A.D. and the young Emperor Severus Alexander has just been assasinated by his own legions enveloping the empire in chaos for the next half century. Within coming century the Empire would see a total of 24 emperors don the purple. ")
print("Your goal as the newest emperor is to survive as long as you can muster, Whether for the glory of Rome, personal wealth or you own dynasty. This world is brutish and short, even on top of the largest empire ever seen by mankind. You will die and die often")
print(f"It is now your turn to don the purple {genAge} Augustus {name}")


game = Game()
game.setup()
game.run()