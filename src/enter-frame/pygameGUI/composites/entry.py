import pygame, sys, random, os
from pygame.locals import *
from pygameGUI import Group,Widget,PG_Error,Label


class Entry(Widget):
    """
    Entry -> 单行输入框
    各种的组件都是由它组织起来的
    内部有一个内置的组(Group)，用于管理其他组件
    """
    frame = True # 表示这是一个框架结构
    
    def __init__(self, group=None, # 组
                 text = None, # 文本label
                 insert = (0,0,0),# image 光标样式
                 insertontime = 120, # 光标闪烁时间(亮)(帧)
                 insertofftime =60, # 光标闪烁时间(灭)(帧)
                 insert_size = [2,-4], # 光标的大小[宽度，高度(跟随字体高度变化，短于字体多少)]
                 pos = [0,0],size=[200,50], # 位置，大小
                 texture=(190,190,190), # 纹理
                 block=True, # 是否阻断
                 command = None, # 当位于鼠标下方时连续调用(被阻断时无效
                 unblock = False, # 是否免疫阻断
                 backspace_interval = 5, # 长按间隔多久触发（帧）
                 backspace_delay = 30, # 延迟多久触发长按
                 ):
        """初始化"""
        
        super().__init__(group)
        pygame.key.start_text_input() # 打开输入模式
        self.block = block
        self.unblock = unblock
        self.command=command
        self.insert = insert
        self.insert_size = insert_size
        self.insertofftime = insertofftime
        self.insertontime = insertontime
        self.insert_timer = [True,self.insertontime]
        self.label = text
        self.backspace_delay = backspace_delay
        self.backspace_interval = backspace_interval
        self.backspace_repeat = [self.backspace_delay,self.backspace_interval] # [延迟，间隔]

        # 生成图像
        self.size = size
        self.__image = self.__draw_texture(texture,size)

        # 生成光标图像
        self.insert = self.__draw_texture(insert,[insert_size[0],size[1]-abs(insert_size[0]*2)])
        
        # 得到矩形位置
        self.rect = self.__image.get_rect()
        self.rect.x, self.rect.y = pos

        # 内置组
        self.widgets = Group(master = False)

        # 是否被选中焦点
        self.select = False

        # 默认光标位置
        self.insert_index = -1 

        # 如果传入了text
        if not self.label is None:
            self.label = Label(group=self,pos=[0,0],
                          text = self.label.text, font = self.label.font,
                          color = self.label.color, bg = self.label.bg, alpha = self.label.alpha,
                          bold = self.label.bold, italic = self.label.italic, underline = self.label.underline,
                          antialias = self.label.antialias,
                          )

    def __draw_texture(self,texture,size):
        """绘制纹理"""
        # 生成空白图片
        image = pygame.Surface(size, pygame.SRCALPHA)
        # 绘制纹理
        if type(texture) == tuple or type(texture) == list:
            image.fill(texture)
        else:
            image = texture(image)
        return image

        
    def __replace_rect(self,rect,image):
        """用于改变纹理之后刷新rect"""
        x,y = rect.center
        self.rect = image.get_rect()
        self.rect.center = x,y
        
    def update(self,args,kwargs):
        "刷新"
        for widget in self.widgets[::-1]: # 注：这里不能使用self.widgets.update() 由于万能参数的传参格式
            widget.update(args,kwargs)

        # 鼠标位于上方
        if (not Group.block_start or self.unblock) \
           and pygame.Rect(self.get_rect()).collidepoint(kwargs["pos"]):
            for event in kwargs["events"]:
                if event.type == MOUSEBUTTONDOWN:
                    self.select = True
                    self.insert_index = self.get_pos_index(kwargs["pos"])
                    pygame.key.set_text_input_rect(
                        (self.get_label_index_x(self.insert_index),
                         self.rect.bottom,0,0)
                        )
                    break
                    
            if self.block == True:
                Group.block_start = True
            if self.command:
                self.command()

        else:     
            for event in kwargs["events"]:
                if event.type == MOUSEBUTTONDOWN:
                    self.select = False
                    break
        # 普遍
        if self.select:
            for event in kwargs["events"]:
                if event.type == TEXTINPUT:
                    # 输入法位置
                    pygame.key.set_text_input_rect(
                        (self.get_label_index_x(self.insert_index),
                         self.rect.bottom,0,0)
                        )
                    # 调整文本内容
                    self.label.text = self.label.text[:self.insert_index] + event.text\
                                      + self.label.text[self.insert_index:]
                    self.insert_index += len(event.text)
                    # 移动
                    x = self.get_label_index_x(self.insert_index)
                    if x < self.rect[0]:
                        self.label.rect.x += self.rect[0] - x + 1
                    elif x > self.rect[2]:
                        self.label.rect.x += self.rect[2] - x - self.insert_size[0]-1
                        
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        #删除
                        if not self.insert_index < 1:
                            self.label.text = self.label.text[:self.insert_index-1]\
                                      + self.label.text[self.insert_index:]
                        self.insert_index -= 1
                        if self.insert_index <= 0:
                            self.insert_index = 0
                    # 移动光标
                    if event.key == K_LEFT:
                        self.insert_index -= 1
                        if self.insert_index <= 0:
                            self.insert_index = 0
                    if event.key == K_RIGHT:
                        self.insert_index += 1
                        if self.insert_index >= len(self.label.text):
                            self.insert_index = len(self.label.text)
                        

        # 删除键长按判定
        if pygame.key.get_pressed()[K_BACKSPACE]:
            if not self.backspace_repeat[0]:
                if not self.backspace_repeat[1]:
                    #删除
                    if not self.insert_index < 1:
                        self.label.text = self.label.text[:self.insert_index-1]\
                                      + self.label.text[self.insert_index:]
                        self.insert_index -= 1
                        if self.insert_index <= 0 :
                            self.insert_index = 0
                    self.backspace_repeat[1] = self.backspace_interval
                else:
                    self.backspace_repeat[1] -=1
            else:
                self.backspace_repeat[0] -=1
        else:
            self.backspace_repeat[0] = self.backspace_delay
               

                
    def draw(self, surface):
        "绘制"
        image = self.__image.copy()
        if self.select:
            # 调整光标闪烁计时器
            if self.insert_timer[1]:
                self.insert_timer[1] -= 1
                if self.insert_timer[0]:
                    x = self.get_label_index_x(self.insert_index)
                    image.blit(self.insert,[x,abs(self.insert_size[1])/2])
            else:
                self.insert_timer[0] = not self.insert_timer[0]
                if self.insert_timer[0]:
                    self.insert_timer[1] = self.insertontime
                else:
                    self.insert_timer[1] = self.insertofftime
        self.widgets.draw(image)
        surface.blit(image,[self.rect.x,self.rect.y])

    def set_image(self, size=[500,500], texture=None):
        "设置图片，注意要重新设置位置"
        image = pygame.Surface(size, pygame.SRCALPHA)
        self.__image = texture(image)
        x,y = self.rect.center
        self.rect = image.get_rect()
        self.rect.center = x,y

    def set_label(self,
                  pos = [0,0], # 位置
                  text="默认文本...", # 文本 
                  font=("arialms",25), # 字体字号
                  color=[0,0,0], # 前景色（字体颜色）
                  bg=None, # 背景色
                  alpha=255, # 不透明度
                  bold = False, # 加粗
                  italic = False, # 斜体
                  underline = False, # 下划线
                  antialias=True, # 抗锯齿
                  ):
        self.label = Label(group=self,pos=pos,
                          text = text,font = font,
                          color = color, bg = bg, alpha = alpha,
                          bold = bold, italic = italic, underline = underline,
                          antialias = antialias
                          )

    def get_pos_index(self,pos):
        """
        得到距离鼠标按下位置最接近的text字符位置的索引值
        (两字之间，带头带尾)
        """
        distances = []
        distances.append(abs(pos[0]-self.label.get_rect()[0]))
        for index in range(1,len(self.label.text)+1):
            width = self.label.style.size(self.label.text[0:index])[0]
            x = self.label.get_rect()[0]+width
            distances.append(abs(pos[0]-x))
        return distances.index(min(distances))

    def get_label_index_x(self,index):
        """根据索引值得到对应的x位置值"""
        if index == -1:
            pos = self.label.style.size(self.label.text[:])
        else:
            pos = self.label.style.size(self.label.text[0:index])
        return self.label.rect[0] + pos[0]
        
        
    def delete(self):
        for w in self.widgets:
            w.delete()
        super().delete()
            
    def __str__(self):
        return f"Entry"

    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, image):
        self.__image = image
        self.__replace_rect(self.rect,image)





