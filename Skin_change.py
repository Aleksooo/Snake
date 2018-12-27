from Help import *
import sys
def Skin_change(a, b, c):
    font = pygame.font.Font(None, 30)
    white = (255, 255, 255)
    skins = {'label_1': [white, (b / 2) - 127 / 2, (c / 5), (b / 2) + 127 / 2, (c / 5) + 21],
             'label_2': [white, (b / 2) - 127 / 2, 2 * (c / 5), (b / 2) + 127 / 2, 2 *(c / 5) + 21],
    }
    label_head = font.render('Изменить голову', True, skins['label_1'][0])
    label_body = font.render('Изменить туловище', True, skins['label_2'][0])
    while a == True:
        pygame.time.delay(10)
        screen.fill(background)  # цвет фона

        screen.blit(label_head, (skins['label_1'][1], skins['label_1'][2]))
        screen.blit(label_body, (skins['label_2'][1], skins['label_2'][2]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        pygame.display.update()