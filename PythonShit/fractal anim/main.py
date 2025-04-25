from PIL import Image, ImageDraw
import math as m
from cmath import *

def buildcol(i):
    h = 28 if i < 1 / 2 else 142
    s = 1 - m.exp(-5 * (2 * i - 1) ** 2)
    v = 1 - max(0, 0.8 - 5 * i * (1 - i))
    return h, m.floor(s * 255), m.floor(v * 255)


def buildgrid():
    draw = ImageDraw.Draw(img)
    i_, j_ = 0, 0
    p = 1

    while i_ < W:
        i_ = (p - xsh) * k + W / 2
        i__ = (-p - xsh) * k + W / 2
        draw.line((i_, 0, i_, H), width=2, fill=(0, 0, 100))
        draw.line((i__, 0, i__, H), width=2, fill=(0, 0, 100))
        p += 1

    p = 1

    while j_ < H:
        j_ = H / 2 + (p - ysh) * k
        j__ = H / 2 + (-p - ysh) * k
        print(j_)
        draw.line((0, j_, W, j_), width=2, fill=(0, 0, 100))
        draw.line((0, j__, W, j__), width=2, fill=(0, 0, 100))
        p += 1

    draw.line((W / 2, 0, W / 2, H), width=3, fill=(1, 1, 1))
    draw.line((0, H / 2, W, H / 2), width=3, fill=(1, 1, 1))


def DomainColoring():

    for j in range(H):
        for i in range(W):
            x = (i - W / 2) / k + xsh
            y = (H / 2 - j) / k + ysh

            z = complex(x, y)

            try:
                z = f(z)

            except OverflowError:
                z = 1000 + 1000j

            except (ValueError, ZeroDivisionError):
                z = f(z + 0.01)

            x = z.real
            y = z.imag

            if abs(x) > 1000: x = 1000
            if abs(y) > 1000: y = 1000

            z = complex(x, y)

            zarg = m.atan2(y, x)

            h = zarg / m.pi / 2 + (1 if zarg < 0 else 0)
            #h = 0.805555555556 + 0.0884194128288 * m.asin(m.cos(zarg-0.1))

            if naked:
                s = 1
                v = 1
            else:
                s = 1 - m.tanh((x ** 2 + y ** 2) ** .5 / 5)
                v = m.tanh((x ** 2 + y ** 2) ** .5 / 2)

            color = (m.floor(h * 255), m.floor(s * 255), m.floor(v * 255))

            img.putpixel((i, j), color)


def Fractal(I, N, R=1, nu=1):
    bgcol = buildcol(nu / N)
    cap = m.fmod(nu * I/N, 1)

    for j in range(H):
        for i in range(W):
            x = (i - W / 2) / k + xsh
            y = (H / 2 - j) / k + ysh

            z = complex(x, y)
            w = complex(x, y)

            for _ in range(I):
                try:
                    z = f(z) + w

                except (ValueError, OverflowError):
                    z = 1000 + 1000j
                    break

                # except ZeroDivisionError:
                #     z = f(z + 0.01)

            x = z.real
            y = z.imag

            if abs(x) > 1000: x = 1000
            if abs(y) > 1000: y = 1000

            if I == N-1:
                color = (1, 0, 0)

            else:
                color = buildcol(cap)

            if (x**2 + y**2 < R**2): #and (img.getpixel((i,j)) == bgcol):
                img.putpixel((i, j), color)


W, H = 1200, 800
k = 100
xsh = 0
ysh = 0
N = 10
R = 2
nu = 2
naked = False

img = Image.new("HSV", (W, H), buildcol(nu / N))

def f(z):
    return exp(z) / (exp(2 * pi * 1j * z) + 1)

#(z+1j)/(z-1)/(z+1+1j)
#1/cosh(z + tan(z))
#atan(2/z/z)*exp(1j * z)
#(exp(1j * z) - 1) * tanh(z) / z / z
#log(z)/(exp(z)+1)
#log(1 + exp(z)) / z / 1j
#log(1 + cos(z)/z)
#1/(exp(-z)-z)
#1/(z - cos(cos(z)))
#log(1 + exp(z/tan(z))*sin(z)/z)
# #sin(z) * ( (1 + cosh(2)) + z*z*(cosh(2) - 1) ) / (z*z - 2j * z / sinh(2) + 1) / (1 + z*z)

