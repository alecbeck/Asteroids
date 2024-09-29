#Powerup class
import pygame
import random
from constants import *
from circleshape import CircleShape


class Powerup(CircleShape):
	speed_counter = 0
	mulit_shot_counter = 0
	rate_of_fire_counter = 0
	def __init__(self, x, y):
		super().__init__(x, y, POWERUP_RADIUS)
		self.name = random.sample(POWERUPS, 1)
		self.velocity = pygame.Vector2(0, 0)
		self.radous = POWERUP_RADIUS
		self.position = pygame.Vector2(x, y)
	
	def draw(self, screen):
		if self.name[0] == "SPEED":
			pygame.draw.circle(screen, (0, 0, 255), self.position, self.radius , 2)
		elif self.name[0] == "MULTI_SHOT":
			pygame.draw.circle(screen, (255, 150, 0), self.position, self.radius , 2)
		elif self.name[0] == "FIRE_RATE":
			pygame.draw.circle(screen, (0, 255, 0), self.position, self.radius , 2)
	
	def update(self, dt):
		self.position += (self.velocity * dt)

	def destroy(self, player):
		self.kill()
		# This will give the player a powerup depending on what the shot
		if self.name[0] == "SPEED":
			if self.speed_counter <= POWERUP_MAX_SPEED:
				player.speed += POWERUP_SPEED_INC_RATE
				self.speed_counter += 1
			#pygame.draw.circle(screen, (0, 0, 255), self.position, self.radius , 2)
		elif self.name[0] == "MULTI_SHOT":
			if self.mulit_shot_counter <= POWERUP_MAX_MULTI_SHOT_:
				player.shots_per_shot += 1
				self.mulit_shot_counter += 1
				#print(f"SHOTS: {player.shots_per_shot}")
			#pygame.draw.circle(screen, (255, 150, 0), self.position, self.radius , 2)
		elif self.name[0] == "FIRE_RATE":
			if self.rate_of_fire_counter <= POWERUP_MAX_RATE_OF_FIRE:
				self.rate_of_fire_counter += 1
				player.max_cool_down -= POWERUP_RATE_OF_FIRE_INC
				#print(f"Cool down: {player.max_cool_down}")
				pass
			#pygame.draw.circle(screen, (0, 255, 0), self.position, self.radius , 2)