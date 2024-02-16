import pygame,random
import sys
from pygame.locals import *

import pygameGUI as pg

# 颜色常量
WHITE = (255,255,255)
BLACK = (0,0,0)

# 载入背景音乐
pygame.mixer.music.load("game_music.ogg")

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

# 操作展示
event_text = pg.Message(group=guis,text="111",color=[255,255,255],font=("arialms",15),)

# 窗口

w1 = pg.Window(group=guis,size=[600,400],texture=(255,255,255))
def texture(image):
    image.fill([220,220,220])
    pygame.draw.rect(surface=image,rect=image.get_rect(),color=[175,175,175],width=2)
    return image
w1.set_image(size=[600,400],texture=texture)
t = w1.set_title()
def texture(image):
    image.fill([85,255,90])
    rect = image.get_rect()
    pygame.draw.rect(surface=image,rect=image.get_rect(),color=(175,175,175),width=2)
    text = pg.Label(text="<——播放音频——>").image
    r = text.get_rect()
    image.blit(text,[(rect[2]-r[2])/2,(rect[3]-r[3])/2])
    return image
t.set_image(size=[w1.rect[2]/2,30],texture=texture)
t.set_pos("center",[w1.rect[2]/2,0])
t.set_pos("top",w1.rect.top+2)

# 内框架
def texture(image):
    image.fill([255,255,255])
    pygame.draw.rect(surface=image,rect=image.get_rect(),color=(100,100,100),width=1)
    return image

f = pg.Frame(group=w1,size=[w1.rect[2]-10,w1.rect[3]-70],pos=[5,60])
f.set_image(size=[w1.rect[2]-10,w1.rect[3]-70],texture=texture)

# 滑条
def texture(image):
    image.fill((100,100,100))
    pygame.draw.line(surface=image,start_pos=(0,0),
                     end_pos=(image.get_rect()[2],0),
                     color=(0,0,0))
    pygame.draw.line(surface=image,start_pos=(0,image.get_rect()[3]-1),
                     end_pos=(image.get_rect()[2],image.get_rect()[3]-1),
                     color=(200,200,200))
    return image
sc1 = pg.Scrollbar(group=f,size=[400,3],texture=texture)
sc1.rect.x = 65
sc1.rect.y = 55
l1 = pg.Label(group=f,text="50%",font=("stfangsong",20))

def callback():
    l1.text=f"{round(sc1.get_percent()*100)}%"
    l1.set_pos("center",[sc1.slider.rect.center[0],0])
    l1.set_pos("bottom",sc1.slider.rect.y-3)
    pygame.mixer.music.set_volume(sc1.get_percent())
sc1.set_slider(group=f,size=[10,20],orient=[True,False],
               init_texture=(85,255,90,),down_texture=(65,230,70),active_texture=(45,210,50),
               command=callback)
sc1.slider.set_pos("center",[sc1.rect[0]+sc1.rect[2],sc1.rect.center[1]])
sc1.set_percent(0.5)
pygame.mixer.music.set_volume(sc1.get_percent())
l1.set_pos("center",[sc1.slider.rect.center[0],0])
l1.set_pos("bottom",sc1.slider.rect.y-3)

# 音量-
def texture(image,color):
    pygame.draw.rect(surface=image,rect=[0,6,15,3],color=color)
    return image
def callback():
    sc1.set_percent(sc1.get_percent()-0.05)
    l1.text=f"{round(sc1.get_percent()*100)}%"
    l1.set_pos("center",[sc1.slider.rect.center[0],0])
    l1.set_pos("bottom",sc1.slider.rect.y-3)
    pygame.mixer.music.set_volume(sc1.get_percent())
down_b = pg.Button(group=f,size=[15,15],pos=[sc1.rect.x-25,sc1.rect.y-6,],
                   init_texture=lambda image : texture(image,[120,120,120]),
                   active_texture=lambda image : texture(image,[100,100,100]),
                   down_texture=lambda image : texture(image,[80,80,80]),
                   command=callback,repeat=10)

# 音量+
def texture(image,color):
    pygame.draw.rect(surface=image,rect=[0,6,15,3],color=color)
    pygame.draw.rect(surface=image,rect=[6,0,3,15],color=color)
    return image
