import pygame
import math

class Raquette:
    def __init__(self, x, y, radius, vitesse, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.vitesse = vitesse
        self.mass = mass
        self.angle = 0

    def check_rebond_vertical(self, hauteur):
        # top
        if self.y - self.radius <= 0:
            self.y = self.radius
        # bottom
        elif self.y + self.radius > hauteur:
            self.y = hauteur - self.radius

    def check_rebond_gauche(self, largeur):
        if self.x - self.radius <= 0:
            self.x = self.radius
        elif self.x + self.radius > int(largeur / 2):
            self.x = int(largeur / 2) - self.radius

    def check_rebond_droit(self, largeur):
        if self.x + self.radius > largeur:
            self.x = largeur - self.radius
        elif self.x - self.radius < int(largeur / 2):
            self.x = int(largeur / 2) + self.radius

    def move(self, up, down, left, right, time_delta):
        dx, dy = self.x, self.y
        self.x += (right - left) * self.vitesse * time_delta
        self.y += (down - up) * self.vitesse * time_delta

        dx = self.x - dx
        dy = self.y - dy

        self.angle = math.atan2(dy, dx)

    def draw(self, ecran, color):
        position = (int(self.x), int(self.y))

        pygame.draw.circle(ecran, color, position, self.radius, 0)
        pygame.draw.circle(ecran, (0, 0, 0), position, self.radius, 2)
        pygame.draw.circle(ecran, (0, 0, 0), position, self.radius - 5, 2)
        pygame.draw.circle(ecran, (0, 0, 0), position, self.radius - 10, 2)

    def get_pos(self):
        return self.x, self.y

    def reset(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
