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

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.metaheuristic import Metaheuristic 

class MetaheuristicVoid(Metaheuristic):
    def __init__(self, 
            name:str, 
            evaluations_max:int, 
            iterations_max:int,
            seconds_max:int, 
            random_seed:int, 
            keep_all_solution_codes:bool,
            distance_calculation_cache_is_used:bool,
            output_control:OutputControl, 
            target_problem:TargetProblem
    )->None:
        super().__init__(
                name=name, 
                evaluations_max=evaluations_max,
                iterations_max=iterations_max,
                seconds_max=seconds_max,
                random_seed=random_seed,
                keep_all_solution_codes=keep_all_solution_codes,
                output_control=output_control, 
                target_problem=target_problem
        )

    def __copy__(self):
        return super().__copy__()

    def copy(self):
        return self.__copy__()

    def init(self):
        return
    def __str__(self)->str:
        return super().__str__()

    def __repr__(self)->str:
        return super().__repr__()

    def __format__(self, spec:str)->str:
        return super().__format__()


class TestMetaheuristicProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestMetaheuristicProperties\n")

    def setUp(self):
        self.metaheuristicName = 'Name of the metaheuristic'
        self.evaluations_max = 42
        self.iterations_max = 42
        self.seconds_max = 42
        self.random_seed = 42

        self.output_control = mock.MagicMock()
        type(self.output_control).write_to_output = False

        self.problem = mock.MagicMock()
        type(self.problem).name = mock.PropertyMock(return_value='some_problem')
        type(self.problem).is_minimization = mock.PropertyMock(return_value=True)
        type(self.problem).file_path = mock.PropertyMock(return_value='some file path')
        type(self.problem).dimension = mock.PropertyMock(return_value=42)

        self.optimizer = MetaheuristicVoid(
                name=self.name,
                evaluations_max=self.evaluations_max,
                iterations_max=self.iterations_max, 
                seconds_max=self.seconds_max, 
                random_seed=self.random_seed, 
                keep_all_solution_codes=True, 
                output_control=self.output_control,
                target_problem=self.problem
        )
        return
    
    def test_name_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.optimizer.name, self.metaheuristicName)

    def test_evaluations_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.evaluations_max, self.evaluations_max)

    def test_iterations_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.iterations_max, self.iterations_max)

    def test_seconds_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.seconds_max, self.seconds_max)

    def test_random_seed_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.vns_optimizer.random_seed, self.random_seed)

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
        print("\ntearDownClass TestMetaheuristicProperties")
    
if __name__ == '__main__':
    unittest.main()