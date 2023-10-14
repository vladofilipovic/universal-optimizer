from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl

from opt.single_objective.teaching.max_function_1_variable_problem.max_function_1_variable_problem import \
                MaxFunction1VariableProblem
from opt.single_objective.teaching.max_function_1_variable_problem_int_solution.\
        max_function_1_variable_problem_int_solution import MaxFunction1VariableProblemIntSolution

def main():
        output_control:OutputControl = OutputControl(write_to_output=False)
        problem_to_solve:MaxFunction1VariableProblem = MaxFunction1VariableProblem.from_input_file(
                input_file_path='./opt/single_objective/teaching/function_1_variable_maximization/inputs/7-x^2f-3t3.txt',
                input_format='txt')
        print('Problem: {}'.format(problem_to_solve))            
        solution:MaxFunction1VariableProblemIntSolution = MaxFunction1VariableProblemIntSolution(
                problem_to_solve.domain_low, problem_to_solve.domain_up, 100 )
        solution.init_random()
        print('Solution: {}'.format(solution))
        obj = solution.calculate_quality_directly()            

if __name__ == '__main__':
        main()