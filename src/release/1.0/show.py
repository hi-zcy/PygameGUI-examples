import pygame
import sys
import pygameGUI as pgui
from pygame.locals import *
pygame.init()

def main():
    # 颜色常量
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    GRAY = (170,170,170)

    size = width, height = 800,600

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("title")

    GUIs = pgui.Group() #UI组


    # 生成GUI
    title = pgui.Label(
                    text="1.0组件展示",
                    font=("和音体.ttf",30),
                    color=(0,0,0),
                    alpha=255
                    )
    title.set_pos("center",[400,40])
    
    GUIs.add(title)

    GUIs.add(pgui.Label(
                    pos=[100,100],
                    text="我是Lable组件",
                    font=("和音体.ttf",20),
                    color=(255,255,0),
                    background=(0,255,255),
                    )
             )

    text = pgui.Label(text="我是一个默认材质的Button组件",font=("和音体.ttf",20))
    b1 = pgui.Button(
                    pos = [300,100],
                    text = text,
                    pad=[10,10])
    GUIs.add(b1)

    text = pgui.Label(text="我是一个3D材质的Button组件",font=("和音体.ttf",20))
    def draw(image):
        image.blit(pgui.Effect.raised(image),[0,0])
    b1 = pgui.Button(
                    pos = [300,200],
                    text = text,
                    pad=[10,10],
                    draw=draw,
                    )
    def draw(image):
        image.blit(pgui.Effect.sunken(image),[0,0])
    b1.set_down_image(draw,text=text,pad=[10,10],)
    
    GUIs.add(b1)

    def create_window():
        root = pgui.Frame(pos=[300,200],size=[200,200],title=True)

        root.set_title(pgui.Label(text="我是Frame组件!",font=("和音体.ttf",15)))
        b1 = root.set_close_button()
        b1.set_pos("right",root.rect[3])
        GUIs.add(root,b1)
        
        def callback():
            print("你好！")
        text = pgui.Label(text="我是Button组件!",font=("和音体.ttf",20))
        b1 = pgui.Button(master=root,text=text,pos=[20,40],command=callback)

        GUIs.add(b1)

    f1 = pgui.Frame(pos=[200,300],size=[400,200],draw=(80,255,180))
    GUIs.add(f1)

    GUIs.add(pgui.Label(master=f1,pos=[30,10],text="我是一个在Frame中的Label!",font=("和音体.ttf",20)))
    
    text = pgui.Label(text="我是一个在Frame中的Button!点我!",font=("和音体.ttf",20))
    b1 = pgui.Button(master=f1,text=text,pos=[20,70],pad=[10,10],draw=(150,150,250),command=create_window)
    GUIs.add(b1)

    clock = pygame.time.Clock()

    delay = 60 # 延时计时器(1秒)

    # 是否全屏
    fullscreen = False
    screen_change = False

    # 背景颜色设定
    bg_color = GRAY

    running = True

    while running:
        pos = pygame.mouse.get_pos()
        rel = pygame.mouse.get_rel()

        # 设定帧数
        clock.tick(60)

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
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # 鼠标
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1: # 左键按下，获取鼠标位置
                    GUIs.press()

            if event.type == MOUSEBUTTONUP:
                if event.button == 1: # 左键松开，获取鼠标位置
                    GUIs.release()

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

        # 移动被拖动的控件
        GUIs.move()

        # 刷新xxx
        GUIs.update(pos,rel)

        #画 xxxx
        GUIs.draw(screen)


        # 刷新界面
        pygame.display.update()


if __name__ == "__main__":
    main()




