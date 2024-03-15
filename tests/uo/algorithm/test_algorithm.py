
import unittest   
import unittest.mock as mocker

from copy import deepcopy

from uo.problem.problem import Problem
from uo.algorithm.output_control import OutputControl
from uo.algorithm.algorithm import Algorithm
from uo.algorithm.algorithm_void import AlgorithmVoid
from uo.problem.problem_void import ProblemVoid
from uo.solution.quality_of_solution import QualityOfSolution
from uo.solution.solution_void import SolutionVoid

class TestAlgorithmProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestAlgorithmProperties\n")

    def setUp(self):
        self.name = "some algorithm"
        self.evaluations_max = 42
        self.seconds_max = 42

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
        self.problem_stub.copy = mocker.Mock(return_value=self.problem_stub)

        self.algorithm = AlgorithmVoid(output_control=self.output_control_stub,
                name=self.name,
                problem=self.problem_stub 
        )


    def test_name_should_be_as_it_is_in_constructor(self):
        self.assertEqual(self.algorithm.name, self.name)

    def test_problem_name_should_be_same_that_it_is_in_constructor(self):
        self.assertEqual(self.algorithm.problem.name, self.pr_name)

    def test_problem_is_minimization_should_be_same_that_it_is_in_constructor(self):
        self.assertEqual(self.algorithm.problem.is_minimization, self.pr_is_minimization)

    def test_problem_file_path_should_be_same_that_it_is_in_constructor(self):
        self.assertEqual(self.algorithm.problem.file_path, self.pr_file_path)

    def test_problem_dimension_should_be_same_that_it_is_in_constructor(self):
        self.assertEqual(self.algorithm.problem.dimension, self.pr_dimension)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestAlgorithmProperties")
    
if __name__ == '__main__':
    unittest.main()
    

class TestAlgorithm(unittest.TestCase):

    # Algorithm can be initialized with a name, an OutputControl instance, and a Problem instance.
    def test_algorithm_initialization(self):
        # Arrange
        problem = ProblemVoid("problem", False)
        output_control = OutputControl(write_to_output=True, output_file=None, fields='iteration, evaluation', moments='after_algorithm')
        # Act
        algorithm = AlgorithmVoid(name='MyAlgorithm', output_control=output_control, problem=problem)
        # Assert
        self.assertEqual(algorithm.name, 'MyAlgorithm')
        self.assertEqual(algorithm.output_control.write_to_output, output_control.write_to_output)
        self.assertEqual(algorithm.output_control.output_file, output_control.output_file)
        self.assertEqual(algorithm.output_control.moments, output_control.moments)
        self.assertEqual(algorithm.problem.name, problem.name)
        self.assertEqual(algorithm.problem.is_minimization, problem.is_minimization)

    # Algorithm can be copied to create a new instance with the same properties.
    def test_algorithm_copy(self):
        # Arrange
        problem = ProblemVoid("problem", False)
        output_control = OutputControl(write_to_output=True, output_file=None, fields='iteration, evaluation', moments='after_algorithm')
        algorithm = AlgorithmVoid(name='MyAlgorithm', output_control=output_control, problem=problem)
        # Act
        algorithm_copy = algorithm.copy()
        # Assert
        self.assertIsNot(algorithm, algorithm_copy)
        self.assertEqual(algorithm.name, algorithm_copy.name)
        self.assertEqual(algorithm.output_control.write_to_output, output_control.write_to_output)
        self.assertEqual(algorithm.output_control.output_file, output_control.output_file)
        self.assertEqual(algorithm.output_control.moments, output_control.moments)
        self.assertEqual(algorithm.problem.name, problem.name)
        self.assertEqual(algorithm.problem.is_minimization, problem.is_minimization)

    # Algorithm has properties for current number of evaluations, iteration, and iteration when the best solution is found.
    def test_algorithm_properties(self):
        # Arrange
        problem = ProblemVoid("problem", False)
        output_control = OutputControl(write_to_output=True, output_file=None, fields='iteration, evaluation', moments='after_algorithm')
        algorithm = AlgorithmVoid(name='MyAlgorithm', output_control=output_control, problem=problem)
        # Act
        algorithm.evaluation = 100
        algorithm.iteration = 10
        algorithm.iteration_best_found = 5

        # Assert
        self.assertEqual(algorithm.evaluation, 100)
        self.assertEqual(algorithm.iteration, 10)
        self.assertEqual(algorithm.iteration_best_found, 5)

    # Raises a ValueError if the target problem is not defined within the metaheuristic.
    def test_problem_not_defined(self):
        # Arrange
        # Act & Assert
        with self.assertRaises(TypeError):
            algorithm = AlgorithmVoid(name="MyAlgorithm", output_control=OutputControl(), problem=None)

    # Algorithm can generate a string representation of itself.
    def test_algorithm_string_representation(self):
        # Arrange
        problem = ProblemVoid("problem", False)
        output_control = OutputControl(write_to_output=True, output_file=None, fields='iteration, evaluation', moments='after_algorithm')
        algorithm = AlgorithmVoid(name='MyAlgorithm', output_control=output_control, problem=problem)
        # Act
        string_rep = str(algorithm)
        # Assert
        self.assertIsInstance(string_rep, str)
        self.assertIn('name=MyAlgorithm', string_rep)
        self.assertIn('problem=', string_rep)
        self.assertIn('__evaluation=0', string_rep)
        self.assertIn('__iteration=0', string_rep)
    
class TestEvaluation(unittest.TestCase):

    # Set evaluation to a positive integer value
    def test_set_evaluation_positive_integer(self):
        # Arrange
        algorithm = AlgorithmVoid("MyAlgorithm", OutputControl(), ProblemVoid("problem", False))
        value = 10
        # Act
        algorithm.evaluation = value
        # Assert
        self.assertEqual(algorithm.evaluation, value)

    # Set evaluation to zero
    def test_set_evaluation_zero(self):
        # Arrange
        algorithm = AlgorithmVoid("MyAlgorithm", OutputControl(), ProblemVoid("problem", False))
        value = 0
        # Act
        algorithm.evaluation = value
        # Assert
        self.assertEqual(algorithm.evaluation, value)

    # Set evaluation to None
    def test_set_evaluation_none(self):
        # Arrange
        algorithm = AlgorithmVoid("MyAlgorithm", OutputControl(), ProblemVoid("problem", False))
        value = None
        # Act & Assert
        with self.assertRaises(TypeError):
            algorithm.evaluation = value

    # Set evaluation to a float value
    def test_set_evaluation_float_value(self):
        # Arrange
        algorithm = AlgorithmVoid("MyAlgorithm", OutputControl(), ProblemVoid("problem", False))
        value = 3.14
        # Act & Assert
        with self.assertRaises(TypeError):
            algorithm.evaluation = value
