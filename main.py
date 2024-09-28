# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	#create groups
	updatable_group = pygame.sprite.Group()
	drawable_group = pygame.sprite.Group()
	asteroid_group = pygame.sprite.Group()
	shoot_group = pygame.sprite.Group()

	#set the class containers
	Player.containers = (updatable_group, drawable_group)
	Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
	AsteroidField.containers = (updatable_group)
	Shot.containers = (shoot_group, updatable_group, drawable_group)

	p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	#game loop
	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill((0,0,0))

		for obj in updatable_group:
			obj.update(dt)
		
		for obj in drawable_group:
			obj.draw(screen)

		for obj in asteroid_group:
			if obj.collision_check(p):
				return
				#print("GAME OVER!")

		for obj in shoot_group:
			for asteroid in asteroid_group:
				if obj.collision_check(asteroid):
					#print("Asteroid Hit!")
					obj.kill()
					asteroid.split()

		
		
		pygame.display.flip()	

		dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()