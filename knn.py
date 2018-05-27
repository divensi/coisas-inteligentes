#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 17:39:56 2018

@author: Felipe Divensi
"""
import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Trabalho final De IA2.')
parser.add_argument('--knn', dest='knn',
                   help='Habilita o KNN', action='store_true')
parser.add_argument('-k', dest='vizinhos', default=3,
                   help='Numero de vizinhos a serem considerados')
parser.add_argument('-d', dest='distancia', default=2,
                   help='Tipo de Distancia')
parser.add_argument('--imp', dest='imp',
                   help='Tipo de calculo de impureza')
parser.add_argument('-a', dest='atributo', default=0,
                   help='Indica o Atributo Binario a ser usado no ' +
                   'calculo da impureza')
parser.add_argument('arquivo', nargs='?')

args = parser.parse_args()
print(args)


def distanciaMinkowski(p1, p2, dimensao):
    if (dimensao == 0):
        return np.max(np.abs(p2 - p1))
    else:
        soma = np.sum(np.power(np.abs(p2 - p1), dimensao))
        return np.power(soma, 1/dimensao)

ponto1 = np.array([1.0, 1.0, 1.0])
ponto2 = np.array([2.0, 3.0, 6.0])
print(distanciaMinkowski(ponto1, ponto2, 2))
print(distanciaMinkowski(ponto1, ponto2, 1))
print(distanciaMinkowski(ponto1, ponto2, 0))