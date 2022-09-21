from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
while (x < 800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x = x + 2
    delay(0.01)
y = 0
while (y < 600):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(90,y)
    x = x + 2
    delay(0.01)
    

close_canvas()
