from Help import *
from Settings import *

clik1, clik2, clik3 = False, False, False


def main(a, b, c):
    font = pygame.font.Font(None, 30)
    white = (255, 255, 255)
    grey = (192, 192, 192)
    global set
    dic = {'cont': [white, grey, (b / 2) - 127 / 2, (c / 5), (b / 2) + 127 / 2, (c / 5) + 21],
           'sett': [white, grey, (b / 2) - 105 / 2, 2 * (c / 5), (b / 2) + 105 / 2, 2 * (c / 5) + 21],
           'quit': [white, grey, (b / 2) - 69 / 2, 3 * (c / 5), (b / 2) + 69 / 2, 3 * (c / 5) + 21]}
    cont = font.render('Продолжить', True, dic['cont'][0])
    sett = font.render('Настройки', True, dic['sett'][0])
    quit = font.render('Выход', True, dic['quit'][0])
    while a == True:
        pygame.time.delay(10)
        screen.fill(background)  # цвет фона
        screen.blit(cont, (dic['cont'][2], dic['cont'][3]))
        screen.blit(sett, (dic['sett'][2], dic['sett'][3]))
        screen.blit(quit, (dic['quit'][2], dic['quit'][3]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(9)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    a = False
            if event.type == pygame.MOUSEMOTION:
                if dic['cont'][2] - 10 < pygame.mouse.get_pos()[0] < dic['cont'][4] + 10 and dic['cont'][3] - 10 < \
                        pygame.mouse.get_pos()[1] < dic['cont'][5] + 10:
                    cont = font.render('Продолжить', True, grey)
                    clik1 = True
                else:
                    cont = font.render('Продолжить', True, white)
                    clik1 = False

                if dic['sett'][2] - 10 < pygame.mouse.get_pos()[0] < dic['sett'][4] + 10 and dic['sett'][3] - 10 < \
                        pygame.mouse.get_pos()[1] < dic['sett'][5] + 10:
                    sett = font.render('Настройки', True, grey)
                    clik2 = True
                else:
                    sett = font.render('Настройки', True, white)
                    clik2 = False

                if dic['quit'][2] - 10 < pygame.mouse.get_pos()[0] < dic['quit'][4] + 10 and dic['quit'][3] - 10 < \
                        pygame.mouse.get_pos()[1] < dic['quit'][5] + 10:
                    quit = font.render('Выход', True, grey)
                    clik3 = True
                else:
                    quit = font.render('Выход', True, white)
                    clik3 = False

            if event.type == pygame.MOUSEBUTTONDOWN and clik1 == True:
                if event.button == 1:
                    print('ok')
                    a = False
                    clik1 = False
            if event.type == pygame.MOUSEBUTTONDOWN and clik2 == True:
                if event.button == 1:
                    print('ok')
                    set = True
                    settings()
                    a = False
                    clik2 = False
            if event.type == pygame.MOUSEBUTTONDOWN and clik3 == True:
                if event.button == 1:
                    sys.exit(0)
                    clik3 = False

        pygame.display.update()
