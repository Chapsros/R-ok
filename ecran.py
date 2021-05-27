import sys
import random
import string
from globals import *
from constants import *
from os import listdir, close
from os.path import isfile, join

x = Taille_cercle+30
positionGrid = [145, 145+x, 145+2*x, 145+3*x+250, 145+4*x+250, 145+5*x+250]

# ecran fin de jeu
def fin_jeu(ecran, clock, couleur_fond, nom_joueur):

    texte1 = pygame.font.Font(os.path.join(assets, 'MR ROBOT.ttf'), 140)
    texte2 = pygame.font.Font('freesansbold.ttf', 45)
    texte3 = pygame.font.Font('freesansbold.ttf', 30)

    while True:
        delay = 0
        ecran.fill(couleur_fond)

        # inputs souris
        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            # R pour reset le jeu
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return 1
            # M pour aller au menu
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                return 2
            # esc ou Q pour quitter
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # affichage du nombre de victoire
        if delay == 0:
            disp_text(ecran, "{0} WINS".format(string.upper(nom_joueur)), (largeur / 2, hauteur / 2 - 150),
                      texte1, NOIR)
        # Boutton reset
        if abs(mouse_pos[0] - 200) < bouttonRadius and abs(mouse_pos[1] - 470) < bouttonRadius:
            button_circle(ecran, colors[0][0], (200, 470), "Reset", texte2, (255, 255, 255),
                          (largeur / 2 - 400, hauteur / 2 + 170), bouttonRadius)
            if mouse_press[0] == 1:
                return 1

        else:
            button_circle(ecran, colors[0][0], (200, 470), "Reset", texte3, (255, 255, 255),
                          (largeur / 2 - 400, hauteur / 2 + 170), bouttonRadius)

        # Boutton Menu
        if abs(mouse_pos[0] - 600) < bouttonRadius and abs(mouse_pos[1] - 470) < bouttonRadius:
            button_circle(ecran, colors[4][1], (600, 470), "Menu", texte2, (255, 255, 255),
                          (largeur / 2, hauteur / 2 + 170), bouttonRadius)
            if mouse_press[0] == 1:
                return 2

        else:
            button_circle(ecran, colors[4][1], (600, 470), "Menu", texte3, (255, 255, 255),
                          (largeur / 2, hauteur / 2 + 170), bouttonRadius)

        # Boutton quitter
        if abs(mouse_pos[0] - 1000) < bouttonRadius and abs(mouse_pos[1] - 470) < bouttonRadius:
            button_circle(ecran, colors[1][1], (1000, 470), "Quit", texte2, (255, 255, 255),
                          (largeur / 2 + 400, hauteur / 2 + 170), bouttonRadius)
            if mouse_press[0] == 1:
                pygame.quit()        
                return 3
        else:
            button_circle(ecran, colors[1][0], (1000, 470), "Quit", texte3, (255, 255, 255),
                          (largeur / 2 + 400, hauteur / 2 + 170), bouttonRadius)

        pygame.display.update()
        clock.tick(10)


selected_color = theme_colors[0][0]


def theme_ecran(ecran, clock, scr_largeur, scr_hauteur):

    # initialisation du font
    petit_texte = pygame.font.SysFont("comicsans", 35)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        ecran.fill((60, 90, 100))
        global selected_color

        # parametre de la souris
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # positions du terrain
        pos_of_boxes = [[200, 50], [scr_largeur-500, 50], [200, scr_hauteur / 2 - 50], [scr_largeur - 500,
                                                                                     scr_hauteur / 2 - 50]]

        # loop pour tracer les lignes du terrain
        i = 0
        for xy in pos_of_boxes:
            if (mouse[0] > xy[0]) and (mouse[0] < xy[0] + 300) and (mouse[1] > xy[1]) and (mouse[1] < xy[1] + 150):
                pygame.draw.rect(ecran, theme_colors[i][0], (xy[0], xy[1], 300, 150), 0)  # rectangle
                if click[0] == 1:
                    selected_color = theme_colors[i][0]
            else:
                pygame.draw.rect(ecran, theme_colors[i][1], (xy[0], xy[1], 300, 150), 0)   # rectangle
            pygame.draw.rect(ecran, const.BLANC, (xy[0], xy[1], 300, 150), 2)  # bordure
            pygame.draw.circle(ecran, const.BLANC, (xy[0] + 150, xy[1] + 75), 30, 2)   # cercle au milieu
            pygame.draw.line(ecran, const.BLANC, (xy[0] + 150, xy[1]), (xy[0] + 150, xy[1] + 150), 2)  # ligne du milieu
            pygame.draw.rect(ecran, const.BLANC, (xy[0], xy[1] + 30, 50, 95), 2)   # rectangle devant les gages gauche
            pygame.draw.rect(ecran, const.BLANC, (xy[0] + 300 - 50, xy[1] + 30, 50, 95), 2)    # rectangle devant les gages droite
            i = i+1

        # ecran selection couleur du terrain
        disp_text(ecran, "Couleur choisie", (largeur / 2, 450), petit_texte, selected_color)

        # start
        x, y = largeur / 2 - 50, 500
        if (mouse[0] > x) and (mouse[0] < x + 90) and (mouse[1] > 500) and (mouse[1] < 530):
            pygame.draw.rect(ecran, colors[0][1], (largeur / 2 - 50, 500, 90, 30), 0)
            if click[0] == 1:
                return selected_color
        else:
            pygame.draw.rect(ecran, colors[0][0], (largeur / 2 - 50, 500, 90, 30), 0)
        text_start = petit_texte.render("START", True, const.BLANC)
        ecran.blit(text_start, [largeur / 2 - 44, 500])

        pygame.display.update()
        clock.tick(10)


