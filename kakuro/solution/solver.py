import tabulate
import json
import sys
import gurobipy as gp
from gurobipy import GRB
import numpy as np


# print(puzzle)


def to_right(i, j, puzzle):
    j += 1
    l = []
    while j < 11 and puzzle[i, j] == '@':
        l.append((i, j))
        j += 1

    return l


def to_down(i, j, puzzle):
    i += 1
    l = []
    while i < 11 and puzzle[i, j] == '@':
        l.append((i, j))
        i += 1
    return l


def solve(puzzle, exclude_sol=None):

    m = gp.Model("kakuro")
    m.setParam('OutputFlag', 0)

    # Variables
    x = m.addVars(11, 11, 9, vtype=GRB.BINARY, name="x")

    if exclude_sol is not None:
        not_equal = []
        for i in range(11):
            for j in range(11):
                if puzzle[i, j] == '@':
                    not_equal.append((i, j, int(exclude_sol[i, j]) - 1))

        # Or of all the not equal constraints
        m.addConstrs(gp.quicksum(x[i, j, k] for i, j, k in not_equal) <= len(not_equal) - 1
                     for i in range(11) for j in range(11) if puzzle[i, j] == '@')

    for i in range(11):
        for j in range(11):
            if puzzle[i, j] == '@':
                m.addConstr(gp.quicksum(x[i, j, k] for k in range(9)) == 1)
            else:
                m.addConstr(gp.quicksum(x[i, j, k] for k in range(9)) == 0)

    for i in range(11):
        for j in range(11):
            if puzzle[i, j] != '@' and puzzle[i, j] != '#':
                clue_down, clue_right = puzzle[i, j].split(',')

                right = to_right(i, j, puzzle)
                down = to_down(i, j, puzzle)

                if clue_right != '-1':
                    assert len(right) >= 1
                    m.addConstr(gp.quicksum((1 + k) * x[_i, _j, k]
                                for k in range(9) for _i, _j in right) == int(clue_right))
                    for k in range(9):  # ensure one digit used once
                        m.addConstr(gp.quicksum(x[_i, _j, k]
                                    for _i, _j in right) <= 1)

                if clue_down != '-1':
                    assert len(down) >= 1

                    m.addConstr(gp.quicksum((1 + k) * x[_i, _j, k]
                                for k in range(9) for _i, _j in down) == int(clue_down))
                    for k in range(9):
                        m.addConstr(gp.quicksum(x[_i, _j, k]
                                                for _i, _j in down) <= 1)

                # if len(clues) == 1:
                #     if len(right) != 0:
                #         m.addConstr(gp.quicksum((1 + k) * x[_i, _j, k]
                #                     for k in range(9) for _i, _j in right) == int(clues[0]))
                #         for k in range(9):  # ensure one digit used once
                #             m.addConstr(gp.quicksum(x[_i, _j, k]
                #                         for _i, _j in right) <= 1)
                #     if len(down) != 0:
                #         m.addConstr(gp.quicksum((1 + k) * x[_i, _j, k]
                #                     for k in range(9) for _i, _j in down) == int(clues[0]))
                #         for k in range(9):
                #             m.addConstr(gp.quicksum(x[_i, _j, k]
                #                         for _i, _j in down) <= 1)

    m.optimize()

    if m.status != GRB.OPTIMAL:
        print("No solution")
        return None

    sol = puzzle.copy()

    for i in range(11):
        for j in range(11):
            if puzzle[i, j] == '@':
                for k in range(9):
                    if x[i, j, k].x > 0.5:
                        sol[i, j] = str(k + 1)
            else:
                sol[i, j] = puzzle[i, j]

    return sol


def convert(puzzle):
    new_puzzle = [['#' for _ in range(11)] for _ in range(11)]
    # new_puzzle = np.array(new_puzzle)
    for i in range(11):
        for j in range(11):
            if puzzle[i, j] == '#':
                new_puzzle[i][j] = '#'
            elif puzzle[i, j] == '@':
                new_puzzle[i][j] = '@'
            else:
                clues = puzzle[i, j][1:-1].split('-')

                right = to_right(i, j, puzzle)
                down = to_down(i, j, puzzle)

                if len(clues) == 2:
                    assert len(right) >= 1
                    assert len(down) >= 1

                    new_puzzle[i][j] = f"{clues[0]},{clues[1]}"

                if len(clues) == 1:
                    assert (len(right) == 0 and len(down) >= 1) or (
                        len(right) >= 1 and len(down) == 0), (i, j, len(right), len(down))

                    if len(right) != 0:
                        new_puzzle[i][j] = f"-1,{clues[0]}"

                    if len(down) != 0:
                        new_puzzle[i][j] = f"{clues[0]},-1"

    return new_puzzle


if __name__ == "__main__":

    puzzle = json.loads(open(sys.argv[1]).read())
    assert len(puzzle) == 11 * 11
    puzzle = np.array(puzzle).reshape(11, 11)

    puzzle = convert(puzzle)
    puzzle = np.array(puzzle)

    with open(f"problems/{sys.argv[1].split('/')[-1]}", "w") as f:
        f.write(json.dumps(puzzle.flatten().tolist()))

    print(tabulate.tabulate(puzzle))  # prvi je dolje, drugi desno
    sol1 = solve(puzzle)
    assert sol1 is not None
    print(tabulate.tabulate(sol1))
    sol = solve(puzzle, exclude_sol=sol1)
    assert sol is None

    with open(f"solutions/{sys.argv[1].split('/')[-1]}", "w") as f:
        f.write(json.dumps(sol1.flatten().tolist()))
