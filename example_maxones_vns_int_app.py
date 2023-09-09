from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from app.max_ones_problem.max_ones_problem import MaxOnesProblem
from app.max_ones_problem.max_ones_problem_binary_int_solution import MaxOnesProblemBinaryIntSolution
from app.max_ones_problem.max_ones_problem_binary_int_solution_vns_support import MaxOnesProblemBinaryIntSolutionVnsSupport

problem_to_solve:MaxOnesProblem = MaxOnesProblem(dim=10)
initial_solution:MaxOnesProblemBinaryIntSolution = MaxOnesProblemBinaryIntSolution()
initial_solution.random_init(problem_to_solve)
vns_support:MaxOnesProblemBinaryIntSolutionVnsSupport = MaxOnesProblemBinaryIntSolutionVnsSupport()
optimizer:VnsOptimizer = VnsOptimizer(target_problem=problem_to_solve, 
        initial_solution=initial_solution, 
        problem_solution_vns_support=vns_support,
        evaluations_max=0, 
        seconds_max=10, 
        random_seed=None, 
        keep_all_solution_codes=False, 
        k_min=1, 
        k_max=3, 
        max_local_optima=10, 
        local_search_type='local_search_best_improvement')
optimizer.solution_code_distance_cache_cs.is_caching = False
optimizer.output_control.write_to_output_file = False
optimizer.optimize()
print('Best solution: {}'.format(optimizer.best_solution.solution_code()))            
print('Best solution fitness: {}'.format(optimizer.best_solution.fitness_value))
print('Number of iterations: {}'.format(optimizer.iteration))            

