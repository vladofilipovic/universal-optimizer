from copy import deepcopy
from random import randint
from random import choice

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.trivial.max_ones_problem.max_ones_problem import MaxOnesProblem
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_bit_array_solution import MaxOnesProblemBinaryBitArraySolution
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_bit_array_solution_vns_support import MaxOnesProblemBinaryBitArraySolutionVnsSupport

def main():
        problem_to_solve:MaxOnesProblem = MaxOnesProblem(dim=24)
        solution:MaxOnesProblemBinaryBitArraySolution = MaxOnesProblemBinaryBitArraySolution()
        vns_support:MaxOnesProblemBinaryBitArraySolutionVnsSupport = MaxOnesProblemBinaryBitArraySolutionVnsSupport()
        output_control:OutputControl = OutputControl(write_to_output=False)
        optimizer:VnsOptimizer = VnsOptimizer(output_control=output_control,
                target_problem=problem_to_solve, 
                initial_solution=solution,
                problem_solution_vns_support=vns_support,
                evaluations_max=500, 
                seconds_max=0, 
                random_seed=None, 
                keep_all_solution_codes=False,
                distance_calculation_cache_is_used=False,  
                k_min=1, 
                k_max=3, 
                max_local_optima=10, 
                local_search_type='local_search_best_improvement')
        optimizer.optimize()
        print('Best solution representation: ' + str(optimizer.best_solution.representation.bin))            
        print('Best solution code: ' + str(optimizer.best_solution.string_representation()))            
        print('Best solution fitness: ' + str(optimizer.best_solution.fitness_value))
        print('Number of iterations: ' + str(optimizer.iteration))            
        print('Number of evaluations: ' + str(optimizer.evaluation))            

if __name__ == '__main__':
        main()
