from Help import *
import sys

clik_1, clik_2, clik_3 = False, False, False
size_set = False
speed_set = False


def settings():
    font = pygame.font.Font(None, 30)
    white = (255, 255, 255)
    grey = (192, 192, 192)
    w = True
    h = False
    global s
    global set
    dict = {'wid': [white, grey, (s['width'] / 2) - 127 / 2, (s['height'] / 5), (s['width'] / 2) + 127 / 2,
                    (s['height'] / 5) + 21],
            'hig': [white, grey, (s['width'] / 2) - 105 / 2, 2 * (s['height'] / 5), (s['width'] / 2) + 105 / 2,
                    2 * (s['height'] / 5) + 21],
            'quit': [white, grey, (s['width'] / 2) - 69 / 2, 3 * (s['height'] / 5), (s['width'] / 2) + 69 / 2,
                     3 * (s['height'] / 5) + 21]}
    wid = font.render('Ширина: {} {}'.format(s['width'], s['height']), True, dict['wid'][0])
    hig = font.render('Скорость: {}'.format(s['speed']), True, dict['hig'][0])
    quit = font.render('Выход', True, dict['quit'][0])
    while set == True:

        with open('text.txt', 'rb') as f:
            s = pickle.load(f)

        pygame.time.delay(10)
        screen.fill(background)  # цвет фона

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEMOTION:
                if dict['wid'][2] - 10 < pygame.mouse.get_pos()[0] < dict['wid'][4] + 10 and dict['wid'][3] - 10 < \
                        pygame.mouse.get_pos()[1] < dict['wid'][5] + 10:
                    wid = font.render('Ширина: {} {}'.format(s['width'], s['height']), True, dict['wid'][1])
                    clik_1 = True
                else:
                    wid = font.render('Ширина: {} {}'.format(s['width'], s['height']), True, dict['wid'][0])
                    clik_1 = False

                if dict['hig'][2] - 10 < pygame.mouse.get_pos()[0] < dict['hig'][4] + 10 and dict['hig'][3] - 10 < \
                        pygame.mouse.get_pos()[1] < dict['hig'][5] + 10:
                    hig = font.render('Скорость: {}'.format(s['speed']), True, dict['hig'][1])
                    clik_2 = True
                else:
                    hig = font.render('Скорость: {}'.format(s['speed']), True, dict['hig'][0])
                    clik_2 = False

                if dict['quit'][2] - 10 < pygame.mouse.get_pos()[0] < dict['quit'][4] + 10 and dict['quit'][3] - 10 < \
                        pygame.mouse.get_pos()[1] < dict['quit'][5] + 10:
                    quit = font.render('Выход', True, dict['quit'][1])
                    clik_3 = True
                else:
                    quit = font.render('Выход', True, dict['quit'][0])
                    clik_3 = False

            if event.type == pygame.MOUSEBUTTONDOWN and clik_1 == True:
                if event.button == 1:
                    size_set = True
                    speed_set = False

            if event.type == pygame.MOUSEBUTTONDOWN and clik_2 == True:
                if event.button == 1:
                    speed_set = True
                    size_set = False

            if event.type == pygame.KEYDOWN and size_set == True:
                if event.key == pygame.K_UP:
                    if w == True:
                        s['width'] += 40
                        with open('text.txt', 'wb') as f:
                            pickle.dump(s, f)
                        wid = font.render('Ширина: {} {}'.format(s['width'], s['height']), True, dict['wid'][1])
                    if h == True:
                        s['height'] += 40
                        with open('text.txt', 'wb') as f:
                            pickle.dump(s, f)
                        wid = font.render('Ширина: {} {}'.format(s['width'], s['height']), True, dict['wid'][1])
                if event.key == pygame.K_DOWN:
                    if w == True:
                        if s['width'] > 40:
                            s['width'] -= 40
                            with open('text.txt', 'wb') as f:
                                pickle.dump(s, f)
                            wid = font.render('Ширина: {} {}'.format(s['width'], s['height']), True, dict['wid'][1])
                    if h == True:
                        if s['height'] > 40:
                            s['height'] -= 40
                            with open('text.txt', 'wb') as f:
                                pickle.dump(s, f)
                            wid = font.render('Ширина: {} {}'.format(s['width'], s['height']), True, dict['wid'][1])
                if event.key == pygame.K_RIGHT:
                    w = False
                    h = True
                if event.key == pygame.K_LEFT:
                    w = True
                    h = False

            if event.type == pygame.KEYDOWN and speed_set == True:
                if event.key == pygame.K_UP:
                    s['speed'] += 50
                    with open('text.txt', 'wb') as f:
                        pickle.dump(s, f)
                    hig = font.render('Скорость: {}'.format(s['speed']), True, dict['hig'][1])
                if event.key == pygame.K_DOWN:
                    if s['speed'] > 50:
                        s['speed'] -= 50
                        with open('text.txt', 'wb') as f:
                            pickle.dump(s, f)
                        hig = font.render('Скорость: {}'.format(s['speed']), True, dict['hig'][1])

            if event.type == pygame.MOUSEBUTTONDOWN and clik_3 == True:
                if event.button == 1:
                    print(s['width'], s['height'])
                    set = False

        screen.fill(background)  # цвет фона
        screen.blit(wid, (dict['wid'][2], dict['wid'][3]))
        screen.blit(hig, (dict['hig'][2], dict['hig'][3]))
        screen.blit(quit, (dict['quit'][2], dict['quit'][3]))

        pygame.display.update()
