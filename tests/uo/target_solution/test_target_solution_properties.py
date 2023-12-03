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

from copy import deepcopy

from uo.target_problem.target_problem import TargetProblem 
from uo.target_solution.target_solution import QualityOfSolution
from uo.target_solution.target_solution import TargetSolution 


class TargetSolutionVoid(TargetSolution[int, str]):
    
    def __init__(self, name:str, random_seed:int, fitness_value:float, 
            objective_value:float, is_feasible:bool, 
            evaluation_cache_is_used:bool=False, 
            evaluation_cache_max_size:int=0,
            distance_calculation_cache_is_used:bool=False,
            distance_calculation_cache_max_size:int=0)->None:
        super().__init__(name, random_seed=random_seed, 
                fitness_value=fitness_value, fitness_values=[], 
                objective_value=objective_value, objective_values=[],
                is_feasible=is_feasible, 
                evaluation_cache_is_used=evaluation_cache_is_used,
                evaluation_cache_max_size=evaluation_cache_max_size,
                distance_calculation_cache_is_used=distance_calculation_cache_is_used,
                distance_calculation_cache_max_size=distance_calculation_cache_is_used)

    def __copy__(self):
        pr = deepcopy(self)
        return pr

    def copy(self):
        return self.__copy__()

    def copy_to(self, destination)->None:
        destination =  copy(self)

    def argument(self, representation:int)->str:
        return "42"

    def init_random(self, problem:TargetProblem)->None:
        self.representation = 42
        return

    def init_from(self, representation:int, problem:TargetProblem)->None:
        self.representation = 42

    def native_representation(self, representation_str:str)->int:
        return 42

    def calculate_quality_directly(self, representation:int, 
            problem:TargetProblem)->QualityOfSolution:
        return QualityOfSolution(42, None, 42, None, True)

    def representation_distance_directly(solution_code_1:str, solution_code_2:str)->float:
        return 42.0

    def __str__(self)->str:
        return super().__str__()

    def __repr__(self)->str:
        return super().__repr__()

    def __format__(self, spec:str)->str:
        return super().__format__()    

class TestTargetSolutionProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestTargetSolutionProperties\n")

    def setUp(self):       
        self.solution_name = "void solution"
        self.random_seed = 42
        self.fitness_value = 42.0
        self.objective_value = -42.0
        self.is_feasible = True
        self.solution = TargetSolutionVoid(name=self.solution_name, 
                random_seed=self.random_seed,
                fitness_value=self.fitness_value,
                objective_value=self.objective_value,
                is_feasible= self.is_feasible
        )
        return
    
    def test_solution_name_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.solution.name, self.solution_name)

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