#!/home/cloudera/anaconda3/bin/python3.7

import sys
wordList = dict()
# input venant de STDIN (standard input)
for line in sys.stdin:
	# Suppression d'espaces vides à la  fin de chaque ligne
	line = line.strip()
	# découpage en mots, on découpe avec le symbole ";", car le input est un fichier csv
	words = line.split(';')

	if words[2].strip()=="Sydney" and words[1].strip()=="O" and words[10].strip()=="0":
		# Pour chaque ligne, afficher certaines des valeurs dont don a besoin 
		#dans le mapper sur la consolde STDIN
		# Dans le cadre de ce travail, on récupère 
		# informations sur l'année et le nombre de passagers uniquement
		#pour les lignes les Vols entrant et sortant= ="O",
		# la ville =="Sydney", 
		#L'information sur l'arrets(transit ou final) =="0" 
		print(words[0].strip()+'|'+words[12].strip())
