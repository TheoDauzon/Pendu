from tkinter import *
import math
from tkinter.messagebox import showerror
from tkinter import messagebox
from xml.dom import minidom
import tkinter
from tkinter import scrolledtext
import random
from timeit import default_timer

global zoneSaisie
global j
global img
global score


def pageDegestion():
    global listeMotImpo
    #appel fonction
    def toutesFonctions():
        btnAjouterImpossible()
        btnSupprimer()
        btnEnregistrer()
        ecritureImpo()
        Menu()
        facile()
        moyen()
        difficile()

        impossible()

    #GESTION MOT
    #Mots facile
    def facile():
        doc = minidom.parse("fichierFacile.xml")
        mots = doc.getElementsByTagName("mot")
        #Variable cache des mots
        global motFacile
        global listeMotFac
        listeMotFac=[]
        #titre
        titreMotFacile = Label(gestion,text="Liste de Mots Facile", font=("Carlito", 15),bg="lightblue", fg="green")
        titreMotFacile.place(x=120,y=120)
        #tableau
        motFacile = Listbox(gestion, width = 20, height = 20, font=("Carlito", 10))
        motFacile.place(x=150,y=170)
        for mot in mots:
            liste=(mot.getElementsByTagName("text")[0])
            listeMotFac.append(liste.firstChild.data)
        for i in range (0,len(listeMotFac)):
            motFacile.insert(i+1,listeMotFac[i])
    #Mots moyen
    def moyen():
        doc = minidom.parse("fichierMoyen.xml")
        mots = doc.getElementsByTagName("mot")
        #Variable cache des mots
        global motMoyen
        global listeMotMoy
        listeMotMoy=[]
        #titre
        titreMotMoyen = Label(gestion,text="Liste de Mots Moyen", font=("Carlito", 15),bg="lightblue", fg="darkorange")
        titreMotMoyen.place(x=415,y=120)
        #tableau
        motMoyen = Listbox(gestion, width = 20, height = 20, font=("Carlito", 10))
        motMoyen.place(x=450,y=170)
        for mot in mots:
            liste=(mot.getElementsByTagName("text")[0])
            listeMotMoy.append(liste.firstChild.data)
        for i in range (0,len(listeMotMoy)):
            motMoyen.insert(i+1,listeMotMoy[i])
    #Mots difficile
    def difficile():
        doc = minidom.parse("fichierDifficile.xml")
        mots = doc.getElementsByTagName("mot")
        #Variable cache des mots
        global motDifficile
        global listeMotDiff
        listeMotDiff=[]
        #titre
        titreMotDifficile = Label(gestion,text="Liste de Mots Difficile", font=("Carlito", 15),bg="lightblue", fg="crimson")
        titreMotDifficile.place(x=765,y=120)
        #tableau
        motDifficile = Listbox(gestion, width = 20, height = 20, font=("Carlito", 10))
        motDifficile.place(x=800,y=170)
        for mot in mots:
            liste=(mot.getElementsByTagName("text")[0])
            listeMotDiff.append(liste.firstChild.data)
        for i in range (0,len(listeMotDiff)):
            motDifficile.insert(i+1,listeMotDiff[i])
    #Mots impossible
    def impossible():
        doc = minidom.parse("fichierImpossible.xml")
        mots = doc.getElementsByTagName("mot")
        #Variable cache des mots
        global motImpossible
        global listeMotImpo
        listeMotImpo=[]
        #titre
        titreMotImpossible = Label(gestion,text="Liste de Mots Impossible", font=("Carlito", 15),bg="lightblue", fg="darkmagenta")
        titreMotImpossible.place(x=1100,y=120)
        #tableau
        motImpossible = Listbox(gestion, width = 20, height = 20, font=("Carlito", 10))
        motImpossible.place(x=1150,y=170)
        for mot in mots:
            liste=(mot.getElementsByTagName("text")[0])
            listeMotImpo.append(liste.firstChild.data)
        for i in range (0,len(listeMotImpo)):
            motImpossible.insert(i+1,listeMotImpo[i])
    #Bouton Enregistrer
    def btnEnregistrer():
        boutonEnreg=Button(gestion, text="ENREGISTRER", bg="gold", font = ("Carlito", 15),fg="black", width=15, height=1, command=lambda:btnEnre())
        boutonEnreg.place(x=550,y=800)
    #Bouton Ajouter
    def btnAjouterImpossible():
        boutonAjout=Button(gestion, text="AJOUTER", bg="springgreen", font = ("Carlito", 15),fg="black", width=15, height=1, command=lambda:btnAjoutImpo())
        boutonAjout.place(x=450,y=650)
    #Bouton Supprimer
    def btnSupprimer():
        global btnSupp
        btnSupp=Button(gestion, text="SUPPRIMER", bg="salmon", font = ("Carlito", 15),fg="black", width=16, height=1, command=lambda:btnSuppImpo())
        btnSupp.place(x=650,y=650)
    #Commande Enregistrer
    def btnEnre():
        messagebox.showinfo("MERCI QUAND MEME","Suite à des bugs, l'enregistrement n'est pas disponible")
    #Commande Ajouter
    def btnAjoutImpo():
        mot=eImpo.get()
        if len(mot)<3:
            messagebox.showerror("ERREUR","Veuillez entrer un mot d'au moins 3 lettres")
        elif len(mot)<=5:
            motFacile.insert(END,mot)
        elif len(mot)<=8:
            motMoyen.insert(END,mot)
        elif len(mot)<=11:
            motDifficile.insert(END,mot)
        elif len(mot)<=14:
            motDifficile.insert(END,mot)
        else:
            messagebox.showerror("ERREUR","L'équipe de développeur a fait le choix de ne pas intégrer des mots de plus de 14 lettres")
    #Commande Supprimer
    def btnSuppImpo():
        messagebox.showinfo("DOMMAGE","C'est pas gentil de vouloir enlever des mots")
    #Zone écriture
    def ecritureImpo():
        global eImpo
        eImpo = Entry(gestion, font = ("Carlito", 13),fg="black", width=20)
        eImpo.place(x=500,y=550)
    #FIN

    #Retourne a l'accueil
    def retourAccueil():
        gestion.destroy()
        pageDAcceuil()
    #Menu
    def Menu():
        btnAcc=Button(gestion, text ="ACCUEIL", bg="lightgrey", font = ("Carlito", 12),fg="black", width=8, height=2, command=lambda:retourAccueil())
        btnAcc.place(x=50,y=30)
        titreGestion=Label(gestion, text="Gestion des mots", font = ("Carlito", 20),bg="lightblue", fg="black", relief="solid")
        titreGestion.place(x=450,y=30)


    #Affichage fenêtre
    gestion = Tk ()
    #caractristique fenêtre
    gestion.title("Pendu Game")
    gestion.geometry("1080x720")
    gestion.minsize(1440, 980)
    gestion.maxsize(1440,98)
    gestion.config(background="lightblue")

    toutesFonctions()

    gestion.mainloop()

