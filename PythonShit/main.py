import math, cmath
import colorsys as cs
import multiprocessing as mp
from PIL import Image


import time
start = time.time()
end = start

width, height = 1920, 1080
X, Y = 0, 0
scale = 200

img = Image.new("RGB", (width, height))
w = 1+1j


def frac(N_):
    global w

    for x in range(width):
        for y in range(height):

            z = complex((x - width/2)/scale + X, (height/2 - y)/scale + Y)
            w = z

            for _ in range(N_):
                try:
                    z = cmath.sin(z) + w
                except (ZeroDivisionError, OverflowError): ...

            try:
                zmod = abs(z)
                zarg = cmath.phase(z)

                if (zmod < 2) and (img.getpixel((x,y)) == (0,0,0)):
                    h = 1 / math.tau * zarg + (zarg < 0)
                    s = 1-math.tanh(zmod/3)
                    v = math.tanh(zmod)

                    col = cs.hsv_to_rgb(h, s, v)
                    col = tuple(round(c*253) + 1 for c in col)

                    img.putpixel((x,y), col)

            except OverflowError: ...


def Fractal(N_, I):
    global w

    w = complex(-math.sin(math.tau * I / 100), math.cos(math.tau * I / 100))

    # w = complex(
    #     math.cos(math.tau * I / 100)/2 - 0.25,
    #     math.cos(math.tau * I / 100 + math.cos(math.tau * I / 100))/2
    # )

    # angle = math.tau * I / 100
    # factor = math.cos(angle) / (1 + math.sin(angle)**2)
    # w = complex(factor, math.sin(angle) * factor)

    for x in range(width):
        for y in range(height):

            z = complex((x - width/2)/scale + X, (height/2 - y)/scale + Y)

            for _ in range(N_):
                try:
                    z = (z**2).conjugate() + w
                except (ZeroDivisionError, OverflowError): ...

            try:
                zmod = abs(z)
                zarg = cmath.phase(z)

                if (zmod < 2) and (img.getpixel((x,y)) == (0,0,0)):
                    h = 1 / math.tau * zarg + (zarg < 0)
                    s = 1-math.tanh(zmod/3)
                    v = math.tanh(zmod)

                    col = cs.hsv_to_rgb(h, s, v)
                    col = tuple(round(c*253) + 1 for c in col)

                    img.putpixel((x,y), col)

            except OverflowError: ...

def frame(index):
    global img, start, end

    img = Image.new("RGB", (width, height))
    for i in range(5, 1, -1): Fractal(i, index)
    img.save("a2\\{:d}.png".format(index))

    end = time.time()
    print(index, end - start)
    start = end


def convert_parallel(start_frame, finish_frame):
    num_processes = mp.cpu_count()
    pool = mp.Pool(processes=num_processes)
    pool.map(frame, range(start_frame, finish_frame + 1))

    pool.close()
    pool.join()


# https://www.desmos.com/calculator/bxnflo0ugn
if __name__ == '__main__':
    mp.freeze_support()
    convert_parallel(0, 100)

    # img = Image.new("RGB", (width, height))
    # for i in range(10, 1, -1): frac(i)
    # img.save("100.png")
    #
    # print(time.time() - start)


# for k in range(50):
#     img = Image.new("RGB", (width, height))
#     for i in range(10,1,-1): Fractal(i, k)
#     img.save("hui2\\{:d}.png".format(k))
#
#     end = time.time()
#     print(k, end - start)
#     start = end

#print([(-math.sin(math.tau * I / 50), math.cos(math.tau * I / 50)) for I in range(50)])





            # for i in range(N_):
            #     try:
            #         z = cmath.sin(z) + w
            #     except OverflowError as e:
            #         #print("lmao overflow")
            #         ...
            # try:
            #     zmod = abs(z)
            #     zarg = cmath.phase(z)
            #
            #     if zmod < 2:
            #
            #         h = 180 / math.pi * zarg
            #         s = 100
            #         v = 100
            #
            #         col = cs.hsv_to_rgb(h, s, v)
            #         col = tuple(round(c) for c in col)
            #
            #         img.putpixel((x,y), col)
            #
            #
            # except OverflowError as e:
            #     #print("lmao overflow")
            #     ...



