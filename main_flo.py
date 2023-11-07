import json

from docplex.cp.model import *


with open("./tiny.json") as f:
    data = json.load(f)

parameters = data["parameters"]
jobs = data["jobs"]
data_tasks = data["tasks"]


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

    model.add(sum(task["B"] for task in tasks) <= 10)
    model.add(task["m"] == 1 for task in tasks)
    model.add(task["o"] == 1 for task in tasks)

    # OBJECTIVE

    # SOLVE

    res = model.solve(TimeLimit=10)

    # PRINT

    if res:
        for i, _ in enumerate(tasks):
            task_job = -1
            for job in jobs:
                if i in job["sequence"]:
                    task_job = job["job"]
            print(
                f"La task {i} (job {task_job}) commence à {res[tasks[i]['B']]} et est effectué par l'opérateur {res[tasks[i]['o']]} sur la machine {res[tasks[i]['m']]}"
            )


cplexsolve()
