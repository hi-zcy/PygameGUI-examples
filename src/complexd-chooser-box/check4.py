import pygame,random
import sys
from pygame.locals import *

import pygameGUI as pg

# 颜色常量
WHITE = (255,255,255)
BLACK = (0,0,0)

size = width, height = 800,600

screen = pygame.display.set_mode(size)

pygame.display.set_caption("title")

clock = pygame.time.Clock()

delay = 60 # 延时计时器(1秒)

# 是否全屏
fullscreen = False
screen_change = False

# 背景颜色设定
bg_color = (80,80,80)

running = True

# ui=====

guis = pg.Group()

# 窗口
def w_image(image):
    image.fill([50,200,200])
    pygame.draw.rect(image,rect=image.get_rect(),color=[0,0,0],width=1)
    return image
w = pg.Window(group=guis,pos=[250,100],size=[300,400],texture=w_image)
 # 标题
text=pg.Label(text="世界上最好的脚本语言是？",font=("arialms",15)).image
def title_image(image):
    image.fill((80,200,200))
    image.blit(text,[35,5])
    image.blit(pygame.image.load("pygame.png"),[12,8])
    return image
w.set_title(pos=[1,1],size=[298,28],texture=title_image)
 # 关闭按钮
def init_texture(image):
    image.fill([255,10,10])
    image.blit(pg.Label(text="X",font=("arialms",20),bold=False,color=(255,255,255)).image,[7,0])
    return image
def active_texture(image):
    image.fill([255,10,10])
    image.blit(pg.Label(text="X",font=("arialms",20),bold=False,color=(255,255,255)).image,[7,0])
    i = image.copy()
    i.fill([0,0,0,10])
    image.blit(i,[0,0])
    return image
w_cb = w.set_close_button(pos=[10,10],size=[28,28],init_texture=init_texture,active_texture=active_texture,block=True)
w_cb.set_pos("topright",[w.rect[2]-1-2,1+2])

# 内部外层框架
f = pg.Frame(group=w,pos=[10,w.title.rect[3]+w.title.rect[1]+10],
             size=[w.rect[2]-20,w.rect[3]-w.title.rect[3]-2-20],
             texture=[255,255,255])
def image(image):
    image.fill(([255,255,255]))
    pygame.draw.rect(image,rect=image.get_rect(),color=[0,0,0],width=1)
    return image
f.set_image(size=[f.rect[2], f.rect[3]],texture=image)

# 内部框架内层
def image(image):
    image.fill(([255,255,255]))
    pygame.draw.rect(image,rect=image.get_rect(),color=[100,100,100],width=1)
    return image
f1 = pg.Frame(group=f,pos=[10,30],
             size=[w.rect[2]-40,w.rect[3]-w.title.rect[3]-2-60],
             texture=image)

# 内部框架标签
l1 = pg.Label(group=f,text="最好的脚本语言是：",font=("stfangsong",25),bg=(255,255,255))
l1.set_pos("center",[f1.rect.center[0],f1.rect.y])

# 按钮 python
text=pg.Label(text="Python",font=("stfangsong",25),bg=(255,255,255)).image
rect=text.get_rect()
def image(image):
    image.fill((255,255,255))
    pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)
    image.blit(text,[5,3])
    return image
b1 = pg.Button(group=f1,size=(rect[2]+10,rect[3]+10),init_texture=image)
b1.set_pos("topleft",[f1.rect[0]+2,l1.rect[3]/2+2])
def image(image):
    image.fill((255,255,255))
    pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(0,0,0),width=1)
    image.blit(text,[5,3])
    return image
b1.set_image(state="active",texture=image,size=(rect[2]+10,rect[3]+10))
def image(image):
    image.fill((255,255,255))
    image.blit(pg.Label(text="Python",font=("stfangsong",24),
                        color=(0,0,0),bg=(255,255,255)).image,[5,3])
    pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)

    return image
