
from datetime import datetime
import unittest   
import unittest.mock as mocker

from linopy import Model

from uo.problem.problem_void_min_so import ProblemVoidMinSO

from uo.algorithm.output_control import OutputControl


from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem import MaxOnesCountProblem
from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem_ilp_linopy import MaxOnesCountProblemIntegerLinearProgrammingSolver
from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem_ilp_linopy import MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters
from uo.solution.solution import Solution
from uo.solution.solution_void_representation_int import SolutionVoidInt
from uo.solution.solution_void_representation_object import SolutionVoidIntObject

class TestMaxOnesCountProblemIlpLinopy(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestIntegrationMaxOnesCountProblemIlpLinopy\n")

    def setUp(self):
        self.problem_to_solve:MaxOnesCountProblem = MaxOnesCountProblem.from_dimension(dimension=12)
        self.optimizer:MaxOnesCountProblemIntegerLinearProgrammingSolver = MaxOnesCountProblemIntegerLinearProgrammingSolver(
            problem=self.problem_to_solve
        )
        self.bs = self.optimizer.optimize()
    
    def test_best_solution_after_optimization_should_be_optimal(self):
        result = ''
        expected = ''
        for i in range(self.optimizer.model.nvars):
            result += str(int(self.optimizer.model.solution.x[i]))
            expected += '1'
        self.assertEqual(expected, result)

    # creating an instance of MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters with valid OutputControl and Problem parameters should return an instance of the class with the same parameters
    def test_valid_parameters(self):
        # Arrange
        output_control = OutputControl(moments="after_algorithm")
        problem = ProblemVoidMinSO('problem_name', False)
        # Act
        construction_params = MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(
            output_control=output_control, problem=problem)
        # Assert
        self.assertIsInstance(construction_params, MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters)
        self.assertEqual(construction_params.output_control, output_control)
        self.assertEqual(construction_params.problem, problem)

    # creating an instance of MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters with default parameters should return an instance of the class with None parameters
    def test_default_parameters(self):
        # Arrange
        # Act & Assert
        with self.assertRaises(TypeError):
            construction_params = MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters()

    # creating an instance of MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters with invalid OutputControl parameter should raise a TypeError
    def test_invalid_output_control(self):
        # Arrange
        output_control = "invalid_output_control"
        problem = ProblemVoidMinSO('problem_name', False)
        # Act & Assert
        with self.assertRaises(TypeError):
            MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(output_control, problem)

    # creating an instance of MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters with invalid Problem parameter should raise a TypeError
    def test_invalid_problem(self):
        # Arrange
        problem = "invalid_problem"
        # Act & Assert
        with self.assertRaises(TypeError):
            MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(problem)

    # creating an instance of MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters with OutputControl and Problem parameters of different types should raise a TypeError
    def test_different_types(self):
        # Arrange
        problem = SolutionVoidInt(42, None, None, False)
        # Act & Assert
        with self.assertRaises(TypeError):
            MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(problem)

    # creating an instance of MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters with OutputControl and Problem parameters of the same type but different from OutputControl and Problem should raise a TypeError
    def test_same_types_different_classes(self):
        # Arrange
        problem = SolutionVoidIntObject()
        # Act & Assert
        with self.assertRaises(TypeError):
            MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters(problem)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestIntegrationMaxOnesCountProblemIlpLinopy")
    
if __name__ == '__main__':
    unittest.main()


class TestOptimize(unittest.TestCase):

    # The method runs without errors when called with a valid instance of MaxOnesCountProblemIntegerLinearProgrammingSolver.
    def test_valid_instance_no_errors(self):
        # Arrange
        problem = MaxOnesCountProblem(dim=5)
        solver = MaxOnesCountProblemIntegerLinearProgrammingSolver(problem=problem)
        # Act
        try:
            bs = solver.optimize()
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")
        # Assert
        self.assertTrue(True)

    # The method creates an instance of Model and adds variables to it.
    def test_model_instance_and_variables_added(self):
        # Arrange
        problem = MaxOnesCountProblem(dim=5)
        solver = MaxOnesCountProblemIntegerLinearProgrammingSolver(problem=problem)
        # Act
        bs = solver.optimize()
        # Assert
        self.assertIsInstance(solver.model, Model)
        self.assertGreater(len(solver.model.variables), 0)

    # The method sets the objective function of the model to minimize or maximize the sum of the variables.
    def test_objective_function_set(self):
        # Arrange
        problem = MaxOnesCountProblem(dim=5)
        solver = MaxOnesCountProblemIntegerLinearProgrammingSolver(problem=problem)
        # Act
        bs = solver.optimize()
        # Assert
        objective = solver.model.objective
        self.assertIsNotNone(objective)
        self.assertIn("LinearExpression: +1 x[0] + 1 x[0] + 1 x[0] + 1 x[0] + 1 x[0] + 0\nSense: max\nValue: 5.0", str(objective))

    # The method raises a TypeError if called with an invalid instance of OutputControl or MaxOnesCountProblem.
    def test_invalid_instance_type_error(self):
        # Arrange
        output_control = "invalid_output_control"
        problem = MaxOnesCountProblem(dim=5)
        # Act & Assert
        with self.assertRaises(TypeError):
            solver = MaxOnesCountProblemIntegerLinearProgrammingSolver(output_control, problem)
            bs = solver.optimize()
        output_control = OutputControl()
        problem = "invalid_problem"
        # Act & Assert
        with self.assertRaises(TypeError):
            solver = MaxOnesCountProblemIntegerLinearProgrammingSolver(output_control, problem)
            bs = solver.optimize()

    # The method solves the model and sets the best solution to the solution of the model.
    def test_model_solved_and_best_solution_set(self):
        # Arrange
        problem = MaxOnesCountProblem(dim=5)
        solver = MaxOnesCountProblemIntegerLinearProgrammingSolver(problem=problem)
        # Act
        bs = solver.optimize()
        # Assert
        self.assertIsNotNone(bs)
        self.assertIsNotNone(solver.best_solution)
        

class TestStringRep(unittest.TestCase):

    # Returns a string representation of the 'MaxOnesCountProblemIntegerLinearProgrammingSolver' instance
    def test_returns_string_representation(self):
        # Arrange
        problem = MaxOnesCountProblem(dim=5)
        solver = MaxOnesCountProblemIntegerLinearProgrammingSolver(problem=problem)
        solver.execution_started = datetime.now()
        self.best_solution_mock = mocker.MagicMock(spec=Solution)
        self.best_solution_mock.copy = mocker.Mock(return_value=self.best_solution_mock)
        self.best_solution_mock.string_rep = mocker.Mock(return_value="solution mock")
        solver.best_solution = self.best_solution_mock
        # Act
        result = solver.string_rep("|")
        # Assert
        self.assertIsInstance(result, str)

    # The string representation contains the name of the class and its properties
    def test_contains_class_name_and_properties(self):
        # Arrange
        output_control = OutputControl()
        problem = MaxOnesCountProblem(dim=5)
        solver = MaxOnesCountProblemIntegerLinearProgrammingSolver(output_control, problem)
        solver.execution_started = datetime.now()
        self.best_solution_mock = mocker.MagicMock(spec=Solution)
        self.best_solution_mock.copy = mocker.Mock(return_value=self.best_solution_mock)
        self.best_solution_mock.string_rep = mocker.Mock(return_value="solution mock")
        solver.best_solution = self.best_solution_mock    
        # Act
        result = solver.string_rep("|")
        # Assert
        self.assertIn("MaxOnesCountProblemIntegerLinearProgrammingSolver", result)
        self.assertIn("output_control", result)
        self.assertIn("problem", result)

    # The string representation is properly formatted with indentation and grouping symbols
    def test_properly_formatted_with_indentation_and_grouping_symbols(self):
        # Arrange
        output_control = OutputControl()
        problem = MaxOnesCountProblem(dim=5)
        solver = MaxOnesCountProblemIntegerLinearProgrammingSolver(output_control, problem)
        solver.execution_started = datetime.now()
        self.best_solution_mock = mocker.MagicMock(spec=Solution)
        self.best_solution_mock.copy = mocker.Mock(return_value=self.best_solution_mock)
        self.best_solution_mock.string_rep = mocker.Mock(return_value="solution mock")
        solver.best_solution = self.best_solution_mock    
        # Act
        result = solver.string_rep("|", indentation=2, indentation_symbol="-", group_start="[", group_end="]")    
        # Assert
        self.assertIn( "output_control", result)
        self.assertIn( "problem", result)

 