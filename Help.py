import pygame
import pickle

player_size_x = 20.0
player_size_y = 20.0
obj = {'width': 300, 'height': 300, 'speed': 400, 'skin1': True, 'skin2': False, 'skin3': False}
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
skin = False
num = 1

body1 = pygame.image.load('skin1\\body1.png')
body1 = pygame.transform.scale(body1, (20, 20))

head1 = pygame.image.load('skin1\\head1.png')
head1 = pygame.transform.scale(head1, (20, 20))


body2 = pygame.image.load('skin2\\body2.png')
body2 = pygame.transform.scale(body2, (20, 20))

head2 = pygame.image.load('skin2\\head2.png')
head2 = pygame.transform.scale(head2, (20, 20))

if s['skin1'] == True:
    m_head = head2
    m_body = body2
    c_head = head1
'''
elif s['skin2'] == True:
    m_head = head2
    m_body = body2
    c_head = head2
'''
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
