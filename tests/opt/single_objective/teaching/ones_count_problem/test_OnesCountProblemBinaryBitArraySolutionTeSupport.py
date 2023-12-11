
import unittest

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

import unittest.mock as mock

from bitstring import BitArray

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import TargetSolution

from uo.algorithm.algorithm import Algorithm
from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.teaching.ones_count_problem.ones_count_problem import OnesCountProblem
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_binary_bit_array_solution import OnesCountProblemBinaryBitArraySolution
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_binary_bit_array_solution_te_support import OnesCountProblemBinaryBitArraySolutionTeSupport

# should use Mock instead of this
class AlgorithmVoid(Algorithm):
    def __init__(self, name:str, output_control:OutputControl,
            target_problem:TargetProblem)->None:
        super().__init__(name, output_control, target_problem)

    def __copy__(self):
        return super().__copy__()

    def copy(self):
        return self.__copy__()

    def init(self):
        return

    def optimize(self):
        return
        
    def __str__(self)->str:
        return super().__str__()

    def __repr__(self)->str:
        return super().__repr__()

    def __format__(self, spec:str)->str:
        return super().__format__()

class TestOnesCountProblemBinaryBitArraySolutionTeSupport(unittest.TestCase):

    # can reset the internal counter of the total enumerator and set the internal state of the solution to reflect reset operation
    def test_reset_internal_counter_and_state(self):
        problem = OnesCountProblem()
        solution = OnesCountProblemBinaryBitArraySolution()
        solution.init_from(BitArray(bin='0'), problem)
        optimizer = AlgorithmVoid("test", None, problem)
        te_support = OnesCountProblemBinaryBitArraySolutionTeSupport()
    
        te_support.reset(problem, solution, optimizer)
    
        self.assertEqual(te_support._OnesCountProblemBinaryBitArraySolutionTeSupport__bit_array_counter.current_state(), BitArray(bin='0'))
        self.assertEqual(solution.bit_array, BitArray(bin='0'))
        self.assertEqual(optimizer.evaluation, 1)

    # can progress the internal counter of the total enumerator and set the internal state of the solution to reflect progress operation
    def test_progress_internal_counter_and_state(self):
        problem = OnesCountProblem()
        solution = OnesCountProblemBinaryBitArraySolution()
        optimizer = Algorithm()
        te_support = OnesCountProblemBinaryBitArraySolutionTeSupport()
    
        te_support.reset(problem, solution, optimizer)
        te_support.progress(problem, solution, optimizer)
    
        self.assertEqual(te_support._OnesCountProblemBinaryBitArraySolutionTeSupport__bit_array_counter.current_state(), BitArray(bin='1'))
        self.assertEqual(solution.bit_array, BitArray(bin='1'))
        self.assertEqual(optimizer.evaluation, 2)

    # can check if total enumeration process is not at end
    def test_can_progress(self):
        problem = OnesCountProblem()
        solution = OnesCountProblemBinaryBitArraySolution()
        optimizer = Algorithm()
        te_support = OnesCountProblemBinaryBitArraySolutionTeSupport()
    
        te_support.reset(problem, solution, optimizer)
    
        self.assertTrue(te_support.can_progress(problem, solution, optimizer))

    # can reset the internal counter of the total enumerator and set the internal state of the solution to reflect reset operation when the problem has dimension 0
    def test_reset_internal_counter_and_state_dimension_0(self):
        problem = OnesCountProblem()
        problem.dimension = 0
        solution = OnesCountProblemBinaryBitArraySolution()
        optimizer = Algorithm()
        te_support = OnesCountProblemBinaryBitArraySolutionTeSupport()
    
        te_support.reset(problem, solution, optimizer)
    
        self.assertEqual(te_support._OnesCountProblemBinaryBitArraySolutionTeSupport__bit_array_counter.current_state(), BitArray(bin=''))
        self.assertEqual(solution.bit_array, BitArray(bin=''))
        self.assertEqual(optimizer.evaluation, 1)

    # can progress the internal counter of the total enumerator and set the internal state of the solution to reflect progress operation when the problem has dimension 0
    def test_progress_internal_counter_and_state_dimension_0(self):
        problem = OnesCountProblem()
        problem.dimension = 0
        solution = OnesCountProblemBinaryBitArraySolution()
        optimizer = Algorithm()
        te_support = OnesCountProblemBinaryBitArraySolutionTeSupport()
    
        te_support.reset(problem, solution, optimizer)
        te_support.progress(problem, solution, optimizer)
    
        self.assertEqual(te_support._OnesCountProblemBinaryBitArraySolutionTeSupport__bit_array_counter.current_state(), BitArray(bin=''))
        self.assertEqual(solution.bit_array, BitArray(bin=''))
        self.assertEqual(optimizer.evaluation, 2)

    # can check if total enumeration process is not at end when the problem has dimension 0
    def test_can_progress_dimension_0(self):
        problem = OnesCountProblem()
        problem.dimension = 0
        solution = OnesCountProblemBinaryBitArraySolution()
        optimizer = Algorithm()
        te_support = OnesCountProblemBinaryBitArraySolutionTeSupport()
    
        te_support.reset(problem, solution, optimizer)
    
        self.assertFalse(te_support.can_progress(problem, solution, optimizer))

    def test_calculate_ones_dimension_greater_than_0(self):
        problem = OnesCountProblem()
        problem.dimension = 5
        solution = OnesCountProblemBinaryBitArraySolution()
        optimizer = Algorithm()
        te_support = OnesCountProblemBinaryBitArraySolutionTeSupport()

        te_support.reset(problem, solution, optimizer)
        ones_count = te_support.calculate_ones(problem, solution, optimizer)

        self.assertEqual(ones_count, 5)

    def test_calculate_ones_dimension_0(self):
        problem = OnesCountProblem()
        problem.dimension = 0
        solution = OnesCountProblemBinaryBitArraySolution()
        optimizer = Algorithm()
        te_support = OnesCountProblemBinaryBitArraySolutionTeSupport()

        te_support.reset(problem, solution, optimizer)
        ones_count = te_support.calculate_ones(problem, solution, optimizer)

        self.assertEqual(ones_count, 0)

    def test_reset_internal_counter_and_state_dimension_greater_than_0(self):
        problem = OnesCountProblem()
        problem.dimension = 5
        solution = OnesCountProblemBinaryBitArraySolution()
        optimizer = Algorithm()
        te_support = OnesCountProblemBinaryBitArraySolutionTeSupport()

        te_support.reset(problem, solution, optimizer)

        self.assertEqual(te_support._OnesCountProblemBinaryBitArraySolutionTeSupport__bit_array_counter.current_state(), BitArray(bin='0'))
        self.assertEqual(solution.bit_array, BitArray(bin='0'))
        self.assertEqual(optimizer.evaluation, 1)

    def test_reset_internal_counter_and_state_dimension_0(self):
        problem = OnesCountProblem()
        problem.dimension = 0
        solution = OnesCountProblemBinaryBitArraySolution()
        optimizer = Algorithm()
        te_support = OnesCountProblemBinaryBitArraySolutionTeSupport()

        te_support.reset(problem, solution, optimizer)

        self.assertEqual(te_support._OnesCountProblemBinaryBitArraySolutionTeSupport__bit_array_counter.current_state(), BitArray(bin=''))
        self.assertEqual(solution.bit_array, BitArray(bin=''))
        self.assertEqual(optimizer.evaluation, 1)