import pygame
from data import *

class Sprite(pygame.Rect):
    def __init__(self, cord, width, height,
                    image= None, color= None, speed= None):
        super().__init__(cord[0], cord [1], width, height)
        self.IMAGE_LIST = image
        self.IMAGE = self.IMAGE_LIST[1]
        self.IMAGE_NOW = self.IMAGE
        self.IMAGE_COUNT = 0
        self.COLOR = all_color
        self.SPEED = speed


    def move_image(self):
        self.IMAGE_COUNT += 1
        if self.IMAGE_COUNT == len(self.IMAGE_LIST) * 10 - 1:
            self.IMAGE_COUNT = 0
        if self.IMAGE_COUNT % 10 == 0:
            self.IMAGE = self.IMAGE_LIST[self.IMAGE_COUNT // 10]

class Bot(Sprite):
    def __init__(self, cord, width, height, image = None, color = None, speed = 5, vertical= None, horizontal = None):
        super().__init__(cord, width, height, image, color, speed)
        self.x1 = self.x
        self.y1 = self.y
        self.BULLET = None
        self.vertical = vertical
        self.horizontal = horizontal

    def move(self, hero, distance, way):
        if self.vertical:
            if self.collidelist(map.wall_list)!= -1 or self.y < 0 or self.y > setting_win['HEIGHT']:    
                self.SPEED *= -1
            self.y += self.SPEED
        if self.horizontal:
            if self.collidelist(map.wall_list)!= -1 or self.x < 0 or self.x > setting_win['WIDTH']:    
                self.SPEED *= -1
            self.x += self.SPEED
        self.move_image()
    def shot(self, hero, window):
        if  str(type(self.BULLET)) != "<class 'maze.Bullet'>":
            self.BULLET = Bullet(self.x, self.y + self.width // 2, 20, 10, bullet_image, 6)
        self.BULLET.x -= self.BULLET.SPEED
        self.move_image()
        window.blit(self.BULLET.IMAGE, (self.BULLET.x, self.BULLET.y))
        if hero.colliderect(self.BULLET):
            hero.restart()
            self.BULLET = None
        elif self.BULLET.x <= 0:
            self.BULLET = None

class Hero(Sprite):
    def __init__(self, cord, width, height, image = None, color = None, speed = 5):
        super().__init__(cord, width, height, image, color, speed)
        self.IMAGE = image
        self.COLOR = color
        self.SPEED = speed
        self.DIRECTION = False
        self.MOVE = {"UP": False, "DOWN": False, "RIGHT": False, "LEFT": False}

    def move(self, window):
        #функція руху
        if self.MOVE["UP"] and self.y > 0:
            self.y -= self.SPEED
            #якщо ми зтикаємся з стіною зі списка стін, то ми робимо крок назад
            if self.collidelist(map.wall_list) != -1:
                self.y += self.SPEED 
        elif self.MOVE["DOWN"]and self.y < setting_win["HEIGHT"] - self.height:
            self.y += self.SPEED
            #якщо ми зтикаємся з стіною зі списка стін, то ми робимо крок назад
            if self.collidelist(map.wall_list) != -1:
                self.y -= self.SPEED
        if self.MOVE["LEFT"] and self.x > 0:
            self.x -= self.SPEED
            #якщо ми зтикаємся з стіною зі списка стін, то ми робимо крок назад
            if self.collidelist(map.wall_list) != -1:
                self.x += self.SPEED
            self.DIRECTION = True      #потрібно дивись вліво
        elif self.MOVE["RIGHT"] and self.x < setting_win["WIDTH"] - self.width:
            self.x += self.SPEED
            #якщо ми зтикаємся з стіною зі списка стін, то ми робимо крок назад
            if self.collidelist(map.wall_list) != -1:
                self.x -= self.SPEED
            self.DIRECTION = False     #потрібно дивитись вправо

        #якщо персонаж рухується, то потрібно змінювати картинки, інакше ставимо картинку героя, де він стоїть на місці
        if self.MOVE["UP"] or self.MOVE["DOWN"] or self.MOVE["LEFT"] or self.MOVE["RIGHT"]:
            print('1')
            self.move_image()
        else:
            self.IMAGE = self.IMAGE_LIST[1]
        if self.DIRECTION:
            self.IMAGE_NOW = pygame.transform.flip(self.IMAGE, True, False)
        else:
            self.IMAGE_NOW = self.IMAGE
        #демонструємо картинку на екран
        window.blit(self.IMAGE_NOW, (self.x, self.y))
    def restart(self):
        self.x = 10
        self.y = 10


class Wall(pygame.Rect):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height)
        self.COLOR = color

    def draw_rect(self, window):
        pygame.draw.rect(window, self.COLOR, self)

class Bullet(pygame.Rect):
    def __init__(self, x, y, width, height, image, speed):
        super().__init__(x, y, width, height)   
        self.IMAGE = image
        self.SPEED = speed

    def move(self, x1, y1, distance, way):
        if way == 'x':
            if self.x > self.x1 + distance // 2 or self.x < self.x1 - distance // 2:
                self.SPEED *= -1
            self.x += self.SPEED
        elif way == 'y':
            if self.y > self.y1 + distance // 2 or self.y < self.y1 - distance // 2:
                self.SPEED *= -1
            self.y += self.SPEED
        self.move_image()
        
class Key(pygame.Rect):
    def __init__(self, cord, width, height, image):
        super().__init__(cord[0], cord [1], width, height)   
        self.IMAGE = image
        self.CHECK = False

    def collide(self, hero, window):
        window.blit(self.IMAGE, (self.x, self.y))

        if hero.colliderect(self):
            self.CHECK = True
            self.x = 2000

class Door(pygame.Rect):
    def __init__(self, cord, width, height, image):
        super().__init__(cord[0],cord[1], width, height)   
        self.IMAGE = image
    
    def collide(self, hero, window, lvl, bot1, bot2):
        window.blit(self.IMAGE, (self.x, self.y))

        if hero.colliderect(self):
            render = pygame.font.Font(None, 200).render("YOU WIN", True, all_color["BLACK"])
            window.blit(render, (setting_win["WIDTH"] // 2 - 50, setting_win["HEIGHT"] // 2))
            lvl.level += 1 
            restart(lvl.level, hero, bot1, bot2)

class Map():
    def __init__(self, maps):
        self.maps = maps
        self.wall_list = list()
map = Map(maps)

class Level():
    def __init__(self):
        self.level = 1
        
def restart(level, hero, bot1, bot2):
    map.wall_list = list()
    create_wall(map.maps["MAP" + str(level)]['map'])
    hero.x, hero.y = map.maps["MAP" + str(level)]['hero']
    bot1.x, bot1.y = map.maps["MAP" + str(level)]['bot1']
    bot2.x, bot2.y = map.maps["MAP" + str(level)]['bot2']


def create_wall(map_now):
    x, y = 0, 0
    step = 20
    x1, y1 = 0, 0
    index_x, index_y = 0, 0

    for line in map_now:
        for element in line:
            if element == "1":
                y1 = y
                tmp_index_y = index_y 
                while True:
                    y1 += step
                    tmp_index_y += 1
                    if map_now[tmp_index_y][index_x] == "2":
                        map.wall_list.append(Wall(x, y, step, y1 - y + step, all_color["PURPLE"]))
                        break
            if element == "3":
                x1 = x
                tmp_index_x = index_x
                while True:
                    x1 += step
                    tmp_index_x += 1
                    if map_now[index_y][tmp_index_x] == "4":
                        map.wall_list.append(Wall(x, y, x1 - x + step, step, all_color["PURPLE"]))
                        break
                    
            x += step
            index_x += 1
        x = 0
        y += step
        index_y += 1
        index_x = 0

create_wall(map.maps["MAP1"]['map'])

