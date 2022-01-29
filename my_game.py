import random

import pygame as pg
from start import start_menu, __skin__


class Coin(pg.sprite.Sprite):
    def __init__(self, x, y):
        global coin_here
        super().__init__(coin_group)

        self.image = pg.image.load('./data/coin.png')
        self.rect = self.image.get_rect()

        self.x, self.y = x, y
        self.rect.x, self.rect.y = self.x, self.y

        self.up = True
        coin_here = False
        self.catch = False

    def update(self):
        global coin_n, tic, coin_here

        coin_here = True
        if self.rect.y >= self.y - 10 and self.up:
            self.rect.y -= 0.5
        else:
            self.up = False
            if self.rect.y <= self.y + 20:
                self.rect.y += 1
            else:
                self.up = True

        if pg.sprite.spritecollideany(self, all_sprites):
            self.kill()
            coin_here = False
            coin_n += 1
            f = open('./data/coin.txt', 'w')
            f.write(str(coin_n))
            f.close()


class Wall(pg.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__(wall_group)

        self.image = pg.image.load('./data/wall.png')
        self.rect = self.image.get_rect()

        if x == 0:
            self.image = pg.transform.flip(self.image, 50, 0)

        self.rect.x, self.rect.y = x, y
        self.mask = pg.mask.from_surface(self.image)


class Bird(pg.sprite.Sprite):
    def __init__(self, *group):
        global skin
        super().__init__(*group)

        self.image = skin
        self.rect = self.image.get_rect()

        self.rect.center = WIDTH // 2, HEIGHT // 2

        self.pressed = False
        self.fall = False

        self.isJump = False
        self.jumpCount = 30

        self.speed = 5

        self.mask = pg.mask.from_surface(self.image)

    def update(self):
        global GRAVITY, BG_COLOR, play, count, coin_here

        if pg.sprite.spritecollideany(self, wall_group):
            play = False

        self.pressed = False
        if self.rect.y >= HEIGHT - 150:
            BG_COLOR = (230, 230, 230)
            play = False

        if not self.fall:
            self.rect.y += GRAVITY
            GRAVITY += 0.10
            if self.rect.y > HEIGHT:
                self.rect.y = HEIGHT // 2
                GRAVITY = 1

        self.rect.x += self.speed
        if self.rect.x >= WIDTH - 50 or self.rect.x <= 0:
            wall_group.empty()
            if self.speed > 0:
                wall_create('left')
            elif self.speed < 0:
                wall_create('right')

            if not coin_here:
                coin_create()

            self.speed *= -1

            count += 1
            if count % 10 == 0:
                R, G, B = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
                BG_COLOR = (G, G, B)
            self.image = pg.transform.flip(self.image, 50, 0)

    def jump(self, fall):
        global GRAVITY, press
        press = False
        self.fall = fall
        GRAVITY = 1
        self.rect.x += 1

        self.jumpCount = 30
        if self.fall and not self.pressed:

            if self.jumpCount >= -30:
                self.rect.x += 5
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                if self.rect.y <= 130:
                    l = self.rect.y - 100
                    self.rect.y -= l

                else:
                    self.rect.y -= self.jumpCount ** 2 * 0.1 * neg

                pg.draw.circle(screen, RED, (self.rect.x, self.rect.y), 20)

                self.jumpCount -= 1
            else:
                self.fall = False
                self.isJump = False

                self.jumpCount = 30

        else:
            self.rect.y += GRAVITY
            if self.rect.y > HEIGHT:
                self.rect.y = HEIGHT // 2
                GRAVITY = 1


def coin_create():
    coin_group.empty()
    random_count = random.choice([0, 1, 2, 3, 4, 5])
    coin_x, coin_y = random.randint(50, WIDTH - 50), random.randint(200, HEIGHT - 200)
    if random_count == 0:
        Coin(coin_x, coin_y)


lvl = 3
count_r = 0


def wall_create(now_r):
    global lvl, count_r
    print(count_r)
    wall_group.empty()
    if count_r == 5 and lvl <= 18:
        count_r = 0
        lvl += 1
    count_r += 1

    if now_r == 'right':
        x = WIDTH - 20
    else:
        x = 0
    for i in range(lvl):
        y = random.randrange(100, 650, 50)
        Wall(x, y)
        list_of_left.append(y)


def create():
    wall_create('right')
    coin_create()


def print_text(text, x, y, font_input, font_size, color, screen):
    font = pg.font.SysFont(font_input, font_size, True, False)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


def reset():
    global count, BG_COLOR, coin_here, play

    count = 0
    BG_COLOR = (230, 230, 230)

    wall_create('right')
    coin_create()
    bird.image = __skin__()

    if bird.speed < 0:
        bird.speed *= -1
    coin_here = False
    play = True


pg.init()
size = WIDTH, HEIGHT = 600, 750

GRAVITY = 1
GRAVITY_speed = 600

screen = pg.display.set_mode(size, pg.RESIZABLE)
clock = pg.time.Clock()
FPS = 60

running = True
press = False
coin_here = False

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WALL_GRAY = (96, 96, 96)

tic = 0
skin = pg.image.load('./data/bird.png')

all_sprites = pg.sprite.Group()
wall_group = pg.sprite.Group()
coin_group = pg.sprite.Group()

bird = Bird(all_sprites)

r, g, b = (230, 230, 230)
BG_COLOR = (r, g, b)
x = 0
y = 0
mony = 0

list_of_left = []
list_of_right = []

play = start_menu(False)
reset()

y = 100
x = 0
count = 0
coin_n = int(open('./data/coin.txt', encoding='utf-8').read())
tic = 0
text_x = WIDTH // 2

create()

game_over = pg.image.load('./data/game_over.png')
restart = pg.image.load('./data/restart.png')
home = pg.image.load('./data/home.png')
coin_bar = pg.image.load('./data/coin_bar.png')

while running:
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
            running = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and not press:
                pg.event.poll()
                press = True
                pg.key.set_repeat(0, 0)
                press = True

                bird.jump(True)
                break

        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                bird.jump(False)
                press = False

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if (230 < mouse_pos[0] < 380) and (400 < mouse_pos[1] < 450) and not play:
                reset()
            if (230 < mouse_pos[0] < 380) and (500 < mouse_pos[1] < 550) and not play:
                play = start_menu(False)
                reset()

    screen.fill(BG_COLOR)
    GRAVITY += 0.25

    SECOND_BG_COLOR = (BG_COLOR[0] - BG_COLOR[0] // 4,
                       BG_COLOR[1] - BG_COLOR[1] // 4,
                       BG_COLOR[2] - BG_COLOR[2] // 4)
    if play:
        pg.draw.circle(screen, SECOND_BG_COLOR, (WIDTH // 2, HEIGHT // 2), 150)
        print_text(str(count), text_x, HEIGHT // 2 - 55, "Cascadia Code SemiBold", 192, BG_COLOR, screen)
        text_x = WIDTH // 2 - (len(str(count)) * 40)

        all_sprites.update()
        coin_group.update()

        all_sprites.draw(screen)
        wall_group.draw(screen)

        tic += 1
        coin_group.draw(screen)
    else:
        bird.rect.x, bird.rect.y = WIDTH // 2, HEIGHT // 2
        if bird.speed > 0:
            bird.image = skin
        else:
            bird.image = pg.transform.flip(skin, 50, 0)
        GRAVITY = 1
        screen.blit(game_over, (210, 100))

        print_text(f'Счет: {count}', 240, 250, "", 40, RED, screen)
        screen.blit(restart, (230, 400))
        screen.blit(home, (230, 500))

    pg.draw.rect(screen, SECOND_BG_COLOR, (0, 0, WIDTH, 100))
    pg.draw.rect(screen, SECOND_BG_COLOR, (0, 650, WIDTH, 100))
    screen.blit(coin_bar, (WIDTH - 100, 0))

    print_text(str(coin_n), WIDTH - 50, 13, "", 40 - 4 * len(str(coin_n)), (255, 255, 0), screen)
    clock.tick(FPS)
    pg.display.flip()

pg.quit()