def callback():
    sc1.set_percent(sc1.get_percent()+0.05)
    l1.text=f"{round(sc1.get_percent()*100)}%"
    l1.set_pos("center",[sc1.slider.rect.center[0],0])
    l1.set_pos("bottom",sc1.slider.rect.y-3)
    pygame.mixer.music.set_volume(sc1.get_percent())
down_b = pg.Button(group=f,size=[15,15],pos=[sc1.rect.right+10,sc1.rect.y-6,],
                   init_texture=lambda image : texture(image,[120,120,120]),
                   active_texture=lambda image : texture(image,[100,100,100]),
                   down_texture=lambda image : texture(image,[80,80,80]),
                   command=callback,repeat=10)

# 播放按钮
def start():
    pygame.mixer.music.play()
    start_animation.run()
def stop():
    pygame.mixer.music.stop()
    stop_animation.run()
def start_texture(image,bg,color):
    rect = image.get_rect()
    space=10
    image.fill(bg)
    pygame.draw.polygon(image,color,
                        [[space,space],[rect[2]-space,rect[3]/2],[space,rect[3]-space]])
    return image
def stop_texture(image,bg,color):
    rect = image.get_rect()
    space=10
    image.fill(bg)
    pygame.draw.rect(image,color,[space,space,10,30])
    pygame.draw.rect(image,color,[rect[2]-space-10,space,10,30])
    return image
sw1 = pg.Switch(group=f,size=[50,50],
                    init_textures=[lambda image :start_texture(image,[0,0,0,0],[85,255,90]),
                                   lambda image :stop_texture(image,[0,0,0,0],[85,255,90])],
                    active_textures=[lambda image :start_texture(image,[0,0,0,0],[65,230,70]),
                                     lambda image :stop_texture(image,[0,0,0,0],[65,230,70])],
                    down_textures=[lambda image :start_texture(image,[0,0,0,0],[45,210,50]),
                                   lambda image :stop_texture(image,[0,0,0,0],[45,210,50])],
                    down_command=[None,None],
                    command=[start,stop],
                    active_command=[None,None]
                    )
sw1.set_pos("topright",[f.rect[2]-30,30])

# 生成播放开关平滑变化动画
def image(start_alpha,stop_alpha):
    image1 = pygame.Surface([50,50],pygame.SRCALPHA)
    rect = image1.get_rect()
    space=10
    image1.fill([0,0,0,0])
    pygame.draw.rect(image1,[85,255,90,stop_alpha],[space,space,10,30])
    pygame.draw.rect(image1,[85,255,90,stop_alpha],[rect[2]-space-10,space,10,30])
    image2 = pygame.Surface([50,50],pygame.SRCALPHA)
    pygame.draw.polygon(image2,[85,255,90,start_alpha],
                        [[space,space],[rect[2]-space,rect[3]/2],[space,rect[3]-space]])
    image1.blit(image2,[0,0])
    return image1
start_animation = pg.Player(group=f,widget=sw1,attr="active_images[1]",
                            image_list=[image(240,20),image(220,40),image(160,80),
                                        image(120,120),image(80,160),image(40,220),
                                        image(20,240),image(0,255)],
                            speed=0.5)
def image(start_alpha,stop_alpha):
    image1 = pygame.Surface([50,50],pygame.SRCALPHA)
    rect = image1.get_rect()
    space=10
    image1.fill([0,0,0,0])
    pygame.draw.rect(image1,[85,255,90,stop_alpha],[space,space,10,30])
    pygame.draw.rect(image1,[85,255,90,stop_alpha],[rect[2]-space-10,space,10,30])
    image2 = pygame.Surface([50,50],pygame.SRCALPHA)
    pygame.draw.polygon(image2,[85,255,90,start_alpha],
                        [[space,space],[rect[2]-space,rect[3]/2],[space,rect[3]-space]])
    image1.blit(image2,[0,0])
    return image1
stop_animation = pg.Player(group=f,widget=sw1,attr="active_images[0]",
                            image_list=[image(240,20),image(220,40),image(160,80),
                                        image(120,120),image(80,160),image(40,220),
                                        image(20,240),image(0,255)][::-1],
                            speed=0.5)

