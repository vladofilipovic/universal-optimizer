from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.trivial.max_ones_problem.max_ones_problem import MaxOnesProblem
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_bit_array_solution import MaxOnesProblemBinaryBitArraySolution
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_bit_array_solution_vns_support import MaxOnesProblemBinaryBitArraySolutionVnsSupport

problem_to_solve:MaxOnesProblem = MaxOnesProblem(dim=22)
initial_solution:MaxOnesProblemBinaryBitArraySolution = MaxOnesProblemBinaryBitArraySolution()
initial_solution.random_init(problem_to_solve)
vns_support:MaxOnesProblemBinaryBitArraySolutionVnsSupport = MaxOnesProblemBinaryBitArraySolutionVnsSupport()
optimizer:VnsOptimizer = VnsOptimizer(output_control=OutputControl(write_to_output=false),
        target_problem=problem_to_solve, 
        initial_solution=initial_solution, 
        problem_solution_vns_support=vns_support,
        evaluations_max=500, 
        seconds_max=0, 
        random_seed=None, 
        keep_all_solution_codes=False, 
        k_min=1, 
        k_max=3, 
        max_local_optima=10, 
        local_search_type='local_search_best_improvement')
optimizer.representation_distance_cache_cs.is_caching = False
optimizer.optimize()
print('Best solution representation: {}'.format(optimizer.best_solution.representation.tobytes()))            
print('Best solution code: {}'.format(optimizer.best_solution.string_representation()))            
print('Best solution fitness: {}'.format(optimizer.best_solution.fitness_value))
print('Number of iterations: {}'.format(optimizer.iteration))            
print('Number of evaluations: {}'.format(optimizer.evaluation))            