def pageDAide():
    #création d'une fenêtre
    aide=Tk()

    #paramètres de la fenêtre : titre, taile, taille minimal, taille maximal et la couleur de fond
    aide.title("AIDE")
    aide.geometry("1720x840")
    aide.minsize(1720, 840)
    aide.maxsize(1720, 840)
    aide.config(background = "lightblue")

    #affichage du titre de la page
    titre = Label(aide, text = "Aide", font = ("Carlito", 30), bg = "lightblue", fg = "Black")
    titre.place(x=250, y= 10)

    #création de label pour écrire des textes
    texte = Label(aide, text = "Règles du jeu :", font = ("Carlito", 15), bg = "lightblue", fg = "Black")
    texte.place(x=50, y=70)

    texte1 = Label(aide, text = "Vous avez 8 essais pour trouver un mot qui à une taille qui peut aller ", font = ("Carlito", 15), bg = "lightblue", fg = "Black")
    texte1.place(x=50, y=120)

    texte2 = Label(aide, text = "de 3 à 14 lettres. Un mot composé de 3 à 5 lettres est considéré", font = ("Carlito", 15), bg = "lightblue", fg = "Black")
    texte2.place(x=50, y=150)

    texte3 = Label(aide, text = "comme facile, 6 à 8 lettres comme moyen, 9 à 11 lettres comme", font = ("Carlito", 15), bg = "lightblue", fg = "Black")
    texte3.place(x=50, y=180)

    texte4 = Label(aide, text = "difficile et 11 à 14 lettres comme impossible.", font = ("Carlito", 15), bg = "lightblue", fg = "Black")
    texte4.place(x=50, y=210)

    texte5 = Label(aide, text = "Si au bout des 8 essais, vous n'avez pas réussis à trouver le mot,", font = ("Carlito", 15), bg = "lightblue", fg = "Black")
    texte5.place(x=50, y=240)

    texte6 = Label(aide, text = "vous avez donc perdu !", font = ("Carlito", 15), bg = "lightblue", fg = "Black")
    texte6.place(x=50, y=270)

    texte7 = Label(aide, text = "Bonus :", font = ("Carlito", 15), bg = "lightblue", fg = "Black")
    texte7.place(x=50, y=330)

    texte8 = Label(aide, text = "Vous pouvez déploquer un bonus un bonus de point si vous", font = ("Carlito", 15), bg = "lightblue", fg = "Black")
    texte8.place(x=50, y=390)

    texte9 = Label(aide, text = "parvennez à trouver plusieurs lettres à la suite.", font = ("Carlito", 15), bg = "lightblue", fg = "Black")
    texte9.place(x=50, y=420)

    texte10 = Label(aide, text = "Pour les niveaux facile, moyen et difficile, toute erreur n'entraîne", font = ("Carlito", 15), bg = "lightblue", fg = "Black")
    texte10.place(x=50, y=450)

    texte11 = Label(aide, text = "pas une perte de points, juste une remise à zéro du bonus.", font = ("Carlito", 15), bg = "lightblue", fg = "Black")
    texte11.place(x=50, y=480)

    texte12 = Label(aide, text = "Toutefois, si vous choisissez le niveau impossible et que vous", font = ("Carlito", 15), bg = "lightblue", fg = "Black")
    texte12.place(x=50, y=510)

    texte13 = Label(aide, text = "commettez malencontreusement une erreur, vous perdrez la moité", font = ("Carlito", 15), bg = "lightblue", fg = "Black")
    texte13.place(x=50, y=540)

    texte14 = Label(aide, text = "de vos points ! A vos risques et périls !", font = ("Carlito", 15), bg = "lightblue", fg = "Black")
    texte14.place(x=50, y=570)

    texte15 = Label(aide, text = "Voici le calcul du bonus par niveau de difficulté (facile, moyen, difficile, impossible) :", font = ("Carlito", 15), bg = "lightblue", fg = "Black")
    texte15.place(x=830, y=25)

    texte16 = Label(aide, text = "BON JEU !", font = ("Carlito", 35), bg = "lightblue", fg = "Black")
    texte16.place(x=225, y=680)

    #affichage de l'image explicative du fonctionnement du bonus
    text17 = Label(aide, text="imageDiff = PhotoImage(file=\"IMG\pend0.PNG\")\nlabelBonusParDifficulte=Label(aide, image=imageDiff)\nlabelBonusParDifficulte.place(x=650, y=80)\nimage \"pyimage1\" doesn't exist\nVu avec M. Bazile", font = ("Carlito", 15), bg = "lightblue", fg = "Black")
    text17.place(x=830,y=150)

    #affichage de la fenêtre "aide"
    aide.mainloop()

