import pygame
from data import *
from maze import *

pygame.init()

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("MAZE")

def run():
    game = True
    lvl = Level()
    clock = pygame.time.Clock()
    hero = Hero (maps["MAP" + str(lvl.level)]['hero'], 75, 75, color= all_color["GREEN"], image= hero_list)
    bot1 = Bot(maps["MAP" + str(lvl.level)]['bot1'],75,75,image= walk_list, speed= 4, vertical= True)
    bot2 = Bot(maps["MAP" + str(lvl.level)]['bot2'], 86, 100, image= bullet_list)
    key = Key(maps["MAP" + str(lvl.level)]['key'], 50, 25, key_image)
    

    while game:
        window.fill(all_color["WHITE"])
        
        
        for wall in map.wall_list:
            wall.draw_rect(window)


        hero.move(window)

        bot1.move(hero, 400, 'y')
        window.blit(bot1.IMAGE, (bot1.x, bot1.y))

        bot2.shot(hero, window)
        window.blit(bot2.IMAGE, (bot2.x, bot2.y))
        
        if not key.CHECK:
            key.collide(hero,window)
            door = Door(maps["MAP" + str(lvl.level)]['door'], 900, 150, door_image)
        elif key.CHECK:
            door.collide(hero, window, lvlw, bot1, bot2)
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero.MOVE["UP"] = True
                if event.key == pygame.K_s:
                    hero.MOVE["DOWN"] = True
                if event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = True
                if event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    hero.MOVE["UP"] = False
                if event.key == pygame.K_s:
                    hero.MOVE["DOWN"] = False
                if event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = False
                if event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = False

        clock.tick(60)
        pygame.display.flip()        


run()
