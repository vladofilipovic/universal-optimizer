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

class TestVnSOptimizerProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestVnSOptimizerProperties\n")

    def setUp(self):
        self.evaluations_max = 42

        self.problem = mock.MagicMock()
        type(self.problem).name = mock.PropertyMock(return_value='some_problem')
        type(self.problem).is_minimization = mock.PropertyMock(return_value=True)
        type(self.problem).file_path = mock.PropertyMock(return_value='some file path')
        type(self.problem).dimension = mock.PropertyMock(return_value=42)

        self.vns_optimizer = VnsOptimizer(evaluations_max=self.evaluations_max, seconds_max=42, random_seed=42, 
                keep_all_solution_codes=True, target_problem=self.problem, initial_solution=None, 
                problem_solution_vns_support=None, k_min=3, k_max=42, max_local_optima=42, 
                local_search_type='first_improvement')
        return
    
    def test_name_should_be_vns(self):
        self.assertEqual(self.vns_optimizer.name, 'vns')

    def test_evaluation_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.evaluations_max, self.evaluations_max)

    def test_problem_name_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.target_problem.name, self.problem.name)

    def test_problem_is_minimization_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.target_problem.is_minimization, self.problem.is_minimization)

    def test_problem_file_path_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.target_problem.file_path, self.problem.file_path)

    def test_problem_dimension_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.target_problem.dimension, self.problem.dimension)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestVnSOptimizerProperties")
    
if __name__ == '__main__':
    unittest.main()