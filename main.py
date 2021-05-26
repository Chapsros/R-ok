from os import close
import sys
from pygame.locals import *
from raquette import Raquette
from puck import Puck
from globals import *
from ecran import air_hockey_start, disp_text, show_classement, theme_ecran, fin_jeu


def init():
    global raquetteHit, clock, ecran, smallfont, roundfont
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.init()

    gamelogo = pygame.image.load(os.path.join(assets, 'AHlogo.png'))
    pygame.display.set_icon(gamelogo)
    pygame.display.set_caption('Air Hockey')
    ecran = pygame.display.set_mode((largeur, hauteur))

    smallfont = pygame.font.SysFont("comicsans", 35)
    roundfont = pygame.font.SysFont("comicsans", 45)

    clock = pygame.time.Clock()


def score(score1, score2, player_1_name, player_2_name):
    text1 = smallfont.render("{0} : {1}".format(player_1_name, str(score1)), True, const.NOIR)
    text2 = smallfont.render("{0} : {1}".format(player_2_name, str(score2)), True, const.NOIR)

    ecran.blit(text1, [40, 0])
    ecran.blit(text2, [largeur - 150, 0])


def rounds(rounds_p1, rounds_p2, round_no):
    disp_text(ecran, "Round "+str(round_no), (largeur/2, 20), roundfont, const.NOIR)
    disp_text(ecran, str(rounds_p1) + " : " + str(rounds_p2), (largeur / 2, 50), roundfont, const.NOIR)


def end(option, vitesse):
    global rounds_p1, rounds_p2, round_no, score1, score2

    # reset game avec les parametres de base
    if option == 1:
        puck.reset_fin(vitesse)
        raquette1.reset(22, hauteur / 2)
        raquette2.reset(largeur - 20, hauteur / 2)
        score1, score2 = 0, 0
        rounds_p1, rounds_p2 = 0, 0
        round_no = 1
        return False

    # aller au menu
    elif option == 2:
        return True  # le jeu retourne à l'ecran d'accueil

    # Quit game
    else:
        sys.exit()


def notify_round_change(gagnant, player_point, point):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    return        

        round_text = roundfont.render("ROUND {0} COMPLETE".format(round_no), True, colors[2][0])
        ecran.blit(round_text, [largeur / 2 - 150, hauteur / 2 - 100])

        point_text = roundfont.render("{0} GAGNE {1} POINTS".format(gagnant, point), True, colors[2][0])
        ecran.blit(point_text, [largeur / 2 - 200, hauteur / 2 - 50])

        points_text = roundfont.render("Score total : {0} POINTS".format(player_point), True, const.NOIR)
        ecran.blit(points_text, [largeur / 2 - 150, hauteur / 2])

        score_text = roundfont.render("{0}  :  {1}".format(score1, score2), True, const.NOIR)
        ecran.blit(score_text, [largeur / 2 - 37, hauteur / 2 + 50])

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # continue
        x, y = largeur / 2 - 65, hauteur / 2 + 100
        if (mouse[0] > x) and (mouse[0] < x + 150) and (mouse[1] > y) and (mouse[1] < y + 40):
            pygame.draw.rect(ecran, colors[4][1], (x, y, 150, 40))
            if click[0] == 1:
                return
        else:
            pygame.draw.rect(ecran, colors[4][0], (x, y, 150, 40))
        cont_text = smallfont.render("CONTINUE", True, const.BLANC)
        ecran.blit(cont_text, [x + 10, y + 10])

        text = smallfont.render("OR", True, const.NOIR)
        ecran.blit(text, [largeur / 2 - 18, hauteur - 150])
        text = smallfont.render("press space to continue", True, const.NOIR)
        ecran.blit(text, [largeur / 2 - 120, hauteur - 110])

        pygame.display.flip()
        clock.tick(10)


# fonction qui sert a mettre l'ecran en pause

