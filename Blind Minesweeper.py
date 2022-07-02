Lenght_of_field = int(input('Set lenght (X) of your field: '))
Height_of_field = int(input('Set height (Y) of your field: '))

from random import randint

sField = ''
for iH in range(Height_of_field):
    for iL in range(Lenght_of_field):
        sField += str(randint(0,1))
    sField += '\n'                  # Field generation #
#-----------------------------------------------------------------------------#
print('')
dikt = set()
k1 = 0; k0 = int((sField.count('1')/2 + sField.count('0')/2)/2) + 2
while k1 != sField.count('1') or k0 != 0:
    
    print('Fail maximum:',k0)
    print('Your score:',k1)
    print('Your moves:',sorted(dikt))
    x=int(input('Set value of X pos : '))-1
    y=int(input('Set value of Y pos : '))-1
    print('\n')
    
    file=open('game.txt','w')
    file.write(sField)
    file.close()
    strFile=open('game.txt').readlines()
    # print(srtFile[y],strFile[y][x])
    
    import os
    os.remove('game.txt')           # Setting 2D position and field reading #
#-----------------------------------------------------------------------------#
    gMove=str(x+1) + '-' + str(y+1)
    if strFile[y][x] == '1' and gMove not in dikt:
        k1 += 1
        dikt.add(gMove)
    else: k0 -=1 ; dikt.add(gMove)  # Condition of score and fail maximum #
#-----------------------------------------------------------------------------#   
    if k1 == sField.count('1'):
        print('Victory!\n' + sField)
        break
    if k0 == 0:
        print('Lose\n' + sField)
        break                       # Win/Lose condition #
#-----------------------------------------------------------------------------#