# 文本显示框
def texture(image):
    rect = image.get_rect()
    radius = 10
    bg = (255,255,255)
    pygame.draw.circle(image,(85,85,85),center=(radius,radius),radius=radius,width=2)
    pygame.draw.circle(image,(85,85,85),center=(rect[2]-radius,radius),radius=radius,width=2)
    pygame.draw.circle(image,(85,85,85),center=(rect[2]-radius,rect[3]-radius),radius=radius,width=2)
    pygame.draw.circle(image,(85,85,85),center=(radius,rect[3]-radius),radius=radius,width=2)
    pygame.draw.rect(image,bg,[rect[0]+radius,rect[1],rect[2]-radius*2,rect[3]])
    pygame.draw.rect(image,bg,[rect[0],rect[1]+radius,rect[2],rect[3]-radius*2])
    pygame.draw.line(image,(85,85,85),start_pos=[rect[0]+radius,0],end_pos=[rect[2]-radius,0],width=2)
    pygame.draw.line(image,(85,85,85),start_pos=[rect[0]+radius,rect[3]-2],end_pos=[rect[2]-radius,rect[3]-2],width=2)
    pygame.draw.line(image,(85,85,85),start_pos=[0,radius],end_pos=[0,rect[3]-radius],width=2)
    pygame.draw.line(image,(85,85,85),start_pos=[rect[2]-2,radius],end_pos=[rect[2]-2,rect[3]-radius],width=2)
    return image
def callback():
    for event in events:
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 4:
                sc2.set_percent(sc2.get_percent()-0.1)
                m.set_pos("top",round((m.rect[3]-sc2.rect[3])*-sc2.get_percent()))
            elif event.button == 5:
                sc2.set_percent(sc2.get_percent()+0.1)
                m.set_pos("top",round((m.rect[3]-sc2.rect[3])*-sc2.get_percent()))
ft = pg.Frame(group=f,pos=[40,sc1.rect[1] + sc1.rect[3]+40],texture=texture,size=(400,210),command=callback)

# 文本显示区
ftc = pg.Frame(group=ft,pos=[5,5],texture=(0,0,0,0),size=(390,200),block=False)
text="""音乐简介：\n这段音乐是当年旧版Python教程中的——
当时小甲鱼老师在讲解Pygame包,我们正在学习制作《打飞机》游戏时所使用的素材。
这类游戏距今已有50余年历史了，对世界游戏史的发展造成了深远影响。
听过的老鱼油不妨给个评分支持一下吧~"""
m = pg.Message(group=ftc,pos=[0,0],text=text,font=("stxinwei",25),width=ftc.rect[2]-15)

# 用于移动文本的滑条
sc2 = pg.Scrollbar(group=ftc,size=[11,200],texture=(0,0,0,0))
sc2.set_pos("right",ftc.rect[2])
def callback():
    m.set_pos("top",round((m.rect[3]-sc2.rect[3])*-sc2.get_percent()))
def texture(image,depth):
    rect = image.get_rect()
    radius = 6
    pygame.draw.circle(image,[depth,depth,depth],center=(radius,radius),radius=radius)
    pygame.draw.circle(image,[depth,depth,depth],center=(radius,rect[3]-radius-1),radius=radius)
    pygame.draw.rect(image,[depth,depth,depth],[0,radius,rect[2],rect[3]-radius*2])
    return image
text_slider = sc2.set_slider(size=[11,50],command=callback,
                             init_texture=lambda image:texture(image,180,),
                             active_texture=lambda image:texture(image,160,),
                             down_texture=lambda image:texture(image,140,),
                             )
event_list = ["","","",]
# =================


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
    if len(event_list) > 3:
        event_list.pop(0)
    if events and events[0].type != MOUSEMOTION:
        for event in events:
            event_list.append(str(event))
    event_text.text = f"{event_list[0]}\n{event_list[1]}\n{event_list[2]}"
    event_text.rect.x = 0
    event_text.rect.y = 0
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
    

    # 刷新界面
    pygame.display.update()

    

