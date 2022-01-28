import pygame as pg

import sys

skin_group = pg.sprite.Group()
list_of_buy_skin = []
lock = pg.image.load('./data/lock.png')


class Skin(pg.sprite.Sprite):
    def __init__(self, x, y, im):
        super().__init__(skin_group)

        self.image = lock
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.im = im
        self.lock = True

    def update(self, *args):
        if args and args[0].type == pg.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.lock = False
            self.image = self.im


def print_text(text, x, y, font_input, font_size, color, screen):
    font = pg.font.SysFont(font_input, font_size, True, False)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


# class Skin(pg.sprite.Sprite):
#     def __init__(self, x, y, im):
#         super(self).__init__(skin_group)
#         self.image = im
#         self.rect = self.image.get_rect()
#         self.rect.x, self.rect.y = x, y


def shop():
    pg.init()
    size = WIDTH, HEIGHT = 600, 750

    screen = pg.display.set_mode(size, pg.RESIZABLE)

    shop_running = True

    BG = (255, 173, 173)
    list_of_pos = []
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
    lock = pg.image.load('./data/lock.png')

    terminator = pg.transform.scale(pg.image.load('./data/bird_tirminate.png'), (50, 40))
    samuray = pg.image.load('./data/samuray.png')
    vader = pg.image.load('./data/darth_vader.png')

    list_of_skins = [terminator, samuray, vader]

    shop_bar_x, shop_bar_y = 130, 300
    step = (WIDTH - 50 * 8) // 9
    print(step)

    coin_n = open('./data/coin.txt', encoding='utf-8').read()

    for image in list_of_skins:
        Skin(shop_bar_x, shop_bar_y, image)
        shop_bar_x += step + 50
        
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
                # elif (130 < mouse_pos[0] < 180) and (300 < mouse_pos[1] < 350):
                #     print(44444)
                #     list_of_buy_skin.append(0)
                # elif (202 < mouse_pos[0] < 252) and (300 < mouse_pos[1] < 350):
                #     print(44444)
                #     list_of_buy_skin.append(1)
                # elif (274 < mouse_pos[0] < 324) and (300 < mouse_pos[1] < 350):
                #     print(44444)
                #     list_of_buy_skin.append(2)


                # if (230 < mouse_pos[0] < 380) and (400 < mouse_pos[1] < 450):
                #     return True
                # elif (230 < mouse_pos[0] < 380) and (500 < mouse_pos[1] < 550):
                #     return
                # elif (230 < mouse_pos[0] < 380) and (600 < mouse_pos[1] < 650):
                #     return
                # elif (0 < mouse_pos[0] < 50) and (700 < mouse_pos[1] < 750):
                # pg.quit()
                # sys.exit()
        skin_group.update(event)
        screen.fill(BG)
        skin_group.draw(screen)
        screen.blit(coin_bar, (WIDTH - 100, 0))
        screen.blit(shop_logo, (200, 100))
        screen.blit(exit_btn, (0, 700))


        # for i in range(3):
        #
        #     # screen.blit(buy_btn, (shop_bar_x, shop_bar_y + 70))
        #     if i in list_of_buy_skin:
        #         screen.blit(shop_bar, (shop_bar_x, shop_bar_y))
        #         screen.blit(list_of_skins[i], (shop_bar_x, 305))
        #     else:
        #         screen.blit(lock, (shop_bar_x, shop_bar_y))
        #     list_of_pos.append(shop_bar_x)
        #     shop_bar_x += step + 50
        # print(list_of_scins[1].get_rect())

        shop_bar_x = 130
        print_text(str(coin_n), WIDTH - 50, 13, "", 40 - 4 * len(str(coin_n)), (255, 255, 0), screen)
        pg.display.flip()

# start_menu()
# shop()