DomainColoring()
buildgrid()

# for _ in range(N, 1, -1):
#     Fractal(_, N, R=R, nu=nu)

# for _ in range(1, N):
#     Fractal(_, N, R=R, nu=nu)



img.convert("RGB").save("a.png")






















# from PIL import Image
# import math as m
# from cmath import *
# import time
#
# W, H = 1200, 800
# k = 100#200 #6000
# xsh = 0#-1.5 #-1.76
# ysh = 0#-1.5 #0.03
#
# c1 = (25, 255, 255)
# c2 = (0, 255, 45)
#
# N = 20
#
# def f(z):
#     return (z**2 + 1)*z
#
# # def f(z):
# #     w = complex(abs(z.real), -abs(z.imag))
# #     return sin(w)
#
# #z + sin(z)
# #z*sin(sin(z))
# #complex(abs(z.real), -abs(z.imag))
# #sin(log(z - (1+1j)/(z+1j)))
# #log((1j + sin(z)) / (1j + cosh(z)))
# #log((sin(z) + exp(z)) / (cos(z) - log(z)))
# #log((sin(z-10) + log(z-10)) / (cos(z-10) - log(z-10)))
#
# img = Image.new("HSV", (W, H), c2)
#
# def Fractal(I):
#     #color = tuple([round(c2[_1] - (c2[_1] - c1[_1]) * I / N) for _1 in range(3)])
#
#     for j_ in range(H):
#         for i_ in range(W):
#             curcol = img.getpixel((i_,j_))
#             x = (i_ - W/2 ) / k + xsh
#             y = (H/2 - j_) / k + ysh
#
#             z = complex(x, y)
#             w = z
#
#
#             for _ in range(I):
#                 try:
#                     z = f(z)
#
#                 except (ValueError, OverflowError):
#                     z = 100 + 100j
#                     break
#
#                 except ZeroDivisionError:
#                     z = f(z + 0.01)
#
#             x = z.real
#             y = z.imag
#
#             if abs(x) > 1000 or isnan(x): x = 1000
#             if abs(y) > 1000 or isnan(y): y = 1000
#
#             z = complex(x, y)
#
#             zarg = m.atan2(y, x)
#
#             h = zarg / m.pi / 2 + (1 if zarg < 0 else 0)
#             s = 1 - m.tanh((x**2 + y**2)**.5 / 5)
#             v = m.tanh((x**2 + y**2)**.5 / 2)
#
#             color = (m.floor(h*255), m.floor(s*255), m.floor(v*255))
#
#             if (abs(z) < 2) and (curcol == c2):
#                 img.putpixel((i_, j_), color)
#
# # st = time.time()
# # for i in range(N, 0, -1):
# #     Fractal(i)
# # print(time.time() - st)
#
# for j_ in range(H):
#     for i_ in range(W):
#         x = (i_ - W/2 ) / k + xsh
#         y = (H/2 - j_) / k + ysh
#
#         z = complex(x, y)
#
#         try:
#             z = f(z)
#
#         except OverflowError:
#             z = 1000 + 1000j
#             break
#
#         except (ValueError, ZeroDivisionError):
#             z = f(z + 0.01)
#
#         x = z.real
#         y = z.imag
#
#         if abs(x) > 1000: x = 1000
#         if abs(y) > 1000: y = 1000
#
#         z = complex(x, y)
#
#         zarg = m.atan2(y, x)
#
#         h = zarg / m.pi / 2 + (1 if zarg < 0 else 0)
#         s = 1 - m.tanh((x**2 + y**2)**.5 / 5)
#         v = m.tanh((x**2 + y**2)**.5 / 2)
#
#         color = (m.floor(h * 255), m.floor(s * 255), m.floor(v * 255))
#
#         #if (abs(z) < 2) :#and (curcol[2] == 0):
#         img.putpixel((i_, j_), color)
#
# img.convert("RGB").save("a.png")