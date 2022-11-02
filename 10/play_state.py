from pico2d import *
import random
import game_framework
import logo_state
import title_state
import item_state


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 90
        self.frame = random.randint(0, 7)
        self.dir = 1
        self.image = load_image('animation_sheet.png')
        self.boy_image = load_image('ball21X21.png')
        self.item = None

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 5
        if self.x > 400:
            self.dir = -1
        elif self.x < 100:
            self.dir = 1
            self.x = 100

    def draw(self):
        if self.item == 'Boy':
            if self.dir == 1:
                self.image.clip_draw(self.frame*100, 100, 100, 100, self.x + 50, self.y)
            else:
                self.image.clip_draw(self.frame*100, 0, 100, 100, self.x + 50, self.y)


        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_b:
                game_framework.push_state(item_state)
    delay(0.01)


# 게임 초기화 : 객체들을 생성
boys = [] # C NULL
grass = None
running = None
def enter():
    global grass, running
    boys.append(Boy())
    boys.append(Boy())
    grass = Grass()
    running = True

# 게임 종료 - 객체를 소멸
def exit():
    global grass
    for boy in boys:
        del boy
    del grass

# 게임 월드 객체를 업데이트 - 게임 로직
def update():
    for boy in boys:
        boy.update()

def draw_world():
    grass.draw()
    for boy in boys:
        boy.draw()


def draw():
    # 게임 월드 렌더링
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass

def add_one_boy():
    boys.append(Boy())

def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__': # 만약 단독 실행 상태이면,
    test_self()


