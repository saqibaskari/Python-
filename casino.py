import random

money = 1000
continuegame = True
print("Welcone ! !")

print("You have " + str(money) + "$. Good Luck !")
print("_____________________________________")
rnd_no = random.randint(0, 49)
while continuegame:

    bet_num = int(input("On which number you want to bet"))
    bet_amt = int(input("How much do you want to bet on this number "))

    if bet_num == rnd_no:
        money += bet_amt
    elif bet_num != rnd_no:
         money = money - bet_amt
    print("The output number is " + str(rnd_no ))
    print("Sorry but you lost, try again !")
    print("you are now left with " + str(money) +" $")
    if money <= 0:
        continuegame = False
        print("You are left with no money")
        print("---------------------------")
