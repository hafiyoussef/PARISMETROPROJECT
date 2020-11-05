#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:25:53 2020

@author: HafiRiheb
"""


import re 
from time import time
t0 = time()

with open ("Data/metro.txt", "r",encoding="utf-8") as dataset :

    list_source_destination = []
    list_keys = []
    my_graph = {}
    my_graph_dijkstra = {}
    lists_sources_lists = []
    line_dataset = dataset.readlines()
    
    
    
for i in range(len(line_dataset) - 1): 
    if not re.match(r'([\d]+)', line_dataset[i]):
        line_temp = i
for i in range(line_temp + 1, len(line_dataset) - 1):
    list_source_destination.append((int(line_dataset[i].strip().split(" ")[0]), int(line_dataset[i].strip().split(" ")[1]),
                                     float(line_dataset[i].strip().split(" ")[2])))
    list_keys.append(int(line_dataset[i].strip().split(" ")[0]))
for k in range(len(list_keys)):
    for unit in list_source_destination:
        if unit[0] == k:
            lists_sources_lists.append(((unit[1],unit[2])))
        else:
            pass
    if len(lists_sources_lists) != 0:
        my_graph_dijkstra[k] = lists_sources_lists
        lists_sources_lists = []

        
        
        
        
sourceFileName='/Users/HafiRiheb/desktop/Paris-Metro-Project-master/Data/metro.txt'
def dataset_with_dict():
    f = open(sourceFileName, 'r')
    my_l = []
    my_stations_with_dict = {}
    for unit in f.readlines()[1:]:
        if unit.strip() != '[Edges]':
            #unit = unit.encode("utf-8") # encoding for utf8

            my_l.append(unit[5:])
        else:
            break
    for i in range(len(my_l)):
        my_stations_with_dict[i] = my_l[i]

    return my_stations_with_dict
dict_my_stations = dataset_with_dict()



def short_path(l, dict_with_stations,b_flag=None):
    l_s_path = []
    for unit in l:
        l_s_path.append(("id:{0}  Station :{1}\n".format(unit, dict_with_stations[unit])))
    if b_flag:
        return '-'.join(l_s_path)
    else:
        return (l_s_path)



def dijkstra(graph,start,target):
    inf = 0
    for u in graph: 
        for v ,w in graph[u]:
           inf = inf + w
    dist = dict([(u,inf) for u in graph])
    prev = dict([(u,None) for u in graph])
    q = list(graph.keys())
    dist[start] = 0
    def x(v):
        return dist[v]
    while q != []:
        u = min(q, key=x)
        q.remove(u)
        for v,w in graph[u]:
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    trav = []
    temp = target
    while temp != start:
        trav.append(prev[temp])
        temp = prev[temp]
    trav.reverse()
    trav.append(target)
    return trav,dist[target]


depart=int(input("donner la referance de la station de depart"))
print("station de depart=",dict_my_stations[depart])
arrivee=int(input("donner la referance de la station d'arrivée"))
print("station d'arrivée=",dict_my_stations[arrivee])



traverse = dijkstra(my_graph_dijkstra,depart,arrivee)[0]
dist = dijkstra(my_graph_dijkstra,depart,arrivee)[1]
print ("le chemin le plus court avec Djekstra",traverse,'\n')
printed_drijkstra = dijkstra(my_graph_dijkstra,depart,arrivee)[0]
print("le plus cour chemin enter {} et {} est le suivant :".format(dict_my_stations[depart],dict_my_stations[arrivee]))

short_path_printed_for_dijkstra = short_path(printed_drijkstra, dict_my_stations,"p")


print (short_path_printed_for_dijkstra)


print ("la distance entre le station de depart et la station d'arrivée est :" ,("%.0f" % dist),'\n')
t1 = time()
print ("le §temps d'excution est egale à %f" %(t1-t0))
