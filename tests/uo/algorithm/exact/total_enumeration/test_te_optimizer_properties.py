import unittest   
import unittest.mock as mocker

from copy import deepcopy

from uo.target_problem.target_problem import TargetProblem 
from uo.target_solution.target_solution import TargetSolution
from uo.algorithm.output_control import OutputControl
from uo.algorithm.exact.total_enumeration.problem_solution_te_support import ProblemSolutionTeSupport 
from uo.algorithm.exact.total_enumeration.te_optimizer import TeOptimizer

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
        self.problem_stub = mocker.MagicMock(spec=TargetProblem)
        type(self.problem_stub).name = mocker.PropertyMock(return_value=self.pr_name)
        type(self.problem_stub).is_minimization = mocker.PropertyMock(return_value=self.pr_is_minimization)
        type(self.problem_stub).file_path = mocker.PropertyMock(return_value=self.pr_file_path)
        type(self.problem_stub).dimension = mocker.PropertyMock(return_value=self.pr_dimension)


        self.solution_name = "void solution"
        self.random_seed = 42
        self.fitness_value = 42.0
        self.objective_value = -42.0
        self.is_feasible = True
        self.solution_mock = mocker.MagicMock(spec=TargetSolution)
        type(self.solution_mock).name = self.solution_name, 
        type(self.solution_mock).random_seed = self.random_seed,
        type(self.solution_mock).fitness_value=self.fitness_value,
        type(self.solution_mock).objective_value=self.objective_value,
        type(self.solution_mock).is_feasible= self.is_feasible
        
        self.te_support_stub = mocker.MagicMock(spec=ProblemSolutionTeSupport)

        self.te_optimizer = TeOptimizer(output_control=self.output_control_stub,
                target_problem=self.problem_stub,
                initial_solution= self.solution_mock,
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
    
if __name__ == '__main__':
    unittest.main()