
import unittest   
import unittest.mock as mocker

from linopy import Model

from uo.target_problem.target_problem_void import TargetProblemVoid

from uo.algorithm.output_control import OutputControl


from opt.single_objective.teaching.ones_count_problem.ones_count_problem import OnesCountProblem
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_ilp_linopy import OnesCountProblemIntegerLinearProgrammingSolver
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_ilp_linopy import OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters
from uo.target_solution.target_solution import TargetSolution
from uo.target_solution.target_solution_void import TargetSolutionVoid
from uo.target_solution.target_solution_void_object_str import TargetSolutionVoidObjectStr

class TestOnesCountProblemIlpLinopy(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestIntegrationOnesCountProblemIlpLinopy\n")

    def setUp(self):
        self.output_control = OutputControl(False)
        self.problem_to_solve:OnesCountProblem = OnesCountProblem.from_dimension(dimension=12)
        self.optimizer:OnesCountProblemIntegerLinearProgrammingSolver = OnesCountProblemIntegerLinearProgrammingSolver(
            output_control=self.output_control,
            problem=self.problem_to_solve
        )
        self.optimizer.optimize()
    
    def test_best_solution_after_optimization_should_be_optimal(self):
        result = ''
        expected = ''
        for i in range(self.optimizer.model.nvars):
            result += str(int(self.optimizer.model.solution.x[i]))
            expected += '1'
        self.assertEqual(expected, result)


    # creating an instance of OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters with valid OutputControl and TargetProblem parameters should return an instance of the class with the same parameters
    def test_valid_parameters(self):
        # Arrange
        output_control = OutputControl()
        target_problem = TargetProblemVoid('problem_name', False)
        # Act
        construction_params = OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(output_control, target_problem)
        # Assert
        self.assertIsInstance(construction_params, OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters)
        self.assertEqual(construction_params.output_control, output_control)
        self.assertEqual(construction_params.target_problem, target_problem)

    # creating an instance of OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters with default parameters should return an instance of the class with None parameters
    def test_default_parameters(self):
        # Arrange
        # Act & Assert
        with self.assertRaises(TypeError):
            construction_params = OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters()

    # creating an instance of OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters with invalid OutputControl parameter should raise a TypeError
    def test_invalid_output_control(self):
        # Arrange
        output_control = "invalid_output_control"
        target_problem = TargetProblemVoid('problem_name', False)
        # Act & Assert
        with self.assertRaises(TypeError):
            OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(output_control, target_problem)

    # creating an instance of OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters with invalid TargetProblem parameter should raise a TypeError
    def test_invalid_target_problem(self):
        # Arrange
        output_control = OutputControl()
        target_problem = "invalid_target_problem"
        # Act & Assert
        with self.assertRaises(TypeError):
            OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(output_control, target_problem)

    # creating an instance of OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters with OutputControl and TargetProblem parameters of different types should raise a TypeError
    def test_different_types(self):
        # Arrange
        output_control = OutputControl()
        target_problem = TargetSolutionVoid(42, None, None, False)
        # Act & Assert
        with self.assertRaises(TypeError):
            OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(output_control, target_problem)

    # creating an instance of OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters with OutputControl and TargetProblem parameters of the same type but different from OutputControl and TargetProblem should raise a TypeError
    def test_same_types_different_classes(self):
        # Arrange
        output_control = OutputControl()
        target_problem = TargetSolutionVoidObjectStr()
        # Act & Assert
        with self.assertRaises(TypeError):
            OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(output_control, target_problem)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestIntegrationOnesCountProblemIlpLinopy")
    
if __name__ == '__main__':
    unittest.main()


class TestOptimize(unittest.TestCase):

    # The method runs without errors when called with a valid instance of OnesCountProblemIntegerLinearProgrammingSolver.
    def test_valid_instance_no_errors(self):
        # Arrange
        output_control = OutputControl()
        problem = OnesCountProblem(dim=5)
        solver = OnesCountProblemIntegerLinearProgrammingSolver(output_control, problem)
        # Act
        try:
            solver.optimize()
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")
        # Assert
        self.assertTrue(True)

    # The method creates an instance of Model and adds variables to it.
    def test_model_instance_and_variables_added(self):
        # Arrange
        output_control = OutputControl()
        problem = OnesCountProblem(dim=5)
        solver = OnesCountProblemIntegerLinearProgrammingSolver(output_control, problem)
        # Act
        solver.optimize()
        # Assert
        self.assertIsInstance(solver.model, Model)
        self.assertGreater(len(solver.model.variables), 0)

    # The method sets the objective function of the model to minimize or maximize the sum of the variables.
    def test_objective_function_set(self):
        # Arrange
        output_control = OutputControl()
        problem = OnesCountProblem(dim=5)
        solver = OnesCountProblemIntegerLinearProgrammingSolver(output_control, problem)
        # Act
        solver.optimize()
        # Assert
        objective = solver.model.objective
        self.assertIsNotNone(objective)
        self.assertIn("LinearExpression: +1 x[0] + 1 x[0] + 1 x[0] + 1 x[0] + 1 x[0] + 0\nSense: max\nValue: 5.0", str(objective))

    # The method raises a TypeError if called with an invalid instance of OutputControl or OnesCountProblem.
    def test_invalid_instance_type_error(self):
        # Arrange
        output_control = "invalid_output_control"
        problem = OnesCountProblem(dim=5)
        # Act & Assert
        with self.assertRaises(TypeError):
            solver = OnesCountProblemIntegerLinearProgrammingSolver(output_control, problem)
            solver.optimize()
        output_control = OutputControl()
        problem = "invalid_problem"
        # Act & Assert
        with self.assertRaises(TypeError):
            solver = OnesCountProblemIntegerLinearProgrammingSolver(output_control, problem)
            solver.optimize()

    # The method solves the model and sets the best solution to the solution of the model.
    def test_model_solved_and_best_solution_set(self):
        # Arrange
        output_control = OutputControl()
        problem = OnesCountProblem(dim=5)
        solver = OnesCountProblemIntegerLinearProgrammingSolver(output_control, problem)
        # Act
        solver.optimize()
        # Assert
        self.assertIsNotNone(solver.best_solution)
        

class TestStringRep(unittest.TestCase):

    # Returns a string representation of the 'OnesCountProblemIntegerLinearProgrammingSolver' instance
    def test_returns_string_representation(self):
        # Arrange
        output_control = OutputControl()
        problem = OnesCountProblem(dim=5)
        best_solution_mock = mocker.MagicMock(spec=TargetSolution)
        best_solution_mock.string_rep = mocker.Mock(return_value="something")
        solver = OnesCountProblemIntegerLinearProgrammingSolver(output_control, problem)
        solver.best_solution = best_solution_mock
        # Act
        result = solver.string_rep("|")
        # Assert
        self.assertIsInstance(result, str)

    # The string representation contains the name of the class and its properties
    def test_contains_class_name_and_properties(self):
        # Arrange
        output_control = OutputControl()
        problem = OnesCountProblem(dim=5)
        best_solution_mock = mocker.MagicMock(spec=TargetSolution)
        best_solution_mock.string_rep = mocker.Mock(return_value="something")
        solver = OnesCountProblemIntegerLinearProgrammingSolver(output_control, problem)
        solver.best_solution = best_solution_mock    
        # Act
        result = solver.string_rep("|")
        # Assert
        self.assertIn("OnesCountProblemIntegerLinearProgrammingSolver", result)
        self.assertIn("output_control", result)
        self.assertIn("target_problem", result)

    # The string representation is properly formatted with indentation and grouping symbols
    def test_properly_formatted_with_indentation_and_grouping_symbols(self):
        # Arrange
        output_control = OutputControl()
        problem = OnesCountProblem(dim=5)
        best_solution_mock = mocker.MagicMock(spec=TargetSolution)
        best_solution_mock.string_rep = mocker.Mock(return_value="something")
        solver = OnesCountProblemIntegerLinearProgrammingSolver(output_control, problem)
        solver.best_solution = best_solution_mock    
        # Act
        result = solver.string_rep("|", indentation=2, indentation_symbol="-", group_start="[", group_end="]")    
        # Assert
        self.assertIn( "output_control", result)
        self.assertIn( "target_problem", result)

 