import re
from flask import flash
from sqlalchemy import func, case

def nettoyage_string_to_int(chaine):
    # Dans le cas où plusieurs informations sont données dans la chaine comme 
    # <strong>Saint Helena: </strong>60 km<br> <strong>Ascension Island: </strong>NA<br> <strong>Tristan da Cunha (island only): </strong>34 km
    # il faut retourner la somme de ces nombres
    res = None

    def clean(ch):
        res = re.sub(r'\(.*\)', '', ch) # pour supprimer les dates entre parenthèses
        res = re.sub(r'[^0-9\.]*', '', res) # pour supprimer tous les carctères sauf les points
        res = re.sub(r'\..*', '', res) # pour supprimer toutes les décimales
        if res:
            res = int(res)
        else:
            res = None
        return res
    
    if chaine :
        # cas normal 
        if "<" not in chaine:
            res = clean(chaine)
        # cas de la somme
        else :
            tmp = 0
            for el in chaine.split("<br"):
                tmp = tmp + int(clean(el))
            res = tmp
    return res

def clean_arg(arg):
    if arg == "":
        return None
    else:
        return arg
    
def normaliser(expression):
    expression = func.lower(expression)
    return case(
        (expression.like('%á%'), 'a'),
        (expression.like('%é%'), 'e'),
        (expression.like('%ê%'), 'e'),
        (expression.like('%è%'), 'e'),
    else_=expression)


def supprimer_accents(chaine):
    accents = {
        'à': 'a', 'â': 'a', 'ä': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'î': 'i', 'ï': 'i',
        'ô': 'o', 'ö': 'o',
        'ù': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c',
        'À': 'A', 'Â': 'A', 'Ä': 'A',
        'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
        'Î': 'I', 'Ï': 'I',
        'Ô': 'O', 'Ö': 'O',
        'Ù': 'U', 'Û': 'U', 'Ü': 'U',
        'Ç': 'C'
    }

    for accent, sans_accent in accents.items():
        chaine = chaine.replace(accent, sans_accent)

    return chaine