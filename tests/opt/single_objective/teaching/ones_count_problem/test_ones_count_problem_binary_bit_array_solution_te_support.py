
import unittest
import unittest.mock as mocker

from bitstring import BitArray

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import TargetSolution

from uo.algorithm.algorithm import Algorithm
from uo.algorithm.algorithm_void import AlgorithmVoid
from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.teaching.ones_count_problem.ones_count_problem import OnesCountProblem
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_binary_bit_array_solution import OnesCountProblemBinaryBitArraySolution
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_binary_bit_array_solution_te_support import OnesCountProblemBinaryBitArraySolutionTeSupport

class TestOnesCountProblemBinaryBitArraySolutionTeSupport(unittest.TestCase):

    # can reset the internal counter of the total enumerator and set the internal state of the solution to reflect reset operation
    def test_reset_internal_counter_and_state(self):
        result:str = '00'
        problem = OnesCountProblem(dim=len(result))
        solution = OnesCountProblemBinaryBitArraySolution()
        solution.init_from(BitArray(bin=result), problem)
        optimizer = AlgorithmVoid("test", None, problem)
        optimizer.output_control = OutputControl(write_to_output=False)
        te_support = OnesCountProblemBinaryBitArraySolutionTeSupport()
    
        te_support.reset(problem, solution, optimizer)
    
        self.assertEqual(te_support._OnesCountProblemBinaryBitArraySolutionTeSupport__bit_array_counter.current_state(), BitArray(bin=result))
        self.assertEqual(solution.representation, BitArray(bin=result))
        self.assertEqual(optimizer.evaluation, 1)

    # can progress the internal counter of the total enumerator and set the internal state of the solution to reflect progress operation
    def test_progress_internal_counter_and_state(self):
        result:str = '10'
        problem = OnesCountProblem(dim=len(result))
        solution = OnesCountProblemBinaryBitArraySolution()
        solution.init_from(BitArray(bin=result), problem)
        optimizer = AlgorithmVoid("test", None, problem)
        optimizer.output_control = OutputControl(write_to_output=False)
        te_support = OnesCountProblemBinaryBitArraySolutionTeSupport()
    
        te_support.reset(problem, solution, optimizer)
        te_support.progress(problem, solution, optimizer)
    
        self.assertEqual(te_support._OnesCountProblemBinaryBitArraySolutionTeSupport__bit_array_counter.current_state(), BitArray(bin=result))
        self.assertEqual(solution.representation, BitArray(bin=result))
        self.assertEqual(optimizer.evaluation, 2)

    # can check if total enumeration process is not at end
    def test_can_progress(self):
        result:str = '00000'
        problem = OnesCountProblem(dim=len(result))
        solution = OnesCountProblemBinaryBitArraySolution()
        solution.init_from(BitArray(bin=result), problem)
        optimizer = AlgorithmVoid("test", None, problem)
        optimizer.output_control = OutputControl(write_to_output=False)
        te_support = OnesCountProblemBinaryBitArraySolutionTeSupport()
    
        te_support.reset(problem, solution, optimizer)
    
        self.assertTrue(te_support.can_progress(problem, solution, optimizer))

class TestCalculateQualityDirectly(unittest.TestCase):

    # Calculate quality of a binary BitArray solution with all bits set to 1
    def test_all_bits_set_to_1(self):
        # Arrange
        representation = BitArray('0b111111')
        problem = OnesCountProblem(dim=6)
        solution = OnesCountProblemBinaryBitArraySolution()
        solution.init_from(representation, problem)
    
        # Act
        quality = solution.calculate_quality_directly(representation, problem)
    
        # Assert
        self.assertEqual(quality.objective_value, 6)
        self.assertEqual(quality.fitness_value, 6)
        self.assertTrue(quality.is_feasible)

    # Calculate quality of a binary BitArray solution with all bits set to 0
    def test_all_bits_set_to_0(self):
        # Arrange
        representation = BitArray('0b000000')
        problem = OnesCountProblem(dim=6)
        solution = OnesCountProblemBinaryBitArraySolution()
        solution.init_from(representation, problem)
    
        # Act
        quality = solution.calculate_quality_directly(representation, problem)
    
        # Assert
        self.assertEqual(quality.objective_value, 0)
        self.assertEqual(quality.fitness_value, 0)
        self.assertTrue(quality.is_feasible)

    # Calculate quality of a binary BitArray solution with a random bit string
    def test_random_bit_string(self):
        # Arrange
        representation = BitArray('0b101010')
        problem = OnesCountProblem(dim=6)
        solution = OnesCountProblemBinaryBitArraySolution()
        solution.init_from(representation, problem)
    
        # Act
        quality = solution.calculate_quality_directly(representation, problem)
    
        # Assert
        self.assertEqual(quality.objective_value, 3)
        self.assertEqual(quality.fitness_value, 3)
        self.assertTrue(quality.is_feasible)

    # Calculate quality of a binary BitArray solution with a None representation
    def test_none_representation(self):
        # Arrange
        representation = None
        problem = OnesCountProblem(dim=6)
        solution = OnesCountProblemBinaryBitArraySolution()
        
        # Act & Assert
        with self.assertRaises(TypeError):
            solution.init_from(representation, problem)

    # Calculate quality of a binary BitArray solution with a non-BitArray representation
    def test_non_bitarray_representation(self):
        # Arrange
        representation = "101010"
        problem = OnesCountProblem(dim=6)
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act & Assert
        with self.assertRaises(TypeError):
            solution.init_from(representation, problem)

    # Calculate quality of a binary BitArray solution with a BitArray representation of length 0
    def test_bitarray_length_0(self):
        # Arrange
        representation = BitArray()
        problem = OnesCountProblem(dim=6)
        solution = OnesCountProblemBinaryBitArraySolution()

        # Act & Assert
        with self.assertRaises(ValueError):
            solution.init_from(representation, problem)
