import os

for x in os.listdir("src"):
    # compile to solutions
    s = os.system(
        f"g++-13 \"src/{x}\" -o \"solutions/{x.split('.')[0]}\" -std=c++17 -O2 -DONLINE_JUDGE")

    print(f"Compiled {x} to solutions/{x.split('.')[0]}, status: {s}")
