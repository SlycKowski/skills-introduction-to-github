import random
import math
houseChoice = 0
rng = 0
aisleChoice = 0
decision = 0
money = 10
smarts = 0
food = 5
happiness = 5
job = False
resourceMult = 1
prisonChoice = 0
days = 0
moneyEarned = 0
taxDay = 0
taxes = 0
print("You are in a supermarket in California and need to get a house!")
while True:
    days += 1
    tax = math.ceil(moneyEarned * 0.25)
    if days % 6 == 0:
        print(f"Tomorrow is a tax day. You will have to pay {tax} as tax.")
    elif days % 7 == 0:
        money -= tax
        print(f"You paid the IRS {tax} dollars in taxes.")
        tax = 0
        moneyEarned = 0
    print(f"You have {money} money, {food} food and {happiness} happiness. You have {80 + smarts} iq. "
          f"It has been {days} days since your redemption arc and owe the IRS {tax}")
    if happiness <= 0:
        print("You died of depression.")
        break

    if food <= 0:
        print("You died of hungry")
        break
    if money <= 0:
        print("You died of poor")
        break

    decision = input(" What do you do?\n Type Help for Options\n")
    decision = decision.lower()

    if decision == "help":
        print("\nOptions: \n Work, Buy food\n Steal food, Study\n Steal money, Get job\n Buy tent, Buy house\n"
              " Sleep, Therapy")
    if decision == "work":
        if job:
            money += 8 * resourceMult
            moneyEarned += 8 * resourceMult
            food -= 2
            print("Worked at your job for money")
        else:
            money += 4 * resourceMult
            moneyEarned += 4 * resourceMult
            food -= 2
            print("Did some side gigs for money")
    if decision == "buy food":
        if money >= 4:
            money -= 4
            food += 4 * resourceMult
            print("Bought and ate some food")
        else:
            happiness -= 1
            print("Not enough money. You took some emotional damage!")
    if decision == "steal food":
        aisleChoice = input("Would you like to steal from the candy, bread, or meat aisle?")
        aisleChoice = aisleChoice.lower()
        if aisleChoice == "candy":
            rng = random.randint(1, 10)
            if rng + smarts >= 5:
                food += 2 * resourceMult
                print("You stole some food you big back")
            else:
                prisonChoice = input("You got caught! Prison or fine? \n")
                prisonChoice = prisonChoice.lower()
                if prisonChoice == "prison":
                    happiness -= 8
                    print("You went to prison for 30 seconds. You cried so bad you took 8 emotional damage!")
                elif prisonChoice == "fine":
                    if money >= 8:
                        money -= 8
                        print("You got slapped with a hefty fine and left!")
                    else:
                        happiness -= 10
                        print("You realized you didn't have enough money. You took 10 emotional damage!")
        elif aisleChoice == "bread":
            rng = random.randint(1, 20)
            if rng + smarts >= 15:
                food += 6 * resourceMult
                print("You stole some food you big back")
            else:
                prisonChoice = input("You got caught! Prison or fine? \n")
                prisonChoice = prisonChoice.lower()
                if prisonChoice == "prison":
                    happiness -= 8
                    print("You went to prison for 30 seconds. You cried so bad you took 8 emotional damage!")
                elif prisonChoice == "fine":
                    if money >= 8:
                        money -= 8
                        print("You got slapped with a hefty fine and left!")
                    else:
                        happiness -= 10
                        print("You realized you didn't have enough money. You took 10 emotional damage!")
        elif aisleChoice == "meat":
            rng = random.randint(1, 40)
            if rng + smarts >= 35:
                food += 10 * resourceMult
                print("You stole some food you big back")
            else:
                prisonChoice = input("You got caught! Prison or fine? \n")
                prisonChoice = prisonChoice.lower()
                if prisonChoice == "prison":
                    happiness -= 8
                    print("You went to prison for 30 seconds. You cried so bad you took 8 emotional damage!")
                elif prisonChoice == "fine":
                    if money >= 8:
                        money -= 8
                        print("You got slapped with a hefty fine and left!")
                    else:
                        happiness -= 10
                        print("You realized you didn't have enough money. You took 10 emotional damage!")
        else:
            print("You got confused and stared at the ceiling for the rest of the day.")

    if decision == "study":
        happiness -= 1
        food -= 1
        smarts += 2 * resourceMult
        print("You studied for a while.")

    if decision == "steal money":
        rng = random.randint(1, 40)
        if rng + smarts >= 35:
            money += 16 * resourceMult
            moneyEarned += 16 * resourceMult
            print("You stole some money you criminal. You take 2 emotional damage from stealing")
            happiness -= 2
        else:
            prisonChoice = input("You got caught! Prison or fine? \n")
            prisonChoice = prisonChoice.lower()
            if prisonChoice == "prison":
                happiness -= 8
                print("You went to prison for 30 seconds. You cried so bad you took 8 emotional damage!")
            elif prisonChoice == "fine":
                if money >= 8:
                    money -= 8
                    print("You got slapped with a hefty fine and left!")
                else:
                    happiness -= 10
                    print("You realized you didn't have enough money. You took 10 emotional damage!")

    if decision == "get job":
        rng = random.randint(1, 20)
        if rng + smarts >= 20:
            job = True
            print("You got the job!")
        else:
            happiness -= 8
            print("You did not get the job. You took 8 emotional damage!")
    if decision == "buy tent":
        if money >= 300:
            print("Bought a tent! This multiplies your earnings since you have an actual living space.")
            resourceMult = 3
            money -= 300
        else:
            print(f"Not enough money! You realized you need {300 - money} more money and took 2 emotional damage!")
            happiness -= 2

    if decision == "buy house":
        if money >= 1000:
            print("Congratulations! You bought house!")
            break
        else:
            print("you don't even have enough money. You took 2 emotional damage!")
    if decision == "sleep":
        happiness += 2
        food -= 1
        money -= 1
        print("You slept")
    if decision == "therapy":
        if money >= 4:
            happiness += 6
            print("You seeked therapy! You only have to pay 4 dollars thanks to your health insurance!")
        else:
            happiness -= 1
            print("You are so poor that even with insurance you could not get therapy. You took 1 emotional damage!")
    if decision == "insurance fraud":
        rng = random.randint(1, 6)
        if rng + smarts >= 3:
            money += 8 * resourceMult
            moneyEarned += 8 * resourceMult
            print("You got hit by a car and got 8 dollars with barely a scratch!")
        else:
            print("You got hit by a car so bad you died!")
            break
