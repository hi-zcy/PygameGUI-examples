import pygame
import sys
from pygame.locals import *
pygame.init()

class Effect():
    """pygame-GUI专用的默认特效，
        输入image,输出image
        把输出的image对象,会返回带有效果的image对象"""
    def light(image=None,color=(255,255,255),width=0,alpha=(50)):
        image = image.copy() # image原图
        rect = image.get_rect()
        n_image = pygame.Surface([rect[2],rect[3]], pygame.SRCALPHA) # n_image要贴在原图上的新图
        pygame.draw.rect(n_image,color,rect,width)
        n_image.set_alpha(alpha)
        return n_image
    
    def dark(image=None,color=(0,0,0),width=0,alpha=(50)):
        image = image.copy() # image原图
        rect = image.get_rect()
        n_image = pygame.Surface([rect[2],rect[3]], pygame.SRCALPHA) # n_image要贴在原图上的新图
        pygame.draw.rect(n_image,color,rect,width)
        n_image.set_alpha(alpha)
        return n_image

    def raised(image=None,light_color=(255,255,255),dark_color = (0,0,0),alpha=255,width=3):
        image = image.copy() # image原图
        rect = image.get_rect()
        o_image = pygame.Surface([rect[2],rect[3]], pygame.SRCALPHA)
        depth=0
        for i in range(width):
            n_image = pygame.Surface([rect[2],rect[3]], pygame.SRCALPHA) # n_image要贴在原图上的新图
            depth = int((light_color[0]/width)*(width-i))
            pygame.draw.line(n_image,light_color,[i,i],[rect[2]-i,i])
            pygame.draw.line(n_image,light_color,[i,i],[i,rect[3]-i])
            pygame.draw.line(n_image,dark_color,[rect[2]-i,i],[rect[2]-i,rect[3]-i])
            pygame.draw.line(n_image,dark_color,[i,rect[3]-i],[rect[2]-i,rect[3]-i])
            n_image.set_alpha(depth)
            o_image.blit(n_image,[0,0])
        o_image.set_alpha(alpha)
        return o_image

    def sunken(image=None,light_color=(255,255,255),dark_color = (0,0,0),alpha=255,width=3):
        image = image.copy() # image原图
        rect = image.get_rect()
        o_image = pygame.Surface([rect[2],rect[3]], pygame.SRCALPHA)
        depth=0
        for i in range(width):
            n_image = pygame.Surface([rect[2],rect[3]], pygame.SRCALPHA) # n_image要贴在原图上的新图
            depth = int((light_color[0]/width)*i)
            pygame.draw.line(n_image,light_color,[i,rect[3]-i],[rect[2]-i,rect[3]-i])
            pygame.draw.line(n_image,light_color,[rect[2]-i,i],[rect[2]-i,rect[3]-i])
            pygame.draw.line(n_image,dark_color,[i,i],[rect[2]-i,i])
            pygame.draw.line(n_image,dark_color,[i,i],[i,rect[3]-i])
            n_image.set_alpha(depth)
            o_image.blit(n_image,[0,0])
        o_image.set_alpha(alpha)
        return o_image
            

class Variable():
    """pygame-GUI专用的变量，支持python的数据类型"""
    def __init__(self,value=None):
        """value : 设定初始值"""
        self.value = value

    def get(self):
        """得到变量的值"""
        return self.value

    def set(self,value):
        """设置变量的值"""
        self.value = value

class Group(pygame.sprite.Group):
    "用来控制UI的组"
    def __init__(self):
        super().__init__()
        self.pos = 0
        self.rel = 0
        
    def press(self):
        "鼠标按下时调用"
        for sprite in self.sprites():
            sprite.press(self.pos)

    def release(self):
        "鼠标松开时调用"
        for sprite in self.sprites():
            sprite.release(self.pos)

    def move(self):
        "每帧调用，被拖动的组件判断是否需要移动"
        for sprite in self.sprites():
            sprite.move(self.rel)
            
    def update(self,pos,rel):
        super().update(pos,rel)
        self.pos = pos
        self.rel = rel

    '''def add(self,*sprites):
        if type(sprites) == list or type(sprites) == tuple:
            print(type(sprites),sprites)
            for sprite in sprites:
                super().add(sprite)
        else:
            super().add(sprites)'''

