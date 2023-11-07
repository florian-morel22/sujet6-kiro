import json

from docplex.cp.model import *


with open("./sujet/tiny.json") as f:
    data = json.load(f)

parameters = data["parameters"]
data_jobs = data["jobs"]
data_tasks = data["tasks"]

nb_machines = parameters["size"]["nb_machines"]
nb_operateurs = parameters["size"]["nb_operators"]
nb_tasks = parameters["size"]["nb_tasks"]
nb_jobs = parameters["size"]["nb_jobs"]


def cplexsolve():
    # MODEL
    model = CpoModel(name="sujet6-kiro")

    # VARIABLES
    tasks = [
        model.integer_var_dict(
            ["B", "m", "o"],
            min=1,
            name="task_" + str(i),
        )
        for i in range(nb_tasks)
    ]

    jobs = [
        model.integer_var_dict(
            ["B", "C"],
            min=1,
            name="job_" + str(i),
        )
        for i in range(nb_jobs)
    ]

    # CONSTRAINTS

    model.add(task["m"] <= nb_machines for task in tasks)
    model.add(task["o"] <= nb_operateurs for task in tasks)
    model.add(task["B"] <= nb_tasks for task in tasks)

    model.add(job["B"] <= job["C"] for job in jobs)
    model.add(job["C"] <= nb_tasks for job in jobs)

    for job in data_jobs:
        rj = job["release_date"]
        model.add(tasks[job["sequence"][0]]["B"] == rj)

    # OBJECTIVE

    # SOLVE

    res = model.solve(TimeLimit=10)

    # PRINT

    if res:
        for i, _ in enumerate(tasks):
            task_job = -1
            for job in data_jobs:
                if i in job["sequence"]:
                    task_job = job["job"]
            print(
                f"La task {i} (job {task_job}) commence à {res[tasks[i]['B']]} et est effectué par l'opérateur {res[tasks[i]['o']]} sur la machine {res[tasks[i]['m']]}"
            )


cplexsolve()
