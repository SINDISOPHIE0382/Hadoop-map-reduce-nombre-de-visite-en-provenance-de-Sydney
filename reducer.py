#!/home/cloudera/anaconda3/bin/python3.7

from operator import itemgetter
import sys

PeriodeVols = dict()
# Lecture des données renvoyées par le mapper
for line in sys.stdin:
	# suppresion d'eventuels espaces vides
	line = line.strip()

	# on récupère les input recus de mapper.py
	mois_Annee, Nbre_Passagers = line.split('|')
	
	try:
		Nbre_Passagers = int(Nbre_Passagers)
	except ValueError:
		# test sur le contenu de Nbre_Passagers
		#pour s'assurer que c'est un int, sinon, on l'ignore
		continue

	if mois_Annee in PeriodeVols :
		# Pour chaque valeur mois+annee
		PeriodeVols[mois_Annee]+=Nbre_Passagers  
		#Sommer le nombre de passagers par mois+annee
	else:
		PeriodeVols[mois_Annee]=Nbre_Passagers  
		# première accès à l'occurence de la clé mois+annee,
		# on affecte stocke la la valeur du nombre de passagers
		#dans le dictionnaire

#On affiche le contenu de la liste : la cle "mois+anne"
#et la valeur agrége y relatif: nombre de passagers
for key in PeriodeVols:
	print(key+':'+str(PeriodeVols[key]))



