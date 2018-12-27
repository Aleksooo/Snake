from random import randint
from Menu import *
import sys

screen = pygame.display.set_mode((s['width'], s['height']), pygame.RESIZABLE)


def food():
    global five
    five = False
    color = [apple, cherry, orange, banana, strawberry]
    while five == False:
        global pos_x
        pos_x = randint(0, s['width'] - 20)
        global pos_y
        pos_y = randint(20, s['height'] - 20)
        global colors
        colors = color[randint(0, len(color) - 1)]
        if [pos_x, pos_y] not in snake_len:
            if pos_x % 20 == 0 and pos_y % 20 == 0:
                five = True
                return pos_x, pos_y, colors

def render():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, s['width'], 20))

    score = font.render('score: {0}'.format(num), True, [255, 255, 255])
    screen.blit(score, (0, 0))

    screen.blit(colors, (pos_x, pos_y))

    for j in range(len(snake_len)):
        if j < len(snake_len) - 1:
            screen.blit(m_body, (snake_len[j][0], snake_len[j][1])) # отрисовываем змейку
        else:
            screen.blit(c_head, (snake_len[j][0], snake_len[j][1]))  # отрисовываем голову

pygame.init()
pygame.display.set_caption('Тритон')
font = pygame.font.Font(None, 30)

while game == True:

    with open('text.txt', 'rb') as f:
        s = pickle.load(f)

    pygame.time.delay(s['speed'])
    screen.fill(background) # цвет фона

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                count = {i: False for i in count}
                count['left'] = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                count = {i: False for i in count}
                count['right'] = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                count = {i: False for i in count}
                count['up'] = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                count = {i: False for i in count}
                count['down'] = True
            if event.key == pygame.K_ESCAPE:
                menu = True
                main(menu, s['width'], s['height'])

    if count['left'] == True:
        speed_x = -player_size_x
        speed_y = 0.0
        x += speed_x
        snake_len.append([x, y])
        del snake_len[0]
        c_head = pygame.transform.rotate(m_head, 90)
    elif count['right'] == True:
        speed_x = player_size_x
        speed_y = 0.0
        x += speed_x
        snake_len.append([x, y])
        del snake_len[0]
        c_head = pygame.transform.rotate(m_head, -90)
    elif count['up'] == True:
        speed_y = -player_size_y
        speed_x = 0.0
        y += speed_y
        snake_len.append([x, y])
        del snake_len[0]
        c_head = m_head
    elif count['down'] == True:
        speed_y = player_size_y
        speed_x = 0.0
        y += speed_y
        snake_len.append([x, y])
        del snake_len[0]
        c_head = pygame.transform.rotate(m_head, 180)

    for i in range(len(snake_len) - 1):
        if x == snake_len[i][0] and y == snake_len[i][1]:
            sys.exit(0)

    if eat == True: # находим положение еды
        pos_x, pos_y, colors = food()
        eat = False

    if snake_len[len(snake_len) - 1][0] == pos_x and snake_len[len(snake_len) - 1][1] == pos_y:
        eat = True
        num += 1
        snake_len.append([float(pos_x), float(pos_y)])

    if snake_len[len(snake_len) - 1][0] > s['width'] - player_size_x or snake_len[len(snake_len) - 1][0] < 0 or snake_len[len(snake_len) - 1][1] < 20 or snake_len[len(snake_len) - 1][1] > s['height'] - player_size_y:
        game = False

    render()

    pygame.display.update()