import RPi.GPIO as GPIO
import pygame

ch = [11,13,15,16,18,22]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ch,GPIO.IN,pull_up_down = GPIO.PUD_UP)
def get_state():
    state = 0
    for x in ch:
        if not GPIO.input(x):
            state += 2**ch.index(x)
    return state
pygame.mixer.init()

p_state = 0
pygame.mixer.music.load( str(p_state)+'.wav')
pygame.mixer.music.play()
while True:
    while get_state() == p_state:
        continue
    p_state = get_state()
    pygame.mixer.music.stop()
    pygame.mixer.music.load( str(p_state)+'.wav')
    pygame.mixer.music.play()



GPIO.cleanup()
