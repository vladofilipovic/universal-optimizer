from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.trivial.max_ones_problem.max_ones_problem import MaxOnesProblem
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_int_solution import MaxOnesProblemBinaryIntSolution
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_int_solution_vns_support import MaxOnesProblemBinaryIntSolutionVnsSupport

def main():
        problem_to_solve:MaxOnesProblem = MaxOnesProblem(dim=24)
        solution:MaxOnesProblemBinaryIntSolution = MaxOnesProblemBinaryIntSolution()
        vns_support:MaxOnesProblemBinaryIntSolutionVnsSupport = MaxOnesProblemBinaryIntSolutionVnsSupport()
        output_control:OutputControl = OutputControl(write_to_output=False)
        optimizer:VnsOptimizer = VnsOptimizer(output_control=output_control,
                target_problem=problem_to_solve, 
                initial_solution=solution,
                problem_solution_vns_support=vns_support,
                evaluations_max=500, 
                iterations_max=0,
                seconds_max=0, 
                random_seed=None, 
                keep_all_solution_codes=False, 
                distance_calculation_cache_is_used=False,
                k_min=1, 
                k_max=3, 
                max_local_optima=10, 
                local_search_type='local_search_best_improvement')
        optimizer.optimize()
        print('Best solution representation: {}'.format(optimizer.best_solution.representation))            
        print('Best solution code: {}'.format(optimizer.best_solution.string_representation()))            
        print('Best solution fitness: {}'.format(optimizer.best_solution.fitness_value))
        print('Number of iterations: {}'.format(optimizer.iteration))            
        print('Number of evaluations: {}'.format(optimizer.evaluation))            

if __name__ == '__main__':
        main()
