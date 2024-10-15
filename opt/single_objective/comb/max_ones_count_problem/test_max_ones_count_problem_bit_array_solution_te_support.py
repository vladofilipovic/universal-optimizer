
import unittest
import unittest.mock as mocker

from bitstring import BitArray


from uo.algorithm.output_control import OutputControl
from uo.algorithm.exact.total_enumeration.te_operations_support_bit_array import \
    TeOperationsSupportBitArray
from uo.algorithm.algorithm_void import AlgorithmVoid

from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem import MaxOnesCountProblem
from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem_bit_array_solution import MaxOnesCountProblemBitArraySolution

class TestMaxOnesCountProblemBitArraySolutionTeSupport(unittest.TestCase):

    # can reset the internal counter of the total enumerator and set the internal state of the solution to reflect reset operation
    def test_reset_internal_counter_and_state(self):
        result:str = '00'
        problem = MaxOnesCountProblem(dim=len(result))
        solution = MaxOnesCountProblemBitArraySolution()
        solution.init_from(BitArray(bin=result), problem)
        optimizer = AlgorithmVoid(name="test", 
                            problem=problem)
        te_support = TeOperationsSupportBitArray()
    
        te_support.reset(problem, solution, optimizer)
    
        self.assertEqual(te_support._TeOperationsSupportBitArray__bit_array_counter.current_state(), BitArray(bin=result))
        self.assertEqual(solution.representation, BitArray(bin=result))
        self.assertEqual(optimizer.evaluation, 1)

    # can progress the internal counter of the total enumerator and set the internal state of the solution to reflect progress operation
    def test_progress_internal_counter_and_state(self):
        result:str = '10'
        problem = MaxOnesCountProblem(dim=len(result))
        solution = MaxOnesCountProblemBitArraySolution()
        solution.init_from(BitArray(bin=result), problem)
        optimizer = AlgorithmVoid(name="test", 
                            problem=problem)
        te_support = TeOperationsSupportBitArray()
    
        te_support.reset(problem, solution, optimizer)
        te_support.progress(problem, solution, optimizer)
    
        self.assertEqual(te_support._TeOperationsSupportBitArray__bit_array_counter.current_state(), BitArray(bin=result))
        self.assertEqual(solution.representation, BitArray(bin=result))
        self.assertEqual(optimizer.evaluation, 2)

    # can check if total enumeration process is not at end
    def test_can_progress(self):
        result:str = '00000'
        problem = MaxOnesCountProblem(dim=len(result))
        solution = MaxOnesCountProblemBitArraySolution()
        solution.init_from(BitArray(bin=result), problem)
        optimizer = AlgorithmVoid()
        te_support = TeOperationsSupportBitArray()
    
        te_support.reset(problem, solution, optimizer)
    
        self.assertTrue(te_support.can_progress(problem, solution, optimizer))

