from random import shuffle

def make_shuffle(list1):
    shuffle(list1)
    return list1

def player():
    guess=''
    while guess  not in ['0','1','2']:
        guess=input('0 or 1 or 2 ? ')
    return int(guess)

def check_guess(list,guess):
    
    if list[guess]=='O':
        t=True
        print("you find it !")
        print(game_list)    
    else:
      
       print("bad luck :( ")
       print(game_list)
       
game_list=['X','X','O']
shuffle=make_shuffle(game_list)
player_guess = player()
check_guess(shuffle,player_guess)
