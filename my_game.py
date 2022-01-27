import random
import sys

import pygame as pg
from start import start_menu


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
        # print('coin')
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
            # self.catch = True
            # self.rect.x, self.rect.y = random.randint(50, WIDTH - 50), random.randint(200, HEIGHT - 200)
            self.kill()
            coin_here = False
            coin_n += 1
            f = open('./data/coin.txt', 'w')
            f.write(str(coin_n))
            f.close()
            # print('coin', coin_n)
            # self.catch = False
            # else:
            #     self.up = True
        # else:
        #     self.up = True

        # if pg.sprite.spritecollideany(self, all_sprites):
        #     coin_n += 1
        #     print('                                                                 ' + str(coin_n))
        #     # self.kill()
        #     tic = 0


# import keyboard
class Wall(pg.sprite.Sprite):

    def __init__(self, screen, x, y):
        super().__init__(wall_group)

        self.image = pg.image.load('./data/wall.png')
        self.rect = self.image.get_rect()
        if x == 0:
            self.image = pg.transform.flip(self.image, 50, 0)

        self.rect.x, self.rect.y = x, y

        self.mask = pg.mask.from_surface(self.image)

        # if rotate == 'left':
        #     self.image = pg.transform.flip(self.image, 50, 0)

        # for k in range(int(lvl)):
        #     self.rect.copy()

        # for i in range(lvl):
        #     y = random.randrange(100, 650, 26)
        #     print(lvl)
        #     self.image = pg.transform.flip(self.image, 50, 0)
        #     self.rect = self.image.get_rect().copy()
        #     self.rect.x, self.rect.y = x, y

        # if rotate == 'left':
        #     self.image = pg.transform.flip(self.image, 50, 0)
        # if rotate == 'up':
        #     self.image = pg.transform.rotate(self.image, 90)
        # if rotate == 'down':
        #     self.image = pg.transform.rotate(self.image, 270)

    # def update(self):

    #


class Bird(pg.sprite.Sprite):
    image = pg.image.load('./data/bird.png')

    def __init__(self, *group):
        super().__init__(*group)

        self.image = Bird.image
        self.rect = self.image.get_rect()
        # print(self.rect)

        self.rect.center = WIDTH // 2, HEIGHT // 2

        self.pressed = False
        self.fall = False

        self.isJump = False
        self.jumpCount = 30

        self.speed = 5

        self.mask = pg.mask.from_surface(self.image)

    def update(self):
        global GRAVITY, BG_COLOR, play, count, coin_here
        up_gravity = 1
        keys = pg.key.get_pressed()
        # pg.key.set_repeat(0)
        # if keys[pg.K_SPACE]:
        #     print(tic)

        # print(self.pressed)

        if pg.sprite.spritecollideany(self, wall_group):
            play = False

        # if -10 < self.rect.x < 10:
        #     print(list_of_left)
        #
        #     for i in list_of_left:
        #         print(i)
        #         pg.draw.rect(screen, RED, (0, i, 20, 25), 0)
        #         if i - 25 < self.rect.y < i + 50:
        #             play = False
        #             # self.speed = 0
        #             print(44555)
        #     list_of_left.clear()

        self.pressed = False
        if self.rect.y >= HEIGHT - 150:
            # print('lose')
            BG_COLOR = (230, 230, 230)
            play = False
        #
        #     self.fall = True
        #     self.pressed = True
        #     print(12222)
        #     self.pressed = False
        # self.jump()
        # if GRAVITY >= 3:
        #     GRAVITY = 1
        # self.pressed = True
        # self.fall = False
        # self.rect.y -= up_gravity
        # up_gravity += 0.25
        # GRAVITY = 1

        if not self.fall:

            self.rect.y += GRAVITY
            GRAVITY += 0.10
            # else:
            #     self.rect.y -= 50
            if self.rect.y > HEIGHT:
                self.rect.y = HEIGHT // 2
                GRAVITY = 1
                # if self.rect.y == 700:
                #     print('end')
        self.rect.x += self.speed
        if self.rect.x >= WIDTH - 50 or self.rect.x <= 0:
            # print(self.rect.x)
            wall_group.empty()
            # list_of_left.clear()
            if self.speed > 0:
                wall_create('left')

            elif self.speed < 0:
                wall_create('right')

            self.image = pg.transform.flip(self.image, 50, 0)

            if not coin_here:
                coin_create()

            self.speed *= -1

            # if self.speed > 0 and self.rect.x > WIDTH // 2:
            #     list_of_left.clear()

            # list_of_left.clear()

            count += 1
            # print(count)
            if count % 10 == 0:
                R, G, B = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
                BG_COLOR = (G, G, B)

        # if pg.sprite.collide_rect(self, wall_group):
        #     print(155 )
        # for i in list_of_right:
        #     print(i)
        #     if i < self.rect.y < i + 25:
        #         print(222)
        # if pg.sprite.collide_mask(self, Wall):
        #     print(1858585)

    def jump(self, fall):
        global GRAVITY, press
        press = False
        self.fall = fall
        GRAVITY = 1
        self.rect.x += 1
        # Check if mario is jumping and then execute the
        # jumping code.

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
                # if self.rect.y <= 0:
                #     self.rect.y += self.jumpCount ** 2 * 0.1 * neg
                # self.jumpCount += 1
            else:
                self.fall = False
                self.isJump = False

                self.jumpCount = 30
            # self.pressed = False

        else:
            self.rect.y += GRAVITY
            if self.rect.y > HEIGHT:
                self.rect.y = HEIGHT // 2
                GRAVITY = 1

        # keys = pg.key.get_pressed()
        # pg.key.set_repeat(0)
        # if keys[pg.K_SPACE]:
        #     self.pressed = True
        #     pg.key.set_repeat(70, 100)
        #     save_y = self.rect.y
        #     if self.rect.y <= save_y:
        #         self.rect.y += -GRAVITY
        #         GRAVITY = 1
        #     # self.pressed = False
        # else:
        #     self.pressed = False
        # self.rect.y += GRAVITY
        # if self.fall:

    # def fly(self):
    #     if self.rect.y <= 50:
    #         self.rect.y += -GRAVITY
    #         self.fall = True
    #     # if self.rect.y >=
    # print(self.rect.y)


