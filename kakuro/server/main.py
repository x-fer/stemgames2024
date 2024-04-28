import time
from typing import List
import fastapi
import os
import json
import numpy as np
from uuid import uuid4

from pydantic import BaseModel

app = fastapi.FastAPI()

problem_solutions = [
    (
        json.loads(open(
            f"problems/{problem}").read()
        ),
        json.loads(open(
            f"solutions/{problem}").read()
        )
    )
    for problem in os.listdir("problems")
]

problems = [problem for problem, _ in problem_solutions]
solutions = [solution for _, solution in problem_solutions]


db = {}


@ app.get("/")
def get_puzzle():
    global db
    uuid = str(uuid4())

    problem_index = np.random.randint(len(problems))

    db[uuid] = {
        "problem": problem_index,
        "timestamp": time.time()
    }

    return {"uuid": uuid,
            "instructions": "Within 10 seconds, solve 11x11 Kakuro i.e. fill in all @ cells with numbers 1-9 according to the rules of Kakuro. Then submit to /submit_solution/{uuid} with a post request with the solution FLATTENED (121 entries list) and AS STRINGS in the body as json. Example: {'solution': ['#', '#', '-1,2', '3', '4', '5', '6', '7', '8', '9', '1', '2', ...]}.",
            "problem": problems[problem_index]}


class Body(BaseModel):
    solution: List[str]


@app.post("/submit_solution/{uuid}")
def submit_solution(uuid: str, body: Body):
    global db

    solution = body.solution

    db = {uuid: db[uuid]
          for uuid in db if time.time() - db[uuid]["timestamp"] <= 10}

    if uuid not in db:
        return {"error": "Invalid UUID or timed out."}

    problem_index = db[uuid]["problem"]

    if len(solution) != 11 * 11:
        return {"error": "Invalid solution length, must be 11 * 11 (121)"}

    if all([solution[i] == solutions[problem_index][i] for i in range(11 * 11)]):
        return {"status": "correct", "message": "Congratulations! Your solution is correct.", "flag": "STEM24{k0Kolo_KokOLO_kOKo1o_afee7c5c}"}

    return {"status": "incorrect", "message": "Your solution is incorrect."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
