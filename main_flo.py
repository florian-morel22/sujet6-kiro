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

    model.add(sum(tasks[i]["B"] for i in range(len(data_tasks))) <= 10)

    # OBJECTIVE

    # SOLVE

    res = model.solve(TimeLimit=10)

    return res


res = cplexsolve()
