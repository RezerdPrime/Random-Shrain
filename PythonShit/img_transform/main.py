import math, cmath
import numpy as np
import multiprocessing as mp
from PIL import Image


import time
start = time.time()
end = start
S = start


img = Image.open("smeh.png") #"smeh.png" "SUSCHTSCH2.jpg"
pixar = np.array(img)
#canvas = Image.new(img.mode, img.size)
width, height = img.size
X, Y = 0, 0
s = 350
reps = 1


def mean_col(_p, eps):
    borderx = round(_p[0] - eps)
    bordery = round(_p[1] - eps)
    lst = []

    for i in range(2 * eps):
        for j in range(2 * eps):
            if (-1 < borderx + i < width) and (-1 < bordery + j < height):
                lst.append(pixar[bordery + j, borderx + i])

    l = len(lst)
    Rsum = sum([lst[_][0] for _ in range(l)])
    Gsum = sum([lst[_][1] for _ in range(l)])
    Bsum = sum([lst[_][2] for _ in range(l)])

    return round(Rsum / (l+.01)), round(Gsum / (l+.01)), round(Bsum / (l+.01))


def frame(I):
    global start, end
    w = complex(-math.sin(math.tau * I / 100)/2, math.cos(math.tau * I / 100)/2)
    canvas = Image.new(img.mode, img.size)

    for _j in range(height):
        for _i in range(width):

            z = complex((_i - width/2) / s + X, (height/2 - _j) / s + Y)

            for _ in range(7):
                try:
                    z = z**2 + w
                except OverflowError: ...

            try:
                if abs(z) < 2:

                    col = mean_col(((z.real - X) * s + width/2, height/2 - (z.imag - Y) * s), reps)
                    canvas.putpixel((_i, _j), col)
            except OverflowError: ...

    canvas.save("hui\\{:d}.png".format(I))
    end = time.time()
    print(I, end - start)
    start = end


def convert_parallel(start_frame, finish_frame):
    num_processes = mp.cpu_count()
    pool = mp.Pool(processes=num_processes)
    pool.map(frame, range(start_frame, finish_frame + 1))

    pool.close()
    pool.join()



if __name__ == '__main__':
    mp.freeze_support()
    convert_parallel(11, 100)

    #frame(0)

    print(time.time() - S)
