import json

from docplex.cp.model import *


with open("./tiny.json") as f:
    data = json.load(f)

parameters = data["parameters"]
jobs = data["jobs"]
tasks = data["tasks"]


def cplexsolve():
    print("solve model")


cplexsolve()
