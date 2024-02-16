import pygame
import os
from pygame.locals import *

os.environ["SDL_IME_SHOW_UI"] = "1" # 显示输入候选框 0是False 1是True

pygame.init()
screen = pygame.display.set_mode((400, 300)) 

font = pygame.font.SysFont("arialms", 28) 

text = ""

running = True
while running:
    pos = pygame.mouse.get_pos()
    pygame.key.start_text_input() # 打开输入模式（默认就是打开的
    #pygame.key.stop_text_input() # 关闭
    """调用上面的stop_text_input()方法可以使得游戏在一开始时就不会被输入法阻断，
    不会出现“点击wasd无反应，把电脑键盘键帽扣掉的事故”"""
    pygame.key.set_text_input_rect((0,0,0,0)) # 输入法框框的矩形位置，一般只有前两位有效，代表输入法左上角的位置
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                text = text[:-1] # 如果是backspace就删除一个字

        if event.type == TEXTINPUT: # 如果是输入文字,就加入到字符串内显示
            text += event.text
    screen.fill((255, 255, 255))
    text_image = font.render(text, True, (0, 0, 0))
    screen.blit(text_image, (10, 10))

    pygame.display.update()

pygame.quit()

