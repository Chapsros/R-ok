import pygame
import random as rand
import math
import constants as const


class Puck:
    def __init__(self, x, y, radius, vitesse, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.vitesse = vitesse
        self.mass = mass
        self.angle = 0

    def move(self, time_delta):
        self.x += math.sin(self.angle) * self.vitesse * time_delta
        self.y -= math.cos(self.angle) * self.vitesse * time_delta

        self.vitesse *= const.FRICTION

    def check_limite(self, largeur, hauteur):
        # coté droit
        if self.x + self.radius > largeur:
            self.x = 2 * (largeur - self.radius) - self.x
            self.angle = -self.angle

        # coté gauche
        elif self.x - self.radius < 0:
            self.x = 2 * self.radius - self.x
            self.angle = -self.angle

        # en bas
        if self.y + self.radius > hauteur:
            self.y = 2 * (hauteur - self.radius) - self.y
            self.angle = math.pi - self.angle

        # en haut
        elif self.y - self.radius < 0:
            self.y = 2 * self.radius - self.y
            self.angle = math.pi - self.angle

    def add_vectors(self, angle1, length1, angle2, length2):
        x = math.sin(angle1) * length1 + math.sin(angle2) * length2
        y = math.cos(angle1) * length1 + math.cos(angle2) * length2

        length = math.hypot(x, y)
        angle = math.pi / 2 - math.atan2(y, x)
        return angle, length

    def collision_raquette(self, raquette):
        dx = self.x - raquette.x
        dy = self.y - raquette.y

        # distance par rapport au centre du cercle
        distance = math.hypot(dx, dy)

        if distance > self.radius + raquette.radius:
            return False

        # calcule l'angle de projection.
        tangent = math.atan2(dy, dx)
        temp_angle = math.pi / 2 + tangent
        total_mass = self.mass + raquette.mass

        (self.angle, self.vitesse) = self.add_vectors(self.angle, self.vitesse * (self.mass - raquette.mass) / total_mass, temp_angle, 2 * raquette.vitesse * raquette.mass / total_mass)

        # permet de pas depasser la vitesse max
        if self.vitesse > const.MAX_VITESSE:
            self.vitesse = const.MAX_VITESSE

        temp_vitesse = raquette.vitesse
        (raquette.angle, raquette.vitesse) = self.add_vectors(raquette.angle, raquette.vitesse * (raquette.mass - self.mass) / total_mass, temp_angle + math.pi, 2 * self.vitesse * self.mass / total_mass)
        raquette.vitesse = temp_vitesse

        offset = 0.5 * (self.radius + raquette.radius - distance + 1)
        self.x += math.sin(temp_angle) * offset
        self.y -= math.cos(temp_angle) * offset
        raquette.x -= math.sin(temp_angle) * offset
        raquette.y += math.cos(temp_angle) * offset
        return True

    def cercle_reset(self, player):
        if player == 1:
            self.x = 3*const.LARGEUR/4
        if player == 2:
            self.x = const.LARGEUR/4
        self.y = const.HAUTEUR/2
        self.angle = 0
        self.vitesse = 0

    def reset(self, vitesse, player):
        if player == 1:
            self.angle = rand.uniform(-math.pi, 0)
        elif player == 2:
            self.angle = rand.uniform(0, math.pi)
        self.vitesse = vitesse
        self.x = const.LARGEUR / 2
        self.y = const.HAUTEUR / 2

    def reset_fin(self, vitesse):
        self.angle = 0
        self.vitesse = vitesse
        self.x = const.LARGEUR / 2
        self.y = const.HAUTEUR / 2

    def draw(self, ecran):
        pygame.draw.circle(ecran, const.BLANC, (int(self.x), int(self.y)), self.radius)

    def get_pos(self):
        print(self.x, self.y)
