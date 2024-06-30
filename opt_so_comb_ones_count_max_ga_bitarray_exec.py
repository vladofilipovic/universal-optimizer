from random import seed

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.genetic_algorithm.selection_roulette import SelectionRoulette
from uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support_one_point_rep_bit_array import \
                GaCrossoverSupportOnePointRepresentationBitArray
from uo.algorithm.metaheuristic.genetic_algorithm.ga_mutation_support_one_point_rep_bit_array import \
                GaMutationSupportOnePointRepresentationBitArray
from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer_gen import GaOptimizerGenerationalConstructionParameters
from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer_gen import GaOptimizerGenerational

from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_bit_array_solution import \
                OnesCountMaxProblemBitArraySolution

def main():
        output_control:OutputControl = OutputControl(write_to_output=False)
        problem_to_solve:OnesCountMaxProblem = OnesCountMaxProblem.from_dimension(dimension=7)
        solution:OnesCountMaxProblemBitArraySolution = OnesCountMaxProblemBitArraySolution()
        finish:FinishControl = FinishControl(criteria='evaluations', evaluations_max=5000)
        ga_selection:SelectionRoulette = SelectionRoulette()
        additional_statistics_control:AdditionalStatisticsControl = AdditionalStatisticsControl(is_active=False, keep='')
        ga_crossover_support:GaCrossoverSupportOnePointRepresentationBitArray[str]= \
                GaCrossoverSupportOnePointRepresentationBitArray[str](crossover_probability=0.95)
        ga_mutation_support:GaMutationSupportOnePointRepresentationBitArray = \
                GaMutationSupportOnePointRepresentationBitArray[str](mutation_probability=0.0005)
        ga_construction_params:GaOptimizerGenerationalConstructionParameters = \
                GaOptimizerGenerationalConstructionParameters()
        ga_construction_params.output_control = output_control
        ga_construction_params.problem = problem_to_solve
        ga_construction_params.solution_template = solution
        ga_construction_params.finish_control = finish
        ga_construction_params.ga_selection = ga_selection
        ga_construction_params.ga_crossover_support = ga_crossover_support
        ga_construction_params.ga_mutation_support = ga_mutation_support
        ga_construction_params.additional_statistics_control = additional_statistics_control
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
