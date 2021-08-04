#!/usr/bin/env python3

import pygame
import pygame_gui
import subprocess
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (1700, 50)


print('initializing with webcam as input')
fakecam = subprocess.Popen(['python', 'cam.py', '0'])


pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((200, 50))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

video_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 50)),
                                            text='video',
                                            manager=manager)

camera_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 0), (100, 50)),
                                            text='camera',
                                            manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == camera_button:
                    print('switching to camera')
                    fakecam.terminate()
                    fakecam = subprocess.Popen(['python', 'cam.py', '0'])
                if event.ui_element == video_button:
                    print('switching to video')
                    fakecam.terminate()
                    fakecam = subprocess.Popen(['python', 'cam.py', '1'])
        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
