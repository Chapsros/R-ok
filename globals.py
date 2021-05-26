import constants as const
import pygame
import os

assets = os.path.join(os.path.dirname(__file__), 'assets')
if os.path.exists(assets):
    if len(os.listdir('assets')) == 0:
        #error("Dossier d'image est vide", "Ou n'a pas le bon nombre d'image")
        quit()
    else:
        img_dir = assets
else:
    #error("Dossier d'image introuvable", "Ou ne porte pas le bon nom 'assets'")
    quit()

smallfont = None
score1, score2 = 0, 0

play_image = pygame.image.load(os.path.join(assets, 'play.png'))
pause_image = pygame.image.load(os.path.join(assets, 'pause.png'))
info_image = pygame.image.load(os.path.join(assets, "info.png"))
shop_image = pygame.image.load(os.path.join(assets, "shop.png"))

clock = None
ecran = None
largeur, hauteur = const.LARGEUR, const.HAUTEUR

# boutton
bouttonRadius = 60
bouttonRadius_shop = 10
Taille_cercle = 80

# couleur globals
# (dimvert, vert) , (dimrouge, rouge) , (dimbleu, bleu ) , (jaune, dimjaune), (orange, dimorange)
colors = [[(46, 120, 50), (66, 152, 60)], [(200, 72, 72), (255, 92, 92)],
          [(0, 158, 239), (100, 189, 219)], [(221, 229, 2), (252, 255, 59)],
          [(232, 114, 46), (244, 133, 51)]]

theme_colors = [[(255, 169, 119), (255, 161, 107)], [(230, 232, 104), (217, 219, 92)],
                [(125, 216, 201), (103, 178, 166)], [(164, 229, 121), (117, 168, 84)]]
