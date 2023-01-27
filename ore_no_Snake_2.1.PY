# -*- coding: utf-8 -*-
"""
Programme Snake

"""
from tkinter import * # Importation de la bibliothèque  Tkinter 
from random import randint
from PIL import Image, ImageTk 
from subprocess import Popen
import pygame 


tk = Tk()
im_teteN = Image.open("tête_haut.png") 
teteN = ImageTk.PhotoImage(im_teteN) 

im_teteS = Image.open("tête_bas.png") 
teteS = ImageTk.PhotoImage(im_teteS)
 
im_teteE = Image.open("tête_droite.png") 
teteE = ImageTk.PhotoImage(im_teteE) 

im_teteW = Image.open("tête_gauche.png") 
teteW = ImageTk.PhotoImage(im_teteW)
 
im_noeud1 = Image.open("bonus.png")
noeud1 = ImageTk.PhotoImage(im_noeud1)

pomme = Image.open("bonus2-20230127-114724.piskel") 
pomme = ImageTk.PhotoImage(pomme)

im_fantome = Image.open("fantome.png")
fantome = ImageTk.PhotoImage(im_fantome)

im_fantome2 = Image.open("fantome2.png")
fantome2 = ImageTk.PhotoImage(im_fantome2)

im_fantome3 = Image.open("fantome3.png")
fantome3 = ImageTk.PhotoImage(im_fantome3)

im_fantome4 = Image.open("fantome4.png")
fantome4 = ImageTk.PhotoImage(im_fantome4)

pygame.mixer.init()

def right(event):
    global direction
    direction = 'right'
    
def left(event):
    global direction
    direction = 'left'
    
def down(event):
    global direction
    direction = 'down'
    
def up(event):
    global direction
    direction = 'up'
    
def play():
    pygame.mixer.music.load("pacman_chomp")
        
def play2():
    pygame.mixer.music.load("pacman_death")
    pygame.mixer.music.play(loops=0)
    
def play3():
    pygame.mixer.mixer.load("pacman_eatfruit")
    pygame.mixer.music.play(loops=0)

def computeNextFrame(numFrame,coordonnee, objet):
    global direction
    global game_over
    numFrame = numFrame + 1
   
    can.delete('all')
    
    for n in range (len(coordonnee)-1,0,-1):
        coordonnee[n][0] = coordonnee[n-1][0]
        coordonnee[n][1] = coordonnee[n-1][1]
        
    if direction == 'right':
        coordonnee[0][0] += 20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteE)
        if coordonnee[0][0] > 480:
            coordonnee[0][0] = 0
    if direction == 'left':
        coordonnee[0][0] += -20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteW)
        if coordonnee[0][0] < 0:
            coordonnee[0][0] = 480
    if direction == 'up':
        coordonnee[0][1] += -20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteN)
        if coordonnee[0][1] < 0:
            coordonnee[0][1] = 480
    if direction == 'down':
        coordonnee[0][1] += 20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteS)
        if coordonnee[0][1] > 480:
            coordonnee[0][1] = 0
            
    for n in range (1,len(coordonnee)):
        can.create_image(coordonnee[n][0], coordonnee[n][1], anchor = NW, image = noeud1)
        
    # Dessine les objets
    for p in range(len(objet)):
        can.create_image(objet3[0][0], objet3[0][1], anchor = NW, image = fantome)
        can.create_image(objet[0][0], objet[0][1], anchor = NW, image = pomme)
        can.create_image(objet2[0][0], objet2[0][1], anchor = NW, image = fantome2)
        can.create_image(objet4[0][0], objet4[0][1], anchor = NW, image = fantome3)
        can.create_image(objet5[0][0], objet5[0][1], anchor = NW, image = fantome4)
        
    for p in range(len(objet)):
        if coordonnee[0][0] == objet [0][0] and coordonnee[p][1] == objet [p][1]:
            # Déplacement de la pomme et des fantomes
            objet[0][0] = randint(1,24)* 20
            objet[0][1] = randint(1,24)* 20
            objet2[0][0] = randint(1,24)* 20
            objet2[0][1] = randint(1,24)* 20
            objet3[0][0] = randint(1,24)* 20
            objet3[0][1] = randint(1,24)* 20
            objet4[0][0] = randint(1,24)* 20
            objet4[0][1] = randint(1,24)* 20
            objet5[0][0] = randint(1,24)* 20
            objet5[0][1] = randint(1,24)* 20
            
            # Ajout d'un noeud au serpent (à la même place que le dernier noeud)
            coordonnee.append([-20, -20]) # Caché pour l'instant
        """elif coordonnee[0][0] == objet[0][0] and coordonnee[0][1] == objet[0][1] :
            play3"""
        elif coordonnee[0][0] == objet2[0][0] and coordonnee[0][1] == objet2[0][1] :
            game_over = True
        elif coordonnee[0][0] == objet3[0][0] and coordonnee[0][1] == objet3[0][1] :
            game_over = True
        elif coordonnee[0][0] == objet4[0][0] and coordonnee[0][1] == objet4[0][1] :
            game_over = True
        elif coordonnee[0][0] == objet5[0][0] and coordonnee[0][1] == objet5[0][1] :
            game_over = True
        elif coordonnee[0][0] == objet[0][0] and coordonnee[0][1] == objet[0][1] :
         play3
            
    for n in range(1,len(coordonnee)): # L'indice 0 est exclu, c'est la tête
        if coordonnee[0][0] == coordonnee [n][0] and coordonnee[0][1] == coordonnee [n][1]:
            game_over = True # La partie est finie
            
    if game_over == True :
        #Fin de partie
        """play2"""
        can.create_text(250,250,text = "GAME OVER", fill='red', font=("Arial",35,"bold"))
        can.create_text(250,300,text = "wanna try again? press -Space-", fill='red', font=("Arial",15,"bold"))
        #si le joueur presse espace quand Game_over = True il relance le jeu
        """if :
            game_over == False""" 
    else :
        # Calcule une nouvelle frame toute les 100 ms
        tk.after(100, lambda:computeNextFrame(numFrame,coordonnee, objet))

    

if __name__ == "__main__":
    game_over = False
    can = Canvas(tk, width=500, height=500, bg='black')
    if game_over = True:
        play2
    
   
    can.pack()
    
    direction = 'up' 
    
    coordonnee = [ [200, 200], [200, 220], [200, 240], [220, 240] ]
    objet = []
    objet2 = []
    objet3 = []
    objet4 = []
    objet5 = []
    
    x = randint(1, 24)
    y = randint(1, 24)
    objet.append([x*20, y*20, 0])
    x2 = randint(1, 24)
    y2 = randint(1, 24)
    objet2.append([x2*20, y2*20, 0])
    x3 = randint(1, 24)
    y3 = randint(1, 24)
    objet3.append([x3*20, y3*20, 0])
    x4 = randint(1, 24)
    y4 = randint(1, 24)
    objet4.append([x4*20, y4*20, 0])
    x5 = randint(1, 24)
    y5 = randint(1, 24)
    objet5.append([x5*20, y5*20, 0])
    
    computeNextFrame(0,coordonnee, objet)
    
    tk.bind('<Right>', right) 
    tk.bind('<Left>', left) 
    tk.bind('<Down>', down) 
    tk.bind('<Up>', up)    
    
    tk.bind('<d>', right) 
    tk.bind('<q>', left) 
    tk.bind('<s>', down) 
    tk.bind('<z>', up)


    tk.mainloop() 

