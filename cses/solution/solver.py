import os
import subprocess
import requests


def solve():
    response = requests.get("http://localhost:10001/")
    problem = response.json()["task"]
    data = response.json()["input"]
    uuid = response.json()["uuid"]

    for x in os.listdir("cses-solutions/solutions/"):
        if x.startswith(f"{problem}"):
            binary = x
            break

    # write input to file
    with open("input.txt", "w") as f:
        f.write(data)

    # check output
    output = subprocess.check_output(
        f"./cses-solutions/solutions/{binary} <input.txt", shell=True).decode()

    response = requests.post(
        f"http://localhost:10001/submit_solution/{uuid}", json={"solution": output})

    print(response.json())


if __name__ == "__main__":
    solve()
