from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl

from opt.single_objective.teaching.max_ones_problem.max_ones_problem import MaxOnesProblem
from opt.single_objective.teaching.max_ones_problem.max_ones_problem_ilp_linopy import \
                MaxOnesProblemIntegerLinearProgrammingSolver

def main():
        output_control:OutputControl = OutputControl(write_to_output=False)
        problem_to_solve:MaxOnesProblem = MaxOnesProblem.from_dimension(dimension=10)
        optimizer:MaxOnesProblemIntegerLinearProgrammingSolver = MaxOnesProblemIntegerLinearProgrammingSolver(
                        output_control=output_control, problem=problem_to_solve)
        optimizer.solve()
        print('Best solution code: {}'.format(optimizer.model.solution.x))            

if __name__ == '__main__':
        main()
