print(Info := '\n1 - Left\n2 - Right\n3 - Up\n4 - Down\n5 - Up+Left\n6 - Up+Right\n7 - Down+Left\n8 - Down+Right\n')
Xfield = int(input('Set length of field: '))
Yfield = int(input('Set height of field: '))

from random import randint
import os

Repeats = 1; comment = ''; Player_score = 0
while Repeats == 1:
    field = '*' * (Xfield + 2) + '\n'
    field_elements = [' ',' ',' ',' ',' ',' ',' ',' ','X','X','*']
    
    if (Xfield <= 3 and Yfield >= 10) or (Xfield <= 3 and Yfield <= 3):
        field_elements = [' ','X','X','*','*']
        comment = "But it's unplayable field lmao"
        
    for iY in range(Yfield):
        field += '*'
        for iX in range(Xfield):
            field += field_elements[randint(0, len(field_elements) - 1)]
        field += '*\n'
    field += '*' * (Xfield + 2)
    
    gamedata = open('gamedata.txt', 'w')
    gamedata.write(field)
    gamedata.close()
    gamedata = open('gamedata.txt').readlines()                  # Field generation
#---------------------------------------------------------------------------------#
    maxStrcount = 0
    for iStr in range(1,len(gamedata) - 1):
        if ' ' in gamedata[iStr]:
            maxStrcount = max(maxStrcount, gamedata.count(gamedata[iStr]))
            print(maxStrcount)
        else: print(maxStrcount)
    print('\n')

    if (maxStrcount > 1) or (field.count(' ') == 0): Repeats = 1
    else: Repeats = 0
print('Generation successful!', comment, '\n')               # Re-generation system
#---------------------------------------------------------------------------------#
place_list = []
for iY2 in range(len(gamedata)):
    for iX2 in range(len(gamedata[iY2])):
        if gamedata[iY2][iX2] == ' ':
            place_list.append(str(iX2) + '-' + str(iY2))      # List of free pos'es
#---------------------------------------------------------------------------------#
Xpos = 0; Ypos = 0
Userpos = place_list[randint(0, len(place_list) - 1)]
place_list.remove(Userpos)

for i3 in range(len(Userpos)):
    if Userpos[i3] == '-':
        Xpos = int(Userpos[:i3])
        Ypos = int(Userpos[i3 + 1:])                          # Random player's pos
#---------------------------------------------------------------------------------#
Userstr = gamedata[Ypos]
UserstrNew = ''
str1 = Userstr[:Xpos]; str2 = Userstr[(Xpos + 1):]

field = field.replace(Userstr, str1 + 'O' + str2)
gamedataNew = open('gamedataNew.txt', 'w')
gamedataNew.write(field)
gamedataNew.close()                                          # Adding of the player
#---------------------------------------------------------------------------------#
Condition_of_win = int(((field.count('X') + field.count(' ') + field.count('*')) / ((Xfield + Yfield) / 2)) / 2)
counter = 0
while counter < Condition_of_win:

    Xpos_xp = 0; Ypos_xp = 0
    XP_pos = place_list[randint(0,len(place_list) - 1)]
    place_list.remove(XP_pos)
    
    for i3 in range(len(XP_pos)):
        if XP_pos[i3] == '-':
            Xpos_xp = int(XP_pos[:i3])
            Ypos_xp = int(XP_pos[i3 + 1:])                          # Random XP pos
#---------------------------------------------------------------------------------#
    gamedataNew = open('gamedataNew.txt').readlines()
    XP_str = gamedataNew[Ypos_xp]
    str1 = XP_str[:Xpos_xp]; str2 = XP_str[(Xpos_xp + 1):] 

    field = field.replace(XP_str,str1 + '1' + str2)
    gamedataNew = open('gamedataNew.txt', 'w')
    gamedataNew.write(field)
    gamedataNew.close()
    counter += 1

print(field)
field_without_player = field.replace('O', ' ')
gamedata = open('gamedata.txt', 'w')
gamedata.write(field_without_player)
gamedata.close()
gamedata = open('gamedata.txt').readlines()                             # XP adding
#---------------------------------------------------------------------------------#
HP = 1
while HP == 1:
    Move = int(input('Your move (1-8): '))                 # Condition of game life