def coin_create():
    coin_group.empty()
    random_count = random.choice([0, 1, 2, 3, 4, 5])
    coin_x, coin_y = random.randint(50, WIDTH - 50), random.randint(200, HEIGHT - 200)
    # if coin_n == 0:
    #     coin = Coin(coin_x, coin_y)
    # else:
    if random_count == 0:
        coin = Coin(coin_x, coin_y)


lvl = 3
count_r = 0


def wall_create(now_r):
    global lvl, count_r
    print(count_r)
    wall_group.empty()
    count_of_place = (HEIGHT - 100 - 100) // 25
    # print('count', count_of_place)

    # print(str(lvl))
    if count_r == 5 and lvl <= 18:
        count_r = 0
        lvl += 1
    count_r += 1
    # if count == 0:
    #     lvl = 1
    # else:
    #     lvl = count_of_place // count

    # if count % 10 == 0:
    #     lvl += 1

    if now_r == 'right':
        x = WIDTH - 20
    else:
        x = 0
    for i in range(lvl):
        y = random.randrange(100, 650, 50)
        Wall(screen, x, y)
        list_of_left.append(y)


def create():
    wall_create('right')
    coin_create()

    # if x == 0:
    #     pg.draw.polygon(screen, RED, [(x, y),
    #                                   (x + 20, y + 25 // 2),
    #                                   (x, y + 25)], 1)
    # x_pos, y_pos = 0, 630
    # for i in range(WIDTH // 25):
    #     wall = Wall(screen, x_pos, y_pos)
    #     x_pos += 25


def print_text(text, x, y, font_input, font_size, color, screen):
    font = pg.font.SysFont(font_input, font_size, True, False)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


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
# play = False


BLACK = (0, 0, 0)
RED = (255, 0, 0)
WALL_GRAY = (96, 96, 96)
tic = 0
# random_count = 0

all_sprites = pg.sprite.Group()
wall_group = pg.sprite.Group()
coin_group = pg.sprite.Group()
bird = Bird(all_sprites)

r, g, b = (230, 230, 230)
BG_COLOR = (r, g, b)
x = 0
y = 0
# procents = [10, 20, 30, 40, 50, 60, 70, 80]
mony = 0

