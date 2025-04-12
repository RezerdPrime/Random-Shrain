from engine import *
import pygame as pg

if __name__ == "__main__":

    Map = Map((20, 12))
    Map.random_generate(0.1)
    player = Player((100, 100), (2, 5), (0, 0))
    player.acceleration = (0, -0.1)

    #Map.print_map()

    blockbuttom = Block((player.position[0], Map.size[1]*scale))
    blocktop = Block((player.position[0], scale))
    blockleft = Block((0, player.position[1]))
    blockright = Block((Map.size[0]*scale, player.position[1]))


    pg.init()
    width = 1920/2
    height = 1080/2

    screen = pg.display.set_mode((width, height))
    clock = pg.time.Clock()
    fps = 60
    dt = 1/fps
    globaltime = 0
    #f = False

    font = pg.font.Font(pg.font.get_default_font(), 20)


    running = True
    while running:

        pos = pg.mouse.get_pos()
        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                v = norm((width/2 - pos[0], height/2 - pos[1]))
                player.velocity = (player.velocity[0] - v[0]*10, player.velocity[1] + v[1]*10)
                player.acceleration = (0, -0.1)

        # отрисовка говна ================================================================================ #

        screen.fill((0, 0, 0))

        for j in range(Map.size[1]):
            for i in range(Map.size[0]):
                if Map.objlst[j][i].__class__ == Block:
                    pg.draw.rect(screen, (50, 100, 150),
                    (i*scale + 60,
                     j*scale + 60, scale, scale))

                if Map.objlst[j][i].__class__ == KillingBlock:
                    pg.draw.rect(screen, (147, 50, 58),
                    (i*scale + 60,
                     j*scale + 60, scale, scale))

        pg.draw.rect(screen, (255, 255, 255),
                     (60, 60, Map.size[0] * scale, Map.size[1] * scale), width=2)


        pg.draw.rect(screen, (255, 255, 255),
                     ((1 - player_side) * scale/2 + player.position[0] + 60,
                      (1-player_side) * scale/2 + player.position[1] + 60,#(Map.size[1] - 1) * scale + (player_side) * scale/2 + player.position[1],
                      player_side * scale, player_side * scale))


        pg.draw.line(screen, (255, 255, 255), (width/2, height/2), pos)


        # text_surface = font.render(f'{player.position}', antialias=True, color=(255, 255, 255))
        # screen.blit(text_surface, dest=(500, 400))
        # text_surface = font.render(f'{player.velocity}', antialias=True, color=(255, 255, 255))
        # screen.blit(text_surface, dest=(500, 500))

        # pg.draw.rect(screen, (50, 50, 50),
        #              (player.position[0] + 60,
        #               Map.size[1]*scale + 60,
        #               scale, scale))
        #
        # pg.draw.rect(screen, (50, 50, 50),
        #              (player.position[0] + 60,
        #               -scale + 60,
        #               scale, scale))
        #
        # pg.draw.rect(screen, (50, 50, 50),
        #              (-scale + 60,
        #               player.position[1] + 60,
        #               scale, scale))
        #
        # pg.draw.rect(screen, (50, 50, 50),
        #              (Map.size[0]*scale + 60,
        #               player.position[1] + 60,
        #               scale, scale))


        pg.display.flip()
        clock.tick(fps)


        # калькулятеонс ================================================================================== #

        #player.acceleration = (0, -0.1)

        #print(player.intersect(blockbuttom))

        globaltime += dt
        #print(pg.mouse.get_pos())

        blockbuttom.position = (player.position[0], (Map.size[1]+1/2)*scale)
        blocktop.position = (player.position[0], -1.8*scale)
        blockleft.position = (-2*scale, player.position[1])
        blockright.position = ((Map.size[0]+1)*scale, player.position[1])

        if player.intersect(blockbuttom):
            #print(player.position, blockbuttom.position)

            if player.velocity[0]**2 + player.velocity[1]**2 < scale/3:
                player.velocity = (0,0)
                player.acceleration = (0,0)
                player.position = (player.position[0], (Map.size[1]-1 + (1-player_side)/2)*scale)
            else:
                player.velocity = (0.6*player.velocity[0], -0.6*player.velocity[1])
                player.position = (player.position[0], player.position[1] - scale / 2)

        elif player.intersect(blocktop):
            player.velocity = (0.6 * player.velocity[0], -0.6 * player.velocity[1])
            player.position = (player.position[0], player.position[1] + scale / 2)

        elif player.intersect(blockleft):
            player.velocity = (-0.6 * player.velocity[0], 0.6 * player.velocity[1])
            player.position = (player.position[0] + scale / 2, player.position[1])

        elif player.intersect(blockright):
            player.velocity = (-0.6 * player.velocity[0], 0.6 * player.velocity[1])
            player.position = (player.position[0] - scale / 2, player.position[1])

        else:
            player.velocity = (player.velocity[0], player.velocity[1] + globaltime * player.acceleration[1])
            player.position = (player.position[0] + globaltime * player.velocity[0],
                               player.position[1] - globaltime * player.velocity[1])

        # if player.velocity[0]**2 + player.velocity[1]**2 < 10:
        #     player.velocity = (0, 0)
            #player.acceleration = (0, 0)

        #print(player.intersect(blockbuttom), blockbuttom.position)
        #print(Map.objlst[10][0].position)


        # if player.position[1] < 0:
        #     print("hui")
        #     player.position = (player.position[0], 1)
        #     player.velocity = (player.velocity[0], -player.velocity[1])


    # GlobalMap = Map((10, 6))
    # GlobalMap.random_generate(1)
    #
    # player = Player((36, 30))
    # pim = position_in_matrix(player.position, GlobalMap)
    # block = GlobalMap.objlst[pim[1]][pim[0]+2]
    # print(pim)
    #
    # #block = GlobalMap.objlst[pim[1]][pim[0]]
    # print(player.position, block.position, player.intersect(block))
    # print((block.position[0] - scale - player.position[0] - player_side*scale),
    #                       (abs(block.position[1] - player.position[1]) <= (block.position[0] - player.position[0])))

# https://www.desmos.com/calculator/vv3jkxtxwm

    # pim = position_in_matrix(player.position, GlobalMap)
    # print(pim)
    #
    # GlobalMap.add_player_spawn(pim)
    # GlobalMap.print_map()
    #
    # player.nearest_block(GlobalMap)