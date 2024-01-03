import unittest   
import unittest.mock as mocker

from uo.target_problem.target_problem import TargetProblem
from uo.target_problem.target_problem_void import TargetProblemVoid
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.metaheuristic import Metaheuristic 
from uo.algorithm.metaheuristic.metaheuristic_void import MetaheuristicVoid


class TestAdditionalStatisticsControl(unittest.TestCase):

    # Creating an instance of AdditionalStatisticsControl with valid parameters should initialize all properties correctly.
    def test_valid_parameters_initialization(self):
        # Arrange
        keep = 'all_solution_code'
        max_local_optima = 10
        # Act
        control = AdditionalStatisticsControl(keep, max_local_optima)
        # Assert
        self.assertEqual(control.keep_all_solution_codes, True)
        self.assertEqual(control.keep_more_local_optima, False)
        self.assertEqual(control.max_local_optima, max_local_optima)

    # Setting the 'keep' property with valid values should update the 'keep_all_solution_codes' and 'keep_more_local_optima' properties correctly.
    def test_valid_keep_property_update(self):
        # Arrange
        control = AdditionalStatisticsControl()
        # Act
        control.keep = 'all_solution_code'
        # Assert
        self.assertEqual(control.keep_all_solution_codes, True)
        self.assertEqual(control.keep_more_local_optima, False)
        # Act
        control.keep = 'more_local_optima'
        # Assert
        self.assertEqual(control.keep_all_solution_codes, False)
        self.assertEqual(control.keep_more_local_optima, True)    
        # Act
        control.keep = 'all_solution_code, more_local_optima'
        # Assert
        self.assertEqual(control.keep_all_solution_codes, True)
        self.assertEqual(control.keep_more_local_optima, True)

    # Calling 'add_to_all_solution_codes_if_required' with 'keep_all_solution_codes' set to True should add the solution representation to the 'all_solution_codes' set.
    def test_add_to_all_solution_codes_if_required(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='all_solution_code')
        representation = 'solution_representation'
    
        # Act
        control.add_to_all_solution_codes_if_required(representation)
    
        # Assert
        self.assertIn(representation, AdditionalStatisticsControl.all_solution_codes)

    # Calling 'add_to_more_local_optima_if_required' with 'keep_more_local_optima' set to True and a new solution representation should add the solution to the 'more_local_optima' dictionary.
    def test_add_to_more_local_optima_if_required_new_solution(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='more_local_optima')
        solution_to_add_rep = 'solution_representation'
        solution_to_add_fitness = 0.5
        best_solution_rep = 'best_solution_representation'
    
        # Act
        result = control.add_to_more_local_optima_if_required(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
    
        # Assert
        self.assertTrue(result)
        self.assertIn(solution_to_add_rep, AdditionalStatisticsControl.more_local_optima)
        self.assertEqual(AdditionalStatisticsControl.more_local_optima[solution_to_add_rep], solution_to_add_fitness)

    # Calling 'add_to_more_local_optima_if_required' with 'keep_more_local_optima' set to True and an existing solution representation should not add the solution to the 'more_local_optima' dictionary.
    def test_add_to_more_local_optima_if_required_existing_solution(self):
        # Arrange
        control = AdditionalStatisticsControl(keep='more_local_optima')
        solution_to_add_rep = 'solution_representation'
        solution_to_add_fitness = 0.5
        best_solution_rep = 'best_solution_representation'
        AdditionalStatisticsControl.more_local_optima[solution_to_add_rep] = solution_to_add_fitness
    
        # Act
        result = control.add_to_more_local_optima_if_required(solution_to_add_rep, solution_to_add_fitness, best_solution_rep)
    
        # Assert
        self.assertFalse(result)
        self.assertIn(solution_to_add_rep, AdditionalStatisticsControl.more_local_optima)
        self.assertEqual(AdditionalStatisticsControl.more_local_optima[solution_to_add_rep], solution_to_add_fitness)

    # Creating an instance of AdditionalStatisticsControl with invalid 'keep' parameter should raise a TypeError.
    def test_invalid_keep_parameter_type(self):
        # Arrange
        keep = 123
        max_local_optima = 10
    
        # Act & Assert
        with self.assertRaises(TypeError):
            AdditionalStatisticsControl(keep, max_local_optima)

    # Creating an instance of AdditionalStatisticsControl with invalid 'max_local_optima' parameter should raise a TypeError.
    def test_invalid_max_local_optima_parameter_type(self):
        # Arrange
        keep = 'all_solution_code, more_local_optima'
        max_local_optima = '10'
    
        # Act & Assert
        with self.assertRaises(TypeError):
            AdditionalStatisticsControl(keep, max_local_optima)

    # Setting the 'keep' property with invalid values should raise a ValueError.
    def test_invalid_keep_property_value(self):
        # Arrange
        control = AdditionalStatisticsControl()
    
        # Act & Assert
        with self.assertRaises(ValueError):
            control.keep = 'invalid_value'