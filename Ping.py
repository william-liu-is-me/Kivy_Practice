













import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongBall(Widget):
    speed_x = NumericProperty(0)
    speed_y = NumericProperty(0)
    speed = ReferenceListProperty(speed_x,speed_y)
    score = NumericProperty(0)

    def move(self):
        self.pos = Vector(*self.speed) + self.pos

    def ball_collides(self,ball):
        if self.collide_widget(ball):
            vx,vy = self.speed
            vx1,vy1 = ball.speed
            ball.speed,self.speed = (vx,vy) , (vx1,vy1)
            self.score += 1
            

            

class PongBall2(Widget):
    speed_x = NumericProperty(0)
    speed_y = NumericProperty(0)
    speed = ReferenceListProperty(speed_x,speed_y)
    score = NumericProperty(2)

    def move(self):
        self.pos = Vector(*self.speed) + self.pos

    #def ball_collides(self,ball):
    #    if self.collide_widget(ball):
            
            

class Pongs(Widget):
    ball = ObjectProperty(None)
    ball2 = ObjectProperty(None)


    
    def put_ball(self):
        
        self.ball.speed = Vector(8,0).rotate(randint(0,360))
        #self.ball2.center = self.center
        self.ball2.speed = Vector(8,0).rotate(randint(0,360))

    def update(self,dt):
        self.ball.move()
        self.ball2.move()
        self.ball.ball_collides(self.ball2)
        #self.ball2.ball_collides(self.ball)

        if self.ball.y< 0 or self.ball.top>self.height:
            self.ball.speed_y *= -1

        if self.ball2.y< 0 or self.ball2.top>self.height:
            self.ball2.speed_y *= -1
            self.ball2.score += 1

        if self.ball.x <0 or self.ball.right> self.width:
            self.ball.speed_x *=-1

        if self.ball2.x <0 or self.ball2.right> self.width:
            self.ball2.speed_x *=-1
            self.ball2.score += 1
        

class PongApp(App):
    def build(self):
        game = Pongs()
        game.put_ball()
        Clock.schedule_interval(game.update,1/180)
        return game

if __name__ == '__main__':
    PongApp().run()

