from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl

from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizerConstructionParameters
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizer

from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_binary_bit_array_solution import OnesCountMaxProblemBinaryBitArraySolution
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_binary_bit_array_solution_te_support import OnesCountMaxProblemBinaryBitArraySolutionTeSupport

def main():
        output_control:OutputControl = OutputControl(write_to_output=False)
        problem_to_solve:OnesCountMaxProblem = OnesCountMaxProblem.from_dimension(dimension=10)
        solution:OnesCountMaxProblemBinaryBitArraySolution = OnesCountMaxProblemBinaryBitArraySolution()
        te_support:OnesCountMaxProblemBinaryBitArraySolutionTeSupport = OnesCountMaxProblemBinaryBitArraySolutionTeSupport()
        construction_params:TeOptimizerConstructionParameters = TeOptimizerConstructionParameters()
        construction_params.output_control = output_control
        construction_params.target_problem = problem_to_solve
        construction_params.solution_template = solution
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
