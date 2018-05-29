#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 17:39:56 2018

@author: Felipe Divensi
"""
import argparse

def datasetFromArff(path):
    dataset = []
    atributos = []

    with open(path, 'r') as lines:
        for line in lines:
            if ('@ATTRIBUTE' in line):
                atributos.append(line.split()[1])
            if (line[0].isdigit()):
                row = []
                for column in line.split(','):
                    try:
                        row.append(float(column))
                    except:
                        row.append(column.replace('\n', ''))
                dataset.append(row)
    return atributos, dataset

def saveDatasetAsText(atributos, dataset, path):
    count = 0

    with open(path, 'w') as file:
        head = []
        for atributo in atributos:
            head.append(atributo)
        file.write('id ')
        file.writelines(' '.join(head))
        file.write('\n')
        for data in dataset:
            file.write(str(count) + ' ')
            count += 1
            file.writelines(' '.join(map(str, data)))
            file.write('\n')
        return True
    return False

def datasetFromText(path):
    atributos   = []
    dataset     = []

    with open(path, 'r') as file:
        atributos = file.readline().split()
        for line in file:
            row = []
            for column in line.split():
                try:
                    row.append(float(column))
                except:
                    row.append(column.replace('\n', ''))
            dataset.append(row)
    return atributos, dataset

if __name__ is '__main__':
    atributos, dataset = datasetFromArff('iris.arff')    
    saveDatasetAsText(atributos, dataset, 'iris.txt')
    atributos2, dataset2 = datasetFromText('iris.txt')
    pass



