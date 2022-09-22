from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('spritesheet_grant1.png')

x = 0
frame = 0
while( x < 800):
    for i in range(12):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 97, 1030, 93, 135, x, 120)
        update_canvas()
        frame = (frame + 1) % 12
        x += 2
        delay(0.03)
        get_events()

    for i in range(12):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 97, 860, 93, 140, x, 120)
        update_canvas()
        frame = (frame + 1) % 12
        x += 2
        delay(0.03)
        get_events()

    for i in range(12):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 97, 688, 93, 140, x, 120)
        update_canvas()
        frame = (frame + 1) % 12
        x += 2
        delay(0.03)
        get_events()

    for i in range(12):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 97, 540, 93, 148, x, 120)
        update_canvas()
        frame = (frame + 1) % 12
        x += 2
        delay(0.03)
        get_events()

    for i in range(12):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 97, 345, 93, 165, x, 120)
        update_canvas()
        frame = (frame + 1) % 12
        x += 2
        delay(0.03)
        get_events()

    for i in range(12):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 97, 175, 93, 130, x, 120)
        update_canvas()
        frame = (frame + 1) % 12
        x += 2
        delay(0.03)
        get_events()

close_canvas()

