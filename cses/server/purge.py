import os
tasks = open("zadaci.txt").read().split("\n")

for x in os.listdir("test_cases"):
    if x not in tasks:
        print("del", x)
        os.system("rm -rf test_cases/" + x)
    else:
        print(x)
