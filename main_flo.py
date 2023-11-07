import json

from docplex.cp.model import *


with open("./sujet/medium.json") as f:
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

    # CONSTRAINTS

    model.add(task["m"] <= nb_machines for task in tasks)
    model.add(task["o"] <= nb_operateurs for task in tasks)
    model.add(task["B"] <= 50 for task in tasks)

    # CONSTRAINT machine et opérateur

    for i, task in enumerate(tasks):
        model.add(
            sum(
                (mach["machine"] == task["m"])
                * sum((op == task["o"]) for op in mach["operators"])
                for mach in data_tasks[i]["machines"]
            )
            == 1
        )

    # CONSTRAINT 4 ET 5
    for job in data_jobs:
        rj = job["release_date"]
        model.add(
            tasks[job["sequence"][0] - 1]["B"] >= rj
        )  # -1 car les tasks commencent à 1

        for i in range(len(job["sequence"]) - 1):
            model.add(
                tasks[job["sequence"][i + 1] - 1]["B"]
                >= tasks[job["sequence"][i] - 1]["B"]
                + data_tasks[job["sequence"][i] - 1]["processing_time"]
            )

    # CONSTRAINT 7

    for i, ip in zip(range(nb_tasks), range(nb_tasks)):
        if i == ip:
            continue
        model.add(
            if_then(
                (tasks[i]["m"] == tasks[ip]["m"]) | (tasks[i]["o"] == tasks[ip]["o"]),
                (tasks[ip]["B"] < tasks[i]["B"])
                | (tasks[i]["B"] + data_tasks[i]["processing_time"] < tasks[ip]["B"]),
            )
        )

    # OBJECTIVE

    # SOLVE

    res = model.solve(TimeLimit=10)

    # PRINT

    if res:
        for job in data_jobs:
            print(f"Job {job['job']} (rj = {job['release_date']})")
            for i in job["sequence"]:
                print(
                    f" -- La task {i} commence à {res[tasks[i-1]['B']]} et termine à {res[tasks[i-1]['B']] + data_tasks[i-1]['processing_time']}. Machine {res[tasks[i-1]['m']]} est utilisé par l'opérateur {res[tasks[i-1]['o']]}"
                )

        # for i, _ in enumerate(tasks):
        #     task_job = -1
        #     for job in data_jobs:
        #         if i in job["sequence"]:
        #             task_job = job["job"]
        #     print(
        #         f"La task {i} (job {task_job}) commence à {res[tasks[i]['B']]} et est effectué par l'opérateur {res[tasks[i]['o']]} sur la machine {res[tasks[i]['m']]}"
        #     )


cplexsolve()
