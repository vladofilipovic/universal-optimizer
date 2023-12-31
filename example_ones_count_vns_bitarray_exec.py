from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.teaching.ones_count_problem.ones_count_problem import OnesCountProblem
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_binary_bit_array_solution import \
                OnesCountProblemBinaryBitArraySolution
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_binary_bit_array_solution_vns_support import \
                OnesCountProblemBinaryBitArraySolutionVnsSupport

def main():
        output_control:OutputControl = OutputControl(write_to_output=False)
        problem_to_solve:OnesCountProblem = OnesCountProblem.from_dimension(dimension=24)
        solution:OnesCountProblemBinaryBitArraySolution = OnesCountProblemBinaryBitArraySolution()
        finish:FinishControl = FinishControl(criteria='evaluations', evaluations_max=5000)
        additional_statistics_control:AdditionalStatisticsControl = AdditionalStatisticsControl(keep='')
        vns_support:OnesCountProblemBinaryBitArraySolutionVnsSupport = OnesCountProblemBinaryBitArraySolutionVnsSupport()
        vns_construction_params:VnsOptimizerConstructionParameters = VnsOptimizerConstructionParameters()
        vns_construction_params.output_control = output_control
        vns_construction_params.target_problem = problem_to_solve
        vns_construction_params.solution_template = solution
        vns_construction_params.finish_control = finish
        vns_construction_params.problem_solution_vns_support = vns_support
        vns_construction_params.additional_statistics_control = additional_statistics_control
        vns_construction_params.random_seed = 43434343
        vns_construction_params.k_min = 1
        vns_construction_params.k_max = 3
        vns_construction_params.local_search_type = 'local_search_best_improvement'
        optimizer:VnsOptimizer = VnsOptimizer.from_construction_tuple(vns_construction_params)
        optimizer.optimize()
        print('Best solution representation: {}'.format(optimizer.best_solution.representation.bin))            
        print('Best solution code: {}'.format(optimizer.best_solution.string_representation()))            
        print('Best solution objective: {}'.format(optimizer.best_solution.objective_value))
        print('Best solution fitness: {}'.format(optimizer.best_solution.fitness_value))
        print('Number of iterations: {}'.format(optimizer.iteration))            
        print('Number of evaluations: {}'.format(optimizer.evaluation))            

if __name__ == '__main__':
        main()