class UI(pygame.sprite.Sprite):
    "所有ui对象的基类"
    def __init__(self):
        super().__init__()

    def press(self,pos):
        "鼠标按下时调用"
        pass

    def release(self,pos):
        "鼠标松开时调用"
        pass

    def move(self,rel):
        "每帧调用，被拖动的组件判断是否需要移动"
        pass

    def set_pos(self,location="center",position=[0,0]):
        "提供了更多的位置设置方法"
        if location == "center":
            self.rect_in_master.center = position
            
        elif location == "top":
            self.rect_in_master.top = position

        elif location == "bottom":
            self.rect_in_master.bottom = position

        elif location == "right":
            self.rect_in_master.right = position

        elif location == "left":
            self.rect_in_master.left = position

    
        


class Button(UI):
    """生成一个UI对象 -> 当鼠标单击这个对象时调用command中输入的函数"""
    def __init__(self, master=None,pos=[0,0], draw=[200,200,200], text=None, pad=[0,0], size=[50,25], command=None, variable=None,alpha=255):
        """
        master : 该对象绘制的对象(跟随移动，而不是真的绘制在上面)，如果None就是绘制在screen上 -> Frame
        pos : 该对象左上角的坐标位 -> [x, y]
        draw :
            1、按钮填充该颜色 -> [R,G,B] / (R,G,B)
            2、按钮的绘制函数 draw(image) -> def draw(image):
                                                image.fill((255,0,0))
                                                pygame.draw.rect(image,......
                                                pygame.draw.circle(image,......
        size : 大小，如果设定了text值，则该属性无效 -> [width, height]
        text : 绘制在draw函数绘制的图像上的文本 -> Text对象
        pad : 当设定text值时有效，将按钮的大小(size)设定为Text对象的(width+pad[0],height+pad[1]) -> [padx, pady]
        command : 当该对象被点击时调用的函数 -> callback(函数名)
        variable : 当该对象被点击时，command中函数的返回值 Variable
        """
        super().__init__()
        self.text = text
        self.variable = variable
        self.command = command
        self.choose = False
        self.down = False
        self.master = master
        
        # 生成Surface对象
        if text:
            self.button_image = pygame.Surface([text.width+pad[0]*2,text.height+pad[1]*2], pygame.SRCALPHA)
        else:
            self.button_image = pygame.Surface(size, pygame.SRCALPHA)

        self.image = self.button_image
        self.rect = self.image.get_rect() # 在screen的位置
        self.rect.x, self.rect.y = pos

        # 如果有master,rect_in_master为在master的位置，否则rect_in_master等同rect
        if self.master:
            self.rect_in_master = self.rect.copy() 
            self.rect.x += self.master.rect.x
            self.rect.y += self.master.rect.y
            master.GUIs.add(self) #在master的组中加入自己
        else:
            self.rect_in_master = self.rect
            
        
        
        # 绘制
        if type(draw) == tuple or type(draw) == list:
            self.button_image.fill(draw)
        else:
            draw(self.button_image)

        if text:
            # 生成文本
            self.button_image.blit(self.text.image,[pad[0],pad[1]])

        # 设置 按下和准备选择状态下的默认图片
        self.choose_image = self.button_image.copy()
        self.choose_image.blit(Effect.light(self.button_image),[0,0])
        self.down_image = self.button_image.copy()
        self.down_image.blit(Effect.dark(self.button_image),[0,0])

    def callback(self):
        if self.command:
            return self.command()

    def update(self,pos,rel):

        # 改变按钮样式
        if self.rect.left < pos[0] < self.rect.right \
           and self.rect.top < pos[1] < self.rect.bottom:
            self.choose = True
            center = self.rect.center
            self.image = self.choose_image
            self.rect = self.image.get_rect()
            self.rect.center = center
        else:
            self.choose = False
            center = self.rect.center
            self.image = self.button_image
            self.rect = self.image.get_rect()
            self.rect.center = center

        if self.down:
            center = self.rect.center
            self.image = self.down_image
            self.rect = self.image.get_rect()
            self.rect.center = center

        # 跟随master移动
        if self.master:
            self.rect.x = self.rect_in_master.x + self.master.rect.x
            self.rect.y = self.rect_in_master.y + self.master.rect.y
            
            
    def press(self,pos):
        "此函数在鼠标按下时调用，检测鼠标是否在此对象处按下"
        if self.choose:
            self.down = True

    def release(self,pos):
        "此函数在鼠标按下时调用，检测鼠标是否在此对象处抬起"
        if self.rect.left < pos[0] < self.rect.right \
           and self.rect.top < pos[1] < self.rect.bottom and self.down:
            if self.variable:
                self.variable.set(self.callback())
            else:
                self.callback()

        self.down = False

    def set_choose_image(self,draw,size=[0,0],text=None,pad=[0,0]):
        # 生成Surface对象
        if text:
            self.choose_image = pygame.Surface([text.width+pad[0]*2,text.height+pad[1]*2], pygame.SRCALPHA)
        else:
            self.choose_image = pygame.Surface(size, pygame.SRCALPHA)
            

        # 绘制
        if type(draw) == type(tuple) or type(draw) == (list):
            self.choose_image.fill(draw)
        else:
            draw(self.choose_image)

        if text:
            # 生成文本
            self.choose_image.blit(text.image,[pad[0],pad[1]])

    def set_down_image(self,draw,size=[0,0],text=None,pad=[0,0]):
        # 生成Surface对象
        if text:
            self.down_image = pygame.Surface([text.width+pad[0]*2,text.height+pad[1]*2], pygame.SRCALPHA)
        else:
            self.down_image = pygame.Surface(size, pygame.SRCALPHA)
            

        # 绘制
        if type(draw) == tuple or type(draw) == list:
            self.down_image.fill(draw)
        else:
            draw(self.down_image)

        if text:
            # 生成文本
            self.down_image.blit(text.image,[pad[0],pad[1]])

    def set_command(self,command):
        self.command = command



