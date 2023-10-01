from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer_constructor_parameters import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.trivial.max_ones_problem.max_ones_problem import MaxOnesProblem
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_bit_array_solution import MaxOnesProblemBinaryBitArraySolution
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_bit_array_solution_vns_support import MaxOnesProblemBinaryBitArraySolutionVnsSupport

def main():
        output_control:OutputControl = OutputControl(write_to_output=False)
        problem_to_solve:MaxOnesProblem = MaxOnesProblem(dim=24)
        solution:MaxOnesProblemBinaryBitArraySolution = MaxOnesProblemBinaryBitArraySolution()
        vns_support:MaxOnesProblemBinaryBitArraySolutionVnsSupport = MaxOnesProblemBinaryBitArraySolutionVnsSupport()
        vns_construction_params:VnsOptimizerConstructionParameters = VnsOptimizerConstructionParameters()
        vns_construction_params.output_control = output_control
        vns_construction_params.target_problem = problem_to_solve
        vns_construction_params.initial_solution = solution
        vns_construction_params.problem_solution_vns_support = vns_support
        vns_construction_params.evaluations_max = 500
        vns_construction_params.iterations_max = 0
        vns_construction_params.seconds_max= 0
        vns_construction_params.random_seed = 43434343
        vns_construction_params.keep_all_solution_codes = False
        vns_construction_params.distance_calculation_cache_is_used = False
        vns_construction_params.k_min = 1
        vns_construction_params.k_max = 3
        vns_construction_params.max_local_optima = 10
        vns_construction_params.local_search_type = 'local_search_best_improvement'
        optimizer:VnsOptimizer = VnsOptimizer.from_construction_tuple(vns_construction_params)
        optimizer.optimize()
        print('Best solution representation: ' + str(optimizer.best_solution.representation.bin))            
        print('Best solution code: ' + str(optimizer.best_solution.string_representation()))            
        print('Best solution fitness: ' + str(optimizer.best_solution.fitness_value))
        print('Number of iterations: ' + str(optimizer.iteration))            
        print('Number of evaluations: ' + str(optimizer.evaluation))            

if __name__ == '__main__':
        main()
