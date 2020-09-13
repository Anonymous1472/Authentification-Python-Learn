#coding:utf-8

"""
Dans ce mini projet nous apprenons à faire des tests afin de valider ou non une "authentification"
Par exemple je veux bloquer l'accès à mon code en mettant un mot de passe et un identifiant.
Mais nous apprenons également les opérateurs de comparaison.

Operateur de comparaison :

== (égal à)
!= (différent de)
< (plus petit que)
> (plus grand que)
<= (inférieur ou égal à)
>= (supérieur ou égal à)

Conditions Multiple :

and (ET)
or (OU)
in / not in (DANS / PAS DANS)
else (SINON)


Mots clés :

if (si)
elif
else (sinon)

"""

identifiant = "Loïc Maurer" #Variable Identifiant
mot_de_passe = "loic1472" # Variable Mot De Passe

print("Bienvenue sur T-Force One !\n") # Affichage Texte

connexion_user = input("Entre ton identifiant :") #Question posé à utilisateur
connexion_mdp = input("Entre ton mot de passe :")#Question posé à utilisateur

if connexion_user == identifiant and connexion_mdp == mot_de_passe: # Conditions Brut
	print("\n") #Affichage
	print("Tu es connecter", identifiant) #Affichage
else: #Conditions (sinon)
	print("\n") # Affichage
	print("Identifiant ou Mot de Passe incorrect !") # Affichage


input()