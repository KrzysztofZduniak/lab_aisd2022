# to chyba wszystko co potrzeba do testówm jak się gdzieś jebłem to sorki
# wal śmiało jak masz jakieś pytania, niejasności, tezy, kontrowersje, zażalenia, wnioski, konkluzje
# tylko jak będziesz to robił w poniedziałek to nie zawsze mogę być dostępny ale postaram się patrzeć co jakiś czas na telefon
import random
import networkx as nx
from graph2 import MatrixGraph, ListGraph
from graph_generation import dag_fulfilment, get_random_dag_edge, make_dag, sort_top, make_undirected_graph, mst3 as mst
import time
import matplotlib.pyplot as plt

#dag_fulfilment to twoja funkcja fulfilment, raczej nie będziesz jej tu używał
#get_random_dag_edge to też fukncja służąca innym, raczej tu nie posłuży
#make_dag - to jest funkcja do robienia dagów - nic nie zwraca, w argumentach przekazujesz pusty graf i te procenty - tylko tutaj zrobiłem to jako ułamek od 0 do 1
#sort_top - funkcja do sortowania topologicznego - przyjmuje tylko graf
#make_undirected_graph - nazwa mówi sama za siebie - tutaj mała niekonsekwencja z mojej strony bo to returnuje grapha czyli trzeba to do czegoś przypisać, argumenty są 3:
#  ilość nodeów, procenty(znów jako ułamek) i typ jako string "matrix" lub "list"
#mst 3 as mst - to zwraca listę krawędzi mst dla grafu domyślnie stworzonego przez make_undirected_graph - jako argument przyjmuje tylko graf, ogólnie jak mamy mierzyć czas to chyba nas nie interesuje co to zwraca