def text_obj(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


# fonction qui rend les bouttons interactif


def button_circle(ecran, butt_color, button_pos, text, text_size, text_color,
                  text_pos, radius):
    pygame.draw.circle(ecran, butt_color, button_pos, radius)
    text_surf, text_rect = text_obj(text, text_size, text_color)
    text_rect.center = text_pos
    ecran.blit(text_surf, text_rect)


# fonction pour ecrire du texte sur l'ecran


def disp_text(ecran, text, center, font_and_size, color):
    text_surf, text_rect = text_obj(text, font_and_size, color)
    text_rect.center = center
    ecran.blit(text_surf, text_rect)


# class pour selectionner les couleurs des terrains


class SelBox:
    def __init__(self, pid, grid_position):
        self.playerId = pid
        self.gridPos = grid_position
        self.length = Taille_cercle + 10
        self.breadth = Taille_cercle + 10
        self.init_gridPos = grid_position

    def move_left(self):
        if self.init_gridPos+2 >= self.gridPos > self.init_gridPos:
            self.gridPos -= 1

    def move_right(self):
        if self.init_gridPos <= self.gridPos < self.init_gridPos+2:
            self.gridPos += 1

    def draw(self, ecran, x, y):
        pygame.draw.rect(ecran, (255, 255, 255),
                         (x, y, self.length, self.breadth))



#ECRAN D'INSTRUCTIONS

def show_info(ecran, scr_largeur, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        ecran.fill((60, 90, 100))
        main_text = pygame.font.Font(os.path.join(assets,'Jelly Crazies.ttf'), 40)
        other_text = pygame.font.Font(os.path.join(assets,'CutieShark.ttf'), 30)

        game_play = main_text.render('INSTRUCTIONS', True, const.VIOLET)
        ecran.blit(game_play, (350, 20))

        line = other_text.render("CONTRÔLES: ", True, const.VIOLINE)
        ecran.blit(line, (130, 120))
        line = other_text.render("PLAYER 1 : Z,Q,S,D     PLAYER 2 : Touches directionnelles", True, const.VIOLINE)
        ecran.blit(line, (150, 150))

        line = other_text.render("1. Entrez le nom et choisissez la couleur de chaque joueur.", True, const.BLANC)
        ecran.blit(line, (100, 200))

        line = other_text.render("2. Choisissez la couleur du terrain.", True, const.BLANC)
        ecran.blit(line, (100, 250))

        line = other_text.render("3. Déplacez votre palais afin de marquer ou de bloquer les tirs adverses.", True, const.BLANC)
        ecran.blit(line, (100, 300))   

        line = other_text.render("4. Le premier joueur à 7 points, gagne la mange.", True, const.BLANC)
        ecran.blit(line, (100, 350))
        line = other_text.render("Le joueur ayant remporté 3 manches est vainqueur.", True, const.BLANC)
        ecran.blit(line, (130, 385))

        line = other_text.render("5. Le vainqueur d'une manche se voit attribuer des points", True, const.BLANC)
        ecran.blit(line, (100, 435))
        line = other_text.render("correspondant à la différence des points des 2 joueurs.", True, const.BLANC)
        ecran.blit(line, (130, 465))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #BOUTON RETOUR
        if abs(mouse[0] - scr_largeur / 2 - 50) < 120 and abs(mouse[1] - 550) < 40:
            pygame.draw.rect(ecran, const.VIOLINE, (scr_largeur / 2 - 50, 520, 130, 30))
            if click[0] == 1:
                return
        else:
            pygame.draw.rect(ecran, const.VIOLET, (scr_largeur / 2 - 50, 520, 130, 30))

        back = other_text.render("RETOUR", True, const.NOIR)
        ecran.blit(back, (scr_largeur / 2 - 29, 515))
        pygame.display.flip()
        clock.tick(10)

#ECRAN SHOP

def show_shop(ecran, scr_largeur, clock, player_1_name, player_2_name):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        ecran.fill((60, 90, 100))
        main_text = pygame.font.Font(os.path.join(assets,'Jelly Crazies.ttf'), 35)
        other_text = pygame.font.Font(os.path.join(assets,'CutieShark.ttf'), 25)
        player_text = pygame.font.Font('freesansbold.ttf', 15)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        game_play = main_text.render('SHOP', True, const.VIOLET)
        ecran.blit(game_play, (500, 10))
        line = other_text.render("Chaque amélioration coûte 10 points", True, const.VIOLINE)
        ecran.blit(line, (420, 80))

        player_1_point = import_save_alljoueur(player_1_name)[0]
        player_1_taille = import_save_alljoueur(player_1_name)[1]
        player_1_vitesse = import_save_alljoueur(player_1_name)[2]
        player_1_mass = import_save_alljoueur(player_1_name)[3]
        player_1_cage = import_save_alljoueur(player_1_name)[4]

        player_2_point = import_save_alljoueur(player_2_name)[0]
        player_2_taille = import_save_alljoueur(player_2_name)[1]
        player_2_vitesse = import_save_alljoueur(player_2_name)[2]
        player_2_mass = import_save_alljoueur(player_2_name)[3]
        player_2_cage = import_save_alljoueur(player_2_name)[4]
        

        line = other_text.render("Points joueur 1 : " + str(player_1_point), True, const.BLEU)
        ecran.blit(line, (20, 20))
        line = other_text.render("Points Joueur 2 : " + str(player_2_point), True, const.BLEU)
        ecran.blit(line, (scr_largeur - 200, 20))

        #TAILLE DU PALAIS
        line = other_text.render("Taille de la raquette", True, const.BLANC)
        ecran.blit(line, (305, 150))

        line = player_text.render(player_1_name, True, const.BLANC)
        ecran.blit(line, (370, 193))

        #BOUTON - JOUEUR 1
        if abs(mouse[0] - (300)) < bouttonRadius_shop and abs(mouse[1] - 200) < bouttonRadius_shop:
            button_circle(ecran, colors[1][1], (300, 200), "-", other_text, (255, 255, 255),
                          (300, 200), bouttonRadius_shop)
            if click[0] == 1:
                if player_1_taille <= 90 and player_1_taille > 40:
                    player_1_point += 10
                    player_1_taille -= 5
                    update_save_joueur(player_1_name, player_1_point, player_1_taille, player_1_vitesse, player_1_mass, player_1_cage)
        else:
            button_circle(ecran, colors[1][0], (300, 200), "-", player_text, (255, 255, 255),
                          (300, 200), bouttonRadius_shop)

        #BOUTON + JOUEUR 1
        if abs(mouse[0] - (500)) < bouttonRadius_shop and abs(mouse[1] - 200) < bouttonRadius_shop:
            button_circle(ecran, colors[0][1], (500, 200), "+", other_text, (255, 255, 255),
                          (500, 200), bouttonRadius_shop)
            if click[0] == 1:
                if player_1_point >= 10 and player_1_taille < 90:
                    player_1_point -= 10
                    player_1_taille += 5
                    update_save_joueur(player_1_name, player_1_point, player_1_taille, player_1_vitesse, player_1_mass, player_1_cage)
        else:
            button_circle(ecran, colors[0][0], (500, 200), "+", player_text, (255, 255, 255),
                          (500, 200), bouttonRadius_shop)
        
        line = player_text.render(player_2_name, True, const.BLANC)
        ecran.blit(line, (370, 223))

        #BOUTON - JOUEUR 2
        if abs(mouse[0] - (300)) < bouttonRadius_shop and abs(mouse[1] - 230) < bouttonRadius_shop:
            button_circle(ecran, colors[1][1], (300, 230), "-", other_text, (255, 255, 255),
                          (300, 230), bouttonRadius_shop)
            if click[0] == 1:
                if player_2_taille <= 90 and player_2_taille > 40:
                    player_2_point += 10
                    player_2_taille -= 5
                    update_save_joueur(player_2_name, player_2_point, player_2_taille, player_2_vitesse, player_2_mass, player_2_cage)
        else:
            button_circle(ecran, colors[1][0], (300, 230), "-", player_text, (255, 255, 255),
                          (300, 230), bouttonRadius_shop)

        #BOUTON + JOUEUR 2
        if abs(mouse[0] - (500)) < bouttonRadius_shop and abs(mouse[1] - 230) < bouttonRadius_shop:
            button_circle(ecran, colors[0][1], (500, 230), "+", other_text, (255, 255, 255),
                          (500, 230), bouttonRadius_shop)
            if click[0] == 1:
                if player_2_point >= 10 and player_2_taille < 90:
                    player_2_point -= 10
                    player_2_taille += 5
                    update_save_joueur(player_2_name, player_2_point, player_2_taille, player_2_vitesse, player_2_mass, player_2_cage)
        else:
            button_circle(ecran, colors[0][0], (500, 230), "+", player_text, (255, 255, 255),
                          (500, 230), bouttonRadius_shop)

        #VITESSE DE LA RAQUETTE
        line = other_text.render("Vitesse de la raquette", True, const.BLANC)
        ecran.blit(line, (305, 300))

        line = player_text.render(player_1_name, True, const.BLANC)
        ecran.blit(line, (370, 343))

        #BOUTON - JOUEUR 1
        if abs(mouse[0] - (300)) < bouttonRadius_shop and abs(mouse[1] - 350) < bouttonRadius_shop:
            button_circle(ecran, colors[1][1], (300, 350), "-", other_text, (255, 255, 255),
                          (300, 350), bouttonRadius_shop)
            if click[0] == 1:
                if player_1_vitesse <= 500 and player_1_vitesse > 300:
                    player_1_point += 10
                    player_1_vitesse -= 20
                    update_save_joueur(player_1_name, player_1_point, player_1_taille, player_1_vitesse, player_1_mass, player_1_cage)
        else:
            button_circle(ecran, colors[1][0], (300, 350), "-", player_text, (255, 255, 255),
                          (300, 350), bouttonRadius_shop)

        #BOUTON + JOUEUR 1
        if abs(mouse[0] - (500)) < bouttonRadius_shop and abs(mouse[1] - 350) < bouttonRadius_shop:
            button_circle(ecran, colors[0][1], (500, 350), "+", other_text, (255, 255, 255),
                          (500, 350), bouttonRadius_shop)
            if click[0] == 1:
                if player_1_point >= 10 and player_1_vitesse < 500:
                    player_1_point -= 10
                    player_1_vitesse += 20
                    update_save_joueur(player_1_name, player_1_point, player_1_taille, player_1_vitesse, player_1_mass, player_1_cage)
        else:
            button_circle(ecran, colors[0][0], (500, 350), "+", player_text, (255, 255, 255),
                          (500, 350), bouttonRadius_shop)

        line = player_text.render(player_2_name, True, const.BLANC)
        ecran.blit(line, (370, 373))

        #BOUTON - JOUEUR 2
        if abs(mouse[0] - (300)) < bouttonRadius_shop and abs(mouse[1] - 380) < bouttonRadius_shop:
            button_circle(ecran, colors[1][1], (300, 380), "-", other_text, (255, 255, 255),
                          (300, 380), bouttonRadius_shop)
            if click[0] == 1:
                if player_2_vitesse <= 500 and player_2_vitesse > 300:
                    player_2_point += 10
                    player_2_vitesse -= 20
                    update_save_joueur(player_2_name, player_2_point, player_2_taille, player_2_vitesse, player_2_mass, player_2_cage)
        else:
            button_circle(ecran, colors[1][0], (300, 380), "-", player_text, (255, 255, 255),
                          (300, 380), bouttonRadius_shop)

        #BOUTON + JOUEUR 2
        if abs(mouse[0] - (500)) < bouttonRadius_shop and abs(mouse[1] - 380) < bouttonRadius_shop:
            button_circle(ecran, colors[0][1], (500, 380), "+", other_text, (255, 255, 255),
                          (500, 380), bouttonRadius_shop)
            if click[0] == 1:
                if player_2_point >= 10 and player_2_vitesse < 500:
                    player_2_point -= 10
                    player_2_vitesse += 20
                    update_save_joueur(player_2_name, player_2_point, player_2_taille, player_2_vitesse, player_2_mass, player_2_cage)
        else:
            button_circle(ecran, colors[0][0], (500, 380), "+", player_text, (255, 255, 255),
                          (500, 380), bouttonRadius_shop)


        #PUISSANCE DE LA RAQUETE
        line = other_text.render("Puissance de la raquette", True, const.BLANC)
        ecran.blit(line, (670,  150))

        line = player_text.render(player_1_name, True, const.BLANC)
        ecran.blit(line, (760, 193))

        #BOUTON - JOUEUR 1
        if abs(mouse[0] - (690)) < bouttonRadius_shop and abs(mouse[1] - 200) < bouttonRadius_shop:
            button_circle(ecran, colors[1][1], (690, 200), "-", other_text, (255, 255, 255),
                          (690, 200), bouttonRadius_shop)
            if click[0] == 1:
                if player_1_mass <= 3500 and player_1_mass > 1500:
                    player_1_point += 10
                    player_1_mass -= 500
                    update_save_joueur(player_1_name, player_1_point, player_1_taille, player_1_vitesse, player_1_mass, player_1_cage)
        else:
            button_circle(ecran, colors[1][0], (690, 200), "-", player_text, (255, 255, 255),
                          (690, 200), bouttonRadius_shop)

        #BOUTON + JOUEUR 1
        if abs(mouse[0] - (890)) < bouttonRadius_shop and abs(mouse[1] - 200) < bouttonRadius_shop:
            button_circle(ecran, colors[0][1], (890, 200), "+", other_text, (255, 255, 255),
                          (890, 200), bouttonRadius_shop)
            if click[0] == 1:
                if player_1_point >= 10 and player_1_mass < 3500:
                    player_1_point -= 10
                    player_1_mass += 500
                    update_save_joueur(player_1_name, player_1_point, player_1_taille, player_1_vitesse, player_1_mass, player_1_cage)
        else:
            button_circle(ecran, colors[0][0], (890, 200), "+", player_text, (255, 255, 255),
                          (890, 200), bouttonRadius_shop)

        line = player_text.render(player_2_name, True, const.BLANC)
        ecran.blit(line, (760, 223))

        #BOUTON - JOUEUR 2
        if abs(mouse[0] - (690)) < bouttonRadius_shop and abs(mouse[1] - 230) < bouttonRadius_shop:
            button_circle(ecran, colors[1][1], (690, 230), "-", other_text, (255, 255, 255),
                          (690, 230), bouttonRadius_shop)
            if click[0] == 1:
                if player_2_mass <= 3500 and player_2_mass > 1500:
                    player_2_point += 10
                    player_2_mass -= 500
                    update_save_joueur(player_2_name, player_2_point, player_2_taille, player_2_vitesse, player_2_mass, player_2_cage)
        else:
            button_circle(ecran, colors[1][0], (690, 230), "-", player_text, (255, 255, 255),
                          (690, 230), bouttonRadius_shop)

        #BOUTON + JOUEUR 2
        if abs(mouse[0] - (890)) < bouttonRadius_shop and abs(mouse[1] - 230) < bouttonRadius_shop:
            button_circle(ecran, colors[0][1], (890, 230), "+", other_text, (255, 255, 255),
                          (890, 230), bouttonRadius_shop)
            if click[0] == 1:
                if player_2_point >= 10 and player_2_mass < 3500:
                    player_2_point -= 10
                    player_2_mass += 500
                    update_save_joueur(player_2_name, player_2_point, player_2_taille, player_2_vitesse, player_2_mass, player_2_cage)
        else:
            button_circle(ecran, colors[0][0], (890, 230), "+", player_text, (255, 255, 255),
                          (890, 230), bouttonRadius_shop)

        #TAILLE DES CAGES
        line = other_text.render("Taille des cages", True, const.BLANC)
        ecran.blit(line, (715, 300))
        line = player_text.render(player_1_name, True, const.BLANC)
        ecran.blit(line, (760, 343))

        #BOUTON - JOUEUR 1
        if abs(mouse[0] - (690)) < bouttonRadius_shop and abs(mouse[1] - 350) < bouttonRadius_shop:
            button_circle(ecran, colors[1][1], (690, 350), "-", other_text, (255, 255, 255),
                          (690, 350), bouttonRadius_shop)
            if click[0] == 1:
                if player_1_cage < 200 and player_1_cage >= 100:
                    player_1_point += 10
                    player_1_cage += 10
                    update_save_joueur(player_1_name, player_1_point, player_1_taille, player_1_vitesse, player_1_mass, player_1_cage)
        else:
            button_circle(ecran, colors[1][0], (690, 350), "-", player_text, (255, 255, 255),
                          (690, 350), bouttonRadius_shop)

        #BOUTON + JOUEUR 1
        if abs(mouse[0] - (890)) < bouttonRadius_shop and abs(mouse[1] - 350) < bouttonRadius_shop:
            button_circle(ecran, colors[0][1], (890, 350), "+", other_text, (255, 255, 255),
                          (890, 350), bouttonRadius_shop)
            if click[0] == 1:
                if player_1_point >= 10 and player_1_cage <= 200 and player_1_cage > 100:
                    player_1_point -= 10
                    player_1_cage -= 10
                    update_save_joueur(player_1_name, player_1_point, player_1_taille, player_1_vitesse, player_1_mass, player_1_cage)
        else:
            button_circle(ecran, colors[0][0], (890, 350), "+", player_text, (255, 255, 255),
                          (890, 350), bouttonRadius_shop)

        line = player_text.render(player_2_name, True, const.BLANC)
        ecran.blit(line, (760, 373))

        #BOUTON - JOUEUR 2
        if abs(mouse[0] - (690)) < bouttonRadius_shop and abs(mouse[1] - 380) < bouttonRadius_shop:
            button_circle(ecran, colors[1][1], (690, 380), "-", other_text, (255, 255, 255),
                          (690, 380), bouttonRadius_shop)
            if click[0] == 1:
                if player_2_cage < 200 and player_2_cage >= 100:
                    player_2_point += 10
                    player_2_cage += 10
                    update_save_joueur(player_2_name, player_2_point, player_2_taille, player_2_vitesse, player_2_mass, player_2_cage)
        else:
            button_circle(ecran, colors[1][0], (690, 380), "-", player_text, (255, 255, 255),
                          (690, 380), bouttonRadius_shop)

        #BOUTON + JOUEUR 2
        if abs(mouse[0] - (890)) < bouttonRadius_shop and abs(mouse[1] - 380) < bouttonRadius_shop:
            button_circle(ecran, colors[0][1], (890, 380), "+", other_text, (255, 255, 255),
                          (890, 380), bouttonRadius_shop)
            if click[0] == 1:
                if player_2_point >= 10 and player_2_cage <= 200 and player_2_cage > 100:
                    player_2_point -= 10
                    player_2_cage -= 10
                    update_save_joueur(player_2_name, player_2_point, player_2_taille, player_2_vitesse, player_2_mass, player_2_cage)
        else:
            button_circle(ecran, colors[0][0], (890, 380), "+", player_text, (255, 255, 255),
                          (890, 380), bouttonRadius_shop)

        #BOUTON RETOUR
        if abs(mouse[0] - scr_largeur / 2 - 50) < 120 and abs(mouse[1] - 550) < 40:
            pygame.draw.rect(ecran, const.VIOLINE, (scr_largeur / 2 - 65, 520, 130, 30))
            if click[0] == 1:
                return
        else:
            pygame.draw.rect(ecran, const.VIOLET, (scr_largeur / 2 - 65, 520, 130, 30))

        back = other_text.render("RETOUR", True, const.NOIR)
        ecran.blit(back, (scr_largeur / 2 - 35, 518))
        pygame.display.flip()
        clock.tick(10)

# fonction ecran classement
def show_classement(ecran, scr_largeur, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        ecran.fill((60, 90, 100))
        main_text = pygame.font.Font('freesansbold.ttf', 35)
        other_text = pygame.font.Font('freesansbold.ttf', 25)

        fichiers = [f for f in listdir("joueur") if isfile(join("joueur", f))]
        all = []
        
        for nom in fichiers:
            one = [nom, import_save_alljoueur(nom)[0]]
            all.append(one)

        all = sorted(all, key=lambda M : M[1], reverse=True)        

        game_play = main_text.render('CLASSEMENT', True, colors[2][0])
        ecran.blit(game_play, (scr_largeur / 2 - 130, 70))

        if (len(fichiers) >= 1):
            line = other_text.render("1er avec " + str(all[0][1]) + " points : " + all[0][0], True, const.NOIR)
            ecran.blit(line, (scr_largeur / 8, 160))

        if (len(fichiers) >= 2):
            line = other_text.render("2eme avec " + str(all[1][1]) + " points : " + all[1][0], True, const.NOIR)
            ecran.blit(line, (scr_largeur / 8, 230))

        if (len(fichiers) >= 3):
            line = other_text.render("3eme avec " + str(all[2][1]) + " points : " + all[2][0], True, const.NOIR)
            ecran.blit(line, (scr_largeur / 8, 300))

        if (len(fichiers) >= 4):
            line = other_text.render("4eme avec " + str(all[3][1]) + " points : " + all[3][0], True, const.NOIR)
            ecran.blit(line, (scr_largeur / 8, 370))

        if (len(fichiers) >= 5):
            line = other_text.render("5eme avec " + str(all[4][1]) + " points : " + all[4][0], True, const.NOIR)
            ecran.blit(line, (scr_largeur / 8, 440))

        if (len(fichiers) >= 6):
            line = other_text.render("6eme avec " + str(all[5][1]) + " points : " + all[5][0], True, const.NOIR)
            ecran.blit(line, (scr_largeur / 2, 160))
        
        if (len(fichiers) >= 7):
            line = other_text.render("7eme avec " + str(all[6][1]) + " points : " + all[6][0], True, const.NOIR)
            ecran.blit(line, (scr_largeur / 2, 230))

        if (len(fichiers) >= 8):
            line = other_text.render("8eme avec " + str(all[7][1]) + " points : " + all[7][0], True, const.NOIR)
            ecran.blit(line, (scr_largeur / 2, 300))

        if (len(fichiers) >= 9):
            line = other_text.render("9eme avec " + str(all[8][1]) + " points : " + all[8][0], True, const.NOIR)
            ecran.blit(line, (scr_largeur / 2, 370))
        
        if (len(fichiers) >= 10):
            line = other_text.render("10eme avec " + str(all[9][1]) + " points : " + all[9][0], True, const.NOIR)
            ecran.blit(line, (scr_largeur / 2, 440))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Boutton retour
        if abs(mouse[0] - scr_largeur / 2 - 70) < 120 and abs(mouse[1] - 550) < 40:
            pygame.draw.rect(ecran, colors[2][1], (scr_largeur / 2 - 70, 520, 130, 30))
            if click[0] == 1:
                return
        else:
            pygame.draw.rect(ecran, colors[2][0], (scr_largeur / 2 - 70, 520, 130, 30))

        back = other_text.render("RETOUR", True, const.NOIR)
        ecran.blit(back, (scr_largeur / 2 - 60, 525))
        pygame.display.flip()
        clock.tick(10)

# fonction qui crée le l'ecran de départ


def air_hockey_start(ecran, clock, scr_largeur, scr_hauteur):

    p1_color_select = 1     # couleur de base des raquettes
    p2_color_select = 1    # couleur de base des raquettes
    player1_color = colors[p1_color_select][1]  # couleur de base des raquettes
    player2_color = colors[p2_color_select][1]  # couleur de base des raquettes
    sel_p1 = SelBox(1, 0)        # box selection couleur
    sel_p2 = SelBox(2, 3)        # box selection couleur
    player_1_key = False     # cela sert pour selectionner le nom des joueurs

    # nom des joueurs
    player_1_name = ""
    player_2_name = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                # joueur 1 controle
                elif event.key == pygame.K_a:
                    if p1_color_select > 1:
                        p1_color_select -= 1
                    sel_p1.move_left()
                elif event.key == pygame.K_d:
                    if p1_color_select < 3:
                        p1_color_select += 1
                    sel_p1.move_right()

                # joueur 2 controle
                elif event.key == pygame.K_LEFT:
                    if p2_color_select > 1:
                        p2_color_select -= 1
                    sel_p2.move_left()
                elif event.key == pygame.K_RIGHT:
                    if p2_color_select < 3:
                        p2_color_select += 1
                    sel_p2.move_right()

        ecran.fill((60, 90, 100))
        texte1 = pygame.font.Font(os.path.join(assets, 'Jelly Crazies.ttf'), 50)
        texte2 = pygame.font.Font('freesansbold.ttf', 40)
        texte3 = pygame.font.Font('freesansbold.ttf', 30)
        disp_text(ecran, "R OKAY", (scr_largeur / 2, 100), texte1, colors[4][0])

        # position de la souris et du click
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # choix des couleurs de la raquette

        x_pos_rect_left = 150
        y_pos_rect_left = scr_hauteur/2 - 70

        x_pos_rect_right = scr_largeur - 150 - 320
        y_pos_rect_right = scr_hauteur/2 - 70

        # bordure ligne blanche
        pygame.draw.rect(ecran, (255, 255, 255), (x_pos_rect_left - 10, y_pos_rect_left - 10, 320, 100), 1)
        # affichage selection box
        sel_p1.draw(ecran, positionGrid[sel_p1.gridPos], y_pos_rect_left - 5)
        sel_p2.draw(ecran, positionGrid[sel_p2.gridPos], y_pos_rect_left - 5)

        # 3 couleur au choix
        for x in range(1, 4):
            if (mouse[0] > x_pos_rect_left) and (mouse[0] < x_pos_rect_left + Taille_cercle) and \
                    (mouse[1] > y_pos_rect_left) and (mouse[1] < (y_pos_rect_left + Taille_cercle)):
                pygame.draw.rect(ecran, colors[x][0], (x_pos_rect_left, y_pos_rect_left, Taille_cercle, Taille_cercle))
                if click[0] == 1:
                    p1_color_select = x
                    sel_p1.gridPos = x-1
            else:
                pygame.draw.rect(ecran, colors[x][1], (x_pos_rect_left, y_pos_rect_left, Taille_cercle, Taille_cercle))
            x_pos_rect_left = x_pos_rect_left + Taille_cercle + 30

        player1_color = colors[p1_color_select][1]

        # couleur raquette joueur 2

        # bordure blanche
        pygame.draw.rect(ecran, (255, 255, 255), (x_pos_rect_right-10, y_pos_rect_right-10, 320, 100), 1)

        # choix des 3 couleurs des raquettes
        for x in range(1, 4):
            if (mouse[0] > x_pos_rect_right) and (mouse[0] < (x_pos_rect_right + Taille_cercle)) and \
                    (mouse[1] > y_pos_rect_right) and (mouse[1] < (y_pos_rect_right + Taille_cercle)):
                pygame.draw.rect(ecran, colors[x][0], (x_pos_rect_right, y_pos_rect_right, Taille_cercle, Taille_cercle))
                if click[0] == 1:
                    p2_color_select = x
                    sel_p2.gridPos = x-1 + 3
            else:
                pygame.draw.rect(ecran, colors[x][1], (x_pos_rect_right, y_pos_rect_right, Taille_cercle, Taille_cercle))
            x_pos_rect_right = x_pos_rect_right + Taille_cercle + 30

        player2_color = colors[p2_color_select][1]

        # ecran couleur choisie

        disp_text(ecran, "Couleur choisie", (scr_largeur / 4, y_pos_rect_left + 120), texte3, player1_color)
        disp_text(ecran, "Couleur choisie", (scr_largeur - scr_largeur/4 - 20, y_pos_rect_left + 120),
                  texte3, player2_color)

        # boutton pour voir le classement
        if abs(mouse[0] - 200) < bouttonRadius and abs(mouse[1] - 470) < bouttonRadius:
            button_circle(ecran, colors[2][1], (200, 470), "Score", texte2, (255, 255, 255),
                          (scr_largeur / 2 - 400, scr_hauteur / 2 + 170), bouttonRadius)
            if click[0] == 1:
                show_classement(ecran, scr_largeur, clock)

        else:
            button_circle(ecran, colors[2][0], (200, 470), "Score", texte3, (255, 255, 255),
                          (scr_largeur / 2 - 400, scr_hauteur / 2 + 170), bouttonRadius)

        # jouer
        if abs(mouse[0] - 600) < bouttonRadius and abs(mouse[1] - 470) < bouttonRadius:
            button_circle(ecran, colors[0][1], (600, 470), "Jouer", texte2, (255, 255, 255),
                          (scr_largeur / 2, scr_hauteur / 2 + 170), bouttonRadius)
            if click[0] == 1:
                if player_1_name is "":
                    player_1_name = "Player 1"
                if player_2_name is "":
                    player_2_name = "Player 2"
                return 2, player1_color, player2_color, player_1_name, player_2_name

        else:
            button_circle(ecran, colors[0][0], (600, 470), "Jouer", texte3, (255, 255, 255),
                          (scr_largeur / 2, scr_hauteur / 2 + 170), bouttonRadius)

        # boutton pour quitter
        if abs(mouse[0] - 1000) < bouttonRadius and abs(mouse[1] - 470) < bouttonRadius:
            button_circle(ecran, colors[1][1], (1000, 470), "Quit", texte2, (255, 255, 255),
                          (scr_largeur / 2 + 400, scr_hauteur / 2 + 170), bouttonRadius)
            if click[0] == 1:
                pygame.quit()
                sys.exit()
        else:
            button_circle(ecran, colors[1][0], (1000, 470), "Quit", texte3, (255, 255, 255),
                          (scr_largeur / 2 + 400, scr_hauteur / 2 + 170), bouttonRadius)

        # boutton quitter
        ecran.blit(info_image, (40, 20))
        if abs(mouse[0] - (40 + 32)) < INFO_BUTTON_RADIUS and abs(mouse[1] - (20 + 32)) < INFO_BUTTON_RADIUS:
            if click[0] == 1:
                show_info(ecran, scr_largeur, clock)

        # position de base joueur 1 et 2
        x1, y1 = 140, 170
        x2, y2 = scr_largeur / 2 + 120, 170
        pygame.draw.rect(ecran, const.BLANC, (x2, y2, 320, 50), 1)

        # nom du joueur 1
        pygame.draw.rect(ecran, (60, 90, 100), (x1, y1, 320, 50), 0)
        pygame.draw.rect(ecran, const.BLANC, (x1, y1, 320, 50), 1)
        if player_1_name is "":
            player_1_text = texte3.render("Nom Player 1", True, const.BLANC)
        else:
            player_1_text = texte3.render(player_1_name, True, const.BLANC)
        ecran.blit(player_1_text, [x1 + 10, y1 + 10])

        # nom du joueur 2
        if player_2_name is "":
            player_2_text = texte3.render("Nom Player 2", True, const.BLANC)
        else:
            player_2_text = texte3.render(player_2_name, True, const.BLANC)
        ecran.blit(player_2_text, [x2 + 10, y2 + 10])

        # boutton shop
        ecran.blit(shop_image, (scr_largeur - 100, 20))
        if abs(mouse[0] - (scr_largeur - 100 + 32)) < INFO_BUTTON_RADIUS and abs(mouse[1] - (20 + 32)) < INFO_BUTTON_RADIUS:
            if click[0] == 1:
                if player_1_name is "":
                    player_1_name = "Player 1"
                if player_2_name is "":
                    player_2_name = "Player 2"
                show_shop(ecran, scr_largeur, clock, player_1_name, player_2_name)

        
        if ((mouse[0] > x1) and (mouse[0] < x1 + 320) and (mouse[1] > y1) and (mouse[1] < y1 + 50)) or player_1_key:
            if click[0] == 1 or player_1_key:
                ret = 0
                blink = 0
                while True:

                    mouse = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()
                    disp_text(ecran, "R OKAY", (scr_largeur / 2, 100), texte1, colors[4][0])

                    if blink:
                        blink_ch = "|"
                        blink = 0
                    else:
                        blink_ch = ""
                        blink = 1
                    if mouse[0] < x1 or mouse[0] > x1 + 320 or mouse[1] < y1 or mouse[1] > y1 + 50:
                        if click[0] == 1:
                            ret = 1
                            player_1_key = False
                    if ret:
                        break
                    for event in pygame.event.get():
                        if event.type == pygame.locals.QUIT:
                            sys.exit()
                        if event.type == pygame.locals.KEYDOWN:
                            if event.unicode.isalpha() and not (len(player_1_name) > 8):
                                player_1_name = "{}{}".format(player_1_name, event.unicode)
                            elif event.key == pygame.locals.K_RETOURSPACE:
                                player_1_name = player_1_name[:-1]
                            elif event.key == pygame.locals.K_RETURN:
                                ret = 1
                                player_1_key = False
                    pygame.draw.rect(ecran, const.BLANC, (x1, y1, 320, 50), 0)
                    if not (player_1_name is ""):
                        player_1_text = texte3.render("{0}{1}".format(player_1_name, blink_ch), True, const.NOIR)
                        ecran.blit(player_1_text, [150, 180])
                    pygame.display.flip()
                    clock.tick(10)

        if (mouse[0] > x2) and (mouse[0] < x2 + 320) and (mouse[1] > y2) and (mouse[1] < y2 + 50):
            if click[0] == 1:
                ret = 0
                blink = 0
                while True:
                    mouse = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()

                    disp_text(ecran, "R OKAY", (scr_largeur / 2, 100), texte1, colors[4][0])

                    if blink:
                        blink_ch = "|"
                        blink = 0
                    else:
                        blink_ch = ""
                        blink = 1

                    if (mouse[0] < x2) or (mouse[0] > x2 + 320) or (mouse[1] < y2) or (mouse[1] > y2 + 50):
                        if click[0] == 1:
                            ret = 1
                        if (mouse[0] > x1) and (mouse[0] < x1 + 320) and (mouse[1] > y1) and (mouse[1] < y1 + 50):
                            if click[0] == 1:
                                player_1_key = True
                    if ret:
                        break
                    for event in pygame.event.get():
                        if event.type == pygame.locals.QUIT:
                            sys.exit()
                        if event.type == pygame.locals.KEYDOWN:
                            if event.unicode.isalpha() and not (len(player_2_name) > 8):
                                player_2_name = "{0}{1}".format(player_2_name, event.unicode)
                            elif event.key == pygame.locals.K_RETOURSPACE:
                                player_2_name = player_2_name[:-1]
                            elif event.key == pygame.locals.K_RETURN:
                                ret = 1
                    pygame.draw.rect(ecran, const.BLANC, (x2, y2, 320, 50), 0)
                    if not (player_2_name is ""):
                        player_2_text = texte3.render("{0}{1}".format(player_2_name, blink_ch), True, const.NOIR)
                        ecran.blit(player_2_text, [scr_largeur / 2 + 130, 180])
                    pygame.display.flip()
                    clock.tick(10)

        pygame.display.update()
        clock.tick(10)


# fonction récupère les données des joueurs
def import_save_alljoueur(nom):
    try:
        with open('joueur/' + nom, 'r') as f:
            lines = f.readlines()
            point = int(lines[0].strip())
            player_taille = int(lines[1].strip())
            player_vitesse = int(lines[2].strip())
            player_mass = int(lines[3].strip())
            player_cage = int(lines[4].strip())
    except:
        point = 0
        player_taille = 40
        player_vitesse = 300
        player_mass = 2000
        player_cage = 200
        with open('joueur/' + nom, 'w+') as f:
            f.write(str(point) + "\n")
            f.write(str(player_taille) + "\n")
            f.write(str(player_vitesse) + "\n")
            f.write(str(player_mass) + "\n")
            f.write(str(player_cage) + "\n")
    return point, player_taille, player_vitesse, player_mass, player_cage

def update_save_joueur(name, points, player_taille, player_vitesse, player_mass, player_cage):
    with open('joueur/' + name, 'w') as f:
        f.write(str(points) + "\n")
        f.write(str(player_taille) + "\n")
        f.write(str(player_vitesse) + "\n")
        f.write(str(player_mass) + "\n")
        f.write(str(player_cage) + "\n")