# img = Image.open("64.png") #SUSCHTSCH2.jpg
# width, height = img.size
# canvas = Image.new(img.mode, (width, height))
#
#
# def scx(x): return x * s + width/2
# def scy(y): return height/2 - y * s
#
# def dex(_scx): return (_scx - width/2) / s
# def dey(_scy): return (height/2 - _scy) / s
#
# def mod(_z): return (_z.real**2 + _z.imag**2)**.5
#
# def mean_col(_p, eps):
#     borderx = round(_p[0] - eps)
#     bordery = round(_p[1] - eps)
#     lst = []
#
#     for i in range(2*eps):
#         for j in range(2 * eps):
#             if (-1 < borderx + i < width) and (-1 < bordery + j < height):
#                 lst.append(img.getpixel((borderx + i, bordery + j)))
#
#     l = len(lst)
#     Rsum = sum([lst[_][0] for _ in range(l)])
#     Gsum = sum([lst[_][1] for _ in range(l)])
#     Bsum = sum([lst[_][2] for _ in range(l)])
#
#     return round(Rsum / (l+.01)), round(Gsum / (l+.01)), round(Bsum / (l+.01))
#
#
#
# s = 100
# reps = 2
#
# for _j in range(height):
#     for _i in range(width):
#
#         #col = img.getpixel((_i, _j))
#         re = dex(_i)
#         im = dey(_j)
#         #z = complex(re+0.01, im-0.03)**.5
#         z = complex(re, im)
#
#         for _ in range(10):
#             z = (z - 0.2 + 0.35j)**.5
#
#         nx = scx(z.real)
#         ny = scy(z.imag)
#
#         col = mean_col((nx, ny), reps)
#         canvas.putpixel((_i, _j), col)
#
#         # if (-1 < nx < width) and (-1 < ny < height):
#         #     #print("a")
#         #     col = mean_col((nx, ny), reps)
#         #     canvas.putpixel( (_i, _j) , col)
#
# canvas.save("100.png")
#
#
# import math, cmath
# import numpy as np
# from PIL import Image
#
#
# def phi(x, y, s): return x+y+s
# #
# # imgorig = Image.new("RGB", (100, 100))
# #
# # for i_ in range(100):
# #     for j_ in range(100):
# #         imgorig.putpixel((i_, j_), (phi(i_, j_, 50), phi(i_, j_, 100), phi(i_, j_, 150)))
# #
# # imgorig.save("0.png")
#
#
# img = Image.open("0.png")
# canvas = Image.new(img.mode, img.size)
# width, height = img.size
#
# s = 40
#
# for _j in range(height):
#     for _i in range(width):
#
#         #col = img.getpixel((_i, _j))
#         re = (_i - width/2) / s
#         im = (height/2 - _j) / s
#         z = complex(re, im)
#
#         #if mod(z) == 0: z = z + .001 + .001j
#
#         z = z**2
#
#         nx = round(z.real * s + width/2)
#         ny = round(height/2 - z.imag * s)
#
#         #canvas.putpixel( (_i, _j), (phi(nx, ny, 50), phi(nx, ny, 100), phi(nx, ny, 150)) )
#
#         if (-1 < nx < width) and (-1 < ny < height):
#             col = img.getpixel((_i, _j))
#             canvas.putpixel((nx, ny), col)
#
#         # if (-1 < nx < width) and (-1 < ny < height):
#         #     #print("a")
#         #     col = mean_col((nx, ny), reps)
#         #     canvas.putpixel( (_i, _j) , col)
#
# canvas.save("100.png")
#
#
#
#
# #
# #
# # img = Image.open("SUSCHTSCH2.jpg")
# # pixels = np.array(img)
# # canvas = Image.new(img.mode, img.size)
# # width, height = img.size
# #
# #
# # # def scx(x): return x * s + width/2
# # # def scy(y): return height/2 - y * s
# # #
# # # def dex(_scx): return (_scx - width/2) / s
# # # def dey(_scy): return (height/2 - _scy) / s
# # #
# # # def mod(_z): return (_z.real**2 + _z.imag**2)**.5
# #
# # def mean_col(_p, eps):
# #     borderx = round(_p[0] - eps)
# #     bordery = round(_p[1] - eps)
# #
# #     L = [pixels[borderx + i, bordery + j] for i in range(2 * eps) for j in range(2 * eps) if (-1 < borderx + i < width) and (-1 < bordery + j < height)]
# #     l = len(L)
# #
# #     return round(sum([L[_][0] for _ in range(l)]) / l), round(sum([L[_][1] for _ in range(l)]) / l), round(sum([L[_][2] for _ in range(l)]) / l)
# #
# #
# #
# #
# #     # col = (0, 0, 0)
# #     # l = 0
# #
# #     # for i in range(2 * eps):
# #     #     for j in range(2 * eps):
# #     #         if (-1 < borderx + i < width) and (-1 < bordery + j < height):
# #     #             l+=1
# #     #             nc = pixels[borderx + i][bordery + j]
# #     #             col = (col[0] + nc[0], col[1] + nc[1], col[2] + nc[2])
# #
# #     #return round(col[0] / (l+.01)), round(col[1] / (l+.01)), round(col[2] / (l+.01))
# #
# #
# #
# # s = 50
# # reps = 2
# #
# # for _j in range(height):
# #     for _i in range(width):
# #
# #         #col = img.getpixel((_i, _j))
# #         re = (_i - width/2) / s
# #         im = (height/2 - _j) / s
# #         z = complex(re, im)
# #
# #         #if mod(z) == 0: z = z + .001 + .001j
# #
# #         z = z**.5
# #
# #         nx = z.real * s + width/2
# #         ny = height/2 - z.imag * s
# #
# #         col = mean_col((nx, ny), reps)
# #         canvas.putpixel((_i, _j), col)
# #
# #         # if (-1 < nx < width) and (-1 < ny < height):
# #         #     #print("a")
# #         #     col = mean_col((nx, ny), reps)
# #         #     canvas.putpixel( (_i, _j) , col)
# #
# # canvas.save("100.png")