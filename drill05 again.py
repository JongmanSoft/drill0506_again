from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def load_resources():
    global TUK_ground, character
    global arrow
    arrow = load_image('hand_arrow.png')
    TUK_ground = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


def reset_world():
    global running, cx, cy, frame, hx, hy, sx, sy, t, action
    running = True
    cx, cy = TUK_WIDTH // 2, TUK_HEIGHT // 2
    frame = 0
    action = 3
    #hx, hy = 50, 50
    set_new_target_arrow()


def set_new_target_arrow():
    global hx, hy, sx, sy, t
    hx, hy = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
    sx, sy = cx, cy
    t = 0.0


def render_world():
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    arrow.draw(hx, hy)
    character.clip_draw(frame * 100, 100 * action, 100, 100, cx, cy)
    update_canvas()


def update_world():
    global frame
    global sx, sy, t, hx, hy, cx, cy, action
    frame = (frame + 1) % 8

    action = 1 if cx < hx else 0
    if t <= 1.0:
        cx = (1 - t) * sx + t * hx
        cy = (1 - t) * sy + t * hy
        t += 0.001
    else:
        cx,cy = hx,hy #목적지위치와 강제로 일치시킴
        set_new_target_arrow()

open_canvas(TUK_WIDTH, TUK_HEIGHT)
load_resources()
hide_cursor()
reset_world()

while running:
    render_world()  # 월드현재내용그리기
    handle_events()  # 월드내 입력 받아들이기
    update_world()  # 객체들의 상호작용 계산 후 그결과를 update

close_canvas()
