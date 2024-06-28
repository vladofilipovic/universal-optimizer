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
from uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support import GaCrossoverSupport
from uo.algorithm.metaheuristic.genetic_algorithm.ga_mutation_support import GaMutationSupport

from opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem import MinimumMultiCutProblem
from opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem_binary_bit_array_solution \
    import MinimumMultiCutProblemBinaryBitArraySolution


class MinimumMultiCutProblemBinaryBitArraySolutionGaCrossoverSupport(GaCrossoverSupport[BitArray,str]):

    def __init__(self, crossover_probability:float)->None:
        """
        Create new `MinimumMultiCutProblemBinaryBitArraySolutionGaCrossoverSupport` instance
        """
        super().__init__(crossover_probability)

    def __copy__(self):
        """
        Internal copy of the `MinimumMultiCutProblemBinaryBitArraySolutionGaCrossoverSupport`

        :return: new `MinimumMultiCutProblemBinaryBitArraySolutionGaCrossoverSupport` instance with the same properties
        :rtype: `MinimumMultiCutProblemBinaryBitArraySolutionGaCrossoverSupport`
        """
        sol = deepcopy(self)
        return sol

    def copy(self):
        """
        Copy the `MinimumMultiCutProblemBinaryBitArraySolutionGaCrossoverSupport` instance

        :return: new `MinimumMultiCutProblemBinaryBitArraySolutionGaCrossoverSupport` instance with the same properties
        :rtype: `MinimumMultiCutProblemBinaryBitArraySolutionGaCrossoverSupport`
        """
        return self.__copy__()

    def crossover(self, problem:MinimumMultiCutProblem, solution1:MinimumMultiCutProblemBinaryBitArraySolution, solution2:MinimumMultiCutProblemBinaryBitArraySolution,
                    child1:MinimumMultiCutProblemBinaryBitArraySolution, child2:MinimumMultiCutProblemBinaryBitArraySolution, optimizer:GaOptimizer) -> None:
        
        child1.representation = BitArray(solution1.representation.len)
        child2.representation = BitArray(solution2.representation.len)
        if random() > self.crossover_probability:
            return
        index:int = randint(0,len(solution1.representation))
        for i in range(index):
            child1.representation.set(solution1.representation[i], i)
            child2.representation.set(solution2.representation[i], i)
        for i in range(index,solution1.representation.len):
            child1.representation.set(solution2.representation[i], i)
            child2.representation.set(solution1.representation[i], i)
        optimizer.evaluation += 2
        child1.evaluate(problem)
        child2.evaluate(problem)        

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
        return 'MinimumMultiCutProblemBinaryBitArraySolutionGaCrossoverSupport'

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

class MinimumMultiCutProblemBinaryBitArraySolutionGaMutationSupport(GaMutationSupport[BitArray,str]):

    def __init__(self, mutation_probability:float)->None:
        """
        Create new `MinimumMultiCutProblemBinaryBitArraySolutionGaMutationSupport` instance
        """
        super().__init__(mutation_probability)

    def __copy__(self):
        """
        Internal copy of the `MinimumMultiCutProblemBinaryBitArraySolutionGaMutationSupport`

        :return: new `MinimumMultiCutProblemBinaryBitArraySolutionGaMutationSupport` instance with the same properties
        :rtype: `MinimumMultiCutProblemBinaryBitArraySolutionGaMutationSupport`
        """
        sol = deepcopy(self)
        return sol

    def copy(self):
        """
        Copy the `MinimumMultiCutProblemBinaryBitArraySolutionGaMutationSupport` instance

        :return: new `MinimumMultiCutProblemBinaryBitArraySolutionGaMutationSupport` instance with the same properties
        :rtype: `MinimumMultiCutProblemBinaryBitArraySolutionGaMutationSupport`
        """
        return self.__copy__()

    def mutation(self, problem:MinimumMultiCutProblem, solution:MinimumMultiCutProblemBinaryBitArraySolution, 
                    optimizer:GaOptimizer)->None:
        for i in range(len(solution.representation)):
            if random() < self.mutation_probability:
                solution.representation.invert(i)
        optimizer.evaluation += 1
        solution.evaluate(problem)

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
        return 'MinimumMultiCutProblemBinaryBitArraySolutionGaMutationSupport'

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