b1.set_image(state="down",texture=image,size=(rect[2]+10,rect[3]+10))
def b1_callback2():
    text=pg.Label(text="Python",font=("stfangsong",25),bg=(255,255,255),underline=True).image
    rect=text.get_rect()
    def image(image):
        image.fill((255,255,255))
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)
        image.blit(text,[5,3])
        return image
    b1.set_image(state="init",texture=image,size=(rect[2]+10,rect[3]+10))
    def image(image):
        image.fill((255,255,255))
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(0,0,0),width=1)
        image.blit(text,[5,3])
        return image
    b1.set_image(state="active",texture=image,size=(rect[2]+10,rect[3]+10))
    def image(image):
        image.fill((255,255,255))
        image.blit(pg.Label(text="Python",font=("stfangsong",24),
                            color=(0,0,0),bg=(255,255,255),underline=True).image,[5,3])
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)

        return image
    b1.set_image(state="down",texture=image,size=(rect[2]+10,rect[3]+10))
    b1.command=b1_callback1
def b1_callback1():
    text=pg.Label(text="Python",font=("stfangsong",25),bg=(255,255,255)).image
    rect=text.get_rect()
    def image(image):
        image.fill((255,255,255))
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)
        image.blit(text,[5,3])
        return image
    b1.set_image(state="init",texture=image,size=(rect[2]+10,rect[3]+10))
    def image(image):
        image.fill((255,255,255))
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(0,0,0),width=1)
        image.blit(text,[5,3])
        return image
    b1.set_image(state="active",texture=image,size=(rect[2]+10,rect[3]+10))
    def image(image):
        image.fill((255,255,255))
        image.blit(pg.Label(text="Python",font=("stfangsong",24),
                            color=(0,0,0),bg=(255,255,255)).image,[5,3])
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)

        return image
    b1.set_image(state="down",texture=image,size=(rect[2]+10,rect[3]+10))
    b1.command=b1_callback2
b1.command=b1_callback2

# 按钮 Java
text=pg.Label(text="Java",font=("stfangsong",25),bg=(255,255,255)).image
rect=text.get_rect()
def image(image):
    image.fill((255,255,255))
    pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)
    image.blit(text,[5,3])
    return image
b2 = pg.Button(group=f1,size=(rect[2]+10,rect[3]+10),init_texture=image)
b2.set_pos("topleft",[f1.rect[0]+2,b1.rect[1]+b1.rect[3]+2])
def image(image):
    image.fill((255,255,255))
    pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(0,0,0),width=1)
    image.blit(text,[5,3])
    return image
b2.set_image(state="active",texture=image,size=(rect[2]+10,rect[3]+10))
def image(image):
    image.fill((255,255,255))
    image.blit(pg.Label(text="Java",font=("stfangsong",24),
                        color=(0,0,0),bg=(255,255,255)).image,[5,3])
    pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)

    return image
b2.set_image(state="down",texture=image,size=(rect[2]+10,rect[3]+10))
def b2_callback2():
    text=pg.Label(text="Java",font=("stfangsong",25),bg=(255,255,255),underline=True).image
    rect=text.get_rect()
    def image(image):
        image.fill((255,255,255))
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)
        image.blit(text,[5,3])
        return image
    b2.set_image(state="init",texture=image,size=(rect[2]+10,rect[3]+10))
    def image(image):
        image.fill((255,255,255))
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(0,0,0),width=1)
        image.blit(text,[5,3])
        return image
    b2.set_image(state="active",texture=image,size=(rect[2]+10,rect[3]+10))
    def image(image):
        image.fill((255,255,255))
        image.blit(pg.Label(text="Java",font=("stfangsong",24),
                            color=(0,0,0),bg=(255,255,255),underline=True).image,[5,3])
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)

        return image
    b2.set_image(state="down",texture=image,size=(rect[2]+10,rect[3]+10))
    b2.command=b2_callback1
def b2_callback1():
    text=pg.Label(text="Java",font=("stfangsong",25),bg=(255,255,255)).image
    rect=text.get_rect()
    def image(image):
        image.fill((255,255,255))
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)
        image.blit(text,[5,3])
        return image
    b2.set_image(state="init",texture=image,size=(rect[2]+10,rect[3]+10))
    def image(image):
        image.fill((255,255,255))
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(0,0,0),width=1)
        image.blit(text,[5,3])
        return image
    b2.set_image(state="active",texture=image,size=(rect[2]+10,rect[3]+10))
    def image(image):
        image.fill((255,255,255))
        image.blit(pg.Label(text="Java",font=("stfangsong",24),
                            color=(0,0,0),bg=(255,255,255)).image,[5,3])
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)
        return image
    b2.set_image(state="down",texture=image,size=(rect[2]+10,rect[3]+10))
    b2.command=b2_callback2
b2.command=b2_callback2

