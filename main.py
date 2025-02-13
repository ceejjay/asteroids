import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	game_clock = pygame.time.Clock()
	dt = 0

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	bullets = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable, bullets)

	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		updatable.update(dt)
		for spri in drawable:
			spri.draw(screen)
		for asteroid in asteroids:
			if(player.iscolliding(asteroid)):
				print("Game Over!")
				return
			for bullet in bullets:
				if bullet.iscolliding(asteroid):
					bullet.kill()
					asteroid.split()
		pygame.display.flip()
		dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
	main()
