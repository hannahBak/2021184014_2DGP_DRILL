import pico2d
import logo_state
import play_state

pico2d.open_canvas()
states = [logo_state, play_state]
for state in states:
    state.enter()

# game main loop code
    while state.running:
        state.handle_events()
        state.update()
        state.draw()

    state.exit()

# finalization code
pico2d.close_canvas()