# lvl = ((HEIGHT - 200) // 26) * procents[5] // 100
# print(((HEIGHT - 200) // 26))
# print(lvl)
list_of_left = []
list_of_right = []
# for i in range(int(lvl)):
# wall = Wall(screen) # x, y, 'left'
# y = random.randrange(100, 650, 26)


play = start_menu(False)

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

# for k in range(WIDTH // 25):
#     wall = Wall()
#     x += 25
# y = 610
# x = 0
# for k in range(WIDTH // 25):
#     wall = Wall()
#     x += 25
# coin_x, coin_y = random.randint(50, WIDTH - 50), random.randint(200, HEIGHT - 200)
# coin = Coin(coin_x, coin_y)

while running:
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
            running = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and not press:
                pg.event.poll()
                print('here')
                press = True
                print(press)
                pg.key.set_repeat(0, 0)
                # if not press:
                press = True

                bird.jump(True)
                break
                    # print(123)
                    # press = True

        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                bird.jump(False)
                press = False

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if (230 < mouse_pos[0] < 380) and (400 < mouse_pos[1] < 450) and not play:
                count = 0
                BG_COLOR = (230, 230, 230)
                wall_create('right')
                coin_create()
                bird.image = pg.image.load('./data/bird.png')
                if bird.speed < 0:
                    bird.speed *= -1
                coin_here = False
                play = True
            if (230 < mouse_pos[0] < 380) and (500 < mouse_pos[1] < 550) and not play:
                count = 0
                BG_COLOR = (230, 230, 230)

                play = start_menu(False)

    # keys = pg.key.get_pressed()
    # if keys[pg.K_SPACE]:
    #     bird.fly()
    #     # print(bird.rect.y)
    # else:
    #     GRAVITY = 1

    # take_fps = clock.tick(FPS)
    # GRAVITY = GRAVITY_speed * take_fps // 1000
    screen.fill(BG_COLOR)
    GRAVITY += 0.25

    # if pg.sprite.spritecollideany(Bird, Wall):
    #     print(11111)
    # if pg.sprite.collide_rect(Bird.rect, Wall.rect):
    #     print(4747)
    # if press:
    #     tic += 1
    #     if tic >= FPS:
    #         bird.jump(False)
    # if Bird.rect > HEIGHT:
    #     GRAVITY = 1
    SECOND_BG_COLOR = (BG_COLOR[0] - BG_COLOR[0] // 4,
                       BG_COLOR[1] - BG_COLOR[1] // 4,
                       BG_COLOR[2] - BG_COLOR[2] // 4)
    if play:

        pg.draw.circle(screen, SECOND_BG_COLOR, (WIDTH // 2, HEIGHT // 2), 150)
        print_text(str(count), text_x, HEIGHT // 2 - 55, "Cascadia Code SemiBold", 192, BG_COLOR, screen)
        text_x = WIDTH // 2 - (len(str(count)) * 40)
        # print(BG_COLOR)
        all_sprites.update()
        coin_group.update()
        all_sprites.draw(screen)
        wall_group.draw(screen)

        tic += 1
        # if tic >= 10 * FPS:
        coin_group.draw(screen)
    else:
        bird.rect.x, bird.rect.y = WIDTH // 2, HEIGHT // 2
        GRAVITY = 1
        screen.blit(game_over, (210, 100))

        print_text(f'Счет: {count}', 240, 250, "", 40, RED, screen)
        screen.blit(restart, (230, 400))
        screen.blit(home, (230, 500))

        # print(255)
        # pg.draw.rect(screen, RED, (0, 0, WIDTH, HEIGHT))

    pg.draw.rect(screen, SECOND_BG_COLOR, (0, 0, WIDTH, 100))
    pg.draw.rect(screen, SECOND_BG_COLOR, (0, 650, WIDTH, 100))
    screen.blit(coin_bar, (WIDTH - 100, 0))
    print_text(str(coin_n), WIDTH - 50, 13, "", 40 - 2 * len(str(coin_n)), (255, 255, 0), screen)
    # pg.draw.rect(screen, RED, (wall.rect.x, wall.rect.y, 20, 25), 1)
    clock.tick(FPS)
    pg.display.flip()

pg.quit()
