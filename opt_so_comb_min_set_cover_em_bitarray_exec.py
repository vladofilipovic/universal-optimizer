from random import randint
from random import choice
from random import randint
import random
import numpy as np

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl

from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_direction_support_one_point_bit_array import \
                EmDirectionSupportOnePointBitArray
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_attraction_support_one_point_bit_array import \
                EmAttractionSupportOnePointBitArray
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_mutation_support_one_point_bit_array import \
                EmMutationSupportOnePointBitArray
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_direction_support_one_point_bit_array import \
                EmDirectionSupportOnePointBitArray
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_optimizer_gen import EmOptimizerGenerational

from opt.single_objective.comb.min_set_cover_problem.min_set_cover_problem import MinSetCoverProblem
from opt.single_objective.comb.min_set_cover_problem.min_set_cover_problem_bit_array_solution import \
        MinSetCoverProblemBitArraySolution
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_optimizer import EmOptimizerConstructionParameters

def main():
        n = randint(0, 500)
        universe_set = set(np.linspace(0, n, n + 1))

        universe_list = list(universe_set)
        universe_set_integer = set()
        for i in range(len(universe_list)):
                universe_set_integer.add(int(universe_list[i]))
        universe_list = list(universe_set_integer)

        m = randint(1, 50)
        subsets = []

        for i in range(len(universe_set_integer)):
                subsets.append({i})

        for i in range(m):
            number_of_elements = randint(1, n)
            random.shuffle(universe_list)
            subset = set(universe_list[0:number_of_elements])
            subsets.append(subset)

        problem_to_solve:MinSetCoverProblem = MinSetCoverProblem(universe_set, subsets)
        solution:MinSetCoverProblemBitArraySolution = MinSetCoverProblemBitArraySolution()
        finish:FinishControl = FinishControl(criteria='iterations', iterations_max=100)
        em_attraction_support:EmAttractionSupportOnePointBitArray[str] = \
                EmAttractionSupportOnePointBitArray[str]()
        em_mut_support:EmMutationSupportOnePointBitArray[str] = \
                EmMutationSupportOnePointBitArray(mutation_probability=0.05)
        em_dir_support:EmDirectionSupportOnePointBitArray[str] = \
                EmDirectionSupportOnePointBitArray[str]()
        em_construction_params:EmOptimizerConstructionParameters = \
                EmOptimizerConstructionParameters()
        em_construction_params.problem = problem_to_solve
        em_construction_params.solution_template = solution
        em_construction_params.finish_control = finish
        em_construction_params.em_attraction_support = em_attraction_support
        em_construction_params.em_mutation_support = em_mut_support
        em_construction_params.em_direction_support = em_dir_support
        em_construction_params.random_seed = 43434343
        em_construction_params.population_size = 10
        optimizer:EmOptimizerGenerational = EmOptimizerGenerational.from_construction_tuple(em_construction_params)
        optimizer.optimize()

        #print('Best solution representation: {}'.format(optimizer.best_solution.representation.bin))
        print('Best solution code: {}'.format(optimizer.best_solution.string_representation()))
        print('Best solution objective: {}'.format(optimizer.best_solution.objective_value))
        print('Best solution fitness: {}'.format(optimizer.best_solution.fitness_value))
        print('Number of iterations: {}'.format(optimizer.iteration))
        print('Number of evaluations: {}'.format(optimizer.evaluation))

if __name__ == '__main__':
        main()