class Label(UI):
    """生成一个sprite对象 -> 可以使用精灵组更好的管理单行文本对象"""
    def __init__(self, master=None, pos=[0,0],text=" ",font=(None,15),antialias=True,color=[0,0,0],background=None,alpha=255):
        """
        pos : 左上角位置 [x,y]
        text : 文本 str
        font : 字体和字号(字体(.ttf文件)，字号(int))
        antialias : 抗锯齿 bool
        color : 字体颜色(RGB)
        background : 背景颜色(RGB) None表示透明
        """
        super().__init__()
        self.pos = pos
        self.text = text
        self.master = master
        self.antialias = antialias
        self.color = color
        self.background = background
        self.alpha = alpha
        self.font = pygame.font.Font(font[0],font[1]) # 生成字体对象
        self.image = self.font.render(text,antialias,color,background)
        self.image.set_alpha(self.alpha)

        
        self.size = self.width, self.height = self.font.size(text) # (width,height)

        # 设置位置
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = pos

        # 如果有master,rect_in_master为在master的位置，否则rect_in_master等同rect
        if self.master:
            self.rect_in_master = self.rect.copy() 
            self.rect.x += self.master.rect.x
            self.rect.y += self.master.rect.y
            master.GUIs.add(self) #在master的组中加入自己
        else:
            self.rect_in_master = self.rect

    def update(self,pos,rel):
        # 跟随master移动
        if self.master:
            self.rect.x = self.rect_in_master.x + self.master.rect.x
            self.rect.y = self.rect_in_master.y + self.master.rect.y

    def set_text(self,text):
        self.image = self.font.render(text,self.antialias,self.color,self.background)
        self.image.set_alpha(self.alpha)
        rect = self.rect
        self.rect = self.image.get_rect()
        self.rect = rect
            

