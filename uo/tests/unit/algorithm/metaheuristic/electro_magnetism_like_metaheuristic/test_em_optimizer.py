from datetime import datetime
import unittest
import unittest.mock as mocker
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_optimizer_gen import EmOptimizerGenerational
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_attraction_support import EmAttractionSupport
from uo.algorithm.metaheuristic.electro_magnetism_like_metaheuristic.em_mutation_support import EmMutationSupport

from uo.problem.problem_void_min_so import ProblemVoidMinSO
from uo.solution.solution_void_representation_int import SolutionVoidInt


class TestEmOptimizerGenerational(unittest.TestCase):

    # EmOptimizerGenerational can be initialized with valid parameters
    def test_em_optimizer_initialized_with_valid_parameters(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidInt( 43, 43, 43, True)
        em_attraction_support_stub = mocker.MagicMock(spec=EmAttractionSupport)
        type(em_attraction_support_stub).attraction = mocker.CallableMixin(spec=lambda x: x)
        em_mutation_support_stub = mocker.MagicMock(spec=EmMutationSupport)
        type(em_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        # Act
        em_optimizer = EmOptimizerGenerational( em_attraction_support=em_attraction_support_stub, 
                                em_mutation_support=em_mutation_support_stub, 
                                population_size=population_size, 
                                finish_control=finish_control, 
                                problem=problem, 
                                solution_template=solution_template,
                                random_seed=random_seed   
                    )
        # Assert
        self.assertIsInstance(em_optimizer, EmOptimizerGenerational)

    # EmOptimizerGenerational can be initialized with None for solution_template parameter
    def test_em_optimizer_initialized_with_none_solution_template_2(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidInt( 43, 0, 0, False)
        em_attraction_support_stub = mocker.MagicMock(spec=EmAttractionSupport)
        type(em_attraction_support_stub).attraction = mocker.CallableMixin(spec=lambda x: x)
        em_mutation_support_stub = mocker.MagicMock(spec=EmMutationSupport)
        type(em_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        # Act
        em_optimizer = EmOptimizerGenerational(em_attraction_support=em_attraction_support_stub, 
                                em_mutation_support=em_mutation_support_stub, 
                                population_size=population_size, 
                                finish_control=finish_control, 
                                problem=problem, 
                                solution_template=solution_template,
                                random_seed=random_seed)
        # Assert
        self.assertIsInstance(em_optimizer, EmOptimizerGenerational)

    # EmOptimizerGenerational can be initialized with None for random_seed parameter
    def test_em_optimizer_initialized_with_none_random_seed(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = None
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidInt( 43, 0, 0, False)
        em_attraction_support_stub = mocker.MagicMock(spec=EmAttractionSupport)
        type(em_attraction_support_stub).attraction = mocker.CallableMixin(spec=lambda x: x)
        em_mutation_support_stub = mocker.MagicMock(spec=EmMutationSupport)
        type(em_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        # Act
        em_optimizer = EmOptimizerGenerational(em_attraction_support=em_attraction_support_stub, 
                                em_mutation_support=em_mutation_support_stub,  
                                population_size=population_size, 
                                finish_control=finish_control, 
                                problem=problem, 
                                solution_template=solution_template,
                                random_seed=random_seed)
        # Assert
        self.assertIsInstance(em_optimizer, EmOptimizerGenerational)

    # EmOptimizerGenerational can not be initialized without EmAttractionSupport parameter
    def test_em_optimizer_initialized_without_em_attraction_support(self):
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = None
        em_attraction_support_stub = None
        em_mutation_support_stub = mocker.MagicMock(spec=EmMutationSupport)
        type(em_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        # Act & Assert
        with self.assertRaises(TypeError):
            EmOptimizerGenerational(em_attraction_support=em_attraction_support_stub, 
                                em_mutation_support=em_mutation_support_stub, 
                                population_size=population_size, 
                                finish_control=finish_control, 
                                problem=problem, 
                                solution_template=solution_template,
                                random_seed=random_seed)

    # EmOptimizerGenerational can successfully execute init
    def test_em_optimizer_init(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = None
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidInt( 43, 43, 43, True)
        em_attraction_support_stub = mocker.MagicMock(spec=EmAttractionSupport)
        type(em_attraction_support_stub).attraction = mocker.CallableMixin(spec=lambda x: x)
        em_mutation_support_stub = mocker.MagicMock(spec=EmMutationSupport)
        type(em_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        em_optimizer = EmOptimizerGenerational(em_attraction_support=em_attraction_support_stub, 
                                em_mutation_support=em_mutation_support_stub, 
                                population_size=population_size, 
                                finish_control=finish_control, 
                                problem=problem, 
                                solution_template=solution_template,
                                random_seed=random_seed)
        # Act
        em_optimizer.execution_started = datetime.now()
        em_optimizer.init()
        # Assert
        # Add assertions here
        self.assertEqual( em_optimizer.evaluation, 1)

    # EmOptimizerGenerational can successfully execute copy
    def test_copy(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = None
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidInt( 43, 43, 43, True)
        em_attraction_support_stub = mocker.MagicMock(spec=EmAttractionSupport)
        type(em_attraction_support_stub).attraction = mocker.CallableMixin(spec=lambda x: x)
        em_mutation_support_stub = mocker.MagicMock(spec=EmMutationSupport)
        type(em_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        em_optimizer = EmOptimizerGenerational(em_attraction_support=em_attraction_support_stub, 
                                em_mutation_support=em_mutation_support_stub, 
                                population_size=population_size,
                                finish_control=finish_control, 
                                problem=problem, 
                                solution_template=solution_template,
                                random_seed=random_seed)
        # Act
        copied_optimizer = em_optimizer.copy()
        # Assert
        self.assertIsNot(em_optimizer, copied_optimizer)
        self.assertEqual(em_optimizer.random_seed, copied_optimizer.random_seed)
        self.assertEqual(em_optimizer.finish_control.criteria, copied_optimizer.finish_control.criteria)

    # EmOptimizerGenerational raises TypeError if finish_control parameter is not of type FinishControl
    def test_finish_control_type_error(self):
        # Arrange
        finish_control = "not a FinishControl"
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidInt( 43, 43, 43, True)
        em_attraction_support_stub = mocker.MagicMock(spec=EmAttractionSupport)
        type(em_attraction_support_stub).attraction = mocker.CallableMixin(spec=lambda x: x)
        em_mutation_support_stub = mocker.MagicMock(spec=EmMutationSupport)
        type(em_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        # Act & Assert
        with self.assertRaises(TypeError):
            EmOptimizerGenerational(em_attraction_support=em_attraction_support_stub, 
                                em_mutation_support=em_mutation_support_stub, 
                                population_size=population_size, 
                                finish_control=finish_control, 
                                problem=problem, 
                                solution_template=solution_template,
                                random_seed=random_seed)

    # EmOptimizerGenerational raises TypeError if random_seed parameter is not of type Optional[int]
    def test_random_seed_type_error(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = "not an int"
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidInt( 43, 43, 43, True)
        em_attraction_support_stub = mocker.MagicMock(spec=EmAttractionSupport)
        type(em_attraction_support_stub).attraction = mocker.CallableMixin(spec=lambda x: x)
        em_mutation_support_stub = mocker.MagicMock(spec=EmMutationSupport)
        type(em_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        # Act & Assert
        with self.assertRaises(TypeError):
            EmOptimizerGenerational(em_attraction_support=em_attraction_support_stub, 
                                em_mutation_support=em_mutation_support_stub, 
                                population_size=population_size, 
                                finish_control=finish_control, 
                                problem=problem, 
                                solution_template=solution_template,
                                random_seed=random_seed)

    # EmOptimizerGenerational raises TypeError if additional_statistics_control parameter is not of type AdditionalStatisticsControl
    def test_additional_statistics_control_type_error(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        additional_statistics_control = "not a valid type"
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidInt( 43, 43, 43, True)
        em_attraction_support_stub = mocker.MagicMock(spec=EmAttractionSupport)
        type(em_attraction_support_stub).attraction = mocker.CallableMixin(spec=lambda x: x)
        em_mutation_support_stub = mocker.MagicMock(spec=EmMutationSupport)
        type(em_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        # Act & Assert
        with self.assertRaises(TypeError):
            EmOptimizerGenerational(em_attraction_support=em_attraction_support_stub, 
                                em_mutation_support=em_mutation_support_stub, 
                                population_size=population_size, 
                                finish_control=finish_control, 
                                problem=problem, 
                                solution_template=solution_template,
                                random_seed=random_seed, 
                                additional_statistics_control=additional_statistics_control)

    # EmOptimizerGenerational raises TypeError if solution_template parameter is not of type Optional[Solution]
    def test_solution_template_parameter_type_error(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = "not a Solution"        
        em_attraction_support_stub = mocker.MagicMock(spec=EmAttractionSupport)
        type(em_attraction_support_stub).attraction = mocker.CallableMixin(spec=lambda x: x)
        em_mutation_support_stub = mocker.MagicMock(spec=EmMutationSupport)
        type(em_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        # Act & Assert
        with self.assertRaises(TypeError):
            EmOptimizerGenerational(em_attraction_support=em_attraction_support_stub, 
                                em_mutation_support=em_mutation_support_stub, 
                                population_size=population_size, 
                                finish_control=finish_control, 
                                problem=problem, 
                                solution_template=solution_template,
                                random_seed=random_seed)

    # EmOptimizerGenerational raises TypeError if em_attraction_support parameter is not of type EmAttractionSupport
    def test_em_attraction_support_parameter_type_error(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidInt( 43, 43, 43, True)        
        em_attraction_support_stub = "not appropriate type"
        em_mutation_support_stub = mocker.MagicMock(spec=EmMutationSupport)
        type(em_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100
        # Act & Assert
        with self.assertRaises(TypeError):
            EmOptimizerGenerational(em_attraction_support=em_attraction_support_stub, 
                                em_mutation_support=em_mutation_support_stub,  
                                population_size=population_size, 
                                finish_control=finish_control, 
                                problem=problem, 
                                solution_template=solution_template,
                                random_seed=random_seed)

    # EmOptimizerGenerational raises TypeError if population_size parameter is not of type int
    def test_population_size_parameter_type_error(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidInt( 43, 43, 43, True)         
        em_attraction_support_stub = mocker.MagicMock(spec=EmAttractionSupport)
        type(em_attraction_support_stub).attraction = mocker.CallableMixin(spec=lambda x: x)
        em_mutation_support_stub = mocker.MagicMock(spec=EmMutationSupport)
        type(em_mutation_support_stub).mutation = mocker.CallableMixin(spec=lambda x: x)
        population_size = 100.2
        # Act & Assert
        with self.assertRaises(TypeError):
            EmOptimizerGenerational(em_attraction_support=em_attraction_support_stub, 
                                em_mutation_support=em_mutation_support_stub, 
                                population_size=population_size, 
                                finish_control=finish_control, 
                                problem=problem, 
                                solution_template=solution_template,
                                random_seed=random_seed)
