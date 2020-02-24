# Hadoop-map-reduce-nombre-de-visite-en-provenance-de-SydneyObjectif : calculer le nombre de vols ayant quitté Sydney chaque mois, les données sont disponibles dans un fichier CSV (International_airline_activity_Australia.csv)

Les étapes pour faire ce calcul :
	Création d’un code Map qui permet de faire un filtre sur les vols de la ville de Sydney, le mois, l’information sur les arrêts, le nombre de passager. 
	Création d’un code Reduce qui permet de compter le nombre de vol par mois
	Tester le code en local
	Exécuter le code sur Hadoop
