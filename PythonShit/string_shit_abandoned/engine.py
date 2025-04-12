import math as m
import random

player_side = 0.6

LEFTCOLLISION = 1
RIGHTCOLLISION = 2
UPCOLLISION = 3
DOWNCOLLISION = 4
NOCOLLISION = 0

g = 9.8
scale = 30


def norm(v):
    r2 = v[0]*v[0] + v[1]*v[1]
    if r2 == 0: return 0,0
    return v[0] / r2 ** .5, v[1] / r2 ** .5

def scx(num):
    return int(num / scale)

def scy(num, ybound):
    return int(ybound - num / scale)

def position_in_matrix(pos, mapa):
    return scx(pos[0]), scy(pos[1], mapa.size[1])

class Block:

    def __init__(self, position):
        self.position = position


class KillingBlock(Block):

    def __init__(self, position):
        super().__init__(position)


class Map:
    def __init__(self, size: tuple[int, int]=None, objlst=None):
        if objlst is None:
            objlst = []
        self.size = size
        self.objlst = objlst

    def random_generate(self, procent):
        #self.size = (width, height)
        self.objlst = [
                    [0 for _ in range(self.size[0])]
                    for _ in range(self.size[1])]

        for j in range(self.size[1]):
            for i in range(self.size[0]):

                if random.random() < procent:
                    if random.random() < .5:
                        self.objlst[j][i] = Block((i * scale, (self.size[1] - j - 1) * scale))
                    else: self.objlst[j][i] = KillingBlock((i * scale, (self.size[1] - j - 1) * scale))

    def add_player_spawn(self, pos):
        self.objlst[pos[1]][pos[0]] = 1

    def print_map(self):
        for j in range(self.size[1]):
            for i in range(self.size[0]):

                if self.objlst[j][i].__class__ == Block:
                    print("B ", end="")

                if self.objlst[j][i].__class__ == KillingBlock:
                    print("K ", end="")

                if isinstance(self.objlst[j][i], int):
                    if self.objlst[j][i] == 0:
                        print("- ", end="")
                    else: print("O ", end="")
            print()

class Player:

    def __init__(self, position=None, velocity=None, acceleration=None):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def intersect(self, block):

        left_collision = (-scale < (block.position[0] - scale - self.position[0] - player_side*scale) < 0) and \
                          (abs(block.position[1] - self.position[1]) <= (block.position[0] - self.position[0]))

        right_collision = (-scale < (self.position[0] - player_side*scale - block.position[0] - scale) < 0) and \
                          (abs(block.position[1] - self.position[1]) <= (self.position[0] - block.position[0]))

        upper_collision = (-scale < (self.position[1] - player_side*scale - block.position[1] - scale) < 0) and \
                          ((self.position[1] - block.position[1]) > abs(self.position[0] - block.position[0]))

        down_collision = (-scale < (block.position[1] - scale - self.position[1] - player_side*scale) < 0) and \
                          ((block.position[1] - self.position[1]) > abs(self.position[0] - block.position[0]))

        if left_collision: return LEFTCOLLISION
        if right_collision: return RIGHTCOLLISION
        if upper_collision: return UPCOLLISION
        if down_collision: return DOWNCOLLISION
        else: return NOCOLLISION


    def nearest_block(self, mapa):
        x, y = position_in_matrix(self.position, mapa)
        poslist = [(x+1, y+1), (x, y+1), (x-1, y+1),
                   (x+1, y), (x-1, y),
                   (x+1, y-1), (x, y-1), (x-1, y-1)]

        poslist = [pos for pos in poslist if (-1 < pos[0] < mapa.size[0]
                    and -1 < pos[1] < mapa.size[1] and isinstance(mapa.objlst[pos[1]][pos[0]], Block))]

        objsublist = [mapa.objlst[j][i] for i, j in poslist]

        collisionlist = [self.intersect(_) for _ in objsublist]

        print(collisionlist)

    def recochet(self):
        ...