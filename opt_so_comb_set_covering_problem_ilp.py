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
        n = randint(0, 1000)
        #universe_set = set(np.linspace(0, n, n + 1))
        #universe_list = list(universe_set)

        #m = randint(0, 10)
        #subsets = []

        #for i in range(m):
        #    number_of_elements = randint(0, 500)
        #    random.shuffle(universe_list)
        #    subset = set(universe_list[0:number_of_elements])
        #    subsets.append(subset)

        universe_set = {0, 1, 2, 3, 4, 5, 6}
        universe_list = list(universe_set)
        subsets = [ {1, 3, 5}, {0, 1, 2, 6}, {2, 3, 4}, {0, 4}, {3}]
        subsets
        problem_to_solve:SetCoveringProblem = SetCoveringProblem(universe_set, subsets)
        solver:SetCoveringProblemIntegerLinearProgrammingSolver = SetCoveringProblemIntegerLinearProgrammingSolver(
                        problem=problem_to_solve)
        bs = solver.optimize()
        print('Best solution: {}'.format(bs.string_representation()))
        #print('Best solution code: {}'.format(solver.model.solution.x))            

if __name__ == '__main__':
        main()
