from datetime import datetime
import unittest
import unittest.mock as mocker
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer_gen import GaOptimizerGenerational
from uo.algorithm.metaheuristic.genetic_algorithm.selection import Selection
from uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support import GaCrossoverSupport
from uo.algorithm.metaheuristic.genetic_algorithm.ga_mutation_support import GaMutationSupport

from uo.problem.problem_void_min_so import ProblemVoidMinSO
from uo.solution.solution_void_representation_int import SolutionVoidRepresentationInt


class TestGaOptimizerGenerational(unittest.TestCase):

    # GaOptimizerGenerational can be initialized with valid parameters
    def test_ga_optimizer_initialized_with_valid_parameters(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)
        selection_stub = mocker.MagicMock(spec=Selection)
        type(selection_stub).selection = mocker.CallableMixin(spec=lambda x: x)
        ga_crossover_support_stub = mocker.MagicMock(spec=GaCrossoverSupport)
        type(ga_crossover_support_stub).crossover = mocker.CallableMixin(spec=lambda x: x)
        ga_mutation_support_stub = mocker.MagicMock(spec=GaMutationSupport)
        type(ga_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        elitism_size = 10
        # Act
        ga_optimizer = GaOptimizerGenerational(finish_control, random_seed, additional_statistics_control, output_control, 
                    problem, solution_template, selection_stub, 
                    ga_crossover_support_stub, ga_mutation_support_stub, population_size, elitism_size)
        # Assert
        self.assertIsInstance(ga_optimizer, GaOptimizerGenerational)

    # GaOptimizerGenerational can be initialized with None for solution_template parameter
    def test_ga_optimizer_initialized_with_none_solution_template_2(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 0, 0, False)
        selection_stub = mocker.MagicMock(spec=Selection)
        type(selection_stub).selection = mocker.CallableMixin(spec=lambda x: x)
        ga_crossover_support_stub = mocker.MagicMock(spec=GaCrossoverSupport)
        type(ga_crossover_support_stub).crossover = mocker.CallableMixin(spec=lambda x: x)
        ga_mutation_support_stub = mocker.MagicMock(spec=GaMutationSupport)
        type(ga_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        elitism_size = 10
        # Act
        ga_optimizer = GaOptimizerGenerational(finish_control, random_seed, additional_statistics_control, output_control, 
                    problem, solution_template, selection_stub, 
                    ga_crossover_support_stub, ga_mutation_support_stub, population_size, elitism_size)
        # Assert
        self.assertIsInstance(ga_optimizer, GaOptimizerGenerational)

    # GaOptimizerGenerational can be initialized with None for random_seed parameter
    def test_ga_optimizer_initialized_with_none_random_seed(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = None
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 0, 0, False)
        selection_stub = mocker.MagicMock(spec=Selection)
        type(selection_stub).selection = mocker.CallableMixin(spec=lambda x: x)
        ga_crossover_support_stub = mocker.MagicMock(spec=GaCrossoverSupport)
        type(ga_crossover_support_stub).crossover = mocker.CallableMixin(spec=lambda x: x)
        ga_mutation_support_stub = mocker.MagicMock(spec=GaMutationSupport)
        type(ga_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        elitism_size = 10
        # Act
        ga_optimizer = GaOptimizerGenerational(finish_control, random_seed, additional_statistics_control, output_control, 
                    problem, solution_template, selection_stub, 
                    ga_crossover_support_stub, ga_mutation_support_stub, population_size, elitism_size)
        # Assert
        self.assertIsInstance(ga_optimizer, GaOptimizerGenerational)

    # GaOptimizerGenerational can not be initialized without GaCrossoverSupport parameter
    def test_ga_optimizer_initialized_without_ga_crossover_support(self):
        finish_control = FinishControl()
        random_seed = 123
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = None
        selection_stub = mocker.MagicMock(spec=Selection)
        type(selection_stub).selection = mocker.CallableMixin(spec=lambda x: x)
        ga_crossover_support_stub = None
        ga_mutation_support_stub = mocker.MagicMock(spec=GaMutationSupport)
        type(ga_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        elitism_size = 10
        # Act & Assert
        with self.assertRaises(TypeError):
            GaOptimizerGenerational(finish_control, random_seed, additional_statistics_control, output_control, 
                    problem, solution_template, selection_stub, 
                    ga_crossover_support_stub, ga_mutation_support_stub, population_size, elitism_size)

    # GaOptimizerGenerational can successfully execute init
    def test_ga_optimizer_init(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = None
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)
        selection_stub = mocker.MagicMock(spec=Selection)
        type(selection_stub).selection = mocker.CallableMixin(spec=lambda x: x)
        ga_crossover_support_stub = mocker.MagicMock(spec=GaCrossoverSupport)
        type(ga_crossover_support_stub).crossover = mocker.CallableMixin(spec=lambda x: x)
        ga_mutation_support_stub = mocker.MagicMock(spec=GaMutationSupport)
        type(ga_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        elitism_size = 10
        ga_optimizer = GaOptimizerGenerational(finish_control, random_seed, additional_statistics_control, output_control, 
                    problem, solution_template, selection_stub, 
                    ga_crossover_support_stub, ga_mutation_support_stub, population_size, elitism_size)
        # Act
        ga_optimizer.execution_started = datetime.now()
        ga_optimizer.init()
        # Assert
        # Add assertions here
        self.assertEqual( ga_optimizer.evaluation, 1)

    # GaOptimizerGenerational can successfully execute copy
    def test_copy(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = None
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)
        selection_stub = mocker.MagicMock(spec=Selection)
        type(selection_stub).selection = mocker.CallableMixin(spec=lambda x: x)
        ga_crossover_support_stub = mocker.MagicMock(spec=GaCrossoverSupport)
        type(ga_crossover_support_stub).crossover = mocker.CallableMixin(spec=lambda x: x)
        ga_mutation_support_stub = mocker.MagicMock(spec=GaMutationSupport)
        type(ga_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        elitism_size = 10
        ga_optimizer = GaOptimizerGenerational(finish_control, random_seed, additional_statistics_control, output_control, 
                    problem, solution_template, selection_stub, 
                    ga_crossover_support_stub, ga_mutation_support_stub, population_size, elitism_size)
        # Act
        copied_optimizer = ga_optimizer.copy()
        # Assert
        self.assertIsNot(ga_optimizer, copied_optimizer)
        self.assertEqual(ga_optimizer.random_seed, copied_optimizer.random_seed)
        self.assertEqual(ga_optimizer.finish_control.criteria, copied_optimizer.finish_control.criteria)

    # GaOptimizerGenerational raises TypeError if finish_control parameter is not of type FinishControl
    def test_finish_control_type_error(self):
        # Arrange
        finish_control = "not a FinishControl"
        random_seed = 123
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)
        selection_stub = mocker.MagicMock(spec=Selection)
        type(selection_stub).selection = mocker.CallableMixin(spec=lambda x: x)
        ga_crossover_support_stub = mocker.MagicMock(spec=GaCrossoverSupport)
        type(ga_crossover_support_stub).crossover = mocker.CallableMixin(spec=lambda x: x)
        ga_mutation_support_stub = mocker.MagicMock(spec=GaMutationSupport)
        type(ga_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        elitism_size = 10
        # Act & Assert
        with self.assertRaises(TypeError):
            GaOptimizerGenerational(finish_control, random_seed, additional_statistics_control, output_control, 
                    problem, solution_template, selection_stub, 
                    ga_crossover_support_stub, ga_mutation_support_stub, population_size, elitism_size)

    # GaOptimizerGenerational raises TypeError if random_seed parameter is not of type Optional[int]
    def test_random_seed_type_error(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = "not an int"
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)
        selection_stub = mocker.MagicMock(spec=Selection)
        type(selection_stub).selection = mocker.CallableMixin(spec=lambda x: x)
        ga_crossover_support_stub = mocker.MagicMock(spec=GaCrossoverSupport)
        type(ga_crossover_support_stub).crossover = mocker.CallableMixin(spec=lambda x: x)
        ga_mutation_support_stub = mocker.MagicMock(spec=GaMutationSupport)
        type(ga_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        elitism_size = 10
        # Act & Assert
        with self.assertRaises(TypeError):
            GaOptimizerGenerational(finish_control, random_seed, additional_statistics_control, output_control, 
                    problem, solution_template, selection_stub, 
                    ga_crossover_support_stub, ga_mutation_support_stub, population_size, elitism_size)

    # GaOptimizerGenerational raises TypeError if additional_statistics_control parameter is not of type AdditionalStatisticsControl
    def test_additional_statistics_control_type_error(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        additional_statistics_control = "not a valid type"
        output_control = OutputControl()
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)
        selection_stub = mocker.MagicMock(spec=Selection)
        type(selection_stub).selection = mocker.CallableMixin(spec=lambda x: x)
        ga_crossover_support_stub = mocker.MagicMock(spec=GaCrossoverSupport)
        type(ga_crossover_support_stub).crossover = mocker.CallableMixin(spec=lambda x: x)
        ga_mutation_support_stub = mocker.MagicMock(spec=GaMutationSupport)
        type(ga_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        elitism_size = 10
        # Act & Assert
        with self.assertRaises(TypeError):
            GaOptimizerGenerational(finish_control, random_seed, additional_statistics_control, output_control, 
                    problem, solution_template, selection_stub, 
                    ga_crossover_support_stub, ga_mutation_support_stub, population_size, elitism_size)

    # GaOptimizerGenerational raises TypeError if solution_template parameter is not of type Optional[Solution]
    def test_solution_template_parameter_type_error(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = "not a Solution"        
        selection_stub = mocker.MagicMock(spec=Selection)
        type(selection_stub).selection = mocker.CallableMixin(spec=lambda x: x)
        ga_crossover_support_stub = mocker.MagicMock(spec=GaCrossoverSupport)
        type(ga_crossover_support_stub).crossover = mocker.CallableMixin(spec=lambda x: x)
        ga_mutation_support_stub = mocker.MagicMock(spec=GaMutationSupport)
        type(ga_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        elitism_size = 10
        # Act & Assert
        with self.assertRaises(TypeError):
            GaOptimizerGenerational(finish_control, random_seed, additional_statistics_control, output_control, 
                    problem, solution_template, selection_stub, 
                    ga_crossover_support_stub, ga_mutation_support_stub, population_size, elitism_size)

    # GaOptimizerGenerational raises TypeError if ga_crossover_support parameter is not of type GaCrossoverSupport
    def test_ga_crossover_support_parameter_type_error(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)        
        selection_stub = mocker.MagicMock(spec=Selection)
        type(selection_stub).selection = mocker.CallableMixin(spec=lambda x: x)
        ga_crossover_support_stub = "not appropriate type"
        ga_mutation_support_stub = mocker.MagicMock(spec=GaMutationSupport)
        type(ga_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        elitism_size = 10
        # Act & Assert
        with self.assertRaises(TypeError):
            GaOptimizerGenerational(finish_control, random_seed, additional_statistics_control, output_control, 
                    problem, solution_template, selection_stub, 
                    ga_crossover_support_stub, ga_mutation_support_stub, population_size, elitism_size)

    # GaOptimizerGenerational raises TypeError if population_size parameter is not of type int
    def test_population_size_parameter_type_error(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        additional_statistics_control = AdditionalStatisticsControl()
        output_control = OutputControl()
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)         
        selection_stub = mocker.MagicMock(spec=Selection)
        type(selection_stub).selection = mocker.CallableMixin(spec=lambda x: x)
        ga_crossover_support_stub = mocker.MagicMock(spec=GaCrossoverSupport)
        type(ga_crossover_support_stub).crossover = mocker.CallableMixin(spec=lambda x: x)
        ga_mutation_support_stub = mocker.MagicMock(spec=GaMutationSupport)
        type(ga_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100.2
        elitism_size = 10
        # Act & Assert
        with self.assertRaises(TypeError):
            GaOptimizerGenerational(finish_control, random_seed, additional_statistics_control, output_control, 
                    problem, solution_template, selection_stub, 
                    ga_crossover_support_stub, ga_mutation_support_stub, population_size, elitism_size)

