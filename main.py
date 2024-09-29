# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from powerup import Powerup
from asteroid import Asteroid
from asteroidfield import AsteroidField
from powerupfield import PowerupField
from shot import Shot

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	screen_score = 0
	#create groups
	updatable_group = pygame.sprite.Group()
	drawable_group = pygame.sprite.Group()
	asteroid_group = pygame.sprite.Group()
	powerup_group = pygame.sprite.Group()
	shoot_group = pygame.sprite.Group()

	#set the class containers
	Player.containers = (updatable_group, drawable_group)
	Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
	AsteroidField.containers = (updatable_group)
	Shot.containers = (shoot_group, updatable_group, drawable_group)
	PowerupField.containers = (updatable_group)
	Powerup.containers = (powerup_group, updatable_group, drawable_group)


	p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()
	powerup_field = PowerupField()

	pygame.font.init()
	my_font = pygame.font.SysFont("Comic Sans MS", 30, False, False)

	text_surface = my_font.render(f"SCORE: {screen_score}", False, (0,255,0))
	

	#game loop
	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				#Quits game if the window x is clicked
				return

		screen.fill((0,0,0))
		screen.blit(text_surface, (10,10))

		for obj in updatable_group:
			obj.update(dt)
		
		for obj in drawable_group:
			obj.draw(screen)

		for obj in asteroid_group:
			if obj.collision_check(p):
				#TODO Add a game over screen and not just close the game
				print(f"Your final Score: {screen_score}")
				return

		for obj in shoot_group:
			for asteroid in asteroid_group:
				if obj.collision_check(asteroid):
					p.score += 1
					obj.kill()
					asteroid.split()
			for powerup in powerup_group:
				if obj.collision_check(powerup):
					powerup.destroy(p)

		if p.score != screen_score:
			screen_score = p.score
			text_surface = my_font.render(f"SCORE: {screen_score}", False, (0,255,0))

		
		pygame.display.flip()	

		dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()