def pageTop10():

    def retourAccueil():
        top10.destroy()
        pageDAcceuil()

    #lie le fichier python au fichier xml
    doc = minidom.parse("Top10.xml")

    #création d'une fenêtre "top10"
    top10=Tk()

    #récupére les données qui sont entre les balises qui ont pour nom "Classement"
    classement = doc.getElementsByTagName("Classement")

    #hauteur où va être affichée le premier du classment
    yi=200

    for Classement in classement:
            #récupére le rang du joueur grâce à l'id qui est dans le fichier xml
            Id = Classement.getAttribute("id")
            #récupére le pseudo du joueur grâce aux balises "Pseudo" qui est dans le fichier xml
            Pseudo = Classement.getElementsByTagName("Pseudo")[0]
            #récupére la difficulté choisis par le joueur grâce aux balises "Difficule" qui est dans le fichier xml
            Difficulte = Classement.getElementsByTagName("Difficulte")[0]
            #récupére le score total du joueur grâce aux balises "Score" qui est dans le fichier xml
            Score = Classement.getElementsByTagName("Score")[0]
            #affichage du classement avec les caractéristiques listées au-dessus
            affichageClassement=("Rang : %s,  Pseudo : %s,  Difficulte : %s,  Score : %s" %(Id, Pseudo.firstChild.data, Difficulte.firstChild.data, Score.firstChild.data))
            classement = Label(top10, text =affichageClassement , font = ("Carlito", 17), bg = "lightblue", fg = "gray25")
            classement.place(x=50, y=yi)
            #l'espace d'affichage entre chaque joueur dans le classement sera tout les 50
            yi+=50


    #paramètres de la fenêtre : titre, taile, taille minimal, taille maximal et la couleur de fond
    top10.title("TOP 10")
    top10.geometry("1080x720")
    top10.minsize(1080, 720)
    top10.maxsize(1920, 1040)
    top10.config(background = "lightblue")

    #affichage du titre de la page
    titreTop10 = Label(top10, text = "Top 10", font = ("Carlito", 70), bg = "lightblue", fg = "Black")
    titreTop10.place(x=50, y= 50)

    #affichage d'un bouton qui permet de revenir à l'accueil
    accueilBTN = Button(top10, text ="Accueil", bg="darkturquoise", font = ("Carlito", 20),fg="black", width=15, height=3, command=lambda:retourAccueil())
    accueilBTN.place(x=800, y=225)

    #affichage de la fenêtre "top10"
    top10.mainloop()

def pageTop10Jeu():

    def retourAccueil():
        top10jeu.destroy()
        pageDAcceuil()

    #lie le fichier python au fichier xml
    doc = minidom.parse("Top10.xml")

    #création d'une fenêtre "top10"
    top10=Tk()

    #récupére les données qui sont entre les balises qui ont pour nom "Classement"
    classement = doc.getElementsByTagName("Classement")

    #hauteur où va être affichée le premier du classment
    yi=200

    for Classement in classement:
            #récupére le rang du joueur grâce à l'id qui est dans le fichier xml
            Id = Classement.getAttribute("id")
            #récupére le pseudo du joueur grâce aux balises "Pseudo" qui est dans le fichier xml
            Pseudo = Classement.getElementsByTagName("Pseudo")[0]
            #récupére la difficulté choisis par le joueur grâce aux balises "Difficule" qui est dans le fichier xml
            Difficulte = Classement.getElementsByTagName("Difficulte")[0]
            #récupére le score total du joueur grâce aux balises "Score" qui est dans le fichier xml
            Score = Classement.getElementsByTagName("Score")[0]
            #affichage du classement avec les caractéristiques listées au-dessus
            affichageClassement=("Rang : %s,  Pseudo : %s,  Difficulte : %s,  Score : %s" %(Id, Pseudo.firstChild.data, Difficulte.firstChild.data, Score.firstChild.data))
            classement = Label(top10, text =affichageClassement , font = ("Carlito", 17), bg = "lightblue", fg = "White")
            classement.place(x=50, y=yi)
            #l'espace d'affichage entre chaque joueur dans le classement sera tout les 50
            yi+=50


    #paramètres de la fenêtre : titre, taile, taille minimal, taille maximal et la couleur de fond
    top10.title("TOP 10")
    top10.geometry("1080x720")
    top10.minsize(1080, 720)
    top10.maxsize(1920, 1040)
    top10.config(background = "lightblue")

    #affichage du titre de la page
    titreTop10 = Label(top10, text = "Top 10", font = ("Carlito", 70), bg = "lightblue", fg = "Black")
    titreTop10.place(x=50, y= 50)

    #affichage de la fenêtre "top10"
    top10.mainloop()

