import time, sys
import pygame

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)

def playWav(music_path):
	pygame.mixer.init()

	sound = pygame.mixer.Sound(music_path)
	sound.play()
	time.sleep(sound.get_length())
