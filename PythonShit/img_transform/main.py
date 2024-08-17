import math, cmath
from PIL import Image


img = Image.open("SUSCHTSCH2.jpg")
canvas = Image.new(img.mode, img.size)
width, height = img.size


def scx(x): return x * s + width/2
def scy(y): return height/2 - y * s

def dex(_scx): return (_scx - width/2) / s
def dey(_scy): return (height/2 - _scy) / s

def mod(_z): return (_z.real**2 + _z.imag**2)**.5

def mean_col(_p, eps):
    borderx = round(_p[0] - eps)
    bordery = round(_p[1] - eps)
    lst = []

    for i in range(2*eps):
        for j in range(2 * eps):
            if (-1 < borderx + i < width) and (-1 < bordery + j < height):
                lst.append(img.getpixel((borderx + i, bordery + j)))

    l = len(lst)
    Rsum = sum([lst[_][0] for _ in range(l)])
    Gsum = sum([lst[_][1] for _ in range(l)])
    Bsum = sum([lst[_][2] for _ in range(l)])

    return round(Rsum / (l+.01)), round(Gsum / (l+.01)), round(Bsum / (l+.01))



s = 200
reps = 2

for _j in range(height):
    for _i in range(width):

        #col = img.getpixel((_i, _j))
        re = dex(_i)
        im = dey(_j)
        z = complex(re, im)

        if mod(z) == 0: z = z + .001 + .001j

        z = cmath.log(z)

        nx = scx(z.real)
        ny = scy(z.imag)

        col = mean_col((nx, ny), reps)
        canvas.putpixel((_i, _j), col)

        # if (-1 < nx < width) and (-1 < ny < height):
        #     #print("a")
        #     col = mean_col((nx, ny), reps)
        #     canvas.putpixel( (_i, _j) , col)

canvas.save("100.png")