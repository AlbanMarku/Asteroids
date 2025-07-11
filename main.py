import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    py_time = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroids.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    astrofield = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        
        for updatable_obj in updatable:
            updatable_obj.update(dt)
            
        for asteroid_obj in asteroids:
            if asteroid_obj.check_collision(player):
                print("Game over!")
                return
            for shot_obj in shots:
                if asteroid_obj.check_collision(shot_obj):
                    asteroid_obj.split()
                    shot_obj.kill()
                    print("Asteroid destroyed!")
                    break
            
        for drawable_obj in drawable:
            drawable_obj.draw(screen)  
            
        pygame.display.flip()
        dt = py_time.tick(60) / 1000
        
if __name__ == "__main__":
    main()