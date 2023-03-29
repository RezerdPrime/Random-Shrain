a=int(input('Введи число: '))
x=a                                          # ГИПОТЕЗА КОЛЛАТЦА
s=[]
while x>1:
    if x%2==0:
        x//=2
        s.append(x)
    else:
        x=x*3+1
        s.append(x)
print(s)                    # Задаём список с результатами

f=open('file.txt','w')
d='Для числа '+str(a)+' результат алгоритма следующий:\n'
f.write(d)
f.write('\n')
for i in range(len(s)):     # Построчная запись результатов в указанный файл
    y=str(s[i])+'\n'
    f.write(y)
    f.write('\n')
f.close()
