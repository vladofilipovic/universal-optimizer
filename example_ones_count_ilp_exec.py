from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl

from opt.single_objective.teaching.ones_count_problem.ones_count_problem_max import OnesCountProblemMax
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_ilp_linopy import \
                OnesCountProblemIntegerLinearProgrammingSolver

def main():
        output_control:OutputControl = OutputControl(write_to_output=False)
        problem_to_solve:OnesCountProblemMax = OnesCountProblemMax.from_dimension(dimension=10)
        solver:OnesCountProblemIntegerLinearProgrammingSolver = OnesCountProblemIntegerLinearProgrammingSolver(
                        output_control=output_control, problem=problem_to_solve)
        solver.optimize()
        print('Best solution code: {}'.format(solver.model.solution.x))            

if __name__ == '__main__':
        main()
