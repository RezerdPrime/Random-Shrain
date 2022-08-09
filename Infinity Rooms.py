from random import randint
import os

print(Info := '\n1 - Left\n2 - Right\n3 - Up\n4 - Down\n5 - Up+Left\n6 - Up+Right\n7 - Down+Left\n8 - Down+Right\n')
field_sizes = [5, 7, 9, 11]

Repeats = 1
while Repeats == 1:
    XYfield = field_sizes[randint(0, len(field_sizes) - 1)]
    field = last_string = '*' * int((XYfield - 1)/2 + 1) + 'H' + '*' * int((XYfield - 1)/2 + 1) + '\n'
    field_elements = [' ',' ',' ',' ',' ',' ',' ',' ','X','X','*']

    for iY in range(XYfield):
        field += '*'
        for iX in range(XYfield):
            field += field_elements[randint(0, len(field_elements) - 1)]
        field += '*\n'
    field += last_string
    
    gamedata = open('gamedata.txt','w')
    gamedata.write(field)
    gamedata.close()
    gamedata = open('gamedata.txt').readlines()
    
    middle_str_old = gamedata[int((XYfield + 1)/2)]
    middle_str_new = 'H' + middle_str_old[1:][:-2] + 'H\n'
    field = field.replace(middle_str_old, middle_str_new)

    gamedata = open('gamedata.txt','w')
    gamedata.write(field)
    gamedata.close()
    gamedata = open('gamedata.txt').readlines()                  # Field generation
#---------------------------------------------------------------------------------#
    maxStrcount = 0
    for iStr in range(1, len(gamedata) - 1):
        if ' ' in gamedata[iStr]:
            maxStrcount = max(maxStrcount, gamedata.count(gamedata[iStr]))
            print(maxStrcount)
        else: print(maxStrcount)
    print('\n')

    if maxStrcount > 1: Repeats = 1
    else: Repeats = 0
print('Generation successful!\n')                            # Re-generation system
#---------------------------------------------------------------------------------#
place_list = []
for iY2 in range(len(gamedata)):
    for iX2 in range(len(gamedata[iY2])):
        if gamedata[iY2][iX2] == ' ':
            place_list.append(str(iX2) + '-' + str(iY2))      # List of free pos'es
#---------------------------------------------------------------------------------#
Xpos = 0; Ypos = 0
Userpos = place_list[randint(0, len(place_list) - 1)]

for i3 in range(len(Userpos)):
    if Userpos[i3] == '-':
        Xpos = int(Userpos[:i3])
        Ypos = int(Userpos[i3 + 1:])                          # Random player's pos
#---------------------------------------------------------------------------------#
Userstr = gamedata[Ypos]
UserstrNew = ''
str1 = Userstr[:Xpos]; str2 = Userstr[(Xpos + 1):]

field = field.replace(Userstr, str1 + 'O' + str2)
gamedataNew = open('gamedataNew.txt','w')
gamedataNew.write(field)
gamedataNew.close()
print(field)                                                 # Adding of the player
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
        field = field.replace(UserstrNew, str1 + 'O' + str2)
        print(Info + '\n' + field)
        
        gamedataNew = open('gamedataNew.txt','w')
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
        
        gamedataNew = open('gamedataNew.txt','w')
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
        
        gamedataNew = open('gamedataNew.txt','w')
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

        field = field.replace(UserstrNew,str1 + 'O' + str2)
        print(Info + '\n' + field)
        
        gamedataNew = open('gamedataNew.txt','w')
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
        print(Info + '\n' + field)
        
        gamedataNew = open('gamedataNew.txt','w')
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
        
        gamedataNew = open('gamedataNew.txt','w')
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
        
        gamedataNew = open('gamedataNew.txt','w')
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
        
        gamedataNew = open('gamedataNew.txt','w')
        gamedataNew.write(field)
        gamedataNew.close()
    elif Move == 8: print(Info + '\n' + field)         # (8) "Down+Right" movenment
