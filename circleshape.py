import pygame

# Base Class for game objects

class CircleShape(pygame.sprite.Sprite):
	def __init__(self, x, y, radius):
		# we will be using this later
		if hasattr(self, "containers"):
			super().__init__(self.containers)
		else:
			super().__init__()

		self.position = pygame.Vector2(x, y)
		self.velocity = pygame.Vector2(0, 0)
		self.radius = radius

	def collision_check(self, other_circle):
		collision_dist = self.position.distance_to(other_circle.position)
		radius_add = self.radius + other_circle.radius

		if collision_dist > radius_add:
			return False
		else:
			return True

	def draw(self, screen):
		pass

	def update(self, dt):
		pass