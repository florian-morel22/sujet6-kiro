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




membership_matrix = np.zeros((num_tasks, num_machines))
membership_matrix_2 = np.zeros((num_tasks, num_machines,8))

for i, task in enumerate(data_tasks):
    task_number = task["task"]
    for machine in task["machines"]:
        machine_number = machine["machine"]
        membership_matrix[task_number - 1, machine_number - 1] = 1
        for operators in machine["operators"]:
            # operators_number = operators["operators"]
            print(operators)
            membership_matrix_2[task_number -1, machine_number - 1,operators-1]=1

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

    jobs = [
        model.integer_var_dict(
            ["B", "C"],
            min=0,
            name="job_" + str(i),
        )
        for i in range(len(data_jobs))
    ]

    # CONSTRAINTS

    model.add(task["m"] < num_machines for task in tasks)
    model.add(task["o"] < 8 for task in tasks)
    model.add(tasks[i]["B"] <= 10 for i in range(len(data_tasks)))


    for i in range(len(data_tasks)):
        for j in range(num_machines):
            model.add(if_then(tasks[i]["m"]==j, membership_matrix[i-1, j-1]==1))
            for k in range(8):
                model.add(if_then(tasks[i]["o"]==k, membership_matrix_2[i-1, j-1,k-1]==1))


    # OBJECTIVE

    # SOLVE

    res = model.solve(TimeLimit=10)

    if res:
        for i, _ in enumerate(tasks):
            task_job = -1
            for job in data_jobs:
                if i in job["sequence"]:
                    task_job = job["job"]
            print(
                f"La task {i} (job {task_job}) commence à {res[tasks[i]['B']]} et est effectué par l'opérateur {res[tasks[i]['o']]} sur la machine {res[tasks[i]['m']]}"
            )


res = cplexsolve()
