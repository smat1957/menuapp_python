import os
import sys
import csv
import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_a, K_q, K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, QUIT
import subprocess
from subprocess import PIPE
import tkinter
import random
from datetime import datetime

path_w = "/home/pi/Videos/"

def shutdown(tstr="16:45"):
    cmd0 = "sudo shutdown -c"
    cmd1 = "sudo shutdown -h "+tstr
    os.system(cmd0)
    os.system(cmd1)

def fine():
    pygame.quit()
    sys.exit()

def key_event(mn):
    for event in pygame.event.get():
        if event.type == QUIT:
            fine()
        elif event.type == KEYDOWN:
            #print('debug=>',event.key)
            if event.key == K_ESCAPE:
                #pygame.display.toggle_fullscreen()
                return
            elif event.key == K_0:
                logkey='1'
                fname = mn[9][1]
            elif event.key == K_1:
                logkey='2'
                fname = mn[0][1]
            elif event.key == K_2:
                logkey='3'
                fname = mn[1][1]
            elif event.key == K_3:
                logkey='4'
                fname = mn[2][1]
            elif event.key == K_4:
                logkey='5'
                fname = mn[3][1]
            elif event.key == K_5:
                logkey='6'
                fname = mn[4][1]
            elif event.key == K_6:
                logkey='7'
                fname = mn[5][1]
            elif event.key == K_7:
                logkey='8'
                fname = mn[6][1]
            elif event.key == K_8:
                logkey='9'
                fname = mn[7][1]
            elif event.key == K_9:
                logkey='0'
                fname = mn[8][1]
            
            elif event.key == K_a:
                rndmlist = random.sample( list(range(10)), 10 )
                fname = ' '
                for n in rndmlist:
                    fname = fname + mn[n][1] + ' '
                flog('A')
                subprocess.run(path_w + "show_all.sh " + fname,\
                               shell=True, stdout=PIPE, stderr=PIPE, text=True)
                return
            
            elif event.key == K_q:
                fine()
            else:
                return
            flog(logkey)
            subprocess.run(path_w + "show.sh " + fname,\
                           shell=True, stdout=PIPE, stderr=PIPE, text=True)
        else:
            pass

def finput():
    with open(path_w + 'menu.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        l = [row for row in reader]
    return l

def flog(item='_'):
    fname = "log_"
    dt_now = str(datetime.now())
    with open(path_w+fname+item, mode='a') as f:
        f.write(dt_now + '\n')
        
def gen_menu(items, HEIGHT):
    #print('debug=>',pygame.font.get_fonts())
    COLOR1 = (10,10,10)
    sk = HEIGHT//len(items)
    menu = []
    font = pygame.font.SysFont("takao", 30)
    for i, t in enumerate(items):
        text = font.render(t[0], True, COLOR1)
        tr   = text.get_rect()
        tr.left = surface.get_rect().left + 10
        tr.top  = surface.get_rect().top + sk * i + 8
        menu.append([text, tr])
    return menu

def screen_pos(WIDTH, HEIGHT, xoff=0, yoff=0):
    root = tkinter.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = WIDTH
    window_height = HEIGHT
    pos_x = (screen_width - window_width)//2 + xoff
    pos_y = (screen_height - window_height)//2 + yoff
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x,pos_y)
    os.environ['SDL_VIDEO_CENTERED'] = '0'

if __name__ == '__main__':
    shutdown('+480')
    pygame.init()
    WIDTH = 800
    HEIGHT = 600
    WSIZE = (WIDTH, HEIGHT)
    screen_pos(WIDTH,HEIGHT)
    surface = pygame.display.set_mode( WSIZE )
    #surface = pygame.display.set_mode( WSIZE, pygame.FULLSCREEN )
    pygame.display.set_caption('左の [数値] を選んで下さい')
    clock = pygame.time.Clock()
    FPS = 10
    WHITE = (255, 255, 255)
    items = finput()
    menu = gen_menu(items, HEIGHT)
    while True:
        key_event( items )
        surface.fill( WHITE )
        for m in menu:
            surface.blit(m[0], m[1])
        pygame.display.update()
        clock.tick( FPS )
    fine()
