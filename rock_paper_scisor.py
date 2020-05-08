from random import choices


class Game():
    
    def __init__(self,choice):
        self.choice = choice
        
    def play(self):
        computer = choices(['rock','paper','scissor'])
        
        if self.choice == 'rock' and computer == ['paper']:
            return f'{computer[0]}\nyou lose'
        elif self.choice == 'paper' and computer == ['scissor']:
            return f'{computer[0]}\nyou lose'
        elif self.choice == 'scissor' and computer == ['rock']:
            return f'{computer[0]}\nyou lose'
        elif self.choice == computer[0]:
            return f'{computer[0]}\nTie'
        else:
            return f'{computer[0]}\nyou win'
        

print("are you ready!!!!")

start = input('Type yes or no:  ')
if start == 'yes':
    player = input('what you chose  rock, paper, scissor: ')
    letsplay = Game(player)
    print(letsplay.play())
elif start == 'no':
    print('bye')
else:
    print('wrong choice')