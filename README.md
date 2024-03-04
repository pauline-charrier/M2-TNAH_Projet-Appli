# Projet de groupe M2 TNAH 2023/2024 : Maisons des Illustres

## 1. Description générale de l’application

Le label "Maison des Illustres" est décerné en France à des maisons, châteaux ou ateliers ayant appartenu à des personnalités éminentes qui ont marqué l'histoire par leurs réalisations dans les domaines de la politique, de la culture, des sciences, ou des arts. Ces lieux doivent alors proposer des visites *a minima* 40 jours dans l'année, mettant en avant leur valeur patrimoniale et l'influence de "l'illustre personne" dans l'Histoire. L’attribution d’un tel label représente une reconnaissance officielle de l’intérêt patrimonial de la Maison. Le label est également un dispositif de valorisation, qui s’accompagne d’avantages divers, en terme de visibilité notamment. De son attribution découle donc des enjeux de représentation et la mise en valeur d'une large diversité de personnes et de lieux avec un intérêt patrimonial. Est-ce vraiment le cas ? 

Le but de cette application est de permettre un suivi de la diversité des lieux labellisés et des personnes qu'elles représentent, ainsi qu'un outil de localisation de ces bâtiments, participant ainsi à leur visibilité.

## 2. Contributeurs

Maddalena ACCARDO

Pauline CHARRIER

Clara GROMETTO

Kutay SEFIL

## 3. Fonctionnalités de l'application

A compléter

## 4. Mode d'emploi de l'application 

Pour une première utilisation sur Ubuntu, veuillez suivre pas à pas les instructions suivantes :

1. Télécharger la base de données disponible dans ce répertoire GitHub. 

2. Cloner le dépôt GitHub de l'application avec la commande suivante : 
```shell
git clone https://github.com/gromettoclara/maisons_illustres.git
```
   
3.  Installer Python :
```shell
sudo apt-get install python3
```

4. Installer Pip :
 ```shell
sudo apt install python3-pip
```

5. Créer un fichier .env dans le dossier "appli" avec les variables ci-dessous :
```Python
DEBUG=True
SQLALCHEMY_DATABASE_URI=
SQLALCHEMY_ECHO=False
WTF_CSRF_ENABLE=True
```

6. Installer le package "virtualenv" avec la commande suivante :
```shell
pip install virtualenv
```

7. Installer un environnement virtuel dans le dossier "appli" :
```shell
virtualenv env -p python3
```

8. Activer l'environnement virtuel avec la commande : 
```shell
source env/bin/activate
```

9. Installer les dépendances requises : 
```shell
pip install -r requirements.txt
```

10. Lancer l'application :
```shell
python run.py
```

Pour une utilisation ultérieure de l'application, il suffit de répéter les étapes 8 et 10 uniquement.



