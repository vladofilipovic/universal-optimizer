"""
..  _py_minimum_multi_cut_problem_binary_bit_array_solution_ga_support:

The :mod:`~opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem_binary_bit_array_solution_ga_support`
contains class :class:`~opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem_binary_bit_array_solution_ga_support.MinimumMultiCutProblemBinaryBitArraySolutionGaSupport`, 
that represents supporting parts of the `GA` algorithm, where solution of the :ref:`Problem_MinimumMultiCut` have `BitArray` 
representation.
"""
import sys
from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory)
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent)

from copy import deepcopy
from random import choice, random, randint

from bitstring import BitArray

from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer import GaOptimizer
from uo.algorithm.metaheuristic.genetic_algorithm.problem_solution_ga_support import ProblemSolutionGaSupport

from opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem import MinimumMultiCutProblem
from opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem_binary_bit_array_solution import MinimumMultiCutProblemBinaryBitArraySolution


class MinimumMultiCutProblemBinaryBitArraySolutionGaSupport(ProblemSolutionGaSupport[BitArray,str]):

    def __init__(self)->None:
        """
        Create new `MinimumMultiCutProblemBinaryBitArraySolutionGaSupport` instance
        """

    def __copy__(self):
        """
        Internal copy of the `MinimumMultiCutProblemBinaryBitArraySolutionGaSupport`

        :return: new `MinimumMultiCutProblemBinaryBitArraySolutionGaSupport` instance with the same properties
        :rtype: `MinimumMultiCutProblemBinaryBitArraySolutionGaSupport`
        """
        sol = deepcopy(self)
        return sol

    def copy(self):
        """
        Copy the `MinimumMultiCutProblemBinaryBitArraySolutionGaSupport` instance

        :return: new `MinimumMultiCutProblemBinaryBitArraySolutionGaSupport` instance with the same properties
        :rtype: `MinimumMultiCutProblemBinaryBitArraySolutionGaSupport`
        """
        return self.__copy__()

    def mutation(self, mutation_probability:float, problem:MinimumMultiCutProblem, solution:MinimumMultiCutProblemBinaryBitArraySolution, optimizer:GaOptimizer)->bool:
        for i in range(len(solution.representation)):
            if random() < mutation_probability:
                solution.representation.invert(i)

        return True

    def crossover(self, problem:MinimumMultiCutProblem, solution1:MinimumMultiCutProblemBinaryBitArraySolution, solution2:MinimumMultiCutProblemBinaryBitArraySolution,
                   child1:MinimumMultiCutProblemBinaryBitArraySolution, child2:MinimumMultiCutProblemBinaryBitArraySolution, optimizer:GaOptimizer):
        child1.representation = BitArray(solution1.representation.len)
        child2.representation = BitArray(solution2.representation.len)

        index:int = randint(0,len(solution1.representation))

        for i in range(index):
            child1.representation.set(solution1.representation[i], i)
            child2.representation.set(solution2.representation[i], i)

        for i in range(index,solution1.representation.len):
            child1.representation.set(solution2.representation[i], i)
            child2.representation.set(solution1.representation[i], i)

    def selection_roulette(self, problem:MinimumMultiCutProblem, solution:list[MinimumMultiCutProblemBinaryBitArraySolution],
                            optimizer:GaOptimizer)->MinimumMultiCutProblemBinaryBitArraySolution:
        return choice(solution)

    def selection_tournament(self, problem:MinimumMultiCutProblem, solution:list[MinimumMultiCutProblemBinaryBitArraySolution], tournament_size:int, optimizer:GaOptimizer)->MinimumMultiCutProblemBinaryBitArraySolution:
        return None

    def selection_rang_roulette(self, problem:MinimumMultiCutProblem, solution:list[MinimumMultiCutProblemBinaryBitArraySolution], optimizer:GaOptimizer)->MinimumMultiCutProblemBinaryBitArraySolution:
        return None

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the ga support structure

        :param delimiter: delimiter between fields
        :type delimiter: str
        :param indentation: level of indentation
        :type indentation: int, optional, default value 0
        :param indentation_symbol: indentation symbol
        :type indentation_symbol: str, optional, default value ''
        :param group_start: group start string 
        :type group_start: str, optional, default value '{'
        :param group_end: group end string 
        :type group_end: str, optional, default value '}'
        :return: string representation of ga support instance
        :rtype: str
        """
        return 'MinimumMultiCutProblemBinaryBitArraySolutionGaSupport'

    def __str__(self)->str:
        """
        String representation of the ga support instance

        :return: string representation of the ga support instance
        :rtype: str
        """
        return self.string_rep('|')

    def __repr__(self)->str:
        """
        Representation of the ga support instance

        :return: string representation of the ga support instance
        :rtype: str
        """
        return self.string_rep('\n')

    def __format__(self, spec:str)->str:
        """
        Formatted the ga support instance

        :param str spec: format specification
        :return: formatted ga support instance
        :rtype: str
        """
        return self.string_rep('|')


