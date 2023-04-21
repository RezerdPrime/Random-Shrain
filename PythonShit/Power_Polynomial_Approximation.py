max_pow = int(input("Set the max pow of the polynomial:\n"))

coords = ""
string = ""

file = open("matrix.txt", "w")

while coords != "end":
    coords = input()

    if coords == "end": file.write(string); file.close(); break

    x_flag = float(coords.split(" ")[0])

    for i in range(max_pow):
        string += str(pow(x_flag, i)) + " "

    y_flag = float(coords.split(" ")[1])
    string += str(y_flag) + "\n"
    
    
# https://matrixcalc.org/ru/slu.html
# https://www.desmos.com/calculator/ipfsu2naxz?lang=ru
