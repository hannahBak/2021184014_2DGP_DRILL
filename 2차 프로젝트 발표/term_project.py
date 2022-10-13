from pico2d import *

bath_WIDTH, bath_HEIGHT = 720, 540

open_canvas(bath_WIDTH, bath_HEIGHT)

bath = load_image('bath.png')
character1 = load_image('myCharacter1.png')
character2 = load_image('myCharacter2.png')

p = character1

def handle_events():
    global running
    global dir
    global p, character1, character2
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                p = character1
                
            elif event.key == SDLK_LEFT:
                dir -= 1
                p = character2
               
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1


running = True
x = 720 // 2
frame = 0
dir = 0

while running:
    clear_canvas()
    bath.draw(bath_WIDTH // 2, bath_HEIGHT // 2)
    p.clip_draw(frame * 120, 420, 115, 150, x, 90)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 6
    x += dir * 25
    delay(0.1)

close_canvas()
