#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 17:39:56 2018

@author: Felipe Divensi
"""
import argparse
import numpy as np
from arff2txt import datasetFromText

def distanciaMinkowski(p1, p2, tipoDistancia=2):
    if (tipoDistancia == 0):
        return np.max(np.abs(p2 - p1))
    else:
        soma = np.sum(np.power(np.abs(p2 - p1), tipoDistancia))
        return np.power(soma, 1/tipoDistancia)

def kVizinhosMaisProximos(k, instancia, dataset, tipoDistancia=2):
    distancias = []
    for data in dataset:
        if (instancia[0] != data[0]): #nao fazer o mesmo
            elemento = {}
            elemento['distancia'] = distanciaMinkowski(np.array(instancia[1:-1]), 
                                                    np.array(data[1:-1]), 
                                                    tipoDistancia)
            elemento['instancia'] = data
            distancias.append(elemento)
    
    maisProximas = sorted(distancias, key=lambda vizinho: vizinho['distancia'])[0:k:]
    comparacao = {}
    
    for vizinho in maisProximas:
        if vizinho['instancia'][-1] in comparacao:
            comparacao[vizinho['instancia'][-1]] += 1
        else:
            comparacao[vizinho['instancia'][-1]] = 1
    
    classeEscolhida = max(comparacao, key=comparacao.get)
    return maisProximas, classeEscolhida

def gini(dataset, atributo):
    uns     = len([i for i in dataset if i[atributo] == 1])
    zeros   = len([i for i in dataset if i[atributo] == 0])

    return 1 - (uns/len(dataset))**2 - (zeros/len(dataset))**2

def entropia(dataset, atributo):
    uns     = len([i for i in dataset if i[atributo] == 1])
    zeros   = len([i for i in dataset if i[atributo] == 0])
    
    return - (uns/len(dataset) * np.log2(uns/len(dataset)) +
              zeros/len(dataset) * np.log2(zeros/len(dataset)))

def erroClassificacao(dataset, atributo):
    uns     = len([i for i in dataset if i[atributo] == 1])
    zeros   = len([i for i in dataset if i[atributo] == 0])
    
    if ((uns/len(dataset)) > (zeros/len(dataset))):
        return 1 - (uns/len(dataset))
    else:
        return 1 - (zeros/len(dataset))

def parseArgs():
    parser = argparse.ArgumentParser(description='Trabalho final De IA2.')
    parser.add_argument('--knn', dest='knn',
                    help='Habilita o KNN', action='store_true')
    parser.add_argument('-k', dest='vizinhos', default=3, type=int,
                    help='Numero de vizinhos a serem considerados')
    parser.add_argument('-d', dest='distancia', default=2, type=int,
                    help='Tipo de Distancia')
    parser.add_argument('--imp', dest='imp', type=int,
                    help='Tipo de calculo de impureza')
    parser.add_argument('-a', dest='atributo', default=0, type=int,
                    help='Indica o Atributo Binario a ser usado no ' +
                    'calculo da impureza')
    parser.add_argument('arquivo', nargs='?', default='iris.txt')

    args = parser.parse_args()
    
    return args

def main():
    args = parseArgs()
    atributo = args.atributo
    distancia = args.distancia
    impureza = args.imp
    knn = args.knn
    vizinhos = args.vizinhos
    arquivo = args.arquivo
    
    atributos, dataset = datasetFromText(arquivo)

    if knn:
        for instancia in dataset:
            distancias, classe = kVizinhosMaisProximos(
                    vizinhos, instancia, dataset, distancia)
            
            print('Classe = {} \nvizinhos mais próximos: {} \n'.format(
                classe,
                ', '.join("%0.0f" % d['instancia'][0] for d in distancias)
            ))
            
    elif impureza is not None:
        if impureza == 1:
            print("Gini: {}".format(gini(dataset, atributo)))
        elif impureza == 2:
            print("Entropia: {}".format(entropia(dataset, atributo)))
        elif impureza == 3:
            print("ErroClass: {}".format(erroClassificacao(dataset, atributo)))
        else:
            print("Cálculo de Impureza Inválido")
    else:
        print('Nenhum argumento recebido')

#if __name__ is '__main__':
main()
