import requests
from solver import solve
import numpy as np

r = requests.get("http://127.0.0.1:8000/")

problem = np.array(r.json()["problem"]).reshape(11, 11)
uuid = r.json()["uuid"]

print(solution := solve(problem))

r = requests.post(f"http://127.0.0.1:8000/submit_solution/{uuid}", json={
    "solution":
                  solution.flatten().tolist()})

print(r.json())
