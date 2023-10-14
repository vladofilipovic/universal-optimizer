from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent.parent.parent.parent)

import unittest   
import unittest.mock as mock

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer 
from uo.algorithm.metaheuristic.variable_neighborhood_search.problem_solution_vns_support import \
    ProblemSolutionVnsSupport

class TestVnsOptimizerProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestVnsOptimizerProperties\n")

    def setUp(self):
        self.output_control = mock.MagicMock()
        type(self.output_control).write_to_output = False

        self.problem = mock.MagicMock()
        type(self.problem).name = mock.PropertyMock(return_value='some_problem')
        type(self.problem).is_minimization = mock.PropertyMock(return_value=True)
        type(self.problem).file_path = mock.PropertyMock(return_value='some file path')
        type(self.problem).dimension = mock.PropertyMock(return_value=42)

        self.evaluations_max = 42
        self.iterations_max = 42
        self.seconds_max = 42
        self.finish_control = mock.MagicMock()
        type(self.finish_control).evaluations_max= mock.PropertyMock(return_value=self.evaluations_max)
        type(self.finish_control).iterations_max= mock.PropertyMock(return_value=self.iterations_max)
        type(self.finish_control).seconds_max= mock.PropertyMock(return_value=self.seconds_max)
        
        self.random_seed = 42
        self.k_min = 3
        self.k_max = 42

        self.vns_optimizer = VnsOptimizer(
                output_control=self.output_control,
                target_problem=self.problem, 
                initial_solution=None,
                problem_solution_vns_support=None, 
                finish_control=self.finish_control,
                random_seed=self.random_seed, 
                k_min=self.k_min, 
                k_max=self.k_max, 
                additional_statistics_control=None,
                local_search_type='first_improvement'
        )
        return
    
    def test_name_should_be_vns(self):
        self.assertEqual(self.vns_optimizer.name, 'vns')

    def test_evaluations_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.finish_control.evaluations_max, self.evaluations_max)

    def test_iterations_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.finish_control.iterations_max, self.iterations_max)

    def test_random_seed_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.random_seed, self.random_seed)

    def test_seconds_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.finish_control.seconds_max, self.seconds_max)

    def test_k_min_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.k_min, self.k_min)

    def test_k_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.k_max, self.k_max)

    def test_problem_name_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.target_problem.name, self.problem.name)

    def test_problem_is_minimization_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.target_problem.is_minimization, self.problem.is_minimization)

    def test_problem_file_path_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.target_problem.file_path, self.problem.file_path)

    def test_problem_dimension_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.target_problem.dimension, self.problem.dimension)

    def test_create_with_invalid_local_search_type_should_raise_value_exception_with_proper_message(self):
        with self.assertRaises(ValueError) as context:
            vns_support = mock.MagicMock(spec=ProblemSolutionVnsSupport)
            type(vns_support).local_search_best_improvement = mock.CallableMixin(spec=lambda x: x)
            type(vns_support).local_search_first_improvement= mock.CallableMixin(spec=lambda x: x)
            type(vns_support).copy = mock.CallableMixin(spec="return self")
            vns_optimizer:VnsOptimizer = VnsOptimizer(
                output_control=self.output_control,
                target_problem=self.problem, 
                initial_solution=None,
                problem_solution_vns_support=vns_support, 
                finish_control=self.finish_control,
                random_seed=self.random_seed, 
                k_min=self.k_min, 
                k_max=self.k_max, 
                additional_statistics_control=None,
                local_search_type='xxx'
            )            
        self.assertEqual("Value 'xxx' for VNS local_search_type is not supported", context.exception.args[0])

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestVnsOptimizerProperties")
    
if __name__ == '__main__':
    unittest.main()