#---------------------------------------------------------------------------------#  
    if (Move == 1) and (not('XO' in field)):
        gamedataNew = open('gamedataNew.txt').readlines()
        Xpos -= 1
        UserstrNew = gamedataNew[Ypos]
        str1 = UserstrNew[:Xpos]; str2 = UserstrNew[(Xpos + 1):]

        str1 = str1.replace('O', ' '); str2 = str2.replace('O', ' ')
        field = field.replace(UserstrNew,str1 + 'O' + str2)
        print(Info+'\n'+field)
        gamedataNew = open('gamedataNew.txt', 'w')
        gamedataNew.write(field)
        gamedataNew.close()
    elif Move == 1: print(Info + '\n' + field)              # (1) Leftward movement
#---------------------------------------------------------------------------------#
    if (Move == 2) and (not('OX' in field)):
        gamedataNew = open('gamedataNew.txt').readlines()
        Xpos += 1
        UserstrNew = gamedataNew[Ypos]
        str1 = UserstrNew[:Xpos]; str2 = UserstrNew[(Xpos + 1):]

        str1 = str1.replace('O', ' '); str2 = str2.replace('O', ' ')
        field = field.replace(UserstrNew, str1 + 'O' + str2)
        print(Info + '\n' + field)
        gamedataNew = open('gamedataNew.txt', 'w')
        gamedataNew.write(field)
        gamedataNew.close()
    elif Move == 2: print(Info + '\n' + field)            # (2) Rightward movenment
#---------------------------------------------------------------------------------#
    if (Move == 3) and (gamedata[Ypos - 1][Xpos] != 'X'):
        gamedataNew = open('gamedataNew.txt').readlines()
        Ypos -= 1
        UserstrNew = gamedataNew[Ypos]
        UserstrOld = gamedataNew[Ypos + 1]
        field = field.replace(UserstrOld, gamedata[Ypos + 1])
        str1 = UserstrNew[:Xpos]; str2 = UserstrNew[(Xpos + 1):]

        field = field.replace(UserstrNew, str1 + 'O' + str2)
        print(Info + '\n' + field)
        gamedataNew = open('gamedataNew.txt', 'w')
        gamedataNew.write(field)
        gamedataNew.close()
    elif Move == 3: print(Info + '\n' + field)               # (3) Upward movenment
#---------------------------------------------------------------------------------#
    if (Move == 4) and (gamedata[Ypos + 1][Xpos] != 'X'):
        gamedataNew = open('gamedataNew.txt').readlines()
        Ypos += 1
        UserstrNew = gamedataNew[Ypos]
        UserstrOld = gamedataNew[Ypos - 1]
        field = field.replace(UserstrOld, gamedata[Ypos - 1])
        str1 = UserstrNew[:Xpos]; str2 = UserstrNew[(Xpos + 1):]

        field = field.replace(UserstrNew, str1 + 'O' + str2)
        print(Info+'\n'+field)
        gamedataNew = open('gamedataNew.txt', 'w')
        gamedataNew.write(field)
        gamedataNew.close()
    elif Move == 4: print(Info + '\n' + field)             # (4) Downward movenment
#---------------------------------------------------------------------------------#
    if (Move == 5) and (gamedata[Ypos - 1][Xpos - 1] != 'X'):
        gamedataNew = open('gamedataNew.txt').readlines()
        Ypos -= 1
        Xpos -= 1
        UserstrNew = gamedataNew[Ypos]
        UserstrOld = gamedataNew[Ypos + 1]
        field = field.replace(UserstrOld, gamedata[Ypos + 1])
        str1 = UserstrNew[:Xpos]; str2 = UserstrNew[(Xpos + 1):]

        str1 = str1.replace('O', ' '); str2 = str2.replace('O', ' ')
        field = field.replace(UserstrNew, str1 + 'O' + str2)
        print(Info+'\n'+field)
        gamedataNew = open('gamedataNew.txt', 'w')
        gamedataNew.write(field)
        gamedataNew.close()
    elif Move == 5: print(Info + '\n' + field)            # (5) "Up+Left" movenment
