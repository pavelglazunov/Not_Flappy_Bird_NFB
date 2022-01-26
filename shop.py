import pygame as pg
import sys


def print_text(text, x, y, font_size, color, screen):
    font = pg.font.SysFont("", font_size, True, False)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


def shop():
    pg.init()
    size = WIDTH, HEIGHT = 600, 750

    screen = pg.display.set_mode(size, pg.RESIZABLE)

    shop_running = True

    BG = (255, 173, 173)
    # logo = pg.image.load('./data/logo.png')
    # start_btn = pg.image.load('./data/start_btn.png')
    # shop_btn = pg.image.load('./data/shop_btn.png')
    # exit_btn = pg.image.load('./data/exit.png')
    # setting_btn = pg.image.load('./data/setting.png')
    coin_bar = pg.image.load('./data/coin_bar.png')
    shop_logo = pg.image.load('./data/shop.png')
    exit_btn = pg.image.load('./data/exit.png')
    shop_bar = pg.transform.scale(pg.image.load('./data/shop_bar.png'), (50, 50))
    buy_btn = pg.transform.scale(pg.image.load('./data/buy_btn.png'), (50, 25))

    terminator = pg.transform.scale(pg.image.load('./data/bird_tirminate.png'), (50, 40))
    samuray = pg.image.load('./data/samuray.png')
    vader = pg.image.load('./data/darth_vader.png')

    list_of_scins = [terminator, samuray, vader]

    shop_bar_x, shop_bar_y = 200, 300
    step = (WIDTH - 50 * 8) // 9



    coin_n = open('./data/coin.txt', encoding='utf-8').read()
    print(coin_n)

    while shop_running:
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                shop_running = False
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if (0 < mouse_pos[0] < 50) and (700 < mouse_pos[1] < 750):
                    return
                # if (230 < mouse_pos[0] < 380) and (400 < mouse_pos[1] < 450):
                #     return True
                # elif (230 < mouse_pos[0] < 380) and (500 < mouse_pos[1] < 550):
                #     return
                # elif (230 < mouse_pos[0] < 380) and (600 < mouse_pos[1] < 650):
                #     return
                # elif (0 < mouse_pos[0] < 50) and (700 < mouse_pos[1] < 750):
                # pg.quit()
                # sys.exit()
        screen.fill(BG)
        screen.blit(coin_bar, (WIDTH - 100, 0))
        screen.blit(shop_logo, (200, 100))
        screen.blit(exit_btn, (0, 700))
        for i in range(3):
            screen.blit(shop_bar, (shop_bar_x, shop_bar_y))
            # screen.blit(buy_btn, (shop_bar_x, shop_bar_y + 70))
            screen.blit(list_of_scins[i], (shop_bar_x, 305))
            shop_bar_x += step + 50



        shop_bar_x = 130
        print_text(str(coin_n), WIDTH - 50, 13, 40, (255, 255, 0), screen)
        pg.display.flip()

# start_menu()
# shop()