def show_pause_ecran():

    while True:
        text_pause = smallfont.render("PAUSE", True, const.NOIR)
        ecran.blit(text_pause, [largeur / 2 - 44, 200])
        ecran.blit(play_image, [largeur / 2 - 32, hauteur - 70])

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # RESET
        if (mouse[0] > largeur / 4) and (mouse[0] < largeur / 4 + 150) and (mouse[1] > hauteur - 200) and \
                (mouse[1] < hauteur - 160):
            pygame.draw.rect(ecran, colors[4][0], (largeur / 4, hauteur - 200, 150, 40))
            if click[0] == 1:
                return 2
        else:
            pygame.draw.rect(ecran, colors[4][1], (largeur / 4, hauteur - 200, 150, 40))
        text_restart = smallfont.render("RESET", True, const.BLANC)
        ecran.blit(text_restart, [largeur / 4 + 30, hauteur - 195])

        # CONTINUE
        if (mouse[0] > largeur / 2 - 70) and (mouse[0] < largeur / 2 + 80) and (mouse[1] > hauteur - 200) and \
                (mouse[1] < hauteur - 160):
            pygame.draw.rect(ecran, colors[0][0], (largeur / 2 - 70, hauteur - 200, 150, 40))
            if click[0] == 1:
                return 1
        else:
            pygame.draw.rect(ecran, colors[0][1], (largeur / 2 - 70, hauteur - 200, 150, 40))
        text_cont = smallfont.render("CONTINUE", True, const.BLANC)
        ecran.blit(text_cont, [largeur / 2 - 60, hauteur - 195])

        # QUITTER
        if (mouse[0] > largeur / 2 + 150) and (mouse[0] < largeur / 2 + 300) and (mouse[1] > hauteur - 200) and \
                (mouse[1] < hauteur - 160):
            pygame.draw.rect(ecran, colors[1][0], (largeur / 2 + 150, hauteur - 200, 150, 40))
            if click[0] == 1:
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(ecran, colors[1][1], (largeur / 2 + 150, hauteur - 200, 150, 40))
        text_exit = smallfont.render("QUITTER", True, const.BLANC)
        ecran.blit(text_exit, [largeur / 2 + 170, hauteur - 195])

        # regarde si la souris click quelque part
        events = pygame.event.get()
        for event in events:
            # enleve la pause grace à la barre espace
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return 1

            # boutton continuer
            if event.type == pygame.MOUSEBUTTONUP:
                if hits_pause_area(mouse):
                    return 1

            if event.type == QUIT:
                sys.exit()

        pygame.display.flip()
        clock.tick(10)


# fonction qui test si le boutton pause est clicker

def hits_pause_area(mouse_xy):
    return (abs(mouse_xy[0] - largeur / 2) < const.PAUSE_BUTTON_RADIUS) and \
           (abs(mouse_xy[1] - (hauteur - 70 + 32)) < const.PAUSE_BUTTON_RADIUS)

# fonction couleur de fond

def render_field(couleur_fond):
    ecran.fill(couleur_fond)
    pygame.draw.circle(ecran, const.BLANC, (largeur / 2, hauteur / 2), 70, 5)
    # bordure
    pygame.draw.rect(ecran, const.BLANC, (0, 0, largeur, hauteur), 5)
    pygame.draw.rect(ecran, const.BLANC, (0, hauteur / 2 - 150, 150, 300), 5)
    pygame.draw.rect(ecran, const.BLANC, (largeur - 150, hauteur / 2 - 150, 150, 300), 5)
    # cage
    pygame.draw.rect(ecran, const.NOIR, (0, player_1_CAGE_Y1, 5, player_1_cage))
    pygame.draw.rect(ecran, const.NOIR, (largeur - 5, player_2_CAGE_Y1, 5, player_2_cage))
    # Diviseur
    pygame.draw.rect(ecran, const.BLANC, (largeur / 2, 0, 3, hauteur))

    # PAUSE
    ecran.blit(pause_image, (largeur / 2 - 32, hauteur - 70))


