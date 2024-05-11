import os
from time import sleep
from subprocess import STDOUT, check_output


for id in open("zadaci.txt").read().split("\n"):
    id = int(id)

    tests_path = f"test_cases/{id}/"

    files = sorted(set(".".join(x.split(".")[:-1])
                       for x in os.listdir(tests_path)))

    for x in files:
        in_file = f"{tests_path}{x}.in"
        out_file = f"{tests_path}{x}.out"
        assert os.path.exists(in_file), f"Input file {in_file} not found"
        assert os.path.exists(out_file), f"Output file {out_file} not found"

        binaries = f"cses-solutions/solutions/"
        binary = [f"{binaries}{y}" for y in os.listdir(
            binaries) if y.startswith(f"{id}")]
        print([f"{binaries}{y}" for y in os.listdir(
            binaries) if y.startswith(f"{id}")])
        assert len(binary) >= 1, f"Binary not found for problem {id}"
        binary = binary[0]

        print(f"Running test {x}...")

        try:
            output = check_output(
                f"cat {in_file} | \"{binary}\"", shell=True, stderr=STDOUT, timeout=60).decode()
        except Exception as e:
            print(f"Task {id}, Test {x} failed: {e}")
            raise Exception("Test failed", e)

        expected_output = open(out_file).read()

        if "Time Taken:" in output:
            output = output[:output.index("Time Taken:")]

        if "".join(expected_output.split()).strip() == "".join(output.split()).strip():
            print(f"Task {id}, Test {x} passed")
        else:
            print(f"Task {id}, Test {x} failed")
            print(f"Expected: {expected_output}")
            print(f"Got: {output}")
            print("".join(expected_output.split()).strip(),
                  "".join(output.split()).strip())

            raise Exception("Test failed")
