from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

window = Ursina()
camera.orthographic = True
camera.fov = 10

class killBrick(Entity):
    def __init__(self,origin,y=0,x=0,model='cube',scale=(3,1),color=color.red,collider='box'):
        super().__init__(
            parent=scene,
            scale=scale,
            model=model,
            color=color,
            collider=collider,
            origin=origin,
            y=y,
            x=x

        )

class DoubleJump(Entity):
    def __init__(self,origin,y=0,x=0,model='cube',scale=(3,1),color=color.blue,collider='box'):
        super().__init__(
            parent=scene,
            model=model,
            color=color,
            collider=collider,
            origin=origin,
            scale=scale,
            y=y,
            x=x

        )


class JumpPad(Entity):
    def __init__(self,origin,y=0,x=0,model='cube',scale=(3,1),color=color.blue,collider='box'):
        super().__init__(
            parent=scene,
            model=model,
            color=color,
            collider=collider,
            origin=origin,
            scale=scale,
            y=y,
            x=x

        )

class CheckPoint(Entity):
    def __init__(self,origin,y=0,x=0,model='cube',scale=(2,0.2),color=color.blue,collider='box'):
        super().__init__(
            parent=scene,
            model=model,
            color=color,
            collider=collider,
            origin=origin,
            scale=scale,
            y=y,
            x=x

        )

class CheckPoint2(Entity):
    def __init__(self,origin,y=0,x=0,model='cube',scale=(2,0.2),color=color.blue,collider='box'):
        super().__init__(
            parent=scene,
            model=model,
            color=color,
            collider=collider,
            origin=origin,
            scale=scale,
            y=y,
            x=x

        )


class Enemy(Entity):
    def __init__(self,origin,y=0,x=0,model='cube',scale=(3,1),color=color.red,collider='box'):
        super().__init__(
            parent=scene,
            scale=scale,
            model=model,
            color=color,
            collider=collider,
            origin=origin,
            y=y,
            x=x

        )
    def attack(self,speedx=0.1):
        self.add_script(SmoothFollow(target=player_controller,speed=speedx))
   



checkpoint=None
checky = None
#Level1
ground = Entity(model='cube', color=color.white33, origin_y=.5, scale=(100, 5, 1), collider='box')
jumpobj = Entity(model='cube', color=color.white33, origin_y=.5, scale=(5, 5, 1), x=56, collider='box')
jumpobj2 = Entity(model='cube', color=color.white33, origin_y=.5, scale=(5, 5, 1), x=66, collider='box')
jumpobj3 = Entity(model='cube', color=color.white33, origin_y=.5, scale=(5, 5, 1), x=76, collider='box')
ground2 = Entity(model='cube', color=color.white33, origin_y=.5, scale=(50, 5, 1), x=104, collider='box')
Void = killBrick(model='cube', origin=(-.5,.5), scale=(300,10), x=10, y=-10, collider='box')
killbrick1 = killBrick(model='cube', origin=(-.5,.5), scale=(1,1), x=10, y=2, collider='box')
killbrick1 = killBrick(model='cube', origin=(-.5,.5), scale=(1,1), x=15, y=2, collider='box')
killbrick1 = killBrick(model='cube', origin=(-.5,.5), scale=(1,1), x=20, y=2, collider='box')
dj = DoubleJump(model='cube', origin=(-.5,.5), scale=(1,1), x=25, y=1, collider='box')
checkpoint1 = CheckPoint(model='cube',origin=(-.5,.5),x=30,y=0.1)
checkpoint2 = CheckPoint2(model='cube',origin=(-.5,.5),x=100,y=0.1)
checkpoint=3
checky = 1
wall = Entity(model='cube', color=color.white33, origin_y=-.5, scale=(1, 10, 1), y=0, collider='box')
enemy1= Enemy(model='cube', origin=(-.5,.5), scale=(1,1), x=94, y=2, collider='box')

#player control
player_controller = PlatformerController2d(scale_y=2, jump_height=4, x=checkpoint)

camera.add_script(SmoothFollow(target=player_controller, offset=[0,1,-30], speed=4))

#Functions 
def killPlayer():
    player_controller.x = checkpoint
    player_controller.y =checky
def double_jump(obj=None):
    if obj is not None:
        obj.enabled=False
        obj.visible=False
    player_controller.jump_height*=2
    player_controller.jump()
    player_controller.x+=2
    player_controller.jump_height=4
#Running the functions when a key or mouse button is pressed
def input(key):

    global checkpoint
    global checky
    hit_info = player_controller.intersects()
    hit_info2 = enemy1.intersects()
    if hit_info2.hit:
        if hit_info2.entity.type=='Entity':
            enemy1.y+=1
        
    if hit_info.hit:
        
        if hit_info.entity.type=='killBrick':
            killPlayer()
        elif hit_info.entity.type=='Enemy':
            killPlayer()

        elif hit_info.entity.type=='DoubleJump':
            double_jump(hit_info.entity)
        elif hit_info.entity.type=='JumpPad':
            double_jump()
        elif hit_info.entity.type=='CheckPoint':

            checkpoint = hit_info.entity.x
            checky =hit_info.entity.y
        elif hit_info.entity.type=='CheckPoint2':

            checkpoint = hit_info.entity.x
            checky =hit_info.entity.y
            enemy1.attack()
            print("Stage3")


            
            
        





window.run()
