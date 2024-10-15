import unittest   
import unittest.mock as mocker

from uo.problem.problem import Problem


from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_optimizer_gen import EmOptimizerGenerational
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_attraction_support import EmAttractionSupport
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_direction_support import EmDirectionSupport
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_mutation_support import EmMutationSupport
from uo.solution.solution_void_representation_int import SolutionVoidInt

class TestEmOptimizerGenerationalProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestEmOptimizerGenerationalProperties\n")

    def setUp(self):
        self.output_control_stub = mocker.MagicMock(spec=OutputControl)

        self.problem_mock = mocker.MagicMock(spec=Problem)
        type(self.problem_mock).name = mocker.PropertyMock(return_value='some_problem')
        type(self.problem_mock).is_minimization = mocker.PropertyMock(return_value=True)
        type(self.problem_mock).file_path = mocker.PropertyMock(return_value='some file path')
        type(self.problem_mock).dimension = mocker.PropertyMock(return_value=42)
        self.problem_mock.copy = mocker.Mock(return_value=self.problem_mock)
        
        self.em_support_attraction_stub = mocker.MagicMock(spec=EmAttractionSupport)
        type(self.em_support_attraction_stub).copy = mocker.CallableMixin(spec="return self")        
        self.em_support_mutation_stub = mocker.MagicMock(spec=EmMutationSupport)
        type(self.em_support_mutation_stub).copy = mocker.CallableMixin(spec="return self")  
        self.em_support_direction_stub = mocker.MagicMock(spec=EmDirectionSupport)
        type(self.em_support_direction_stub).copy = mocker.CallableMixin(spec="return self")       
        
        self.evaluations_max = 42
        self.iterations_max = 42
        self.seconds_max = 42
        self.finish_control_mock = mocker.MagicMock(spec=FinishControl)
        type(self.finish_control_mock).evaluations_max= mocker.PropertyMock(return_value=self.evaluations_max)
        type(self.finish_control_mock).iterations_max= mocker.PropertyMock(return_value=self.iterations_max)
        type(self.finish_control_mock).seconds_max= mocker.PropertyMock(return_value=self.seconds_max)
        self.finish_control_mock.copy = mocker.Mock(return_value=self.finish_control_mock)
        
        self.random_seed = 42
        self.mutation_probability = 0.1
        self.tournament_size = 10
        self.population_size = 100

        self.em_optimizer:EmOptimizerGenerational = EmOptimizerGenerational(
                output_control=self.output_control_stub,
                problem=self.problem_mock, 
                solution_template=SolutionVoidInt( 43, 0, 0, False),
                em_attraction_support=self.em_support_attraction_stub,
                em_mutation_support=self.em_support_mutation_stub,
                em_direction_support=self.em_support_direction_stub,
                finish_control=self.finish_control_mock,
                random_seed=self.random_seed,
                population_size=self.population_size,
        )

    def test_name_should_be_em(self):
        self.assertEqual(self.em_optimizer.name, 'em')

    def test_evaluations_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.em_optimizer.finish_control.evaluations_max, self.finish_control_mock.evaluations_max)

    def test_iterations_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.em_optimizer.finish_control.iterations_max, self.finish_control_mock.iterations_max)

    def test_random_seed_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.em_optimizer.random_seed, self.random_seed)

    def test_seconds_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.em_optimizer.finish_control.seconds_max, self.finish_control_mock.seconds_max)

    def test_problem_name_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.em_optimizer.problem.name, self.problem_mock.name)

    def test_problem_is_minimization_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.em_optimizer.problem.is_minimization, self.problem_mock.is_minimization)

    def test_problem_file_path_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.em_optimizer.problem.file_path, self.problem_mock.file_path)

    def test_problem_dimension_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.em_optimizer.problem.dimension, self.problem_mock.dimension)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestEmOptimizerGenerationalProperties")
if __name__ == '__main__':
    unittest.main()