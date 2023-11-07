import json
import numpy as np
from docplex.cp.model import *


with open("./sujet/tiny.json") as f:
    data = json.load(f)

parameters = data["parameters"]
data_jobs = data["jobs"]
data_tasks = data["tasks"]

num_tasks = len(data_tasks)
machines_set = set()
for task in data_tasks:
    for machine in task["machines"]:
        machines_set.add(machine["machine"])
num_machines = len(machines_set)

<<<<<<< HEAD
def task_i_with_machine_k(i, k):
    for task in data["tasks"]:
        if task["task"] == i:
            for machine in task["machines"]:
                if machine["machine"] == k:
                    return 1
    return 0


=======
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
>>>>>>> f3e9bce05ac2f6d686bc4ba00d80af3ccb06fa0c
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

    jobs = [
        model.integer_var_dict(
            ["B", "C"],
            min=0,
            name="job_" + str(i),
        )
        for i in range(len(data_jobs))
    ]

    # CONSTRAINTS

    model.add(tasks[i]["B"] <= 10 for i in range(len(data_tasks)))
<<<<<<< HEAD

    model.add(
        task_i_with_machine_k(i, tasks[i]["m"]) == 1 for i in range(len(data_tasks))
    )
=======
    for i in range(len(data_tasks)):
        model.add(membership_matrix[i-1,tasks[i]["m"]-1] == 1 )
>>>>>>> f3e9bce05ac2f6d686bc4ba00d80af3ccb06fa0c

    # OBJECTIVE

    # SOLVE

    res = model.solve(TimeLimit=10)


res = cplexsolve()
