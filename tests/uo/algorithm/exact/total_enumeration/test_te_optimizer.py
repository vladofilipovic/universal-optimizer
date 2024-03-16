import unittest   
import unittest.mock as mocker

from copy import deepcopy
from datetime import datetime
from uo.problem.problem_void import ProblemVoid
from uo.solution.solution_void import SolutionVoid

from uo.utils.logger import logger

from uo.problem.problem import Problem
from uo.solution.quality_of_solution import QualityOfSolution 
from uo.solution.solution import Solution
from uo.algorithm.output_control import OutputControl
from uo.algorithm.exact.total_enumeration.problem_solution_te_support import ProblemSolutionTeSupport 
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizer, TeOptimizerConstructionParameters

class TestTeOptimizerProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestTeOptimizerProperties\n")

    def setUp(self):       

        self.oc_write_to_output = True
        self.oc_output_file = "some file path..."
        self.output_control_stub = mocker.MagicMock(spec=OutputControl)
        type(self.output_control_stub).write_to_output = self.oc_write_to_output
        type(self.output_control_stub).output_file = self.oc_output_file

        self.pr_name = 'some_problem'
        self.pr_is_minimization = True
        self.pr_file_path = 'some problem file path'
        self.pr_dimension = 42
        self.problem_stub = mocker.MagicMock(spec=Problem)
        type(self.problem_stub).name = mocker.PropertyMock(return_value=self.pr_name)
        type(self.problem_stub).is_minimization = mocker.PropertyMock(return_value=self.pr_is_minimization)
        type(self.problem_stub).file_path = mocker.PropertyMock(return_value=self.pr_file_path)
        type(self.problem_stub).dimension = mocker.PropertyMock(return_value=self.pr_dimension)


        self.solution_name = "void solution"
        self.random_seed = 42
        self.fitness_value = 42.0
        self.objective_value = -42.0
        self.is_feasible = True
        self.solution_mock = mocker.MagicMock(spec=Solution)
        type(self.solution_mock).name = self.solution_name, 
        type(self.solution_mock).random_seed = self.random_seed,
        type(self.solution_mock).fitness_value=self.fitness_value,
        type(self.solution_mock).objective_value=self.objective_value,
        type(self.solution_mock).is_feasible= self.is_feasible
        
        self.te_support_stub = mocker.MagicMock(spec=ProblemSolutionTeSupport)

        self.te_optimizer = TeOptimizer(output_control=self.output_control_stub,
                problem=self.problem_stub,
                solution_template= self.solution_mock,
                problem_solution_te_support=self.te_support_stub )
    
    def test_is_feasible_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.solution_mock.is_feasible, self.is_feasible)

    def test_fitness_value_should_be_equal_as_value_set_by_property_setter(self):
        val:float = 42.1
        self.solution_mock.fitness_value = val
        self.assertEqual(self.solution_mock.fitness_value, val)

    def test_fitness_value_should_be_equal_as_value_set_by_property_setter_2(self):
        val:int = 11
        self.solution_mock.fitness_value = val
        self.assertEqual(self.solution_mock.fitness_value, val)

    def test_objective_value_should_be_equal_as_value_set_by_property_setter(self):
        val:float = 43.1
        self.solution_mock.objective_value = val
        self.assertEqual(self.solution_mock.objective_value, val)

    def test_is_feasible_should_be_equal_as_value_set_by_property_setter(self):
        val:bool = False
        self.solution_mock.is_feasible = val
        self.assertEqual(self.solution_mock.is_feasible, val)

    def test_is_feasible_should_be_equal_as_value_set_by_property_setter_2(self):
        val:bool = True
        self.solution_mock.is_feasible = val
        self.assertEqual(self.solution_mock.is_feasible, val)

    def test_representation_should_be_equal_as_value_set_by_property_setter(self):
        val:int = 42
        self.solution_mock.representation =  val
        self.assertEqual(self.solution_mock.representation, val)

    def test_representation_should_be_equal_as_value_set_by_property_setter_2(self):
        val:int = -7
        self.solution_mock.representation =  val
        self.assertEqual(self.solution_mock.representation, val)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestTeOptimizerProperties")

