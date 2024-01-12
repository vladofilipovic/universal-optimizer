
from io import TextIOWrapper
import unittest   
import unittest.mock as mocker

from copy import deepcopy

from uo.algorithm.output_control import OutputControl

class TestOutputControlProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestOutputControlProperties\n")

    def setUp(self):
        self.write_to_output = True
        self.output_file = None
        self.output_control = OutputControl(
                write_to_output=self.write_to_output,
                output_file=self.output_file 
        )

    def test_write_to_output_should_be_as_it_is_in_constructor(self):
        self.assertEqual(self.output_control.write_to_output, self.write_to_output)

    def test_output_file_should_be_as_it_is_in_constructor(self):
        self.assertEqual(self.output_control.output_file, self.output_file)

    def test_is_output_file_should_be_same_that_it_is_set(self):
        val:str = "other file path..."
        self.output_control.output_file = val
        self.assertEqual(self.output_control.output_file, val)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestOutputControlProperties")
        

class TestOutputControl(unittest.TestCase):

    # OutputControl object can be initialized with default parameters
    def test_initialized_with_default_parameters(self):
        # Arrange
        # Act
        oc = OutputControl()
        # Assert
        self.assertFalse(oc.write_to_output)
        self.assertIsNone(oc.output_file)
        self.assertIn('iteration', oc.fields_headings)
        self.assertIn('evaluation', oc.fields_headings)
        self.assertIn('step_name', oc.fields_headings)
        self.assertIn('best_solution_string_representation', oc.fields_headings)
        self.assertIn('best_solution_fitness_value',  oc.fields_headings)
        self.assertIn('best_solution_objective_value', oc.fields_headings)
        self.assertIn('best_solution_is_feasible', oc.fields_headings)
        self.assertIn('self.iteration', oc.fields_definitions)
        self.assertIn('self.evaluation', oc.fields_definitions)
        self.assertIn('"step_name"', oc.fields_definitions)
        self.assertIn('self.best_solution.string_representation()', oc.fields_definitions)
        self.assertIn('self.best_solution.fitness_value', oc.fields_definitions)
        self.assertIn('self.best_solution.objective_value', oc.fields_definitions)
        self.assertIn('self.best_solution.is_feasible', oc.fields_definitions)
        self.assertEqual(oc.moments, 'after_algorithm')

    # OutputControl object can be initialized with custom parameters
    def test_initialized_with_custom_parameters(self):
        # Arrange
        write_to_output = True
        output_file = None
        fields = 'iteration, evaluation, "step_name", best_solution.argument(), best_solution.fitness_value, best_solution.objective_value, best_solution.is_feasible'
        moments = 'after_algorithm, before_iteration, after_iteration'
        # Act
        oc = OutputControl(write_to_output, output_file, fields, moments)
        # Assert
        self.assertTrue(oc.write_to_output)
        self.assertEqual(oc.output_file, output_file)
        self.assertIn('iteration', oc.fields_headings)
        self.assertIn('evaluation', oc.fields_headings)
        self.assertIn('step_name', oc.fields_headings)
        self.assertIn('best_solution_string_representation', oc.fields_headings)
        self.assertIn('best_solution_fitness_value',  oc.fields_headings)
        self.assertIn('best_solution_objective_value', oc.fields_headings)
        self.assertIn('best_solution_is_feasible', oc.fields_headings)
        self.assertIn('self.iteration', oc.fields_definitions)
        self.assertIn('self.evaluation', oc.fields_definitions)
        self.assertIn('"step_name"', oc.fields_definitions)
        self.assertIn('self.best_solution.string_representation()', oc.fields_definitions)
        self.assertIn('self.best_solution.fitness_value', oc.fields_definitions)
        self.assertIn('self.best_solution.objective_value', oc.fields_definitions)
        self.assertIn('self.best_solution.is_feasible', oc.fields_definitions)
        self.assertEqual(oc.moments, 'after_algorithm, before_iteration, after_iteration')

    # OutputControl object can have its output_file attribute updated
    def test_update_output_file_attribute(self):
        # Arrange
        oc = OutputControl()
        new_output_file = mocker.MagicMock(spec=TextIOWrapper)
        # Act
        oc.output_file = new_output_file
        # Assert
        self.assertEqual(oc.output_file, new_output_file)

    # OutputControl object can have its fields attribute updated
    def test_update_fields_attribute(self):
        # Arrange
        oc = OutputControl()
        new_fields = 'iteration, evaluation, "step_name", best_solution.argument(), best_solution.fitness_value'
        # Act
        oc.fields = new_fields
        # Assert
        self.assertIn('iteration', oc.fields_headings)
        self.assertIn('evaluation', oc.fields_headings)
        self.assertIn('step_name', oc.fields_headings)
        self.assertIn('best_solution_argument', oc.fields_headings)
        self.assertIn('best_solution_fitness_value',  oc.fields_headings)
        self.assertIn('self.iteration', oc.fields_definitions)
        self.assertIn('self.evaluation', oc.fields_definitions)
        self.assertIn('"step_name"', oc.fields_definitions)
        self.assertIn('self.best_solution.argument()', oc.fields_definitions)
        self.assertIn('self.best_solution.fitness_value', oc.fields_definitions)

    # OutputControl object raises TypeError if write_to_output parameter is not a boolean
    def test_write_to_output_type_error(self):
        # Arrange
        write_to_output = "True"
        # Act & Assert
        with self.assertRaises(TypeError):
            OutputControl(write_to_output)

    # OutputControl object raises TypeError if fields parameter is not a string
    def test_fields_type_error(self):
        # Arrange
        fields = ["iteration", "evaluation"]
        # Act & Assert
        with self.assertRaises(TypeError):
            OutputControl(fields=fields)

    # OutputControl object raises TypeError if moments parameter is not a string
    def test_moments_type_error(self):
        # Arrange
        moments = ["after_algorithm", "before_iteration"]
        # Act & Assert
        with self.assertRaises(TypeError):
            OutputControl(moments=moments)

    # OutputControl object raises ValueError if an invalid moment is passed to moments parameter
    def test_invalid_moment_value_error(self):
        # Arrange
        moments = "before_algorithm, after_algorithm, before_iteration, after_iteration, before_evaluation, after_evaluation, before_step_in_iteration, after_step_in_iteration, invalid_moment"
        # Act & Assert
        with self.assertRaises(ValueError):
            OutputControl(moments=moments)

if __name__ == '__main__':
    unittest.main()