class Frame(UI):
    """生成一个sprite对象 -> 类似与tkinter的frame,但是有更多使用方法,
        例如当成窗口，成为某个组件的一部分"""
    def __init__(self,master=None, pos=[0,0],size=[0,0],draw=(190,190,190), title=False):
        """
        pos : 左上角位置 [x,y]
        size : 大小 [width,height]
        draw :
            1、在这个部件中填充该颜色 -> [R,G,B] / (R,G,B)
            2、输入一个的绘制函数 draw(image) -> def draw(image):
                                                image.fill((255,0,0))
                                                pygame.draw.rect(image,......
                                                pygame.draw.circle(image,......
        title : 是否有标题 -> bool
        
        """
        super().__init__()
        self.width ,self.height = size
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.title=title
        self.close_button = None
        self.down = False
        self.master = master
        self.GUIs = Group()
        
        # 绘制
        if type(draw) == tuple or type(draw) == list:
            self.image.fill(draw)
        else:
            draw(self.image)

        if self.title:
            self.set_title()

        # 如果有master,rect_in_master为在master的位置，否则rect_in_master等同rect
        if self.master:
            self.rect_in_master = self.rect.copy() 
            self.rect.x += self.master.rect.x
            self.rect.y += self.master.rect.y
            master.GUIs.add(self) #在master的组中加入自己
        else:
            self.rect_in_master = self.rect
            

    def _default_close_button_draw(image):
        "close_button的默认样式"
        image.fill((255,0,0))
        rect = image.get_rect()
        pygame.draw.line(image,(255,255,255),[5,5],[rect[2]-5,rect[3]-5])
        pygame.draw.line(image,(255,255,255),[5,rect[3]-5],[rect[2]-5,5])
    def set_close_button(self,
                         pos=[0,0],
                         draw=_default_close_button_draw,
                         text=None,
                         pad=[0,0],
                         size=[28,28],
                         alpha=255):
        "设置close_button的函数 返回Button组件"
        def close():
            self.kill()
            for GUI in self.GUIs:
                GUI.kill()
            print("kill()")
            

        self.close_button = Button(master=self,pos=pos,draw=draw,text=text,pad=pad,size=size,alpha=alpha,command=close)
        return self.close_button


    def set_title(self,
                  text=Label(text="pygame-GUI",font=(None,15),color=(0,0,0)),
                  pad = [10,5],
                  draw=(255,255,255),
                  ):
        "设置title的函数 "
        self.title_pad = pad
        self.title_text = text

        self.title_image = pygame.Surface(
                [self.width + self.title_pad[0]*2,
                 self.title_text.height + self.title_pad[1]*2]
                )
        self.title_rect = self.title_image.get_rect()
        # 绘制
        if type(draw) == tuple or type(draw) == list:
            self.title_image.fill(draw)
        else:
            draw(self.title_image)

        self.title_image.blit(self.title_text.image,self.title_pad)
        self.image.blit(self.title_image,[0,0])
            

    def press(self,pos):
        "此函数在鼠标按下时调用，检测鼠标是否在此对象处按下 必须有title!"
        if self.title:
            if self.close_button:
                if self.rect.left < pos[0] < self.rect.right-self.close_button.rect[2] \
                        and self.rect.top < pos[1] < self.title_rect.bottom+self.rect.top:
                    self.down = True
            else:
                if self.rect.left < pos[0] < self.rect.right \
                   and self.rect.top < pos[1] < self.title_rect.bottom+self.rect.top:
                    self.down = True


    def release(self,pos):
        "此函数在鼠标松开时调用，检测鼠标是否在此对象处抬起 必须有title!"
        self.down=False

    def move(self,rel):
        if self.title and self.down:
            self.rect[0] += rel[0]
            self.rect[1] += rel[1]

    def update(self,pos,rel):
        # 跟随master移动
        if self.master:
            self.rect.x = self.rect_in_master.x + self.master.rect.x
            self.rect.y = self.rect_in_master.y + self.master.rect.y

    def kill(self):
        super().kill()
        for GUI in self.GUIs:
                GUI.kill()

        

            