class TestTeOptimizerMethodInit(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestTeOptimizerMethodInit\n")

    def setUp(self):       
        self.oc_write_to_output = False
        self.oc_output_file = "some file path..."
        self.output_control_stub = mocker.MagicMock(spec=OutputControl)
        type(self.output_control_stub).write_to_output = self.oc_write_to_output
        type(self.output_control_stub).output_file = self.oc_output_file
        self.pr_name = 'some_problem'
        self.pr_is_minimization = True
        self.pr_file_path = 'some .problem_mock file path'
        self.pr_dimension = 42
        self.problem_mock = mocker.MagicMock(spec=Problem)
        type(self.problem_mock).name = mocker.PropertyMock(return_value=self.pr_name)
        type(self.problem_mock).is_minimization = mocker.PropertyMock(return_value=self.pr_is_minimization)
        type(self.problem_mock).file_path = mocker.PropertyMock(return_value=self.pr_file_path)
        type(self.problem_mock).dimension = mocker.PropertyMock(return_value=self.pr_dimension)
        self.problem_mock.copy = mocker.Mock(return_value=self.problem_mock)
        self.solution_name = "void solution"
        self.random_seed = 42
        self.fitness_value = 42.0
        self.objective_value = -42.0
        self.is_feasible = True
        self.solution_mock = mocker.MagicMock(spec=Solution)
        type(self.solution_mock).name = self.solution_name, 
        type(self.solution_mock).random_seed = self.random_seed,
        type(self.solution_mock).fitness_value=self.fitness_value,
        type(self.solution_mock).objective_value=self.objective_value,
        type(self.solution_mock).is_feasible= self.is_feasible
        self.solution_mock.evaluate = mocker.Mock(return_value='evaluate')
        self.solution_mock.copy = mocker.Mock(return_value=self.solution_mock)
        self.te_support = mocker.MagicMock(spec=ProblemSolutionTeSupport)
        self.te_support.reset = mocker.Mock(return_value='reset')
        self.te_optimizer = TeOptimizer(output_control=self.output_control_stub,
                problem=self.problem_mock,
                solution_template= self.solution_mock,
                problem_solution_te_support=self.te_support )
    
    def test_init_method_should_evaluate_solution_template_once(self):
        self.te_optimizer.execution_started = datetime.now()
        self.te_optimizer.init()
        self.solution_mock.evaluate.assert_called_once()

    def test_init_method_should_evaluate_solution_template_once_with_supplied_problem(self):
        self.te_optimizer.execution_started = datetime.now()
        self.te_optimizer.init()
        self.solution_mock.evaluate.assert_called_once_with(self.problem_mock)

    def test_init_method_should_call_support_method_reset_once(self):
        self.te_optimizer.execution_started = datetime.now()
        self.te_optimizer.init()
        self.te_support.reset.assert_called_once()

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestTeOptimizerMethodInit")
    

class TestOptimize(unittest.TestCase):

    # initializes execution_started property
    def test_initializes_execution_started_property(self):
        # Arrange
        output_control = OutputControl()
        problem_mock = mocker.MagicMock(spec=Problem)
        type(problem_mock).name = mocker.PropertyMock(return_value='some_problem')
        type(problem_mock).is_minimization = mocker.PropertyMock(return_value=True)
        type(problem_mock).is_multi_objective = mocker.PropertyMock(return_value=False)
        type(problem_mock).file_path = mocker.PropertyMock(return_value='some .problem_mock file path')
        type(problem_mock).dimension = mocker.PropertyMock(return_value=42)
        problem_mock.copy = mocker.Mock(return_value=problem_mock)
        solution_mock = mocker.MagicMock(spec=Solution)
        type(solution_mock).random_seed = 42,
        type(solution_mock).fitness_value=42.0,
        type(solution_mock).objective_value=42.0,
        type(solution_mock).is_feasible= True
        solution_mock.calculate_quality = mocker.Mock(return_value=QualityOfSolution(42, None, 42, None, True))
        type(solution_mock).quality_single = mocker.PropertyMock(return_value=QualityOfSolution(42, None, 42, None, True))
        solution_mock.evaluate = mocker.Mock(return_value='evaluate')
        solution_mock.copy =  mocker.Mock(return_value=solution_mock)
        te_support_mock = mocker.MagicMock(spec=ProblemSolutionTeSupport)
        te_support_mock.reset = mocker.Mock(return_value='reset')
        te_support_mock.can_progress = mocker.Mock(return_value=False)
        te_optimizer = TeOptimizer(output_control, problem_mock, solution_mock, te_support_mock)
        # Act
        bs = te_optimizer.optimize()
        # Assert
        self.assertIsNotNone(te_optimizer.execution_started)
        
    # # calls init method
    # def test_calls_init_method(self):
    #     # Arrange
    #     output_control = OutputControl()
    #     problem_mock = mocker.MagicMock(spec=Problem)
    #     type(problem_mock).name = mocker.PropertyMock(return_value='some_problem')
    #     type(problem_mock).is_minimization = mocker.PropertyMock(return_value=True)
    #     type(problem_mock).file_path = mocker.PropertyMock(return_value='some .problem_mock file path')
    #     type(problem_mock).dimension = mocker.PropertyMock(return_value=42)
    #     problem_mock.copy = mocker.Mock(return_value=problem_mock)
    #     solution_mock = mocker.MagicMock(spec=Solution)
    #     type(solution_mock).random_seed = 42,
    #     type(solution_mock).fitness_value=42.0,
    #     type(solution_mock).objective_value=42.0,
    #     type(solution_mock).is_feasible= True
    #     solution_mock.calculate_quality = mocker.Mock(return_value=QualityOfSolution(42, None, 42, None, True))
    #     type(solution_mock).quality_single = mocker.PropertyMock(return_value=QualityOfSolution(42, None, 42, None, True))
    #     solution_mock.evaluate = mocker.Mock(return_value='evaluate')
    #     solution_mock.copy =  mocker.Mock(return_value=solution_mock)
    #     te_support_mock = mocker.MagicMock(spec=ProblemSolutionTeSupport)
    #     te_support_mock.reset = mocker.Mock(return_value='reset')
    #     te_support_mock.can_progress = mocker.Mock(return_value=False)
    #     te_optimizer = TeOptimizer(output_control, problem_mock, solution_mock, te_support_mock)
    #     te_optimizer.init = mocker.Mock(return_value='init')
    #     # Act
    #     bs = te_optimizer.optimize()
    #     # Assert
    #     te_optimizer.init.assert_called_once()

    # logs overall number of evaluations
    def test_logs_overall_number_of_evaluations(self):
        # Arrange
        output_control = OutputControl()
        problem_mock = mocker.MagicMock(spec=Problem)
        type(problem_mock).name = mocker.PropertyMock(return_value='some_problem')
        type(problem_mock).is_minimization = mocker.PropertyMock(return_value=True)
        type(problem_mock).is_multi_objective = mocker.PropertyMock(return_value=False)
        type(problem_mock).file_path = mocker.PropertyMock(return_value='some .problem_mock file path')
        type(problem_mock).dimension = mocker.PropertyMock(return_value=42)
        problem_mock.copy = mocker.Mock(return_value=problem_mock)
        solution_mock = mocker.MagicMock(spec=Solution)
        type(solution_mock).name = "void solution", 
        type(solution_mock).random_seed = 42,
        type(solution_mock).fitness_value=42.0,
        type(solution_mock).objective_value=42.0,
        type(solution_mock).is_feasible= True
        solution_mock.calculate_quality = mocker.Mock(return_value=QualityOfSolution(42, None, 42, None, True))
        type(solution_mock).quality_single = mocker.PropertyMock(return_value=QualityOfSolution(42, None, 42, None, True))
        solution_mock.evaluate = mocker.Mock(return_value='evaluate')
        solution_mock.copy =  mocker.Mock(return_value=solution_mock)
        te_support_mock = mocker.MagicMock(spec=ProblemSolutionTeSupport)
        te_support_mock.reset = mocker.Mock(return_value='reset')
        te_support_mock.can_progress = mocker.Mock(return_value=False)
        te_optimizer = TeOptimizer(output_control, problem_mock, solution_mock, te_support_mock)       
        te_optimizer.write_output_values_if_needed = mocker.Mock(return_value='write_output_values_if_needed')
        logger.debug = mocker.MagicMock(spec=logger.debug)
        # Act
        bs = te_optimizer.optimize()
        # Assert
        logger.debug.assert_called_once_with('Overall number of evaluations: {}'.format(
            te_support_mock.overall_number_of_evaluations(problem_mock, solution_mock, te_optimizer)))

    # writes output headers if needed
    def test_writes_output_headers_if_needed(self):
        # Arrange
        output_control = OutputControl()
        problem_mock = mocker.MagicMock(spec=Problem)
        type(problem_mock).name = mocker.PropertyMock(return_value='some_problem')
        type(problem_mock).is_minimization = mocker.PropertyMock(return_value=True)
        type(problem_mock).is_multi_objective = mocker.PropertyMock(return_value=False)
        type(problem_mock).file_path = mocker.PropertyMock(return_value='some .problem_mock file path')
        type(problem_mock).dimension = mocker.PropertyMock(return_value=42)
        problem_mock.copy = mocker.Mock(return_value=problem_mock)
        solution_mock = mocker.MagicMock(spec=Solution)
        type(solution_mock).name = "void solution", 
        type(solution_mock).random_seed = 42,
        type(solution_mock).fitness_value=42.0,
        type(solution_mock).objective_value=42.0,
        type(solution_mock).is_feasible= True
        solution_mock.calculate_quality = mocker.Mock(return_value=QualityOfSolution(42, None, 42, None, True))
        type(solution_mock).quality_single = mocker.PropertyMock(return_value=QualityOfSolution(42, None, 42, None, True))
        solution_mock.evaluate = mocker.Mock(return_value='evaluate')
        solution_mock.copy =  mocker.Mock(return_value=solution_mock)
        te_support_mock = mocker.MagicMock(spec=ProblemSolutionTeSupport)
        te_support_mock.reset = mocker.Mock(return_value='reset')
        te_support_mock.can_progress = mocker.Mock(return_value=False)
        te_optimizer = TeOptimizer(output_control, problem_mock, solution_mock, te_support_mock)       
        te_optimizer.write_output_headers_if_needed = mocker.Mock(return_value='write_output_headers_if_needed')
        # Act
        bs = te_optimizer.optimize()
        # Assert
        te_optimizer.write_output_headers_if_needed.assert_called_once()

    # output_control parameter is not an instance of OutputControl
    def test_output_control_parameter_not_instance_of_OutputControl(self):
        # Arrange
        output_control = "not an instance of OutputControl"
        problem_mock = mocker.MagicMock(spec=Problem)
        type(problem_mock).name = mocker.PropertyMock(return_value='some_problem')
        type(problem_mock).is_minimization = mocker.PropertyMock(return_value=True)
        type(problem_mock).file_path = mocker.PropertyMock(return_value='some .problem_mock file path')
        type(problem_mock).dimension = mocker.PropertyMock(return_value=42)
        problem_mock.copy = mocker.Mock(return_value=problem_mock)
        solution_mock = mocker.MagicMock(spec=Solution)
        type(solution_mock).name = "void solution", 
        type(solution_mock).random_seed = 42,
        type(solution_mock).fitness_value=42.0,
        type(solution_mock).objective_value=42.0,
        type(solution_mock).is_feasible= True
        solution_mock.calculate_quality = mocker.Mock(return_value=QualityOfSolution(42, None, 42, None, True))
        solution_mock.evaluate = mocker.Mock(return_value='evaluate')
        solution_mock.copy =  mocker.Mock(return_value=solution_mock)
        te_support_mock = mocker.MagicMock(spec=ProblemSolutionTeSupport)
        te_support_mock.reset = mocker.Mock(return_value='reset')
        te_support_mock.can_progress = mocker.Mock(return_value=False)
        # Act & Assert
        with self.assertRaises(TypeError):
            TeOptimizer(output_control, problem_mock, solution_mock, te_support_mock)

    # problem parameter is not an instance of Problem
    def test_problem_parameter_not_instance_of_Problem(self):
        # Arrange
        output_control = OutputControl()
        problem = 'not an instance of Problem'
        solution_mock = mocker.MagicMock(spec=Solution)
        type(solution_mock).name = "void solution", 
        type(solution_mock).random_seed = 42,
        type(solution_mock).fitness_value=42.0,
        type(solution_mock).objective_value=42.0,
        type(solution_mock).is_feasible= True
        solution_mock.calculate_quality = mocker.Mock(return_value=QualityOfSolution(42, None, 42, None, True))
        solution_mock.evaluate = mocker.Mock(return_value='evaluate')
        solution_mock.copy =  mocker.Mock(return_value=solution_mock)
        te_support_mock = mocker.MagicMock(spec=ProblemSolutionTeSupport)
        te_support_mock.reset = mocker.Mock(return_value='reset')
        te_support_mock.can_progress = mocker.Mock(return_value=False)
        # Act & Assert
        with self.assertRaises(TypeError):
            TeOptimizer(output_control, problem, solution_mock, te_support_mock)

    # solution_template parameter is not an instance of Solution
    def test_solution_template_parameter_not_instance_of_Solution(self):
        # Arrange
        output_control = OutputControl()
        problem_mock = mocker.MagicMock(spec=Problem)
        type(problem_mock).name = mocker.PropertyMock(return_value='some_problem')
        type(problem_mock).is_minimization = mocker.PropertyMock(return_value=True)
        type(problem_mock).file_path = mocker.PropertyMock(return_value='some .problem_mock file path')
        type(problem_mock).dimension = mocker.PropertyMock(return_value=42)
        problem_mock.copy = mocker.Mock(return_value=problem_mock)
        solution_template = "not an instance of Solution"
        te_support_mock = mocker.MagicMock(spec=ProblemSolutionTeSupport)
        te_support_mock.reset = mocker.Mock(return_value='reset')
        te_support_mock.can_progress = mocker.Mock(return_value=False)
        # Act & Assert
        with self.assertRaises(TypeError):
            TeOptimizer(output_control, problem_mock, solution_template, te_support_mock)

    # problem_solution_te_support parameter is not an instance of ProblemSolutionTeSupport
    def test_problem_solution_te_support_parameter_not_instance_of_ProblemSolutionTeSupport(self):
        # Arrange
        output_control = OutputControl()
        problem_mock = mocker.MagicMock(spec=Problem)
        type(problem_mock).name = mocker.PropertyMock(return_value='some_problem')
        type(problem_mock).is_minimization = mocker.PropertyMock(return_value=True)
        type(problem_mock).file_path = mocker.PropertyMock(return_value='some .problem_mock file path')
        type(problem_mock).dimension = mocker.PropertyMock(return_value=42)
        problem_mock.copy = mocker.Mock(return_value=problem_mock)
        solution_mock = mocker.MagicMock(spec=Solution)
        type(solution_mock).name = "void solution", 
        type(solution_mock).random_seed = 42,
        type(solution_mock).fitness_value=42.0,
        type(solution_mock).objective_value=42.0,
        type(solution_mock).is_feasible= True
        solution_mock.calculate_quality = mocker.Mock(return_value=QualityOfSolution(42, None, 42, None, True))
        solution_mock.evaluate = mocker.Mock(return_value='evaluate')
        solution_mock.copy =  mocker.Mock(return_value=solution_mock)
        problem_solution_te_support = "not an instance of ProblemSolutionTeSupport"
        # Act & Assert
        with self.assertRaises(TypeError):
            TeOptimizer(output_control, problem_mock, solution_mock, problem_solution_te_support)


class TestStringRep(unittest.TestCase):

    # Returns a string representation of the 'TeOptimizer' instance with the current solution included
    def test_returns_string_representation_with_current_solution(self):
        # Arrange
        output_control = OutputControl()
        problem = ProblemVoid("problem name", True)
        solution_template = SolutionVoid(42, 42.0, 42.0, True)
        te_support_mock = mocker.MagicMock(spec=ProblemSolutionTeSupport)
        te_optimizer = TeOptimizer(output_control, problem, solution_template, te_support_mock)
        # Act
        result = te_optimizer.string_rep('|')
        # Assert
        self.assertIsInstance(result, str)

    # Uses the specified delimiter, indentation, indentation symbol, group start and group end
    def test_uses_specified_parameters(self):
        # Arrange
        output_control = OutputControl()
        problem = ProblemVoid("problem name", True)
        solution_template = SolutionVoid(42, 42.0, 42.0, True)
        te_support_mock = mocker.MagicMock(spec=ProblemSolutionTeSupport)
        te_optimizer = TeOptimizer(output_control, problem, solution_template, te_support_mock)
        delimiter = ','
        indentation = 2
        indentation_symbol = '-'
        group_start = '['
        group_end = ']'
        # Act
        result = te_optimizer.string_rep(delimiter, indentation, indentation_symbol, group_start, group_end)
        # Assert
        self.assertIsInstance(result, str)
        self.assertEqual(result[0], indentation_symbol)

    # Returns a string representation of the 'TeOptimizer' instance with default parameters when all parameters are not specified
    def test_returns_string_representation_with_default_parameters(self):
        # Arrange
        output_control = OutputControl()
        problem = ProblemVoid("problem name", True)
        solution_template = SolutionVoid(42, 42.0, 42.0, True)
        te_support_mock = mocker.MagicMock(spec=ProblemSolutionTeSupport)
        te_optimizer = TeOptimizer(output_control, problem, solution_template, te_support_mock)
        expected_result = '|solution_template=|'
        # Act
        result = te_optimizer.string_rep('|')
        # Assert
        self.assertIn(expected_result, result)

    # Returns a string representation of the 'TeOptimizer' instance with default parameters when only delimiter is specified
    def test_returns_string_representation_with_default_parameters_when_only_delimiter_is_specified(self):
        # Arrange
        output_control = OutputControl()
        problem = ProblemVoid("problem name", True)
        solution_template = SolutionVoid(42, 42.0, 42.0, True)
        te_support_mock = mocker.MagicMock(spec=ProblemSolutionTeSupport)
        te_optimizer = TeOptimizer(output_control, problem, solution_template, te_support_mock)
        delimiter = ','
        # Act
        result = te_optimizer.string_rep(delimiter)
        # Assert
        self.assertIn(delimiter, result)


class TestFromConstructionTuple(unittest.TestCase):

    # should create a new instance of TeOptimizer with the given construction parameters
    def test_create_new_instance_with_given_parameters(self):
        # Arrange
        construction_tuple = TeOptimizerConstructionParameters()
        construction_tuple.output_control = OutputControl()
        construction_tuple.problem = ProblemVoid("problem name", True)
        construction_tuple.solution_template = SolutionVoid(42, 42.0, 42.0, True)
        construction_tuple.problem_solution_te_support = mocker.MagicMock(spec=ProblemSolutionTeSupport)
        # Act
        te_optimizer = TeOptimizer.from_construction_tuple(construction_tuple)
        # Assert
        self.assertIsInstance(te_optimizer, TeOptimizer)
        self.assertEqual(te_optimizer.problem.name, construction_tuple.problem.name)
        self.assertEqual(te_optimizer.problem.is_minimization, construction_tuple.problem.is_minimization)
        self.assertEqual(te_optimizer.solution_template.random_seed, construction_tuple.solution_template.random_seed)
        self.assertEqual(te_optimizer.solution_template.fitness_value, construction_tuple.solution_template.fitness_value)
        self.assertEqual(te_optimizer.solution_template.objective_value, construction_tuple.solution_template.objective_value)
        self.assertEqual(te_optimizer.solution_template.is_feasible, construction_tuple.solution_template.is_feasible)

    # should return the created instance
    def test_return_created_instance(self):
        # Arrange
        construction_tuple = TeOptimizerConstructionParameters()
        construction_tuple.output_control = OutputControl()
        construction_tuple.problem = ProblemVoid("problem name", True)
        construction_tuple.solution_template = SolutionVoid(42, 42.0, 42.0, True)
        construction_tuple.problem_solution_te_support = mocker.MagicMock(spec=ProblemSolutionTeSupport)
        # Act
        te_optimizer = TeOptimizer.from_construction_tuple(construction_tuple)
        # Assert
        self.assertIsInstance(te_optimizer, TeOptimizer)

    # should raise a TypeError if output_control parameter is not an instance of OutputControl
    def test_raise_TypeError_if_output_control_not_instance_of_OutputControl(self):
        # Arrange
        construction_tuple = TeOptimizerConstructionParameters()
        construction_tuple.output_control = "not an instance of OutputControl"
        construction_tuple.problem = ProblemVoid("problem name", True)
        construction_tuple.solution_template = SolutionVoid(42, 42.0, 42.0, True)
        construction_tuple.problem_solution_te_support = mocker.MagicMock(spec=ProblemSolutionTeSupport)
        # Act & Assert
        with self.assertRaises(TypeError):
            TeOptimizer.from_construction_tuple(construction_tuple)

    # should raise a TypeError if problem parameter is not an instance of Problem
    def test_raise_TypeError_if_problem_not_instance_of_Problem(self):
        # Arrange
        construction_tuple = TeOptimizerConstructionParameters()
        construction_tuple.output_control = OutputControl()
        construction_tuple.problem = "not an instance of Problem"
        construction_tuple.solution_template = SolutionVoid(42, 42.0, 42.0, True)
        construction_tuple.problem_solution_te_support = mocker.MagicMock(spec=ProblemSolutionTeSupport)
        # Act & Assert
        with self.assertRaises(TypeError):
            TeOptimizer.from_construction_tuple(construction_tuple)

if __name__ == '__main__':
    unittest.main()
    
