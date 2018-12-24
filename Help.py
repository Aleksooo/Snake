import pygame
import pickle

player_size_x = 20.0
player_size_y = 20.0
obj = {'width': 300, 'height': 300, 'speed': 400}
'''
with open('text.txt', 'wb') as f:
    pickle.dump(obj, f)
'''
with open('text.txt', 'rb') as f:
    s = pickle.load(f)
print(s)
screen = pygame.display.set_mode((s['width'], s['height']))
x = float(s['width'] / 2 - player_size_x / 2)
y = float(s['height'] / 2 - player_size_y / 2)
speed_x = 0
speed_y = 0
background = (128, 128, 128)
count = {'left': False, 'right': False, 'up': True, 'down': False}
snake_len = [[x, y]]
eat = True
menu = False
game = True
set = True
num = 1

body = pygame.image.load('body.png')
body = pygame.transform.scale(body, (20, 20))

head = pygame.image.load('head.png')
head = pygame.transform.scale(head, (20, 20))
c_head = head

apple = pygame.image.load('food\\apple.png')  # импортируем яблоко
apple = pygame.transform.scale(apple, (20, 20))

cherry = pygame.image.load('food\\cherry.png')  # импортируем вишню
cherry = pygame.transform.scale(cherry, (20, 20))

banana = pygame.image.load('food\\banana.png')  # импортируем вишню
banana = pygame.transform.scale(banana, (20, 20))

orange = pygame.image.load('food\\orange.png')  # импортируем вишню
orange = pygame.transform.scale(orange, (20, 20))

orange = pygame.image.load('food\\orange.png')  # импортируем вишню
orange = pygame.transform.scale(orange, (20, 20))

strawberry = pygame.image.load('food\\strawberry.png')  # импортируем вишню
strawberry = pygame.transform.scale(strawberry, (20, 20))
