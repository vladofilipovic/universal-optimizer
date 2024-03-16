from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl

from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_ilp_linopy import \
                OnesCountMaxProblemIntegerLinearProgrammingSolver

def main():
        output_control:OutputControl = OutputControl(write_to_output=False)
        problem_to_solve:OnesCountMaxProblem = OnesCountMaxProblem.from_dimension(dimension=10)
        solver:OnesCountMaxProblemIntegerLinearProgrammingSolver = OnesCountMaxProblemIntegerLinearProgrammingSolver(
                        output_control=output_control, problem=problem_to_solve)
        bs = solver.optimize()
        print('Best solution: {}'.format(bs.string_representation()))
        #print('Best solution code: {}'.format(solver.model.solution.x))            

if __name__ == '__main__':
        main()
