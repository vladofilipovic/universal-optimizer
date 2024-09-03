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
        universe = np.linspace(o, n, n + 1)

        m = randint(0, 10)
        subsets = []

        for i in range(m):
            number_of_elements = randint(0, 500)
            random.shuffle(universe)
            subset = set(universe[0:number_of_elements])
            subsets.append(subset)

        problem_to_solve:SetCoveringProblem = SetCoveringProblem(universe, subsets)
        solver:SetCoveringProblemIntegerLinearProgrammingSolver = SetCoveringProblemIntegerLinearProgrammingSolver(
                        problem=problem_to_solve)
        bs = solver.optimize()
        print('Best solution: {}'.format(bs.string_representation()))
        #print('Best solution code: {}'.format(solver.model.solution.x))            

if __name__ == '__main__':
        main()
