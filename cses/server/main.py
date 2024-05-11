import time
from typing import List
import fastapi
import os
import json
import numpy as np
from uuid import uuid4

from pydantic import BaseModel

app = fastapi.FastAPI()

tasks = [
    x.strip() for x in
    open("zadaci.txt").read().split("\n")
    if len(x.strip()) > 0
]

test_cases = {}

for task in tasks:
    files = os.listdir(f"test_cases/{task}")

    ins = [x for x in files if x.endswith(".in")]
    outs = [x for x in files if x.endswith(".out")]

    assert len(ins) == len(
        outs), f"Task {task} has different number of input and output files"

    for in_file in ins:
        test_cases[task] = {
            "task": task,
            "in": open(f"test_cases/{task}/{in_file}").read(),
            "out": open(f"test_cases/{task}/{in_file.replace('.in', '.out')}").read()
        }

db = {}


@app.get("/")
def get_puzzle():
    global test_cases
    global db

    uuid = str(uuid4())

    test_case = np.random.choice(list(test_cases.keys()))
    test_case = test_cases[test_case]

    db[uuid] = {
        "task": test_case["task"],
        "timestamp": time.time()
    }

    return {
        "uuid": uuid,
        "instructions": "Within 10 seconds, solve the task. Then submit to /submit_solution/{uuid} with a post request with the solution in the body as json. Example: {'solution': 'YES'}",
        "task": test_case["task"],
        "input": test_case["in"]
    }


class Body(BaseModel):
    solution: str


FLAG = "STEM24{CS3S_H4CK3R_4L3RT}"


@app.post("/submit_solution/{uuid}")
def submit_solution(uuid: str, body: Body):
    global db

    solution = body.solution

    db = {uuid: db[uuid]
          for uuid in db if time.time() - db[uuid]["timestamp"] <= 10}

    if uuid not in db:
        return {"error": "Time limit exceeded"}

    task = db[uuid]["task"]
    test_case = test_cases[task]

    # print("|".join(test_case["out"].split()), "|".join(solution.split()))

    if "|".join(test_case["out"].split()) == "|".join(solution.split()):
        return {"result": "Correct", "flag": FLAG}

    return {"result": "Incorrect"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10001)
