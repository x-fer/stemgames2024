import os
import subprocess
import time
import requests
from multiprocessing import Pool


def solve():
    response = requests.get("http://209.38.173.120:10001/")
    problem = response.json()["task"]
    data = response.json()["input"]
    uuid = response.json()["uuid"]

    for x in os.listdir("cses-solutions/src/"):
        if problem in x:
            os.system(f"g++ cses-solutions/src/{problem}.cpp")
            break

    # write input to file
    with open("input.txt", "w") as f:
        f.write(data)

    # check output
    output = subprocess.check_output(
        f"./a.out < input.txt", shell=True, timeout=1).decode()

    response = requests.post(
        f"http://209.38.173.120:10001/submit_solution/{uuid}", json={"solution": output})

    # "result": "Correct",

    assert response.status_code == 200 and response.json()[
        "result"] == "Correct", response.json()

    print(response.json())


if __name__ == "__main__":
    for _ in range(100):
        solve()
