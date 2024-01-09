
import unittest   
import unittest.mock as mocker

from copy import deepcopy

from uo.target_problem.target_problem import TargetProblem 

from uo.target_solution.quality_of_solution import QualityOfSolution
from uo.target_solution.target_solution import TargetSolution 
from uo.target_solution.target_solution_void import TargetSolutionVoid

class TestTargetSolutionProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestTargetSolutionProperties\n")

    def setUp(self):       
        self.random_seed = 42
        self.fitness_value = 42.0
        self.objective_value = -42.0
        self.is_feasible = True
        self.solution = TargetSolutionVoid( random_seed=self.random_seed,
                fitness_value=self.fitness_value,
                objective_value=self.objective_value,
                is_feasible= self.is_feasible
        )
    
    def test_fitness_value_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.solution.fitness_value, self.fitness_value)

    def test_objective_value_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.solution.objective_value, self.objective_value)

    def test_is_feasible_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.solution.is_feasible, self.is_feasible)

    def test_fitness_value_should_be_equal_as_value_set_by_property_setter(self):
        val:float = 42.1
        self.solution.fitness_value = val
        self.assertEqual(self.solution.fitness_value, val)

    def test_fitness_value_should_be_equal_as_value_set_by_property_setter_2(self):
        val:int = 11
        self.solution.fitness_value = val
        self.assertEqual(self.solution.fitness_value, val)

    def test_objective_value_should_be_equal_as_value_set_by_property_setter(self):
        val:float = 43.1
        self.solution.objective_value = val
        self.assertEqual(self.solution.objective_value, val)

    def test_is_feasible_should_be_equal_as_value_set_by_property_setter(self):
        val:bool = False
        self.solution.is_feasible = val
        self.assertEqual(self.solution.is_feasible, val)

    def test_is_feasible_should_be_equal_as_value_set_by_property_setter_2(self):
        val:bool = True
        self.solution.is_feasible = val
        self.assertEqual(self.solution.is_feasible, val)

    def test_representation_should_be_equal_as_value_set_by_property_setter(self):
        val:int = 42
        self.solution.representation =  val
        self.assertEqual(self.solution.representation, val)

    def test_representation_should_be_equal_as_value_set_by_property_setter_2(self):
        val:int = -7
        self.solution.representation =  val
        self.assertEqual(self.solution.representation, val)

    def test_evaluation_cache_cs_hit_count_should_be_zero_after_constructor(self):
        self.assertEqual(self.solution.evaluation_cache_cs.cache_hit_count, 0)

    def test_evaluation_cache_cs__request_count_should_be_zero_after_constructor(self):
        self.assertEqual(self.solution.evaluation_cache_cs.cache_request_count, 0)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestTargetSolutionProperties")
    
if __name__ == '__main__':
    unittest.main()