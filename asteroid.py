# Asteroid class
import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		self.position = pygame.Vector2(x, y)
		self. velocity = pygame.Vector2(0, 0)
		self.radius = radius

	def draw(self, screen):
		pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius , 2)

	
	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			angle = random.uniform(20, 50)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			asteroid_one = Asteroid(self.position.x, self.position.y, new_radius) 
			asteroid_two = Asteroid(self.position.x, self.position.y, new_radius) 

			asteroid_one.velocity = self.velocity.rotate(angle)
			asteroid_two.velocity = self.velocity.rotate(-angle)

			