#---------------------------------------------------------------------------------#
    if (Move > 8) or (Move < 1):
        print('\nHaha.. no')
        os.remove('gamedata.txt')
        os.remove('gamedataNew.txt')
        break

    spike_str = open('gamedataNew.txt').readlines()
    if ((open('gamedata.txt').readlines()[Ypos][Xpos] == '*') and (open('gamedataNew.txt').readlines()[Ypos][Xpos] == 'O')) or (spike_str[0][:int((XYfield + 1)/2)].count('O') > 0) or (spike_str[-1][:int((XYfield + 1)/2)].count('O') > 0) or (spike_str[0][int((XYfield + 3)/2):].count('O') > 0) or (spike_str[-1][int((XYfield + 3)/2):].count('O') > 0):
        HP = 0
        print('\nGame Over\nYour HP = 0')
        os.remove('gamedata.txt')
        os.remove('gamedataNew.txt')
        break                                             # Condition of game break
#---------------------------------------------------------------------------------#
    if (open('gamedata.txt').readlines()[Ypos][Xpos] == 'H') and (open('gamedataNew.txt').readlines()[Ypos][Xpos] == 'O'):
        Repeats = 1
        while Repeats == 1:
            field = last_string = '*' * int((XYfield - 1)/2 + 1) + 'H' + '*' * int((XYfield - 1)/2 + 1) + '\n'

            for iY in range(XYfield):
                field += '*'
                for iX in range(XYfield):
                    field += field_elements[randint(0, len(field_elements) - 1)]
                field += '*\n'
            field += last_string
            
            gamedata = open('gamedata.txt','w')
            gamedata.write(field)
            gamedata.close()
            gamedata = open('gamedata.txt').readlines()
    
            middle_str_old = gamedata[int((XYfield + 1)/2)]
            middle_str_new = 'H' + middle_str_old[1:][:-2] + 'H\n'
            field = field.replace(middle_str_old, middle_str_new)

            gamedata = open('gamedata.txt','w')
            gamedata.write(field)
            gamedata.close()
            gamedata = open('gamedata.txt').readlines()
            maxStrcount = 0
            
            for iStr in range(1, len(gamedata) - 1):
                if ' ' in gamedata[iStr]:
                    maxStrcount = max(maxStrcount, gamedata.count(gamedata[iStr]))
                    
            if maxStrcount > 1: Repeats = 1
            else: Repeats = 0                           # New room after the portal
#---------------------------------------------------------------------------------#
    if Xpos == 0:
        Xpos = XYfield
        middle_str_old = gamedata[int((XYfield + 1)/2)]
        middle_str_new = 'H' + middle_str_old[1:][:-3] + 'OH\n'
        field = field.replace(middle_str_old, middle_str_new)
        print(Info + '\n' + field)
            
    if Xpos == XYfield + 1:
        Xpos = 1
        middle_str_old = gamedata[int((XYfield + 1)/2)]
        middle_str_new = 'HO' + middle_str_old[2:][:-2] + 'H\n'
        field = field.replace(middle_str_old, middle_str_new)
        print(Info + '\n' + field)

    if Ypos == 0:
        Ypos = XYfield
        middle_str_old = gamedata[-2]
        middle_str_new = middle_str_old[:int((XYfield + 1)/2)] + 'O' + middle_str_old[int((XYfield + 3)/2):]
        field = field.replace(middle_str_old, middle_str_new)
        print(Info + '\n' + field)

    if Ypos == XYfield + 1:
        Ypos = 1
        middle_str_old = gamedata[1]
        middle_str_new = middle_str_old[:int((XYfield + 1)/2)] + 'O' + middle_str_old[int((XYfield + 3)/2):]
        field = field.replace(middle_str_old, middle_str_new)
        print(Info + '\n' + field)
     
    gamedataNew = open('gamedataNew.txt','w')
    gamedataNew.write(field)
    gamedataNew.close()
    gamedataNew = open('gamedataNew.txt').readlines()         # Position accounting
#---------------------------------------------------------------------------------#     by RezerdPrime
