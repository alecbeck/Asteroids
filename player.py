from circleshape import CircleShape
from shot import Shot
from constants import *
import pygame 

# Player Class
class Player(CircleShape):

	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.cool_down = PLAYER_SHOOT_COOLDOWN
		self.max_cool_down = PLAYER_SHOOT_COOLDOWN
		self.score = 0
		self.speed = PLAYER_SPEED
		self.shots_per_shot = 1


		# in the player class
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
	

	def draw(self, screen):
		pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)


	def update(self, dt):
		keys = pygame.key.get_pressed()
		self.cool_down -= dt
	
		if keys[pygame.K_a]:
			self.rotate(dt * -1)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(dt * -1)
		if keys[pygame.K_SPACE]:
			self.shoot()
	
	
	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt


	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * self.speed * dt

	def shoot(self):
		if self.cool_down <= 0.0:
			player_shot = Shot(self.position.x, self.position.y)
			player_shot.velocity = pygame.Vector2(0, 1)
			player_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
			
			if self.shots_per_shot >= 2:
				player_shot_2 = Shot(self.position.x, self.position.y)
				player_shot_2.velocity = pygame.Vector2(0, 1)
				player_shot_2.velocity = pygame.Vector2(0, 1).rotate(self.rotation+180) * PLAYER_SHOOT_SPEED

			if self.shots_per_shot >= 3:
				player_shot_3 = Shot(self.position.x, self.position.y)
				player_shot_3.velocity = pygame.Vector2(0, 1)
				player_shot_3.velocity = pygame.Vector2(0, 1).rotate(self.rotation+90) * PLAYER_SHOOT_SPEED

			if self.shots_per_shot >= 4:
				player_shot_2 = Shot(self.position.x, self.position.y)
				player_shot_2.velocity = pygame.Vector2(0, 1)
				player_shot_2.velocity = pygame.Vector2(0, 1).rotate(self.rotation+270) * PLAYER_SHOOT_SPEED


			self.cool_down = self.max_cool_down