def pageDeJeu():
    global score
    score=1
    global img
    global nbError
    nbError=0
    global jeu
    global j
    global multiplicateur
    multiplicateur=1

    def scoreJoueur(value):
        global j
        global multiplicateur
        global score
        if value == True:
            if j==1:
                score=score+multiplicateur
            elif j==2:
                score=score+multiplicateur
            elif j==3:
                score=score+multiplicateur
            elif j==4:
                score=score+multiplicateur
        else:
            multiplicateur=1
            if j==4:
                score=int(score*0.5)
                if score<1:
                    score=1

    def updateTime():
        now = default_timer() - start
        minutes, seconds = divmod(now, 60)
        hours, minutes = divmod(minutes, 60)
        str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
        chrono.itemconfigure(text_clock, text=str_time)
        jeu.after(1000, updateTime)

    def victory():
        accueilWin=Button(jeu, text="Retourner à l'accueil", state= NORMAL, bg="darkturquoise", command = lambda:retourAccueil(), font=("Carlito", 15), fg="black", width=20, height=1)
        accueilWin.place(x=430,y=600)

    def verifInMot(lettre,listeMotCache,listeMotDecouvert):
        global nbError
        global j
        global multiplicateur
        if lettre in listeMotDecouvert:
            for i in range(len(motDecouvert)):
                if lettre==motDecouvert[i]:
                    motDecouvrir[i]=lettre
                    motAffiche.config(text=motDecouvrir)
                    if motDecouvert==motDecouvrir:
                        pseudoA = Label(jeu, text=" Bravo vous avez trouvé \n le mot caché ", font=("Carlito", 15), bg="lightgrey", fg="black", relief="sunken")
                        pseudoA.place(x=300, y=500)
                        lettreDesac()
                        victory()
                    multiplicateur=multiplicateur*(j+1)
                    scoreJoueur(True)
                scoreA.configure(text=score)
        else:
            print("lettre non présente")
            nbError=nbError+1
            if(nbError==1):
                #afficher image 1 du pendu
                img = PhotoImage(file="IMG\pend1.png")
                l.configure(image=img)
                l.image=img
                multiplicateur=1
                scoreJoueur(False)
                scoreA.configure(text=score)
            elif nbError==2:
                #afficher image 2 du pendu
                img = PhotoImage(file="IMG\pend2.png")
                l.configure(image=img)
                l.image=img
                multiplicateur=1
                scoreJoueur(False)
                scoreA.configure(text=score)
            elif nbError==3:
                #afficher image 2 du pendu
                img = PhotoImage(file="IMG\pend3.png")
                l.configure(image=img)
                l.image=img
                scoreJoueur(False)
                scoreA.configure(text=score)
            elif nbError==4:
                #afficher image 2 du pendu
                img = PhotoImage(file="IMG\pend4.png")
                l.configure(image=img)
                l.image=img
                multiplicateur=1
                scoreJoueur(False)
                scoreA.configure(text=score)
            elif nbError==5:
                #afficher image 2 du pendu
                img = PhotoImage(file="IMG\pend5.png")
                l.configure(image=img)
                l.image=img
                multiplicateur=1
                scoreJoueur(False)
                scoreA.configure(text=score)
            elif nbError==6:
                #afficher image 2 du pendu
                img = PhotoImage(file="IMG\pend6.png")
                l.configure(image=img)
                l.image=img
                multiplicateur=1
                scoreJoueur(False)
                scoreA.configure(text=score)
            elif nbError==7:
                #afficher image 2 du pendu
                img = PhotoImage(file="IMG\pend7.png")
                l.configure(image=img)
                l.image=img
                multiplicateur=1
                scoreJoueur(False)
                scoreA.configure(text=score)
            elif nbError==8:
                #afficher image 2 du pendu
                img = PhotoImage(file="IMG\pend8.png")
                l.configure(image=img)
                l.image=img
                multiplicateur=1
                scoreJoueur(False)
                scoreA.configure(text=score)
                textPerdu="Vous avez été pendu !!\nLe mot était "+listeMotDecouvert
                lbl_perdu=Label(jeu, text=textPerdu, font=("Carlito", 22), bg="lightblue", fg="black", relief="solid")
                lbl_perdu.place(x=150, y=570)
                btn_perdu=Button(jeu, text ="Retour à l'accueil", bg="lightgrey", font = ("Carlito", 20),fg="black", width=15, height=1,command=lambda:retourAccueil())
                btn_perdu.place(x=550, y=580)

    def lettreDesac():
        A['state'] = DISABLED
        B['state'] = DISABLED
        C['state'] = DISABLED
        D['state'] = DISABLED
        E['state'] = DISABLED
        F['state'] = DISABLED
        G['state'] = DISABLED
        H['state'] = DISABLED
        I['state'] = DISABLED
        J['state'] = DISABLED
        K['state'] = DISABLED
        L['state'] = DISABLED
        M['state'] = DISABLED
        N['state'] = DISABLED
        O['state'] = DISABLED
        P['state'] = DISABLED
        Q['state'] = DISABLED
        R['state'] = DISABLED
        S['state'] = DISABLED
        T['state'] = DISABLED
        U['state'] = DISABLED
        V['state'] = DISABLED
        W['state'] = DISABLED
        X['state'] = DISABLED
        Y['state'] = DISABLED
        Z['state'] = DISABLED

    def onClick(lettreClick):
        if lettreClick=="A":
            A['state'] = DISABLED
            A['bg'] = "lightgreen"
            verifInMot("A",motDecouvrir,motATrouve)
        elif lettreClick=="B":
            B['state'] = DISABLED
            B['bg'] = "lightgreen"
            verifInMot("B",motDecouvrir,motATrouve)
        elif lettreClick=="C":
            C['state'] = DISABLED
            C['bg'] = "lightgreen"
            verifInMot("C",motDecouvrir,motATrouve)
        elif lettreClick=="D":
            D['state'] = DISABLED
            D['bg'] = "lightgreen"
            verifInMot("D",motDecouvrir,motATrouve)
        elif lettreClick=="E":
            E['state'] = DISABLED
            E['bg'] = "lightgreen"
            verifInMot("E",motDecouvrir,motATrouve)
        elif lettreClick=="F":
            F['state'] = DISABLED
            F['bg'] = "lightgreen"
            verifInMot("F",motDecouvrir,motATrouve)
        elif lettreClick=="G":
            G['state'] = DISABLED
            G['bg'] = "lightgreen"
            verifInMot("G",motDecouvrir,motATrouve)
        elif lettreClick=="H":
            H['state'] = DISABLED
            H['bg'] = "lightgreen"
            verifInMot("H",motDecouvrir,motATrouve)
        elif lettreClick=="I":
            I['state'] = DISABLED
            I['bg'] = "lightgreen"
            verifInMot("I",motDecouvrir,motATrouve)
        elif lettreClick=="J":
            J['state'] = DISABLED
            J['bg'] = "lightgreen"
            verifInMot("J",motDecouvrir,motATrouve)
        elif lettreClick=="K":
            K['state'] = DISABLED
            K['bg'] = "lightgreen"
            verifInMot("K",motDecouvrir,motATrouve)
        elif lettreClick=="L":
            L['state'] = DISABLED
            L['bg'] = "lightgreen"
            verifInMot("L",motDecouvrir,motATrouve)
        elif lettreClick=="M":
            M['state'] = DISABLED
            M['bg'] = "lightgreen"
            verifInMot("M",motDecouvrir,motATrouve)
        elif lettreClick=="N":
            N['state'] = DISABLED
            N['bg'] = "lightgreen"
            verifInMot("N",motDecouvrir,motATrouve)
        elif lettreClick=="O":
            O['state'] = DISABLED
            O['bg'] = "lightgreen"
            verifInMot("O",motDecouvrir,motATrouve)
        elif lettreClick=="P":
            P['state'] = DISABLED
            P['bg'] = "lightgreen"
            verifInMot("P",motDecouvrir,motATrouve)
        elif lettreClick=="Q":
            Q['state'] = DISABLED
            Q['bg'] = "lightgreen"
            verifInMot("Q",motDecouvrir,motATrouve)
        elif lettreClick=="R":
            R['state'] = DISABLED
            R['bg'] = "lightgreen"
            verifInMot("R",motDecouvrir,motATrouve)
        elif lettreClick=="S":
            S['state'] = DISABLED
            S['bg'] = "lightgreen"
            verifInMot("S",motDecouvrir,motATrouve)
        elif lettreClick=="T":
            T['state'] = DISABLED
            T['bg'] = "lightgreen"
            verifInMot("T",motDecouvrir,motATrouve)
        elif lettreClick=="U":
            U['state'] = DISABLED
            U['bg'] = "lightgreen"
            verifInMot("U",motDecouvrir,motATrouve)
        elif lettreClick=="V":
            V['state'] = DISABLED
            V['bg'] = "lightgreen"
            verifInMot("V",motDecouvrir,motATrouve)
        elif lettreClick=="W":
            W['state'] = DISABLED
            W['bg'] = "lightgreen"
            verifInMot("W",motDecouvrir,motATrouve)
        elif lettreClick=="X":
            X['state'] = DISABLED
            X['bg'] = "lightgreen"
            verifInMot("X",motDecouvrir,motATrouve)
        elif lettreClick=="Y":
            Y['state'] = DISABLED
            Y['bg'] = "lightgreen"
            verifInMot("Y",motDecouvrir,motATrouve)
        elif lettreClick=="Z":
            Z['state'] = DISABLED
            Z['bg'] = "lightgreen"
            verifInMot("Z",motDecouvrir,motATrouve)

    def recupNiv(value):
        if value==1:
            return "fichierFacile.xml"
        elif value==2:
            return "fichierMoyen.xml"
        elif value==3:
            return "fichierDifficile.xml"
        elif value==4:
            return "fichierImpossible.xml"

    def retouALAccueilBtn():
        reponse=tkinter.messagebox.askyesno(title="Fermeture", message="Voulez-vous fermez la page de jeu ? \nRien ne sera sauvegardé", icon="warning")
        if (reponse == True):
            jeu.destroy()
            pageDAcceuil()

    def retourAccueil():
        jeu.destroy()
        pageDAcceuil()

    def enregistrerRacceuil():
        #command d'enregistrement du score
        jeu.destroy()
        pageDAcceuil()

    def abandonnerBtn():
        abandon = tkinter.messagebox.askyesno(title="Abandonner", message="Voulez-vous vraimennt abandonner ?\nRien ne sera sauvegardé", icon="warning")
        if (abandon == True):
            jeu.destroy()
            pageDAcceuil()

    def niveau(val):
        if val==1:
            return "Facile"
        elif val==2:
            return "Moyen"
        elif val==3:
            return "Difficile"
        elif val==4:
            return "Impossible"

    jeu = Tk()

    # Configuration de la fenetre
    jeu.title("Pendu Game")
    jeu.geometry("1080x720")
    jeu.minsize(1080, 720)
    jeu.maxsize(1080,720)
    jeu.config(background="lightblue")

    # variable
    cptErreur = 0
    clavierNumérique = 0

    #chronnomètre
    chrono = Canvas(jeu, width=80, height=38, bg="white" , borderwidth=2, relief="groove" )
    chrono.place(x=15, y=15)
    start = default_timer()
    text_clock = chrono.create_text(40, 20)
    updateTime()

    # Titre
    titre = Label(jeu, text=" Pendu ", font=("Carlito", 40), bg="lightblue", fg="black", relief="solid")
    titre.pack(pady=50, padx=30)

    #Menu liste bouttons
    accueil = Button(jeu, text ="Accueil", bg="lightgrey", font = ("Carlito", 20),fg="black", width=6, height=1, command=lambda:retouALAccueilBtn())
    accueil.place(x=10, y=75)

    top10 = Button(jeu, text ="TOP 10", bg="lightgrey", font = ("Carlito", 20),fg="black", width=6, height=1, command=lambda:pageTop10Jeu())
    top10.place(x=10, y=150)

    aide = Button(jeu, text ="Aide", bg="lightgrey", font = ("Carlito", 20),fg="black", width=6, height=1, command=lambda:pageDAide())
    aide.place(x=10, y=225)

    abandonner = Button(jeu, text ="Abandonner", bg="red", font = ("Carlito", 20),fg="White", width=10, height=1, command=lambda:abandonnerBtn())
    abandonner.place(x=900, y=30)

    #pseudo
    pseudo = Label(jeu, text=" Pseudo : ", font=("Carlito", 15), bg="lightgrey", fg="black", relief="sunken")
    pseudo.place(x=150, y=10)
    global zoneSaisie
    pseudoA = Label(jeu, text=zoneSaisie, font=("Carlito", 15), bg="lightgrey", fg="black", relief="solid")
    pseudoA.place(x=250,y=10)

    #niveau
    nivau = Label(jeu, text=" Niveau : ", font=("Carlito", 15), bg="lightgrey", fg="black", relief="sunken")
    nivau.place(x=150, y=50)
    global j
    niveauA = Label(jeu, text=niveau(j), font=("Carlito", 15), bg="lightgrey", fg="black", relief="solid")
    niveauA.place(x=250,y=50)

    #score
    scoreB = Label(jeu,text=" Score : ", font=("Carlito", 15), bg="lightgrey", fg="black", relief="sunken")
    scoreB.place(x=150,y=90)
    scoreA = Label(jeu,text=score, font=("Carlito", 15), bg="lightgrey", fg="black", relief="solid")
    scoreA.place(x=250,y=90)

    monCanvas = Canvas(jeu, width=570, height=88, bg='lightgrey', bd=50, highlightthickness=10, highlightbackground="cyan")
    monCanvas.place(x=70,y=310)

    #image déclarée base
    global img
    img = PhotoImage(file="IMG\pend0.png")
    l=Label(jeu, image=img)
    l.place(x=760,y=250)



    #Clavier numérique
    if clavierNumérique == 0:

        A = Button(jeu, text="A", state= NORMAL, bg="darkturquoise", command = lambda:onClick("A"), font=("carlito", 20), fg="black", width=2, height=1)
        A.place(x=100, y=350)

        B = Button(jeu, text="B", state= NORMAL, bg="darkturquoise", command = lambda:onClick("B"),font=("carlito", 20), fg="black", width=2, height=1)
        B.place(x=150, y=350)

        C = Button(jeu, text="C", state= NORMAL, bg="darkturquoise", command = lambda:onClick("C"),font=("carlito", 20), fg="black", width=2, height=1)
        C.place(x=200, y=350)

        D = Button(jeu, text="D", state= NORMAL, bg="darkturquoise", command = lambda:onClick("D"),font=("carlito", 20), fg="black", width=2, height=1)
        D.place(x=250, y=350)

        E = Button(jeu, text="E", state= NORMAL, bg="darkturquoise", command = lambda:onClick("E"),font=("carlito", 20), fg="black", width=2, height=1)
        E.place(x=300, y=350)

        F = Button(jeu, text="F", state= NORMAL, bg="darkturquoise", command = lambda:onClick("F"),font=("carlito", 20), fg="black", width=2, height=1)
        F.place(x=350, y=350)

        G = Button(jeu, text="G", state= NORMAL, bg="darkturquoise", command = lambda:onClick("G"),font=("carlito", 20), fg="black", width=2, height=1)
        G.place(x=400, y=350)

        H = Button(jeu, text="H", state= NORMAL, bg="darkturquoise", command = lambda:onClick("H"),font=("carlito", 20), fg="black", width=2, height=1)
        H.place(x=450, y=350)

        I = Button(jeu, text="I", state= NORMAL, bg="darkturquoise", command = lambda:onClick("I"),font=("carlito", 20), fg="black", width=2, height=1)
        I.place(x=500, y=350)

        J = Button(jeu, text="J", state= NORMAL, bg="darkturquoise", command = lambda:onClick("J"),font=("carlito", 20), fg="black", width=2, height=1)
        J.place(x=550, y=350)

        K = Button(jeu, text="K", state= NORMAL, bg="darkturquoise", command = lambda:onClick("K"),font=("carlito", 20), fg="black", width=2, height=1)
        K.place(x=600, y=350)

        L = Button(jeu, text="L", state= NORMAL,  bg="darkturquoise", command = lambda:onClick("L"),font=("carlito", 20), fg="black", width=2, height=1)
        L.place(x=650, y=350)

        M = Button(jeu, text="M", state= NORMAL, bg="darkturquoise", command = lambda:onClick("M"),font=("carlito", 20), fg="black", width=2, height=1)
        M.place(x=700, y=350)

        N = Button(jeu, text="N", state= NORMAL, bg="darkturquoise", command = lambda:onClick("N"),font=("carlito", 20), fg="black", width=2, height=1)
        N.place(x=100, y=420)

        O = Button(jeu, text="O", state= NORMAL, bg="darkturquoise", command = lambda:onClick("O"),font=("carlito", 20), fg="black", width=2, height=1)
        O.place(x=150, y=420)

        P = Button(jeu, text="P", state= NORMAL, bg="darkturquoise", command = lambda:onClick("P"),font=("carlito", 20), fg="black", width=2, height=1)
        P.place(x=200, y=420)

        Q = Button(jeu, text="Q", state= NORMAL, bg="darkturquoise", command = lambda:onClick("Q"),font=("carlito", 20), fg="black", width=2, height=1)
        Q.place(x=250, y=420)

        R = Button(jeu, text="R", state= NORMAL, bg="darkturquoise", command = lambda:onClick("R"),font=("carlito", 20), fg="black", width=2, height=1)
        R.place(x=300, y=420)

        S = Button(jeu, text="S", state= NORMAL, bg="darkturquoise", command = lambda:onClick("S"),font=("carlito", 20), fg="black", width=2, height=1)
        S.place(x=350, y=420)

        T = Button(jeu, text="T", state= NORMAL, bg="darkturquoise", command = lambda:onClick("T"),font=("carlito", 20), fg="black", width=2, height=1)
        T.place(x=400, y=420)

        U = Button(jeu, text="U", state= NORMAL, bg="darkturquoise", command = lambda:onClick("U"),font=("carlito", 20), fg="black", width=2, height=1)
        U.place(x=450, y=420)

        V = Button(jeu, text="V", state= NORMAL, bg="darkturquoise", command = lambda:onClick("V"),font=("carlito", 20), fg="black", width=2, height=1)
        V.place(x=500, y=420)

        W = Button(jeu, text="W", state= NORMAL, bg="darkturquoise", command = lambda:onClick("W"),font=("carlito", 20), fg="black", width=2, height=1)
        W.place(x=550, y=420)

        X = Button(jeu, text="X", state= NORMAL, bg="darkturquoise", command = lambda:onClick("X"), font=("carlito", 20), fg="black", width=2, height=1)
        X.place(x=600, y=420)

        Y = Button(jeu, text="Y", state= NORMAL, bg="darkturquoise", command = lambda:onClick("Y"),font=("carlito", 20), fg="black", width=2, height=1)
        Y.place(x=650, y=420)

        Z = Button(jeu, text="Z", state= NORMAL, bg="darkturquoise", command = lambda:onClick("Z"),font=("carlito", 20), fg="black", width=2, height=1)
        Z.place(x=700, y=420)

    #mot
    doc = minidom.parse(recupNiv(j))
    mots = doc.getElementsByTagName("mot")
    nbAlea=str(random.randint(0,12))
    for mot in mots:
        if nbAlea == mot.getAttribute("id"):
            mText = mot.getElementsByTagName("text")[0]
            motATrouve=mText.firstChild.data
            motDecouvert=[]
            motDecouvrir=[]
            for i in range(len(motATrouve)):
                motDecouvrir.append("_")
                motDecouvert.append(motATrouve[i])
            motAffiche = Label(jeu, text=motDecouvrir, font=("Carlito", 40), bg="lightblue", fg="black")
            motAffiche.place(x=400, y=150)
        else:
            nbAlea=str(random.randint(0,12))

    erreur = Label(jeu, text="Suite à des problèmes de développement\n le mot peut ne pas bien s'afficher\nIl faut alors retourner à l'accueil et recommencer", font=("Carlito", 10), bg="lightblue", fg="black")
    erreur.place(x=400,y=0)
    jeu.mainloop()

