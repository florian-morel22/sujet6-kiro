import json

from docplex.cp.model import *


with open("./sujet/tiny.json") as f:
    data = json.load(f)

parameters = data["parameters"]
data_jobs = data["jobs"]
data_tasks = data["tasks"]


def task_i_with_machine_k(i, k):
    for task in data["tasks"]:
        if task["task"] == i:
            for machine in task["machines"]:
                if machine["machine"] == k:
                    return 1
    return 0


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

    model.add(
        task_i_with_machine_k(i, tasks[i]["m"]) == 1 for i in range(len(data_tasks))
    )

    # OBJECTIVE

    # SOLVE

    res = model.solve(TimeLimit=10)


res = cplexsolve()
