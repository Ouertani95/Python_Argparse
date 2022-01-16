#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python DNA verification script
"""

__author__ = 'Mohamed Ouertani'


def purify (adn_str):
    """purifies  dna sequence """
    return adn_str


def is_valid(adn_str):
    """ verifies if input is a valid dna sequence"""
    nuc_list = ['T','A','G','C']
    if adn_str is None or len(adn_str.replace(" ",""))==0 :
        return False
    # adn_str.replace(" ","")
    # if len(adn_str)==0 :
    #     return False
    for nuc in adn_str :
        if  nuc.upper() not in nuc_list :
            return False
    return True


def get_valid_adn(prompt='chaîne : '):
    """ main function for dna verification"""
    print("Ce programme permet de vérifier une chaine d'ADN :")
    chaine = input(prompt)
    while not is_valid(chaine) :
        print("Chaine invalide.")
        chaine = input(prompt)
    print("La chaine que vous avez ecrit est : ",chaine.upper())
    return chaine
