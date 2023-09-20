import pygame
import os
import json

setting_win = {
    "WIDTH": 1000,
    "HEIGHT": 600
}

all_color = {
    "WHITE": (255, 255, 255),
    "GREEN": (50, 150, 125),
    "PURPLE": (255, 255, 0),
    "BLACK": (0, 0, 0)
}

maps = {
    "MAP1":{
        "map": [
        "0000010000000000000000000000000000000000010000000000000",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000013000000000004100000000000000000000000000",
        "0000000000000000000000000000000000000000020000000000000",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000020000000000000200000000000013000000000040",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000100000000100000000040000000003000000000040",
        "0000000000000000000000000000000000000000020000000000000",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000030000000200000004100000000000000000000000",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000000000000000000000030000000040000000000000",
        "0000000000000000000000000000000000000000000000000000000",
        "0000023000004200000003000000004200000000000000000000000",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000000000000000000000000000000001300000000040",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000000000000000000000000000000000000000000000",
        "0000000000000000000000000000000000000000002000000000000",
        ],
        "hero": [10, 10],
        "bot1": [150, 300],
        "bot2": [setting_win["WIDTH"] - 100, setting_win['HEIGHT'] - 110],
        "key": [500, 30],
        "door": [900, 10]
    
    },
    "MAP2":{
        "map": [
            "0000000000000000000000000000000000000000010000000000000",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000013000000000004100000000000000000000000000",
            "0000000000000000000000000000000000000000020000000000000",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000020000000000000200000000000013000000000040",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000100000000100000000040000000003000000000040",
            "0000000000000000000000000000000000000000020000000000000",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000030000000200000004100000000000000000000000",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000000000000000000000030000000040000000000000",
            "0000000000000000000000000000000000000000000000000000000",
            "0000003000004200000003000000004200000000000000000000000",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000000000000000000000000000000001300000000040",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000000000000000000000000000000000000000000000",
            "0000000000000000000000000000000000000000002000000000000",
            ],
            "hero": [10, 10],
            "bot1": [150, 300],
            "bot2": [setting_win["WIDTH"] - 100, setting_win['HEIGHT'] - 110],
            "key": [500, 30],
            "door": [900, 10]

        }    

}


with open('data.json', "w", encoding= "utf-8") as file:
    json.dump(maps, file, ensure_ascii= False, indent = 4)
with open('data.json', "w", encoding= "utf-8") as file:
    pass




wall_list = list()

abs_path = os.path.abspath(__file__ + "/..") + "\\images\\"
name_images_list = os.listdir(abs_path)
images_list = list()
print (name_images_list)
for name_image in name_images_list:
    images_list.append(pygame.image.load(abs_path + name_image))

print(name_images_list)

hero_list = [images_list[4], images_list[5]]

walk_list = [pygame.transform.scale(images_list[7],(100,100)),
            pygame.transform.scale(images_list[8],(100,100))]
bullet_list = [pygame.transform.scale(images_list[1], (100,100)),
                pygame.transform.scale(images_list[2], (100,100))]
bullet_image = images_list[0]
key_image = images_list[6]
door_image = images_list[3]