def resetround(player):
    puck.cercle_reset(player)
    raquette1.reset(22, hauteur / 2)
    raquette2.reset(largeur - 20, hauteur / 2)


def reset_game(vitesse, player):
    puck.reset(vitesse, player)
    raquette1.reset(22, hauteur / 2)
    raquette2.reset(largeur - 20, hauteur / 2)

# test si le but est entré

def inside_goal(side):
    if side == 0:
        return (puck.x - puck.radius <= 0) and (puck.y >= player_1_CAGE_Y1) and (puck.y <= player_1_CAGE_Y2)

    if side == 1:
        return (puck.x + puck.radius >= largeur) and (puck.y >= player_2_CAGE_Y1) and (puck.y <= player_2_CAGE_Y2)


def import_save_joueur(name):
    try:
        with open('joueur/' + name, 'r') as f:
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
        with open('joueur/' + name, 'w+') as f:
            f.write(str(point) + "\n")
            f.write(str(player_taille) + "\n")
            f.write(str(player_vitesse) + "\n")
            f.write(str(player_mass) + "\n")
            f.write(str(player_cage) + "\n")
        close
    return point, player_taille, player_vitesse, player_mass, player_cage


def update_save_joueur(points, name, player_taille, player_vitesse, player_mass, player_cage):
    with open('joueur/' + name, 'w') as f:
        f.write(str(points) + "\n")
        f.write(str(player_taille) + "\n")
        f.write(str(player_vitesse) + "\n")
        f.write(str(player_mass) + "\n")
        f.write(str(player_cage) + "\n")
    close


# Game Loop
def game_loop(vitesse, player1_color, player2_color, couleur_fond, player_1_name, player_2_name):
    global rounds_p1, rounds_p2, round_no, player_1_point, player_2_point
    rounds_p1, rounds_p2, round_no = 0, 0, 1

    player_1_point = import_save_joueur(player_1_name)[0]
    player_2_point = import_save_joueur(player_2_name)[0]

    while True:
        global score1, score2
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

                ch = show_pause_ecran()

                # si la valeur est 2 le jeu est reset
                if ch == 2:
                    score1 = 0
                    score2 = 0
                    rounds_p1 = 0
                    rounds_p2 = 0
                    round_no = 1
                    reset_game(vitesse, 1)
                    reset_game(vitesse, 2)
                    puck.angle = 0
            
            # quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # verifie la position de la souris
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_xy = pygame.mouse.get_pos()

                # verifie si la souris click sur le boutton pause
                if hits_pause_area(mouse_xy):
                    ch = show_pause_ecran()

                    # si la valeur est 2 le jeu est reset
                    if ch == 2:
                        score1 = 0
                        score2 = 0
                        rounds_p1 = 0
                        rounds_p2 = 0
                        round_no = 1
                        reset_game(vitesse, 1)
                        reset_game(vitesse, 2)
                        puck.angle = 0

        key_presses = pygame.key.get_pressed()

        # Commande player 1
        w = key_presses[pygame.K_w]
        s = key_presses[pygame.K_s]
        d = key_presses[pygame.K_d]
        a = key_presses[pygame.K_a]

        # Commande player 2
        up = key_presses[pygame.K_UP]
        down = key_presses[pygame.K_DOWN]
        right = key_presses[pygame.K_RIGHT]
        left = key_presses[pygame.K_LEFT]

        time_delta = clock.get_time() / 1000.0

        # mouvement Raquette1
        raquette1.move(w, s, a, d, time_delta)
        raquette1.check_rebond_vertical(hauteur)
        raquette1.check_rebond_gauche(largeur)

        # mouvement Raquette2
        raquette2.move(up, down, left, right, time_delta)
        raquette2.check_rebond_vertical(hauteur)
        raquette2.check_rebond_droit(largeur)

        puck.move(time_delta)

        # point pour le joueur 2 si il y a but a gauche
        if inside_goal(0):
            score2 += 1
            reset_game(vitesse, 1)

        # point pour le joueur 1 si il y a but a droite
        if inside_goal(1):
            score1 += 1
            reset_game(vitesse, 2)

        # limite du palet
        puck.check_limite(largeur, hauteur)

        if puck.collision_raquette(raquette1):
            raquetteHit = 0

        if puck.collision_raquette(raquette2):
            raquetteHit = 0

        # mise a jour des points du round
        if score1 == const.SCORE_LIMITE:
            point = score1 - score2
            player_1_point += point
            if not rounds_p1 + 1 == const.ROUND_LIMITE:
                notify_round_change(player_1_name, player_1_point, point)
                update_save_joueur(player_1_point, player_1_name, player_1_taille, player_1_vitesse, player_1_mass, 180)
            round_no += 1
            rounds_p1 += 1
            score1, score2 = 0, 0
            resetround(1)

        if score2 == const.SCORE_LIMITE:
            point = score2 - score1
            player_2_point += point
            if not rounds_p2 + 1 == const.ROUND_LIMITE:
                notify_round_change(player_2_name, player_2_point, point)
                update_save_joueur(player_2_point, player_2_name, player_2_taille, player_2_vitesse, player_2_mass, 180)
            round_no += 1
            rounds_p2 += 1
            score1, score2 = 0, 0
            resetround(2)

        # rendu couleur de fond de jeu
        render_field(couleur_fond)

        # affichage score
        score(score1, score2, player_1_name, player_2_name)

        # affichage round et ecran de fin
        if rounds_p1 == const.ROUND_LIMITE:
            if end(fin_jeu(ecran, clock, couleur_fond, player_1_name), vitesse):
                return
        elif rounds_p2 == const.ROUND_LIMITE:
            if end(fin_jeu(ecran, clock, couleur_fond, player_2_name), vitesse):
                return
        else:
            rounds(rounds_p1, rounds_p2, round_no)

        # draw raquette et palet
        raquette1.draw(ecran, player1_color)
        raquette2.draw(ecran, player2_color)
        puck.draw(ecran)

        # refresh ecran.
        pygame.display.flip()
        clock.tick(const.FPS)


