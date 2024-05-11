
import os

for x in open("tasks.txt"):
    data = x.strip().split()

    id = data[0].split("/")[-1]

    with open(f"{id}.wot.cpp", "w") as f:
        f.write(
            f"#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {{\n\n}}\n")

    os.system(f"./cses-cli submit {id}.wot.cpp")
    os.system(f"rm {id}.wot.cpp")

    # print(id)
    # ./cses-cli submit 1621 1621.cpp
