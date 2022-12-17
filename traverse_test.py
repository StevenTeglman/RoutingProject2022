from util import graph, robustness, traverse_simulator, experiment
from turtle import color
from algorithms import sdto
import networkx as nx
import matplotlib.pyplot as plt
import datetime


print(datetime.datetime.now())
for i in range(21):
    experiment.run_experiment()
print(datetime.datetime.now())