#---------------------------------------------------------------------------------#
    if (Move == 6) and (gamedata[Ypos - 1][Xpos + 1] != 'X'):
        gamedataNew = open('gamedataNew.txt').readlines()
        Ypos -= 1
        Xpos += 1
        UserstrNew = gamedataNew[Ypos]
        UserstrOld = gamedataNew[Ypos + 1]
        field = field.replace(UserstrOld, gamedata[Ypos + 1])
        str1 = UserstrNew[:Xpos]; str2 = UserstrNew[(Xpos + 1):]

        str1 = str1.replace('O', ' '); str2 = str2.replace('O', ' ')
        field = field.replace(UserstrNew, str1 + 'O' + str2)
        print(Info + '\n' + field)
        gamedataNew = open('gamedataNew.txt', 'w')
        gamedataNew.write(field)
        gamedataNew.close()
    elif Move == 6: print(Info + '\n' + field)           # (6) "Up+Right" movenment
#---------------------------------------------------------------------------------#
    if (Move == 7) and (gamedata[Ypos + 1][Xpos - 1] != 'X'):
        gamedataNew = open('gamedataNew.txt').readlines()
        Ypos += 1
        Xpos -= 1
        UserstrNew = gamedataNew[Ypos]
        UserstrOld = gamedataNew[Ypos - 1]
        field = field.replace(UserstrOld, gamedata[Ypos - 1])
        str1 = UserstrNew[:Xpos]; str2 = UserstrNew[(Xpos + 1):]

        str1 = str1.replace('O', ' '); str2 = str2.replace('O', ' ')
        field = field.replace(UserstrNew, str1 + 'O' + str2)
        print(Info + '\n' + field)
        gamedataNew = open('gamedataNew.txt', 'w')
        gamedataNew.write(field)
        gamedataNew.close()
    elif Move == 7: print(Info + '\n' + field)          # (7) "Down+Left" movenment
#---------------------------------------------------------------------------------#
    if (Move == 8) and (gamedata[Ypos + 1][Xpos + 1] != 'X'):
        gamedataNew = open('gamedataNew.txt').readlines()
        Ypos += 1
        Xpos += 1
        UserstrNew = gamedataNew[Ypos]
        UserstrOld = gamedataNew[Ypos - 1]
        field = field.replace(UserstrOld, gamedata[Ypos - 1])
        str1 = UserstrNew[:Xpos]; str2 = UserstrNew[(Xpos + 1):]

        str1 = str1.replace('O', ' '); str2 = str2.replace('O', ' ')
        field = field.replace(UserstrNew, str1 + 'O' + str2)
        print(Info + '\n' + field)
        gamedataNew = open('gamedataNew.txt', 'w')
        gamedataNew.write(field)
        gamedataNew.close()
    elif Move == 8: print(Info + '\n' + field)         # (8) "Down+Right" movenment
#---------------------------------------------------------------------------------#
    if open('gamedata.txt').readlines()[Ypos][Xpos] == '1' and open('gamedataNew.txt').readlines()[Ypos][Xpos] == 'O':
        Player_score += 1
        field_new = field.replace('O', ' ')
        gamedata = open('gamedata.txt', 'w')
        gamedata.write(field_new)
        gamedata.close()
        gamedata = open('gamedata.txt').readlines()               # XP-up condition
#---------------------------------------------------------------------------------#
    if (Move > 8) or (Move < 1):
        print('\nHaha.. no')
        os.remove('gamedata.txt')
        os.remove('gamedataNew.txt')
        break

    if ((open('gamedata.txt').readlines()[Ypos][Xpos] == '*') and (open('gamedataNew.txt').readlines()[Ypos][Xpos] == 'O')) or (open('gamedataNew.txt').readlines()[0].count('O') > 0) or (open('gamedataNew.txt').readlines()[Yfield + 1].count('O') > 0):
        HP = 0
        print('\nGame Over', 'Your HP = 0', 'Your score = ' + str(Player_score), sep = '\n')
        os.remove('gamedata.txt')
        os.remove('gamedataNew.txt')

    if Player_score == Condition_of_win:
        print('\nVictory!\n' + 'Your score = ' + str(Player_score))
        os.remove('gamedata.txt')
        os.remove('gamedataNew.txt')
        break                                             # Condition of game break
#---------------------------------------------------------------------------------#     by RezerdPrime
