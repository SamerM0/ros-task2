import pygame
import time
DEADZONE = 0.1 #ignore small movements (drift)

class JoystickListener:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.joysticks = []
        self.x = 0.0
        self.y = 0.0
    def start_listening(self):
        while True:
            for event in pygame.event.get(): #check if a controller is plugged in
                if event.type == pygame.JOYDEVICEADDED:
                    joy = pygame.joystick.Joystick(event.device_index)
                    self.joysticks.append(joy)

            for joy in self.joysticks: #read the axes of each controller
                self.x = joy.get_axis(0)
                self.y = joy.get_axis(1)
                if abs(self.x) < DEADZONE:
                    self.x = 0
                if abs(self.y) < DEADZONE:
                    self.y = 0
            time.sleep(0.05)

    def get_axes(self): 
        return self.x, self.y