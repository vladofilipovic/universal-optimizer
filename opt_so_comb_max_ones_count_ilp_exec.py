from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl

from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem import MaxOnesCountProblem
from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem_ilp_linopy import \
                MaxOnesCountProblemIntegerLinearProgrammingSolver

def main():
        problem_to_solve:MaxOnesCountProblem = MaxOnesCountProblem.from_dimension(dimension=10)
        solver:MaxOnesCountProblemIntegerLinearProgrammingSolver = MaxOnesCountProblemIntegerLinearProgrammingSolver(
                        problem=problem_to_solve)
        bs = solver.optimize()
        print('Best solution: {}'.format(bs.string_representation()))
        #print('Best solution code: {}'.format(solver.model.solution.x))            

if __name__ == '__main__':
        main()
