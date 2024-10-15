
import unittest   
import unittest.mock as mocker

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


class TestIntegrationMaxOnesCountProblemGaBitArraySolution(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestMaxOnesCountProblemGaBitArraySolution\n")

    def setUp(self):
        self.problem_to_solve:MaxOnesCountProblem = MaxOnesCountProblem.from_dimension(dimension=7)
        self.solution:MaxOnesCountProblemBitArraySolution = MaxOnesCountProblemBitArraySolution()
        self.finish:FinishControl = FinishControl(criteria='evaluations', evaluations_max=5000)
        self.ga_selection:GaSelectionRoulette = GaSelectionRoulette()
        self.ga_crossover_support:GaCrossoverSupportOnePointBitArray[str]= \
                GaCrossoverSupportOnePointBitArray[str](crossover_probability=0.95)
        self.ga_mutation_support:GaMutationSupportOnePointBitArray = \
                GaMutationSupportOnePointBitArray[str](mutation_probability=0.0005)
        self.ga_construction_params:GaOptimizerGenerationalConstructionParameters = \
                GaOptimizerGenerationalConstructionParameters()
        self.ga_construction_params.problem = self.problem_to_solve
        self.ga_construction_params.solution_template = self.solution
        self.ga_construction_params.finish_control = self.finish
        self.ga_construction_params.ga_selection = self.ga_selection
        self.ga_construction_params.ga_crossover_support = self.ga_crossover_support
        self.ga_construction_params.ga_mutation_support = self.ga_mutation_support
        self.ga_construction_params.random_seed = 43434343
        self.ga_construction_params.population_size = 100
        self.ga_construction_params.elite_count = 10
        seed(self.ga_construction_params.random_seed)
        self.optimizer:GaOptimizerGenerational = GaOptimizerGenerational.from_construction_tuple(
            self.ga_construction_params)
        self.bs = self.optimizer.optimize()

    def test_returned_best_solution_is_equal_to_optimizer_best_solution(self):
        self.assertEqual(self.bs.string_representation(), self.optimizer.best_solution.string_representation())

    def test_best_solution_after_optimization_should_be_optimal(self):
        result:str = '1111111'
        self.assertEqual(self.bs.string_representation(), result)

    def test_best_solution_after_optimization_should_have_optimal_fitness(self):
        self.assertEqual(self.optimizer.best_solution.fitness_value, self.problem_to_solve.dimension)

    def test_best_solution_after_optimization_should_have_optimal_objective_value(self):
        self.assertEqual(self.optimizer.best_solution.objective_value, self.problem_to_solve.dimension)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestMaxOnesCountProblemGaBitArraySolution")
    
if __name__ == '__main__':
    unittest.main()