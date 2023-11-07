import json
import numpy as np
from docplex.cp.model import *


with open("./tiny.json") as f:
    data = json.load(f)

parameters = data["parameters"]
jobs = data["jobs"]
data_tasks = data["tasks"]

num_tasks = len(data_tasks)
machines_set = set()
for task in data_tasks:
    for machine in task["machines"]:
        machines_set.add(machine["machine"])
num_machines = len(machines_set)

# Initialiser une matrice d'appartenance avec des zéros
membership_matrix = np.zeros((num_tasks, num_machines))

# Remplir la matrice d'appartenance en vérifiant les tâches et les machines associées
for i, task in enumerate(data_tasks):
    task_number = task["task"]
    for machine in task["machines"]:
        machine_number = machine["machine"]
        membership_matrix[task_number - 1, machine_number - 1] = 1

# Afficher la matrice d'appartenance
print("Matrice d'appartenance (1 si la tâche peut être effectuée par la machine, sinon 0) :")
print(membership_matrix)
print(membership_matrix[2,3])
def cplexsolve():

    # MODEL
    model = CpoModel(name="sujet6-kiro")

    # VARIABLES
    tasks = [
        model.integer_var_dict(
            ["B", "m", "o"],
            min=0,
            name="task_" + str(i),
        )
        for i in range(len(data_tasks))
    ]

    # CONSTRAINTS

    model.add(tasks[i]["B"] <= 10 for i in range(len(data_tasks)))
    for i in range(len(data_tasks)):
        model.add(membership_matrix[i-1,tasks[i]["m"]-1] == 1 )

    # OBJECTIVE

    # SOLVE

    res = model.solve(TimeLimit=10)


res = cplexsolve()