# 按钮 C
text=pg.Label(text="C",font=("stfangsong",25),bg=(255,255,255)).image
rect=text.get_rect()
def image(image):
    image.fill((255,255,255))
    pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)
    image.blit(text,[5,3])
    return image
b3 = pg.Button(group=f1,size=(rect[2]+10,rect[3]+10),init_texture=image)
b3.set_pos("topleft",[f1.rect[0]+2,b2.rect[1]+b2.rect[3]+2])
def image(image):
    image.fill((255,255,255))
    pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(0,0,0),width=1)
    image.blit(text,[5,3])
    return image
b3.set_image(state="active",texture=image,size=(rect[2]+10,rect[3]+10))
def image(image):
    image.fill((255,255,255))
    image.blit(pg.Label(text="C",font=("stfangsong",24),
                        color=(0,0,0),bg=(255,255,255)).image,[5,3])
    pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)

    return image
b3.set_image(state="down",texture=image,size=(rect[2]+10,rect[3]+10))
def b3_callback2():
    text=pg.Label(text="C",font=("stfangsong",25),bg=(255,255,255),underline=True).image
    rect=text.get_rect()
    def image(image):
        image.fill((255,255,255))
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)
        image.blit(text,[5,3])
        return image
    b3.set_image(state="init",texture=image,size=(rect[2]+10,rect[3]+10))
    def image(image):
        image.fill((255,255,255))
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(0,0,0),width=1)
        image.blit(text,[5,3])
        return image
    b3.set_image(state="active",texture=image,size=(rect[2]+10,rect[3]+10))
    def image(image):
        image.fill((255,255,255))
        image.blit(pg.Label(text="C",font=("stfangsong",24),
                            color=(0,0,0),bg=(255,255,255),underline=True).image,[5,3])
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)

        return image
    b3.set_image(state="down",texture=image,size=(rect[2]+10,rect[3]+10))
    b3.command=b3_callback1
def b3_callback1():
    text=pg.Label(text="C",font=("stfangsong",25),bg=(255,255,255)).image
    rect=text.get_rect()
    def image(image):
        image.fill((255,255,255))
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)
        image.blit(text,[5,3])
        return image
    b3.set_image(state="init",texture=image,size=(rect[2]+10,rect[3]+10))
    def image(image):
        image.fill((255,255,255))
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(0,0,0),width=1)
        image.blit(text,[5,3])
        return image
    b3.set_image(state="active",texture=image,size=(rect[2]+10,rect[3]+10))
    def image(image):
        image.fill((255,255,255))
        image.blit(pg.Label(text="C",font=("stfangsong",24),
                            color=(0,0,0),bg=(255,255,255)).image,[5,3])
        pygame.draw.rect(image,rect=[0,0,rect[2]+10,rect[3]+10],color=(170,170,170),width=1)
        return image
    b3.set_image(state="down",texture=image,size=(rect[2]+10,rect[3]+10))
    b3.command=b3_callback2
b3.command=b3_callback2

# =================

pygame.mouse.set_visible(True)
while running:
    # 设定帧数
    clock.tick(60)

    # 获取鼠标位置
    pos = pygame.mouse.get_pos()

    # 延时计时器刷新
    if delay == 0:
        delay = 60

    delay -= 1

    # 检测是否全屏
    if fullscreen and screen_change:
        screen = pygame.display.set_mode(size,FULLSCREEN,HWSURFACE)
        screen_change = False
    elif screen_change:
        screen = pygame.display.set_mode(size)
        screen_change = False

    # 事件检测
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # 鼠标
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1: # 左键按下，获取鼠标位置
                pass

        # 按键按下事件
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
            #F11切换全屏
            if event.key == K_F11:
                fullscreen = not fullscreen
                screen_change = True

        # 按键抬起事件
        if event.type == KEYUP:
            pass


    #画背景
    screen.fill(bg_color)
    for i in range(int(800/50)):
        pygame.draw.line(screen,(0,0,0),[i*800/16,0],[i*800/16,600])
    for i in range(int(600/50)):
        pygame.draw.line(screen,(0,0,0),[0,i*600/12],[800,i*600/12])

    
    # 刷新xxx
    guis.update(pos=pos,events = events)

    #画 xxxx
    guis.draw(screen)
    pygame.draw.rect(screen,rect=[pos[0],pos[1],5,5],color=(255,10,255))
    

    # 刷新界面
    pygame.display.update()
    

