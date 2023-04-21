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

'''
The program builds a matrix based on a finite power series. 
The number of entered points must be equal to the number of maximal degree in the polynomial.

The resulting matrix is placed in a dedicated window on the matrix calculator website.
The solution to the matrix is the necessary coefficients that specify the desired function itself.

The decision column is copied and placed in the "l" list in Desmos. 
The value of the variable "a" is the maximum degree of the polynomial and also the number of points for which the function is true.
'''
