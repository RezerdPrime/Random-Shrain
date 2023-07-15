import pygame as pg

pg.init()
w = 1600
h = 900

screen = pg.display.set_mode((w, h))
screen.fill((255, 255, 255))
pg.display.set_caption("The Simplest Paint")
font = pg.font.Font(None, 30)
text = ""

x = 0; y = 0; k = 20

COLOR = (100, 100, 100); COLORBUFF = COLOR

cond = True; mode = 0
while cond:

    xbuff = x; ybuff = y
    x, y = pg.mouse.get_pos()

    for event in pg.event.get():

        if event.type == pg.QUIT:
            cond = False

        if event.type == pg.MOUSEBUTTONDOWN:
            mode = 1

        if mode == 1:
            x, y = pg.mouse.get_pos()
            pg.draw.circle(screen, COLOR, (x, y), k)
            screen.blit(screen, (0, 0))
            pg.display.flip()

            if event.type == pg.MOUSEBUTTONUP:
                mode = 0

        if event.type == pg.MOUSEWHEEL:
            direction, speed = event.y, abs(event.x) + abs(event.y)

            if direction > 0:
                if k: k -= speed
            elif direction < 0:
                if k < 200: k += speed

        mouse_buttons = pg.mouse.get_pressed()
        if mouse_buttons[0]:
            COLOR = COLORBUFF

        if mouse_buttons[2]:
            COLOR = (255, 255, 255)

        if event.type == pg.KEYDOWN:

            keys = pg.key.get_pressed()
            
            if keys[pg.K_LALT]:
                screen.fill((255, 255, 255))
                screen.blit(screen, (0, 0))
                pg.display.flip()

            if keys[pg.K_LSHIFT]:
                mode = 2

            if mode == 2:

                if event.unicode.isprintable():
                    if len(text) < 11: text += event.unicode

                elif event.key == pg.K_BACKSPACE:
                    text = text[:-1]

                if keys[pg.K_RETURN]:
                    try:
                        lst = text.split(" ")
                        COLORBUFF = (int(lst[0]) % 256, int(lst[1]) % 256, int(lst[2]) % 256)
                        mode = 0
                        #print("aaa")
                    except Exception as e: pass
                    text = ""
                    pg.draw.rect(screen, COLORBUFF, (0, 0, 130, 40))

    pg.draw.rect(screen, COLORBUFF, (0, 0, 130, 40))
    text_surface = font.render(text, True, (255 - COLORBUFF[0], 255- COLORBUFF[1], 255 - COLORBUFF[2]))
    screen.blit(text_surface, (10, 10))
    pg.display.flip()

pg.quit()

'''
Right Mouse Button - drawing
Left Mouse Button - erasing
Mouseweel - size changing
Left ALT - canvas refreshing
Left Shift - color changing (RGB format)
'''
