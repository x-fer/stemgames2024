import requests
from solver import solve
import numpy as np

r = requests.get("http://209.38.173.120:10000/")

problem = np.array(r.json()["problem"])
uuid = r.json()["uuid"]

print(solution := solve(problem))

r = requests.post(f"http://209.38.173.120:10000/submit_solution/{uuid}", json={
    "solution":
                  solution.tolist()})

print(r.json())
