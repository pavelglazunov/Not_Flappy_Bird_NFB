import pygame as pg
import sys
from shop import shop

skin = pg.image.load('./data/bird.png')


def print_text(text, x, y, font_input, font_size, color, screen):
    font = pg.font.SysFont(font_input, font_size, True, False)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


def __skin__():
    global skin
    return skin


def start_menu(play):
    global skin

    pg.init()
    size = WIDTH, HEIGHT = 600, 750

    screen = pg.display.set_mode(size, pg.RESIZABLE)

    start_menu_running = True

    BG = (255, 173, 173)

    logo = pg.image.load('./data/logo.png')
    start_btn = pg.image.load('./data/start_btn.png')
    shop_btn = pg.image.load('./data/shop_btn.png')
    exit_btn = pg.image.load('./data/exit.png')
    setting_btn = pg.image.load('./data/setting.png')
    coin_bar = pg.image.load('./data/coin_bar.png')

    coin_n = open('./data/coin.txt', encoding='utf-8').read()
    print(coin_n)

    while start_menu_running:
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if (230 < mouse_pos[0] < 380) and (400 < mouse_pos[1] < 450):
                    return True
                elif (230 < mouse_pos[0] < 380) and (500 < mouse_pos[1] < 550):
                    skin = shop()
                elif (230 < mouse_pos[0] < 380) and (600 < mouse_pos[1] < 650):
                    return
                elif (0 < mouse_pos[0] < 50) and (700 < mouse_pos[1] < 750):
                    pg.quit()
                    sys.exit()
        screen.fill(BG)

        screen.blit(logo, (0, 100))
        screen.blit(start_btn, (230, 400))
        screen.blit(shop_btn, (230, 500))
        screen.blit(setting_btn, (230, 600))
        screen.blit(exit_btn, (0, 700))
        screen.blit(coin_bar, (WIDTH - 100, 0))

        print_text(str(coin_n), WIDTH - 50, 13, "", 40 - 4 * len(str(coin_n)), (255, 255, 0), screen)
        pg.display.flip()

# start_menu()
