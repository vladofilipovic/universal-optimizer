from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl

from uo.algorithm.exact.total_enumeration.te_operations_support_bit_array import \
        TeOperationsSupportBitArray
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizerConstructionParameters
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizer

from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_bit_array_solution import OnesCountMaxProblemBitArraySolution

def main():
        problem_to_solve:OnesCountMaxProblem = OnesCountMaxProblem.from_dimension(dimension=10)
        solution:OnesCountMaxProblemBitArraySolution = OnesCountMaxProblemBitArraySolution()
        te_support:TeOperationsSupportBitArray[str] = TeOperationsSupportBitArray[str]()
        construction_params:TeOptimizerConstructionParameters = TeOptimizerConstructionParameters()
        construction_params.problem = problem_to_solve
        construction_params.solution_template = solution
        construction_params.te_operations_support = te_support
        optimizer:TeOptimizer = TeOptimizer.from_construction_tuple(construction_params)
        bs = optimizer.optimize()
        print('Best solution representation: {}'.format(bs.representation.bin))            
        print('Best solution code: {}'.format(bs.string_representation()))            
        print('Best solution objective: {}'.format(bs.objective_value))
        print('Best solution fitness: {}'.format(bs.fitness_value))
        print('Number of iterations: {}'.format(optimizer.iteration))            
        print('Number of evaluations: {}'.format(optimizer.evaluation))            

if __name__ == '__main__':
        main()