def pageTransfert():
    def retourTranfert():
        transfert.destroy()
        pageDAcceuil()

    transfert = Tk()

    transfert.title("Pendu Game")
    transfert.geometry("1080x720")
    transfert.minsize(1080, 720)
    transfert.maxsize(1080,720)
    transfert.config(background="lightblue")

    gestionDesMots = Button(transfert, text ="Transfert",fg="black", width=15, height=3, command=retourTranfert())
    gestionDesMots.place(x=800, y=225)

    tranfert.mainloop()

def pageDAcceuil():

    #start the game
    def demarreJeu():
        pageAccueil.destroy()
        pageDeJeu()
    #open gestion de mot
    def demarreGestion():
        pageAccueil.destroy()
        pageDegestion()
    #open top 10
    def demarreTop():
        pageAccueil.destroy()
        pageTop10()
    #refresh page accueil
    def demarreTransfert():
        pageAccueil.destroy()
        pageTransfert()

    #fonction qui vérifie si un pseudo et un niveau de difficulté sont rentrés par le joueur lorsque ce dernier clique sur le bouton "Jouer"
    def afficheZoneSaisie():
        global zoneSaisie
        zoneSaisie = zoneEcriturePseudo.get("1.0",'end-1c')
        if len(zoneSaisie)==0:
            showerror("Erreur", "Veuillez renseigner un pseudo pour pouvoir jouer !")
        elif j==0:
            showerror("Erreur", "Veuillez renseignez un niveau de difficulté pour pouvoir jouer !")
        else:
            demarreJeu()

    #création de la fenêtre "pageAccueil"
    pageAccueil=Tk()

    #décalration et initialisation d'une variable globale "j" qui désigne la dificulté par un chiffre (1 pour facile, 2 pour moyen, 3 pour difficile et 4 pour impossible)
    global j
    j=0

    #paramètres de la fenêtre : titre, taile, taille minimal, taille maximal et la couleur de fond
    pageAccueil.title("Page d'accueil")
    pageAccueil.geometry("1080x720")
    pageAccueil.minsize(1080, 720)
    pageAccueil.maxsize(1080, 720)
    pageAccueil.config(background = "lightblue")

    #affichage du titre de la page
    titreAccueil = Label(pageAccueil, text = " Accueil ", font = ("Carlito", 70), bg = "lightblue", fg = "Black", relief="solid")
    titreAccueil.place(x=150, y= 50)

    #création du label "Pseudonyme"
    pseudo = Label(pageAccueil, text = "Pseudonyme", font = ("Carlito", 38), bg = "lightblue", fg = "Black")
    pseudo.place(x=50, y=250)

    #création de la zone d'écriture du pseudo
    zoneEcriturePseudo = Text(pageAccueil, height=1, width=19, font = ("Carlito", 30))
    zoneEcriturePseudo.place(x=365, y=262)

    #création du texte associé au choix du niveau de difficulté
    niveau = Label(pageAccueil, text = "Niveau de difficulté", font = ("Carlito", 38), bg = "lightblue", fg = "Black")
    niveau.place(x=45, y=450)

    #création des boutons : Jouer, Gestion des mots, Top10, Aide et ANNULER SAISIE
    jouer = Button(pageAccueil, text ="Jouer", bg="darkturquoise", font = ("Carlito", 20),fg="black", width=15, height=3, command=afficheZoneSaisie)
    jouer.place(x=800, y=75)

    gestionDesMots = Button(pageAccueil, text ="Gestion des mots", bg="darkturquoise", font = ("Carlito", 20),fg="black", width=15, height=3, command=lambda:demarreGestion())
    gestionDesMots.place(x=800, y=225)

    top10 = Button(pageAccueil, text ="Top 10", bg="darkturquoise", font = ("Carlito", 20),fg="black", width=15, height=3, command=lambda:demarreTop())
    top10.place(x=800, y=375)

    aide = Button(pageAccueil, text ="Aide", bg="darkturquoise", font = ("Carlito", 20),fg="black", width=15, height=3, command=lambda:pageDAide())
    aide.place(x=800, y=525)

    annuler = Button(pageAccueil, text ="ANNULER SAISIE", bg="darkturquoise", font = ("Carlito", 16),fg="black", width=14, height=1, command=lambda:[pageAccueil.destroy(),pageTransfert()])
    annuler.place(x=400, y=550)

    #création d'une fonction qui va créer des héxagones
    def hexagone(leCanvas, x0, y0, longueur, couleur) :
        x = []

        y = []

        for i in range(6) :

            angle = math.radians(i*360/6)

            x.append(int(x0+longueur*math.cos(angle)))

            y.append(int(y0+longueur*math.sin(angle)))

        leCanvas.create_polygon(x[0],y[0],x[1],y[1],x[2],y[2],x[3],y[3],x[4],y[4],x[5],y[5], fill="white", outline="red")

    #création de l'héxagone qui va désigné la difficulté "facile"
    facile = Canvas(pageAccueil, width=80, height=80, bg="lightblue", borderwidth=0, highlightthickness=0)
    facile.place(x=475,y=432)
    hexagone(facile,50,50,25,"black")

    #création de l'héxagone qui va désigné la difficulté "moyen"
    moyen = Canvas(pageAccueil, width=80, height=80, bg="lightblue", borderwidth=0, highlightthickness=0)
    moyen.place(x=550,y=432)
    hexagone(moyen,50,50,25,"black")

    #création de l'héxagone qui va désigné la difficulté "difficile"
    difficile = Canvas(pageAccueil, width=80, height=80, bg="lightblue", borderwidth=0, highlightthickness=0)
    difficile.place(x=625,y=432)
    hexagone(difficile,50,50,25,"black")

    #création de l'héxagone qui va désigné la difficulté "impossible"
    impossible = Canvas(pageAccueil, width=80, height=80, bg="lightblue", borderwidth=0, highlightthickness=0)
    impossible.place(x=700,y=432)
    hexagone(impossible,50,50,25,"black")

    #fonction qui colorie le premier héxagone en doré, ce qui signifie que la difficulté choisis est "facile" lorque le joueur va cliqué sur le premier héxagone
    def onClick(event):
        global j
        def hexagone(leCanvas, x0, y0, longueur, couleur) :
            x = []

            y = []

            for i in range(6) :

                angle = math.radians(i*360/6)

                x.append(int(x0+longueur*math.cos(angle)))

                y.append(int(y0+longueur*math.sin(angle)))

            leCanvas.create_polygon(x[0],y[0],x[1],y[1],x[2],y[2],x[3],y[3],x[4],y[4],x[5],y[5], fill="gold", outline="red")
        facile = Canvas(pageAccueil, width=80, height=80, bg="lightblue", borderwidth=0, highlightthickness=0)
        facile.place(x=475,y=432)
        hexagone(facile,50,50,25,"black")
        j=1
    #lie la fonction ci-dessus au clic gauche de la souris
    facile.bind('<Button-1>', onClick)

    #fonction qui colorie les 2 premiers héxagones en doré, ce qui signifie que la difficulté choisis est "moyen" lorque le joueur va cliqué sur le deuxième héxagone
    def onClick(event):
        global j
        def hexagone(leCanvas, x0, y0, longueur, couleur) :
            x = []

            y = []

            for i in range(6) :

                angle = math.radians(i*360/6)

                x.append(int(x0+longueur*math.cos(angle)))

                y.append(int(y0+longueur*math.sin(angle)))

            leCanvas.create_polygon(x[0],y[0],x[1],y[1],x[2],y[2],x[3],y[3],x[4],y[4],x[5],y[5], fill="gold", outline="red")
        moyen = Canvas(pageAccueil, width=80, height=80, bg="lightblue", borderwidth=0, highlightthickness=0)
        moyen.place(x=550,y=432)
        hexagone(moyen,50,50,25,"black")
        def hexagone(leCanvas, x0, y0, longueur, couleur) :
            x = []

            y = []

            for i in range(6) :

                angle = math.radians(i*360/6)

                x.append(int(x0+longueur*math.cos(angle)))

                y.append(int(y0+longueur*math.sin(angle)))

            leCanvas.create_polygon(x[0],y[0],x[1],y[1],x[2],y[2],x[3],y[3],x[4],y[4],x[5],y[5], fill="gold", outline="red")
        facile = Canvas(pageAccueil, width=80, height=80, bg="lightblue", borderwidth=0, highlightthickness=0)
        facile.place(x=475,y=432)
        hexagone(facile,50,50,25,"black")
        j=2
    #lie la fonction ci-dessus au clic gauche de la souris
    moyen.bind('<Button-1>', onClick)

    #fonction qui colorie les 3 premiers héxagones en doré, ce qui signifie que la difficulté choisis est "difficile" lorque le joueur va cliqué sur le troisième héxagone
    def onClick(event):
        global j
        def hexagone(leCanvas, x0, y0, longueur, couleur) :
            x = []

            y = []

            for i in range(6) :

                angle = math.radians(i*360/6)

                x.append(int(x0+longueur*math.cos(angle)))

                y.append(int(y0+longueur*math.sin(angle)))

            leCanvas.create_polygon(x[0],y[0],x[1],y[1],x[2],y[2],x[3],y[3],x[4],y[4],x[5],y[5], fill="gold", outline="red")
        moyen = Canvas(pageAccueil, width=80, height=80, bg="lightblue", borderwidth=0, highlightthickness=0)
        moyen.place(x=550,y=432)
        hexagone(moyen,50,50,25,"black")
        def hexagone(leCanvas, x0, y0, longueur, couleur) :
            x = []

            y = []

            for i in range(6) :

                angle = math.radians(i*360/6)

                x.append(int(x0+longueur*math.cos(angle)))

                y.append(int(y0+longueur*math.sin(angle)))

            leCanvas.create_polygon(x[0],y[0],x[1],y[1],x[2],y[2],x[3],y[3],x[4],y[4],x[5],y[5], fill="gold", outline="red")
        facile = Canvas(pageAccueil, width=80, height=80, bg="lightblue", borderwidth=0, highlightthickness=0)
        facile.place(x=475,y=432)
        hexagone(facile,50,50,25,"black")
        def hexagone(leCanvas, x0, y0, longueur, couleur) :
            x = []

            y = []

            for i in range(6) :

                angle = math.radians(i*360/6)

                x.append(int(x0+longueur*math.cos(angle)))

                y.append(int(y0+longueur*math.sin(angle)))

            leCanvas.create_polygon(x[0],y[0],x[1],y[1],x[2],y[2],x[3],y[3],x[4],y[4],x[5],y[5], fill="gold", outline="red")
        difficile = Canvas(pageAccueil, width=80, height=80, bg="lightblue", borderwidth=0, highlightthickness=0)
        difficile.place(x=625,y=432)
        hexagone(difficile,50,50,25,"black")
        j=3
    #lie la fonction ci-dessus au clic gauche de la souris
    difficile.bind('<Button-1>', onClick)

    #fonction qui colorie tous les héxagones en doré, ce qui signifie que la difficulté choisis est "impossible" lorque le joueur va cliqué sur le dernier héxagone
    def onClick(event):
        global j
        def hexagone(leCanvas, x0, y0, longueur, couleur) :
            x = []

            y = []

            for i in range(6) :

                angle = math.radians(i*360/6)

                x.append(int(x0+longueur*math.cos(angle)))

                y.append(int(y0+longueur*math.sin(angle)))

            leCanvas.create_polygon(x[0],y[0],x[1],y[1],x[2],y[2],x[3],y[3],x[4],y[4],x[5],y[5], fill="gold", outline="red")
        moyen = Canvas(pageAccueil, width=80, height=80, bg="lightblue", borderwidth=0, highlightthickness=0)
        moyen.place(x=550,y=432)
        hexagone(moyen,50,50,25,"black")
        def hexagone(leCanvas, x0, y0, longueur, couleur) :
            x = []

            y = []

            for i in range(6) :

                angle = math.radians(i*360/6)

                x.append(int(x0+longueur*math.cos(angle)))

                y.append(int(y0+longueur*math.sin(angle)))

            leCanvas.create_polygon(x[0],y[0],x[1],y[1],x[2],y[2],x[3],y[3],x[4],y[4],x[5],y[5], fill="gold", outline="red")
        facile = Canvas(pageAccueil, width=80, height=80, bg="lightblue", borderwidth=0, highlightthickness=0)
        facile.place(x=475,y=432)
        hexagone(facile,50,50,25,"black")
        def hexagone(leCanvas, x0, y0, longueur, couleur) :
            x = []

            y = []

            for i in range(6) :

                angle = math.radians(i*360/6)

                x.append(int(x0+longueur*math.cos(angle)))

                y.append(int(y0+longueur*math.sin(angle)))

            leCanvas.create_polygon(x[0],y[0],x[1],y[1],x[2],y[2],x[3],y[3],x[4],y[4],x[5],y[5], fill="gold", outline="red")
        difficile = Canvas(pageAccueil, width=80, height=80, bg="lightblue", borderwidth=0, highlightthickness=0)
        difficile.place(x=625,y=432)
        hexagone(difficile,50,50,25,"black")
        def hexagone(leCanvas, x0, y0, longueur, couleur) :
            x = []

            y = []

            for i in range(6) :

                angle = math.radians(i*360/6)

                x.append(int(x0+longueur*math.cos(angle)))

                y.append(int(y0+longueur*math.sin(angle)))

            leCanvas.create_polygon(x[0],y[0],x[1],y[1],x[2],y[2],x[3],y[3],x[4],y[4],x[5],y[5], fill="gold", outline="red")
        impossible = Canvas(pageAccueil, width=80, height=80, bg="lightblue", borderwidth=0, highlightthickness=0)
        impossible.place(x=700,y=432)
        hexagone(impossible,50,50,25,"black")
        j=4
    #lie la fonction ci-dessus au clic gauche de la souris
    impossible.bind('<Button-1>', onClick)

    #affichage de la fenêtre "pageAccueil"
    pageAccueil.mainloop()

pageDAcceuil()