if __name__ == "__main__":
    init()
    while True:
        gameChoice, player1_color, player2_color, player_1_name, player_2_name = air_hockey_start(
            ecran, clock, largeur, hauteur)
        couleur_fond = theme_ecran(ecran, clock, largeur, hauteur)
        init()
        if gameChoice == 1:
            show_classement(ecran, largeur, clock)
        elif gameChoice == 2:
            player_1_taille = import_save_joueur(player_1_name)[1]
            player_2_taille = import_save_joueur(player_2_name)[1]
            player_1_vitesse = import_save_joueur(player_1_name)[2]
            player_2_vitesse = import_save_joueur(player_2_name)[2]
            player_1_mass = import_save_joueur(player_1_name)[3]
            player_2_mass = import_save_joueur(player_2_name)[3]
            player_1_cage = import_save_joueur(player_1_name)[4]
            player_2_cage = import_save_joueur(player_2_name)[4]
            player_1_CAGE_Y1 = const.HAUTEUR / 2 - player_1_cage / 2
            player_1_CAGE_Y2 = const.HAUTEUR / 2 + player_1_cage / 2
            player_2_CAGE_Y1 = const.HAUTEUR / 2 - player_2_cage / 2
            player_2_CAGE_Y2 = const.HAUTEUR / 2 + player_2_cage / 2
            # Create game objects.
            raquette1 = Raquette(const.RAQUETTE1X, const.RAQUETTE1Y, player_1_taille, player_1_vitesse, player_1_mass)
            raquette2 = Raquette(const.RAQUETTE2X, const.RAQUETTE2Y, player_2_taille, player_2_vitesse, player_2_mass)
            puck = Puck(largeur / 2, hauteur / 2, 30, 450, 500)
            puck.vitesse = const.FACILE
            game_loop(const.FACILE, player1_color, player2_color, couleur_fond, player_1_name, player_2_name)
        elif gameChoice == 0:
            sys.exit()
