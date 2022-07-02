Lenght=int(input('Set lenght of your field: '))
Height=int(input('Set height of your field: '))
from random import randint
strField=''
for iL in range(Lenght):
    for iH in range(Height):
        strField+=str(randint(0,1))
    strField+='\n'                  # Field generation #
#-----------------------------------------------------------------------------#
print('')
dikt=set()
k1=0; k0=int((strField.count('1')/2+strField.count('0')/2)/2)+2
while k1!=strField.count('1') or k0!=0:
    print('Fail maximum:',k0)
    print('Your score:',k1)
    print('Your moves:',sorted(dikt))
    x=int(input('Set value of X pos (1-5): '))-1
    y=int(input('Set value of Y pos (1-5): '))-1
    print('\n')
    file=open('game.txt','w')
    file.write(strField)
    file.close()
    strFile=open('game.txt').readlines()
    # print(srtFile[y],strFile[y][x])
    import os
    os.remove('game.txt')           # Setting 2D position and field reading #
#-----------------------------------------------------------------------------#
    move=str(x+1)+str(y+1)
    if strFile[y][x]=='1' and move not in dikt:
        k1+=1
        dikt.add(move)
    else: k0-=1; dikt.add(move)     # Condition of score and fail maximum #
#-----------------------------------------------------------------------------#   
    if k1==strField.count('1'):
        print('Victory!\n'+strField)
        break
    if k0==0:
        print('Lose\n'+strField)
        break                       # Win/Lose condition #
#-----------------------------------------------------------------------------#
