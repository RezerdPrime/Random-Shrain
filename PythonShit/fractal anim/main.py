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
