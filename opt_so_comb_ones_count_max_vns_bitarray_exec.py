from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support_standard_bit_array import \
        VnsShakingSupportStandardBitArray
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support_standard_bi_bit_array import \
        VnsLocalSearchSupportStandardBestImprovementBitArray
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_bit_array_solution import \
                OnesCountMaxProblemBitArraySolution


def main():
        problem_dimension:int = 7
        problem_to_solve:OnesCountMaxProblem = OnesCountMaxProblem.from_dimension(dimension=problem_dimension)
        solution:OnesCountMaxProblemBitArraySolution = OnesCountMaxProblemBitArraySolution()
        finish:FinishControl = FinishControl(criteria='evaluations', evaluations_max=5000)
        vns_shaking_support:VnsShakingSupportStandardBitArray[str] = \
                VnsShakingSupportStandardBitArray[str](k_max=problem_dimension)
        vns_ls_support:VnsLocalSearchSupportStandardBestImprovementBitArray[str] = \
                VnsLocalSearchSupportStandardBestImprovementBitArray[str](k_max=problem_dimension)
        vns_construction_params:VnsOptimizerConstructionParameters = VnsOptimizerConstructionParameters()
        vns_construction_params.problem = problem_to_solve
        vns_construction_params.solution_template = solution
        vns_construction_params.finish_control = finish
        vns_construction_params.vns_shaking_support = vns_shaking_support
        vns_construction_params.vns_ls_support = vns_ls_support
        vns_construction_params.random_seed = 43434343
        vns_construction_params.k_min = 1
        vns_construction_params.k_max = 3
        vns_construction_params.local_search_type = 'localSearchBestImprovement'
        optimizer:VnsOptimizer = VnsOptimizer.from_construction_tuple(vns_construction_params)
        bs = optimizer.optimize()
        print('Best solution representation: {}'.format(bs.representation.bin))            
        print('Best solution code: {}'.format(bs.string_representation()))            
        print('Best solution objective: {}'.format(bs.objective_value))
        print('Best solution fitness: {}'.format(bs.fitness_value))
        print('Number of iterations: {}'.format(optimizer.iteration))            
        print('Number of evaluations: {}'.format(optimizer.evaluation))            

if __name__ == '__main__':
        main()
