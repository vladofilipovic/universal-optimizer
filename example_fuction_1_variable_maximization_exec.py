from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl

from opt.single_objective.teaching.function_1_variable_maximization.function_1_variable_maximization import Function1VariableMaximization

def main():
        output_control:OutputControl = OutputControl(write_to_output=False)
        problem_to_solve:Function1VariableMaximization = Function1VariableMaximization.from_input_file(
                input_file_path='./opt/single_objective/teaching/function_1_variable_maximization/inputs/7-x^2f-3t3.txt',
                input_format='txt')
        print('Problem: {}'.format(problem_to_solve))            

if __name__ == '__main__':
        main()