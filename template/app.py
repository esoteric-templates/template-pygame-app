import os
import pygame

from pygame.locals import *

class App():
	def __init__(self):
		self.path = os.path.dirname(os.path.abspath(__file__))
		self.step = 0

		self.screen = pygame.display.set_mode((1920, 1080), RESIZABLE)

		pygame.display.set_caption("Pygame App")
		pygame.display.set_icon(pygame.image.load_sized_svg(f"{self.path}/assets/images/logo.svg", (512, 512)))

	def update(self) -> bool:
		keys = pygame.key.get_just_pressed()

		if keys[pygame.K_ESCAPE]:
			return False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False

		if keys[pygame.K_F11]:
			flags = self.screen.get_flags()
			was_fullscreen = flags & FULLSCREEN != 0
			self.screen = pygame.display.set_mode(self.screen.size, RESIZABLE | FULLSCREEN if not was_fullscreen else RESIZABLE)

		self.screen.fill("black")

		pygame.display.flip()

		self.step += 1

		return True

	def quit(self):
		pass
