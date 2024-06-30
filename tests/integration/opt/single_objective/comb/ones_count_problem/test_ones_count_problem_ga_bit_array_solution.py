
import unittest   
import unittest.mock as mocker

from random import seed

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.genetic_algorithm.selection_roulette import SelectionRoulette
from uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support_rep_bit_array import \
                GaCrossoverSupportRepresentationBitArray
from uo.algorithm.metaheuristic.genetic_algorithm.ga_mutation_support_rep_bit_array import \
                GaMutationSupportRepresentationBitArray
from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer import GaOptimizerConstructionParameters
from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer import GaOptimizer

from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_bit_array_solution import \
                OnesCountMaxProblemBitArraySolution


class TestOnesCountMaxProblemGaBitArraySolution(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestOnesCountMaxProblemGaBitArraySolution\n")

    def setUp(self):
        self.output_control:OutputControl = OutputControl(write_to_output=False)
        self.problem_to_solve:OnesCountMaxProblem = OnesCountMaxProblem.from_dimension(dimension=7)
        self.solution:OnesCountMaxProblemBitArraySolution = OnesCountMaxProblemBitArraySolution()
        self.finish:FinishControl = FinishControl(criteria='evaluations', evaluations_max=5000)
        self.ga_selection:SelectionRoulette = SelectionRoulette()
        self.additional_statistics_control:AdditionalStatisticsControl = \
                AdditionalStatisticsControl(is_active=False, keep='')
        self.ga_crossover_support:GaCrossoverSupportRepresentationBitArray[str]= \
                GaCrossoverSupportRepresentationBitArray[str](crossover_probability=0.95)
        self.ga_mutation_support:GaMutationSupportRepresentationBitArray = \
                GaMutationSupportRepresentationBitArray[str](mutation_probability=0.0005)
        self.ga_construction_params:GaOptimizerConstructionParameters = GaOptimizerConstructionParameters()
        self.ga_construction_params.output_control = self.output_control
        self.ga_construction_params.problem = self.problem_to_solve
        self.ga_construction_params.solution_template = self.solution
        self.ga_construction_params.finish_control = self.finish
        self.ga_construction_params.ga_selection = self.ga_selection
        self.ga_construction_params.ga_crossover_support = self.ga_crossover_support
        self.ga_construction_params.ga_mutation_support = self.ga_mutation_support
        self.ga_construction_params.additional_statistics_control = self.additional_statistics_control
        self.ga_construction_params.random_seed = 43434343
        self.ga_construction_params.population_size = 100
        self.ga_construction_params.elite_count = 10
        seed(self.ga_construction_params.random_seed)
        self.optimizer:GaOptimizer = GaOptimizer.from_construction_tuple(self.ga_construction_params)
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
        print("\ntearDownClass TestOnesCountMaxProblemGaBitArraySolution")
    
if __name__ == '__main__':
    unittest.main()