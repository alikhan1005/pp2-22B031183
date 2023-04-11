import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))
surf = pg.Surface((700, 600))
buttons = pg.Surface((100, 210)) # создаю панель кнопок
font = pg.font.SysFont("Verdana", 15)
cur_color = 'white' # текущий цвет который могу менять
# создаем словарь комманд
commands = {
    'line': [4, 4, 44, 44],
    'rect': [52, 4, 44, 44],
    'circle': [4,50, 44, 44],
    'eraser': [52, 50, 44, 44]
}
# функция для установки панели с кнопочек
def setsurf():
    surf.fill('black')
    buttons.fill('white')
    pg.draw.rect(buttons, 'black', (2, 2, 96, 206), 1)
    for i in commands:
        pg.draw.rect(buttons, 'black', commands[i], 1)
    
    pg.draw.aaline(buttons, 'black', (8, 8), (40, 40), 1)
    pg.draw.rect(buttons, 'black', (58, 10, 32, 32), 1)
    pg.draw.circle(buttons, 'black', (27, 70), 15, 1)
    pg.draw.rect(buttons, 'black', (56, 58, 36, 28))
    screen.blit(surf, (0, 0))
    screen.blit(buttons, (700, 0))
# функция для отрисовки линии
def line(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pg.draw.circle(screen, color, (x, y), d)
    else:   
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pg.draw.circle(screen, color, (x, y), d)
# функция для отрисовки прямоугольника
def rectangle(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1-x2)
    height = abs(y1-y2)

    if x1 <= x2:
        if y1 < y2:
            pg.draw.rect(screen, color, (x1, y1, width, height), d)
        else:
            pg.draw.rect(screen, color, (x1, y2, width, height), d)
    else:
        if y1 < y2:
            pg.draw.rect(screen, color, (x2, y1, width, height), d)
        else:
            pg.draw.rect(screen, color, (x2, y2, width, height), d)
# функция для отрисовки круга
def circle(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1-x2)
    height = abs(y1-y2)

    if x1 <= x2:
        if y1 < y2:
            pg.draw.ellipse(screen, color, (x1, y1, width, height), d)
        else:
            pg.draw.ellipse(screen, color, (x1, y2, width, height), d)
    else:
        if y1 < y2:
            pg.draw.ellipse(screen, color, (x2, y1, width, height), d)
        else:
            pg.draw.ellipse(screen, color, (x2, y2, width, height), d)

last_pos = (0, 0)
w = 2
draw_line = False
erase = False
ed = 50

d = {
    'line' : True,
    'rect': False,
    'circle': False,
    'eraser': False
}

setsurf()
running = True
while running:
    pos = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # меняем цвета при нажатии на клавиши  
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                cur_color = 'red'
            if event.key == pg.K_2:
                cur_color = 'green'
            if event.key == pg.K_3:
                cur_color = 'blue'
            if event.key == pg.K_4:
                cur_color = 'white'  
        # при нажатии на область определенной кнопочки меняем значение соответственной команды на True в словаре комманд
        if event.type == pg.MOUSEBUTTONDOWN:
            for k, v in commands.items():
                if v[0] <= pos[0]-700 <= v[0] + v[2] and v[1] <= pos[1] <= v[1] + v[3]:
                    d[k] = True
                    for i, j in d.items():
                        if i != k:
                            d[i] = False
                    break
        # запускаем функции соответственных комманд  
        if d['line'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
                pg.draw.circle(surf, cur_color, pos, w)
                draw_line = True
            if event.type == pg.MOUSEBUTTONUP:
                draw_line = False
            if event.type == pg.MOUSEMOTION:
                if draw_line:
                    line(surf, last_pos, pos, w, cur_color)
                last_pos = pos
        elif d['rect'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                rectangle(surf, last_pos, pos, w, cur_color)
        elif d['circle'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                circle(surf, last_pos, pos, w, cur_color)
        elif d['eraser'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                (x, y) = pos
                pg.draw.rect(surf, 'black', (x, y, ed, ed))
                erase = True
            if event.type == pg.MOUSEMOTION:
                if erase:
                    pg.draw.rect(surf, 'black', (pos[0], pos[1], ed, ed))
            if event.type == pg.MOUSEBUTTONUP:
                erase = False
    # выделяю красной рамкой выбранную комманду
    for k, v in d.items():
        if v == True:
            pg.draw.rect(buttons, 'red', commands[k], 1)
        else:
            pg.draw.rect(buttons, 'black', commands[k], 1)
    
    screen.blit(buttons, (700, 0))
    screen.blit(surf, (0, 0))
    c = font.render('Press:', True, 'black')
    buttons.blit(c, (5, 100))
    r = font.render('1 - Red', True, 'black')
    buttons.blit(r, (5, 120))
    g = font.render('2 - Green', True, 'black')
    buttons.blit(g, (5, 140))
    b = font.render('3 - Blue', True, 'black')
    buttons.blit(b, (5, 160))
    y = font.render('4 - White', True, 'black')
    buttons.blit(y, (5, 180))

    pg.display.update()
pg.quit()