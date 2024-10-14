from random import seed

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl

from uo.algorithm.metaheuristic.genetic_algorithm.ga_selection_roulette import GaSelectionRoulette
from uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support_one_point_bit_array import \
                GaCrossoverSupportOnePointBitArray
from uo.algorithm.metaheuristic.genetic_algorithm.ga_mutation_support_one_point_bit_array import \
                GaMutationSupportOnePointBitArray
from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer_gen import GaOptimizerGenerationalConstructionParameters
from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer_gen import GaOptimizerGenerational

from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem import MaxOnesCountProblem
from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem_bit_array_solution import \
                MaxOnesCountProblemBitArraySolution

def main():
        problem_to_solve:MaxOnesCountProblem = MaxOnesCountProblem.from_dimension(dimension=7)
        solution:MaxOnesCountProblemBitArraySolution = MaxOnesCountProblemBitArraySolution()
        finish:FinishControl = FinishControl(criteria='evaluations', evaluations_max=5000)
        ga_selection:GaSelectionRoulette = GaSelectionRoulette()
        ga_crossover_support:GaCrossoverSupportOnePointBitArray[str]= \
                GaCrossoverSupportOnePointBitArray[str](crossover_probability=0.95)
        ga_mutation_support:GaMutationSupportOnePointBitArray = \
                GaMutationSupportOnePointBitArray[str](mutation_probability=0.0005)
        ga_construction_params:GaOptimizerGenerationalConstructionParameters = \
                GaOptimizerGenerationalConstructionParameters()
        ga_construction_params.problem = problem_to_solve
        ga_construction_params.solution_template = solution
        ga_construction_params.finish_control = finish
        ga_construction_params.ga_selection = ga_selection
        ga_construction_params.ga_crossover_support = ga_crossover_support
        ga_construction_params.ga_mutation_support = ga_mutation_support
        ga_construction_params.random_seed = 43434343
        ga_construction_params.population_size = 100
        ga_construction_params.elite_count = 10
        seed(ga_construction_params.random_seed)
        optimizer:GaOptimizerGenerational = GaOptimizerGenerational.from_construction_tuple(ga_construction_params)
        bs = optimizer.optimize()
        print('Best solution representation: {}'.format(bs.representation.bin))            
        print('Best solution code: {}'.format(bs.string_representation()))            
        print('Best solution objective: {}'.format(bs.objective_value))
        print('Best solution fitness: {}'.format(bs.fitness_value))
        print('Number of iterations: {}'.format(optimizer.iteration))            
        print('Number of evaluations: {}'.format(optimizer.evaluation))            

if __name__ == '__main__':
        main()
