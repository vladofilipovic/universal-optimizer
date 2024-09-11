from copy import deepcopy
from random import randint
from random import choice
import numpy as np
import random

from uo.algorithm.output_control import OutputControl

from opt.single_objective.comb.set_covering_problem.set_covering_problem import SetCoveringProblem
from opt.single_objective.comb.set_covering_problem.set_covering_problem_ilp_linopy import \
                SetCoveringProblemIntegerLinearProgrammingSolver

def main():
        n = randint(0, 500)
        universe_set = set(np.linspace(0, n, n + 1))

        universe_list = list(universe_set)
        universe_set_integer = set()
        for i in range(len(universe_list)):
                universe_set_integer.add(int(universe_list[i]))
        universe_list = list(universe_set_integer)

        m = randint(1, 50)
        subsets = []

        for i in range(len(universe_set_integer)):
                subsets.append({i})

        for i in range(m):
            number_of_elements = randint(1, n)
            random.shuffle(universe_list)
            subset = set(universe_list[0:number_of_elements])
            subsets.append(subset)

        #universe_set = {0, 1, 2, 3, 4, 5, 6}
        #universe_list = list(universe_set)
        #subsets = [ {1, 3, 5}, {0, 1, 2, 6}, {2, 3, 4}, {0, 4}, {3}]
        #subsets
        problem_to_solve:SetCoveringProblem = SetCoveringProblem(universe_set_integer, subsets)
        solver:SetCoveringProblemIntegerLinearProgrammingSolver = SetCoveringProblemIntegerLinearProgrammingSolver(
                        problem=problem_to_solve)
        print("String representation: ", problem_to_solve.string_rep)
        bs = solver.optimize()
        print('Best solution: {}'.format(bs.string_representation()))           

if __name__ == '__main__':
        main()
