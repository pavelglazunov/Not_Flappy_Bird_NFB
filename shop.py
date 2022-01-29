import pygame as pg

import sys

size = WIDTH, HEIGHT = 600, 750

skin_group = pg.sprite.Group()

list_of_buy_skin = []

lock = pg.image.load('./data/lock.png')
bird_skin = pg.image.load('./data/bird.png')
terminator = pg.transform.scale(pg.image.load('./data/bird_tirminate.png'), (50, 40))
samuray = pg.image.load('./data/samuray.png')
vader = pg.image.load('./data/darth_vader.png')

list_of_skins = [bird_skin, terminator, samuray, vader]
skin_now = bird_skin


class Skin(pg.sprite.Sprite):
    def __init__(self, x, y, im):
        super().__init__(skin_group)

        if not im == bird_skin:
            self.image = lock
        else:
            self.image = bird_skin

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

        self.im = im
        self.lock = True
        if self.im in list_of_buy_skin:
            self.image = self.im

    def update(self, *args):
        global skin_now

        if args and args[0].type == pg.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            if self.lock:
                coin_n = open('./data/coin.txt', encoding='utf-8').read()
                if int(coin_n) >= 50:
                    f = open('./data/coin.txt', 'w')
                    f.write(str(int(coin_n) - 50))
                    f.close()
                    list_of_buy_skin.append(self.im)
                    self.lock = False
                    self.image = self.im
            else:
                skin_now = self.im


def print_text(text, x, y, font_input, font_size, color, screen):
    font = pg.font.SysFont(font_input, font_size, True, False)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


shop_bar_x, shop_bar_y = 130, 300
step = (WIDTH - 50 * 8) // 9

for image in list_of_skins:
    Skin(shop_bar_x, shop_bar_y, image)
    shop_bar_x += step + 50


def shop():
    pg.init()

    screen = pg.display.set_mode(size, pg.RESIZABLE)

    shop_running = True

    BG = (255, 173, 173)
    ORANGE = (255, 106, 0)
    BLACK = (0, 0, 0)

    coin_bar = pg.image.load('./data/coin_bar.png')
    shop_logo = pg.image.load('./data/shop.png')
    exit_btn = pg.image.load('./data/exit.png')
    shop_bar = pg.transform.scale(pg.image.load('./data/shop_bar.png'), (50, 50))
    buy_btn = pg.transform.scale(pg.image.load('./data/buy_btn.png'), (50, 25))
    lock = pg.image.load('./data/lock.png')

    while shop_running:
        coin_n = open('./data/coin.txt', encoding='utf-8').read()
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if (0 < mouse_pos[0] < 50) and (700 < mouse_pos[1] < 750):
                    return skin_now

        skin_group.update(event)
        screen.fill(BG)
        skin_group.draw(screen)
        screen.blit(coin_bar, (WIDTH - 100, 0))
        screen.blit(shop_logo, (200, 100))
        screen.blit(exit_btn, (0, 700))

        pg.draw.circle(screen, ORANGE, (WIDTH // 2, 500), 30)
        pg.draw.circle(screen, BLACK, (WIDTH // 2, 500), 30, 2)

        screen.blit(skin_now, (WIDTH // 2 - 25, 500 - 20))
        print_text(str(coin_n), WIDTH - 50, 13, "", 40 - 4 * len(str(coin_n)), (255, 255, 0), screen)
        pg.display.flip()

# start_menu()
# shop()
