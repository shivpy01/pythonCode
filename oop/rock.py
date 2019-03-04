import random

comp_choice = ['rock',"paper",'scissor']

my_choice = input("enter the yours\nrock\npaper\nscissor :  ")

class Comp():

    def __init__(self, comp_choice):
        self.comp_choice = random.choice(comp_choice)


    def __str__(self):
        return self.comp_choice


class Player():

    def __init__(self, my_choice):
        self.my_choice = my_choice

    def __str__(self):
        return self.my_choice

c = str(Player(my_choice))

co = str(Comp(comp_choice))

def play():
    if c == co:
        print(c+" "+" "+co+" Tied")
    elif ((c=='rock' and co =='paper')or(c =='paper' and co == 'scissor') or(c =='scissor' or co == 'rock')):
        print(c+" "+" "+co+" Win")
    else:
        print(c+" "+" "+co+" Lose")
play()
