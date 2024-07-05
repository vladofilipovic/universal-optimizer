from datetime import datetime
import unittest   
import unittest.mock as mocker
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.problem.problem import Problem
from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer 
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support import VnsShakingSupport
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support import VnsLocalSearchSupport
from uo.problem.problem_void_min_so import ProblemVoidMinSO
from uo.solution.solution_void_representation_int import SolutionVoidRepresentationInt


class TestVnsOptimizer(unittest.TestCase):

    # VnsOptimizer can be initialized with valid parameters
    def test_vns_optimizer_initialized_with_valid_parameters(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)
        vns_shaking_support_stub = mocker.MagicMock(spec=VnsShakingSupport)
        type(vns_shaking_support_stub).copy = mocker.CallableMixin(spec="return self")
        vns_ls_support_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
        type(vns_ls_support_stub).local_search_best_improvement = mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).local_search_first_improvement= mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).copy = mocker.CallableMixin(spec="return self")
        k_min = 1
        k_max = 10
        local_search_type = 'localSearchBestImprovement'
        # Act
        vns_optimizer = VnsOptimizer(vns_shaking_support=vns_shaking_support_stub, 
                            vns_ls_support=vns_ls_support_stub,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed)
        # Assert
        self.assertIsInstance(vns_optimizer, VnsOptimizer)

    # VnsOptimizer can be initialized with None for solution_template parameter
    def test_vns_optimizer_initialized_with_none_solution_template_2(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 0, 0, False)
        vns_shaking_support_stub = mocker.MagicMock(spec=VnsShakingSupport)
        type(vns_shaking_support_stub).copy = mocker.CallableMixin(spec="return self")
        vns_ls_support_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
        type(vns_ls_support_stub).local_search_best_improvement = mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).local_search_first_improvement= mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).copy = mocker.CallableMixin(spec="return self")
        k_min = 1
        k_max = 10
        local_search_type = 'localSearchBestImprovement'
        # Act
        vns_optimizer = VnsOptimizer(vns_shaking_support=vns_shaking_support_stub, 
                            vns_ls_support=vns_ls_support_stub,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed)
        # Assert
        self.assertIsInstance(vns_optimizer, VnsOptimizer)

    # VnsOptimizer can be initialized with None for random_seed parameter
    def test_vns_optimizer_initialized_with_none_random_seed(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = None
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 0, 0, False)
        vns_shaking_support_stub = mocker.MagicMock(spec=VnsShakingSupport)
        type(vns_shaking_support_stub).copy = mocker.CallableMixin(spec="return self")
        vns_ls_support_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
        type(vns_ls_support_stub).local_search_best_improvement = mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).local_search_first_improvement= mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).copy = mocker.CallableMixin(spec="return self")
        k_min = 1
        k_max = 10
        local_search_type = 'localSearchBestImprovement'
        # Act
        vns_optimizer = VnsOptimizer(vns_shaking_support=vns_shaking_support_stub, 
                            vns_ls_support=vns_ls_support_stub,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed)
        # Assert
        self.assertIsInstance(vns_optimizer, VnsOptimizer)

    def test_vns_optimizer_initialized_without_vns_shaking_support(self):
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = None
        vns_shaking_support = None
        vns_ls_support_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
        type(vns_ls_support_stub).local_search_best_improvement = mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).local_search_first_improvement= mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).copy = mocker.CallableMixin(spec="return self")
        k_min = 1
        k_max = 10
        local_search_type = 'localSearchBestImprovement'
        # Act & Assert
        with self.assertRaises(TypeError):
            VnsOptimizer(vns_shaking_support=vns_shaking_support, 
                            vns_ls_support=vns_ls_support_stub,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed)

    def test_vns_optimizer_initialized_without_vns_ls_support(self):
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = None
        vns_shaking_support_stub = mocker.MagicMock(spec=VnsShakingSupport)
        type(vns_shaking_support_stub).copy = mocker.CallableMixin(spec="return self")
        vns_ls_support = None
        k_min = 1
        k_max = 10
        local_search_type = 'localSearchBestImprovement'
        # Act & Assert
        with self.assertRaises(TypeError):
            VnsOptimizer(vns_shaking_support=vns_shaking_support_stub, 
                            vns_ls_support=vns_ls_support,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed)

    # VnsOptimizer can successfully execute init
    def test_vns_optimizer_init(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = None
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)
        vns_shaking_support_stub = mocker.MagicMock(spec=VnsShakingSupport)
        type(vns_shaking_support_stub).copy = mocker.CallableMixin(spec="return self")
        vns_ls_support_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
        type(vns_ls_support_stub).local_search_best_improvement = mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).local_search_first_improvement= mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).copy = mocker.CallableMixin(spec="return self")
        k_min = 1
        k_max = 10
        local_search_type = 'localSearchBestImprovement'
        vns_optimizer = VnsOptimizer(vns_shaking_support=vns_shaking_support_stub, 
                            vns_ls_support=vns_ls_support_stub,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed)
        # Act
        vns_optimizer.execution_started = datetime.now()
        vns_optimizer.init()
        # Assert
        # Add assertions here
        self.assertEqual( vns_optimizer.evaluation, 1)

    # VnsOptimizer can successfully execute copy
    def test_copy(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = None
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)
        vns_shaking_support_stub = mocker.MagicMock(spec=VnsShakingSupport)
        type(vns_shaking_support_stub).copy = mocker.CallableMixin(spec="return self")
        vns_ls_support_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
        type(vns_ls_support_stub).local_search_best_improvement = mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).local_search_first_improvement= mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).copy = mocker.CallableMixin(spec="return self")
        k_min = 1
        k_max = 10
        local_search_type = 'localSearchFirstImprovement'
        vns_optimizer = VnsOptimizer(vns_shaking_support=vns_shaking_support_stub, 
                            vns_ls_support=vns_ls_support_stub,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed)
        # Act
        copied_optimizer = vns_optimizer.copy()
        # Assert
        self.assertIsNot(vns_optimizer, copied_optimizer)
        self.assertEqual(vns_optimizer.random_seed, copied_optimizer.random_seed)
        self.assertEqual(vns_optimizer.finish_control.criteria, copied_optimizer.finish_control.criteria)

    # VnsOptimizer can successfully execute string_rep
    def test_string_rep(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)
        vns_shaking_support_stub = mocker.MagicMock(spec=VnsShakingSupport)
        type(vns_shaking_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_shaking_support_stub).string_rep = mocker.Mock(return_value="")
        vns_ls_support_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
        type(vns_ls_support_stub).local_search_best_improvement = mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).local_search_first_improvement= mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_ls_support_stub).string_rep = mocker.Mock(return_value="")
        k_min = 1
        k_max = 10
        local_search_type = 'localSearchFirstImprovement'
        vns_optimizer = VnsOptimizer(vns_shaking_support=vns_shaking_support_stub, 
                            vns_ls_support=vns_ls_support_stub,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed)
        # Act
        string_representation = vns_optimizer.string_rep('|')
        # Assert
        expected_string = "name=vns|"
        self.assertIn(expected_string, string_representation)
        expected_string = "|finish_control="
        self.assertIn(expected_string, string_representation)
        expected_string = "|random_seed=123|"
        self.assertIn(expected_string, string_representation)
        expected_string = "|additional_statistics_control="
        self.assertIn(expected_string, string_representation)
        expected_string = "|problem="
        self.assertIn(expected_string, string_representation)
        expected_string = "|current_solution="
        self.assertIn(expected_string, string_representation)
        expected_string = "|k_min=1|"
        self.assertIn(expected_string, string_representation)
        expected_string = "|k_max=10|"
        self.assertIn(expected_string, string_representation)
        expected_string = "|__vns_shaking_support="
        self.assertIn(expected_string, string_representation)
        expected_string = "|__vns_ls_support="
        self.assertIn(expected_string, string_representation)
        expected_string = "__local_search_type=" + local_search_type + "|"
        self.assertIn(expected_string, string_representation)

    # VnsOptimizer can successfully execute __str__
    def test_str(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)
        vns_shaking_support_stub = mocker.MagicMock(spec=VnsShakingSupport)
        type(vns_shaking_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_shaking_support_stub).string_rep = mocker.Mock(return_value="")
        vns_ls_support_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
        type(vns_ls_support_stub).local_search_best_improvement = mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).local_search_first_improvement= mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_ls_support_stub).string_rep = mocker.Mock(return_value="")
        k_min = 1
        k_max = 10
        local_search_type = 'localSearchFirstImprovement'
        vns_optimizer = VnsOptimizer(vns_shaking_support=vns_shaking_support_stub, 
                            vns_ls_support=vns_ls_support_stub,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed)
        # Act
        string_representation = str(vns_optimizer)
        # Assert
        expected_string = "name=vns|"
        self.assertIn(expected_string, string_representation)
        expected_string = "|finish_control="
        self.assertIn(expected_string, string_representation)
        expected_string = "|random_seed=123|"
        self.assertIn(expected_string, string_representation)
        expected_string = "|additional_statistics_control="
        self.assertIn(expected_string, string_representation)
        expected_string = "|problem="
        self.assertIn(expected_string, string_representation)
        expected_string = "|current_solution="
        self.assertIn(expected_string, string_representation)
        expected_string = "|k_min=1|"
        self.assertIn(expected_string, string_representation)
        expected_string = "|k_max=10|"
        self.assertIn(expected_string, string_representation)
        expected_string = "|__vns_shaking_support="
        self.assertIn(expected_string, string_representation)
        expected_string = "|__vns_ls_support="
        self.assertIn(expected_string, string_representation)
        expected_string = "__local_search_type=" + local_search_type + "|"
        self.assertIn(expected_string, string_representation)

    # VnsOptimizer can successfully execute __repr__
    def test_repr_method(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)
        vns_shaking_support_stub = mocker.MagicMock(spec=VnsShakingSupport)
        type(vns_shaking_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_shaking_support_stub).string_rep = mocker.Mock(return_value="")
        vns_ls_support_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
        type(vns_ls_support_stub).local_search_best_improvement = mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).local_search_first_improvement= mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_ls_support_stub).string_rep = mocker.Mock(return_value="")
        k_min = 1
        k_max = 10
        local_search_type = 'localSearchFirstImprovement'
        vns_optimizer = VnsOptimizer(vns_shaking_support=vns_shaking_support_stub, 
                            vns_ls_support=vns_ls_support_stub,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed)
        # Act
        repr_string = repr(vns_optimizer)
        # Assert
        self.assertIsInstance(repr_string, str)
        expected_string = "name="
        self.assertIn(expected_string, repr_string)
        expected_string = "finish_control="
        self.assertIn(expected_string, repr_string)
        expected_string = "random_seed=123"
        self.assertIn(expected_string, repr_string)
        expected_string = "additional_statistics_control="
        self.assertIn(expected_string, repr_string)
        expected_string = "problem="
        self.assertIn(expected_string, repr_string)
        expected_string = "current_solution="
        self.assertIn(expected_string, repr_string)
        expected_string = "k_min=1"
        self.assertIn(expected_string, repr_string)
        expected_string = "k_max=10"
        self.assertIn(expected_string, repr_string)
        expected_string = "__vns_shaking_support="
        self.assertIn(expected_string, repr_string)
        expected_string = "__vns_ls_support="
        self.assertIn(expected_string, repr_string)
        expected_string = "__local_search_type=" + local_search_type 
        self.assertIn(expected_string, repr_string)

    # VnsOptimizer raises TypeError if finish_control parameter is not of type FinishControl
    def test_finish_control_type_error(self):
        # Arrange
        finish_control = "not a FinishControl"
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)
        vns_shaking_support_stub = mocker.MagicMock(spec=VnsShakingSupport)
        type(vns_shaking_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_shaking_support_stub).string_rep = mocker.Mock(return_value="")
        vns_ls_support_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
        type(vns_ls_support_stub).local_search_best_improvement = mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).local_search_first_improvement= mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_ls_support_stub).string_rep = mocker.Mock(return_value="")
        k_min = 1
        k_max = 10
        local_search_type = 'localSearchFirstImprovement'
        # Act & Assert
        with self.assertRaises(TypeError):
            VnsOptimizer(vns_shaking_support=vns_shaking_support_stub, 
                            vns_ls_support=vns_ls_support_stub,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed)

    # VnsOptimizer raises TypeError if random_seed parameter is not of type Optional[int]
    def test_random_seed_type_error(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = "not an int"
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)
        vns_shaking_support_stub = mocker.MagicMock(spec=VnsShakingSupport)
        type(vns_shaking_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_shaking_support_stub).string_rep = mocker.Mock(return_value="")
        vns_ls_support_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
        type(vns_ls_support_stub).local_search_best_improvement = mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).local_search_first_improvement= mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_ls_support_stub).string_rep = mocker.Mock(return_value="")
        k_min = 1
        k_max = 10
        local_search_type = 'localSearchFirstImprovement'
        # Act & Assert
        with self.assertRaises(TypeError):
            VnsOptimizer(vns_shaking_support=vns_shaking_support_stub, 
                            vns_ls_support=vns_ls_support_stub,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed)

    # VnsOptimizer raises TypeError if additional_statistics_control parameter is not of type AdditionalStatisticsControl
    def test_additional_statistics_control_type_error(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        additional_statistics_control = "not a valid type"
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)
        vns_shaking_support_stub = mocker.MagicMock(spec=VnsShakingSupport)
        type(vns_shaking_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_shaking_support_stub).string_rep = mocker.Mock(return_value="")
        vns_ls_support_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
        type(vns_ls_support_stub).local_search_best_improvement = mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).local_search_first_improvement= mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_ls_support_stub).string_rep = mocker.Mock(return_value="")
        k_min = 1
        k_max = 10
        local_search_type = 'localSearchFirstImprovement'
        # Act & Assert
        with self.assertRaises(TypeError):
            VnsOptimizer(vns_shaking_support=vns_shaking_support_stub, 
                            vns_ls_support=vns_ls_support_stub,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed,
                            additional_statistics_control=additional_statistics_control)

    # VnsOptimizer raises TypeError if solution_template parameter is not of type Optional[Solution]
    def test_solution_template_parameter_type_error(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = "not a Solution"        
        vns_shaking_support_stub = mocker.MagicMock(spec=VnsShakingSupport)
        type(vns_shaking_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_shaking_support_stub).string_rep = mocker.Mock(return_value="")
        vns_ls_support_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
        type(vns_ls_support_stub).local_search_best_improvement = mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).local_search_first_improvement= mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_ls_support_stub).string_rep = mocker.Mock(return_value="")
        k_min = 1
        k_max = 10
        local_search_type = 'localSearchFirstImprovement'
        # Act & Assert
        with self.assertRaises(TypeError):
            VnsOptimizer(vns_shaking_support=vns_shaking_support_stub, 
                            vns_ls_support=vns_ls_support_stub,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed)

    # VnsOptimizer raises TypeError if vns_support parameter is not of proper type 
    def test_vns_shaking_support_parameter_type_error(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)        
        vns_shaking_support = "not appropriate type"       
        vns_ls_support_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
        type(vns_ls_support_stub).local_search_best_improvement = mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).local_search_first_improvement= mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_ls_support_stub).string_rep = mocker.Mock(return_value="")        
        k_min = 1
        k_max = 10
        local_search_type = 'localSearchFirstImprovement'
        # Act & Assert
        with self.assertRaises(TypeError):
            VnsOptimizer(vns_shaking_support=vns_shaking_support, 
                            vns_ls_support=vns_ls_support_stub,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed)


    # VnsOptimizer raises TypeError if vns_support parameter is not of proper type 
    def test_vns_ls_support_parameter_type_error(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)        
        vns_shaking_support_stub = mocker.MagicMock(spec=VnsShakingSupport)
        type(vns_shaking_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_shaking_support_stub).string_rep = mocker.Mock(return_value="")
        vns_ls_support_stub = "not appropriate type"       
        k_min = 1
        k_max = 10
        local_search_type = 'localSearchFirstImprovement'
        # Act & Assert
        with self.assertRaises(TypeError):
            VnsOptimizer(vns_shaking_support=vns_shaking_support_stub, 
                            vns_ls_support=vns_ls_support_stub,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed)

    # VnsOptimizer raises TypeError if k_min parameter is not of type int
    def test_k_min_parameter_type_error(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)         
        vns_shaking_support_stub = mocker.MagicMock(spec=VnsShakingSupport)
        type(vns_shaking_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_shaking_support_stub).string_rep = mocker.Mock(return_value="")
        vns_ls_support_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
        type(vns_ls_support_stub).local_search_best_improvement = mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).local_search_first_improvement= mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_ls_support_stub).string_rep = mocker.Mock(return_value="")
        k_min = "1"
        k_max = 10
        local_search_type = 'localSearchFirstImprovement'
        # Act & Assert
        with self.assertRaises(TypeError):
            VnsOptimizer(vns_shaking_support=vns_shaking_support_stub, 
                            vns_ls_support=vns_ls_support_stub,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed)

    # VnsOptimizer raises TypeError if k_max parameter is not of type int
    def test_k_min_parameter_type_error(self):
        # Arrange
        finish_control = FinishControl()
        random_seed = 123
        problem = ProblemVoidMinSO("a problem", True)
        solution_template = SolutionVoidRepresentationInt( 43, 43, 43, True)         
        vns_shaking_support_stub = mocker.MagicMock(spec=VnsShakingSupport)
        type(vns_shaking_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_shaking_support_stub).string_rep = mocker.Mock(return_value="")
        vns_ls_support_stub = mocker.MagicMock(spec=VnsLocalSearchSupport)
        type(vns_ls_support_stub).local_search_best_improvement = mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).local_search_first_improvement= mocker.CallableMixin(spec=lambda x: x)
        type(vns_ls_support_stub).copy = mocker.CallableMixin(spec="return self")
        type(vns_ls_support_stub).string_rep = mocker.Mock(return_value="")
        k_min = 1
        k_max = "10"
        local_search_type = 'localSearchFirstImprovement'
        # Act & Assert
        with self.assertRaises(TypeError):
            VnsOptimizer(vns_shaking_support=vns_shaking_support_stub, 
                            vns_ls_support=vns_ls_support_stub,
                            local_search_type=local_search_type, 
                            k_min=k_min, 
                            k_max=k_max, 
                            finish_control=finish_control,  
                            problem=problem, 
                            solution_template=solution_template, 
                            random_seed=random_seed)
