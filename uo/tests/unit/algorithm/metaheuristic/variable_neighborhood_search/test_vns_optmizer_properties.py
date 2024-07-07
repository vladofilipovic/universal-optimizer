import unittest   
import unittest.mock as mocker

from uo.problem.problem import Problem
from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer 
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support import VnsShakingSupport
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support import VnsLocalSearchSupport
from uo.solution.solution_void_representation_int import SolutionVoidInt

class TestVnsOptimizerProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestVnsOptimizerProperties\n")

    def setUp(self):
        self.output_control_stub = mocker.MagicMock(spec=OutputControl)

        self.problem_mock = mocker.MagicMock(spec=Problem)
        type(self.problem_mock).name = mocker.PropertyMock(return_value='some_problem')
        type(self.problem_mock).is_minimization = mocker.PropertyMock(return_value=True)
        type(self.problem_mock).file_path = mocker.PropertyMock(return_value='some file path')
        type(self.problem_mock).dimension = mocker.PropertyMock(return_value=42)
        self.problem_mock.copy = mocker.Mock(return_value=self.problem_mock)

        self.vns_shaking_support_stub = mocker.MagicMock(spec=VnsShakingSupport)
        type(self.vns_shaking_support_stub).copy = mocker.CallableMixin(spec="return self")        
        self.vns_ls_support_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
        self.vns_ls_support_stub.local_search_first_improvement = mocker.Mock(return_value="mocked stuff")
        type(self.vns_ls_support_stub).copy = mocker.CallableMixin(spec="return self")        
        
        self.evaluations_max = 42
        self.iterations_max = 42
        self.seconds_max = 42
        self.finish_control_mock = mocker.MagicMock(spec=FinishControl)
        type(self.finish_control_mock).evaluations_max= mocker.PropertyMock(return_value=self.evaluations_max)
        type(self.finish_control_mock).iterations_max= mocker.PropertyMock(return_value=self.iterations_max)
        type(self.finish_control_mock).seconds_max= mocker.PropertyMock(return_value=self.seconds_max)
        self.finish_control_mock.copy = mocker.Mock(return_value=self.finish_control_mock)
        
        self.random_seed = 42
        self.k_min = 3
        self.k_max = 42
                
        self.vns_optimizer = VnsOptimizer(
                output_control=self.output_control_stub,
                problem=self.problem_mock, 
                solution_template=SolutionVoidInt( 43, 0, 0, False),
                vns_shaking_support=self.vns_shaking_support_stub, 
                vns_ls_support=self.vns_ls_support_stub, 
                finish_control=self.finish_control_mock,
                random_seed=self.random_seed, 
                k_min=self.k_min, 
                k_max=self.k_max
        )
    
    def test_name_should_be_vns(self):
        self.assertEqual(self.vns_optimizer.name, 'vns')

    def test_evaluations_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.finish_control.evaluations_max, self.finish_control_mock.evaluations_max)

    def test_iterations_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.finish_control.iterations_max, self.finish_control_mock.iterations_max)

    def test_random_seed_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.random_seed, self.random_seed)

    def test_seconds_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.finish_control.seconds_max, self.finish_control_mock.seconds_max)

    def test_k_min_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.k_min, self.k_min)

    def test_k_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.k_max, self.k_max)

    def test_problem_name_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.problem.name, self.problem_mock.name)

    def test_problem_is_minimization_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.problem.is_minimization, self.problem_mock.is_minimization)

    def test_problem_file_path_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.problem.file_path, self.problem_mock.file_path)

    def test_problem_dimension_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.problem.dimension, self.problem_mock.dimension)

    def test_create_with_invalid_problem_type_should_raise_value_exception_with_proper_message(self):
        with self.assertRaises(TypeError) as context:
            problem = "invalid"
            vns_support_shaking_stub = mocker.MagicMock(spec=VnsShakingSupport)
            type(vns_support_shaking_stub).copy = mocker.CallableMixin(spec="return self")
            vns_support_local_search_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
            type(vns_support_local_search_stub).local_search_best_improvement = mocker.CallableMixin(spec=lambda x: x)
            type(vns_support_local_search_stub).local_search_first_improvement= mocker.CallableMixin(spec=lambda x: x)
            type(vns_support_local_search_stub).copy = mocker.CallableMixin(spec="return self")
            vns_optimizer:VnsOptimizer = VnsOptimizer(
                output_control=self.output_control_stub,
                problem=problem, 
                solution_template=SolutionVoidInt( 43, 0, 0, False),
                vns_shaking_support=vns_support_shaking_stub, 
                vns_ls_support=vns_support_local_search_stub,
                finish_control=self.finish_control_mock,
                random_seed=self.random_seed, 
                k_min=self.k_min, 
                k_max=self.k_max
            )            
        self.assertEqual("Parameter 'problem' must be 'Problem'.", context.exception.args[0])

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestVnsOptimizerProperties")
    
if __name__ == '__main__':
    unittest.main()