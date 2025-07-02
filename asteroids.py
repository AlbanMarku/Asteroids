from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroids(CircleShape):
    containers = None
    def __init__(self,x ,y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroids(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_velocity1
        new_asteroid2 = Asteroids(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_velocity2