from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import \
                VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.teaching.ones_count_problem.ones_count_problem import OnesCountProblem
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_binary_int_solution import \
                OnesCountProblemBinaryIntSolution
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_binary_int_solution_vns_support import \
                OnesCountProblemBinaryIntSolutionVnsSupport

def main():
        problem_to_solve:OnesCountProblem = OnesCountProblem.from_dimension(dimension=24)
        solution:OnesCountProblemBinaryIntSolution = OnesCountProblemBinaryIntSolution()
        finish:FinishControl = FinishControl(criteria='evaluations & seconds', evaluations_max=500, seconds_max=10)
        vns_support:OnesCountProblemBinaryIntSolutionVnsSupport = OnesCountProblemBinaryIntSolutionVnsSupport()
        output_control:OutputControl = OutputControl(write_to_output=False)
        additional_statistics_control:AdditionalStatisticsControl = AdditionalStatisticsControl(keep='')
        vns_construction_params:VnsOptimizerConstructionParameters = VnsOptimizerConstructionParameters()
        vns_construction_params.output_control = output_control
        vns_construction_params.target_problem = problem_to_solve
        vns_construction_params.solution_template = solution
        vns_construction_params.problem_solution_vns_support = vns_support
        vns_construction_params.finish_control = finish
        vns_construction_params.random_seed = 43434343
        vns_construction_params.additional_statistics_control = additional_statistics_control
        vns_construction_params.k_min = 1
        vns_construction_params.k_max = 3
        vns_construction_params.local_search_type = 'local_search_best_improvement'
        optimizer:VnsOptimizer = VnsOptimizer.from_construction_tuple(vns_construction_params)
        optimizer.optimize()
        print('Best solution representation: {}'.format(optimizer.best_solution.representation))            
        print('Best solution code: {}'.format(optimizer.best_solution.string_representation()))            
        print('Best solution objective:  {}'.format(optimizer.best_solution.objective_value))
        print('Best solution fitness: {}'.format(optimizer.best_solution.fitness_value))
        print('Number of iterations: {}'.format(optimizer.iteration))            
        print('Number of evaluations: {}'.format(optimizer.evaluation))            

if __name__ == '__main__':
        main()

