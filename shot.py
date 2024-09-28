#Shot class
import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
	
	def __init__(self, x, y):
		super().__init__(x, y, SHOT_RADIUS)
		self.position = pygame.Vector2(x, y)
		self.velocity = pygame.Vector2(0, 0)
		#print("shot created")
		self.radius = SHOT_RADIUS

	
	def draw(self, screen):
		pygame.draw.circle(screen, (255,0,0), self.position, self.radius, 2)

	def update(self, dt):
		self.position += (self.velocity * dt)
