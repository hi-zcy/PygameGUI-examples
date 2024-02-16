from pygameGUI import Widget,PG_Error

class Player(Widget):
    """
    这是一个假装成组件的动画播放器
    用于播放帧动画并且可以重复使用
    通常用于给某些组件作为插件使用
    使用时应与widget对象处于同一组
    在删除widget对象时需要一并删除
    
    """
    def __init__(self,
                 group=None,
                 widget=None,
                 attr="",
                 image_list=[],
                 speed=1):
        super().__init__(group)
        self.widget = widget
        self.attr = attr
        self.image_list = image_list
        self.index = 0
        self.running = False
        self.speed = speed
        
    def run(self,index=0):
        self.running = True
        self.index = index
        
    def update(self,args,kwargs):
        if self.running:
            index = int(self.index)
            if index >= len(self.image_list)-1:
                image = self.image_list[len(self.image_list)-1]
                self.index = 0
                self.running=False
            else:
                image = self.image_list[index]
                self.index += self.speed 
            setattr(self.widget,self.attr,image)

    def set_pos(self,*args,**kwargs):
        raise PG_Error("'Player对象是一个没有实体的播放器，请勿给它设置位置'")

    def get_pos(self):
        raise PG_Error("'Player对象是一个没有实体的播放器，没有位置属性")
    






    
