from PIL import Image, ImageDraw
from colorsys import hsv_to_rgb as hsv2rgb
from math import *

import multiprocessing as mp
import time
start = time.time()
end = start

width = 16*100; height = 9*100
size = (width, height)

img = Image.new("RGB", size, (0,0,0))
draw = ImageDraw.Draw(img)
scale = 40


def k1(t,x,y,h): return h*fx(t,x,y)
def m1(t,x,y,h): return h*fy(t,x,y)

def k2(t,x,y,h): return h*fx(t+h/2, x+k1(t,x,y,h)/2, y+m1(t,x,y,h)/2)
def m2(t,x,y,h): return h*fy(t+h/2, x+k1(t,x,y,h)/2, y+m1(t,x,y,h)/2)

def k3(t,x,y,h): return h*fx(t+h/2, x+k2(t,x,y,h)/2, y+m2(t,x,y,h)/2)
def m3(t,x,y,h): return h*fy(t+h/2, x+k2(t,x,y,h)/2, y+m2(t,x,y,h)/2)

def k4(t,x,y,h): return h*fx(t+h, x+k3(t,x,y,h), y+m3(t,x,y,h))
def m4(t,x,y,h): return h*fy(t+h, x+k3(t,x,y,h), y+m3(t,x,y,h))

def X(t,x,y,h): return x + (k1(t,x,y,h) + 2*k2(t,x,y,h) + 2*k3(t,x,y,h) + k4(t,x,y,h)) / 6
def Y(t,x,y,h): return y + (m1(t,x,y,h) + 2*m2(t,x,y,h) + 2*m3(t,x,y,h) + m4(t,x,y,h)) / 6


def scx(num): return width/2 + num * scale
def scy(num): return height/2 - num * scale

# for i in range(1, round(width / 2 / scale)+1):
#     draw.line((scx(i), 0, scx(i), height), fill=(25,25,25))
#     draw.line((scx(-i), 0, scx(-i), height), fill=(25, 25, 25))
#
# for i in range(1, round(height / 2 / scale+1)):
#     draw.line((0, scy(i), width, scy(i)), fill=(25, 25, 25))
#     draw.line((0, scy(-i), width, scy(-i)), fill=(25, 25, 25))
#
#
# draw.line((width/2, 0, width/2, height), fill=(25, 25, 25))
# draw.line((0, height/2, width, height/2), fill=(25, 25, 25))


def RungeKutt(b, n, init):
    h = b/n
    t = [h*_ for _ in range(n+1)]
    res = []
    itr = init

    for i in range(n + 1):
        try:
            itr = (X(t[i], itr[0], itr[1], h), Y(t[i], itr[0], itr[1], h))
            res.append(itr)
        except (OverflowError, ZeroDivisionError, ValueError): ...
    return res


def DrawCurve(L, h=0):
    lg = len(L)
    for _ in range(lg - 1):
        col = hsv2rgb(h + _/1000, 1-tanh(_/lg*1.5), tanh(_/lg*2))
        #col = hsv2rgb(h + _ / 1000, 1, 1)
        col = (round(col[0] * 255), round(col[1] * 255), round(col[2] * 255))
        draw.line((scx(L[_][0]), scy(L[_][1]), scx(L[_ + 1][0]), scy(L[_ + 1][1])), fill=col, width = 1 + round(2*sin(pi*_/2)) ) # + round(2*sin(_))


# def fx(t,x,y): return sin(x+cos(y))
# def fy(t,x,y): return cos(y+sin(x))

# def fx(t,x,y): return sin((x**2 + y**2)**.5) #sin(x+cos(y*x))
# def fy(t,x,y): return cos((x**2 + y**2)**.5) #cos(y+sin(x*y))

def fx(t,x,y): return y - t
def fy(t,x,y): return t - x

k = 1
brdx = round(width / 2 / scale+1)
brdy = round(height / 2 / scale+1)

def frame(I):
    global start, end
    for i in range(-brdx*k, brdx*k + 1):
        for j in range(-brdy*k, brdy*k + 1):

            x = i/k; y=j/k

            arg = atan2(y, x) / tau
            arg += arg<0

            DrawCurve(RungeKutt(I/25, 100, (x,y)), arg)

    #img.save(f"fr\\{I}.png")
    img.save("hui.png")

    start = end
    end = time.time()
    print(I, end - start)


def convert_parallel(start_frame, finish_frame):
    num_processes = mp.cpu_count()
    pool = mp.Pool(processes=num_processes)
    pool.map(frame, range(start_frame, finish_frame + 1))

    pool.close()
    pool.join()


if __name__ == '__main__':
    # mp.freeze_support()
    # convert_parallel(0, 300)

    frame(10)

    print(time.time() - start)