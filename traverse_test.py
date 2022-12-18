from util import graph, robustness, traverse_simulator, experiment
from turtle import color
from algorithms import sdto
import networkx as nx
import matplotlib.pyplot as plt
import datetime
from multiprocessing import Process



# print(datetime.datetime.now())
# for i in range(150):
#     try:
#         experiment.run_experiment()
    # except:
    #     print("Something went wrong. Aborting experiment.")
# print(datetime.datetime.now())


if __name__ == '__main__':
    runs = 150
    # define batch size
    batch_size = 5
    # execute in batches
    for i in range(0, runs, batch_size):
        # execute all tasks in a batch
        processes = [Process(target=experiment.run_experiment) for j in range(i, i+batch_size)]
        # start all processes
        for process in processes:
            try:
                process.start()
            except:
                print("Something went wrong. Aborting experiment.")

        # wait for all processes to complete
        for process in processes:
            process.join()
    # report that all tasks are completed
    print('Done', flush=True)