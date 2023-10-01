from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl

from uo.algorithm.exact.total_enumeration.te_optimizer_constructor_parameters import TeOptimizerConstructionParameters
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizer

from opt.single_objective.trivial.max_ones_problem.max_ones_problem import MaxOnesProblem
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_bit_array_solution import MaxOnesProblemBinaryBitArraySolution
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_bit_array_solution_te_support import MaxOnesProblemBinaryBitArraySolutionTeSupport

def main():
        output_control:OutputControl = OutputControl(write_to_output=False)
        problem_to_solve:MaxOnesProblem = MaxOnesProblem(dim=10)
        solution:MaxOnesProblemBinaryBitArraySolution = MaxOnesProblemBinaryBitArraySolution()
        te_support:MaxOnesProblemBinaryBitArraySolutionTeSupport = MaxOnesProblemBinaryBitArraySolutionTeSupport()
        construction_params:TeOptimizerConstructionParameters = TeOptimizerConstructionParameters()
        construction_params.output_control = output_control
        construction_params.target_problem = problem_to_solve
        construction_params.initial_solution = solution
        construction_params.problem_solution_te_support = te_support
        optimizer:TeOptimizer = TeOptimizer.from_construction_tuple(construction_params)
        optimizer.optimize()
        print('Best solution representation: {}'.format(optimizer.best_solution.representation.bin))            
        print('Best solution code: {}'.format(optimizer.best_solution.string_representation()))            
        print('Best solution objective: {}'.format(optimizer.best_solution.objective_value))
        print('Best solution fitness: {}'.format(optimizer.best_solution.fitness_value))
        print('Number of iterations: {}'.format(optimizer.iteration))            
        print('Number of evaluations: {}'.format(optimizer.evaluation))            

if __name__ == '__main__':
        main()
