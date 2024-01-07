""" 
..  _py_ones_count_problem_bit_array_solution_te_support:

The :mod:`~opt.single_objective.teaching.ones_count_problem.ones_count_problem_binary_bit_array_solution_te_support` 
contains class :class:`~opt.single_objective.teaching.ones_count_problem.ones_count_problem_binary_bit_array_solution_te_support.OnesCountProblemBinaryBitArraySolutionTeSupport`, 
that represents supporting parts of the `Total enumeration` algorithm, where solution of the :ref:`Problem_Max_Ones` have `BitArray` 
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
from random import choice
from random import random

from bitstring import Bits, BitArray, BitStream, pack

from uo.utils.complex_counter_bit_array_full import ComplexCounterBitArrayFull

from uo.utils.logger import logger
from uo.utils.complex_counter_uniform_ascending import ComplexCounterUniformAscending

from uo.target_solution.quality_of_solution import QualityOfSolution
from uo.algorithm.algorithm import Algorithm
from uo.algorithm.exact.total_enumeration.problem_solution_te_support import ProblemSolutionTeSupport

from opt.single_objective.teaching.ones_count_problem.ones_count_problem import OnesCountProblem
from opt.single_objective.teaching.ones_count_problem.ones_count_problem_binary_bit_array_solution import OnesCountProblemBinaryBitArraySolution

class OnesCountProblemBinaryBitArraySolutionTeSupport(ProblemSolutionTeSupport[BitArray,str]):
    
    def __init__(self)->None:
        """
        Create new `OnesCountProblemBinaryBitArraySolutionTeSupport` instance
        """
        self.__bit_array_counter = None

    def __copy__(self):
        """
        Internal copy of the `OnesCountProblemBinaryBitArraySolutionTeSupport`

        :return: new `OnesCountProblemBinaryBitArraySolutionTeSupport` instance with the same properties
        :rtype: `OnesCountProblemBinaryBitArraySolutionTeSupport`
        """
        sol = deepcopy(self)
        return sol

    def copy(self):
        """
        Copy the `OnesCountProblemBinaryBitArraySolutionTeSupport` instance

        :return: new `OnesCountProblemBinaryBitArraySolutionTeSupport` instance with the same properties
        :rtype: `OnesCountProblemBinaryBitArraySolutionTeSupport`
        """
        return self.__copy__()

    def reset(self, problem:OnesCountProblem, solution:OnesCountProblemBinaryBitArraySolution, optimizer:Algorithm)->None:
        """
        Resets internal counter of the total enumerator, so process will start over. Internal state of the solution 
        will be set to reflect reset operation. 

        :param `OnesCountProblem` problem: problem that is solved
        :param `OnesCountProblemBinaryBitArraySolution` solution: solution used for the problem that is solved
        :param `Algorithm` optimizer: optimizer that is executed
        """        
        self.__bit_array_counter = ComplexCounterBitArrayFull(problem.dimension)
        self.__bit_array_counter.reset()
        solution.init_from(self.__bit_array_counter.current_state(), problem)
        optimizer.write_output_values_if_needed("before_evaluation", "b_e")
        optimizer.evaluation += 1
        solution.evaluate(problem)
        optimizer.write_output_values_if_needed("after_evaluation", "a_e")

    def progress(self, problem:OnesCountProblem, solution:OnesCountProblemBinaryBitArraySolution, 
            optimizer:Algorithm)->None:
        """
        Progress internal counter of the total enumerator, so next configuration will be taken into consideration. 
        Internal state of the solution will be set to reflect progress operation.  

        :param `OnesCountProblem` problem: problem that is solved
        :param `OnesCountProblemBinaryBitArraySolution` solution: solution used for the problem that is solved
        :param `Algorithm` optimizer: optimizer that is executed
        """        
        self.__bit_array_counter.progress()
        solution.init_from( self.__bit_array_counter.current_state(), problem)
        optimizer.write_output_values_if_needed("before_evaluation", "b_e")
        optimizer.evaluation += 1
        solution.evaluate(problem)
        optimizer.write_output_values_if_needed("after_evaluation", "a_e")

    def can_progress(self, problem:OnesCountProblem, solution:OnesCountProblemBinaryBitArraySolution, 
            optimizer:Algorithm)->bool:
        """
        Check if total enumeration process is not at end.  

        :param `OnesCountProblem` problem: problem that is solved
        :param `OnesCountProblemBinaryBitArraySolution` solution: solution used for the problem that is solved
        :param `Algorithm` optimizer: optimizer that is executed
        :return: indicator if total enumeration process is not at end 
        :rtype: bool
        """        
        return self.__bit_array_counter.can_progress()

    def overall_number_of_evaluations(self, problem:OnesCountProblem, solution:OnesCountProblemBinaryBitArraySolution, 
            optimizer:Algorithm)->int:
        """
        Returns overall number of evaluations required for finishing total enumeration process.  

        :param `OnesCountProblem` problem: problem that is solved
        :param `OnesCountProblemBinaryBitArraySolution` solution: solution used for the problem that is solved
        :param `Algorithm` optimizer: optimizer that is executed
        :return: overall number of evaluations required for finishing total enumeration process
        :rtype: int
        """        
        return pow(2, problem.dimension)

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the te support structure

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
        :return: string representation of vns support instance
        :rtype: str
        """        
        return 'OnesCountProblemBinaryBitArraySolutionTeSupport'

    def __str__(self)->str:
        """
        String representation of the te support instance

        :return: string representation of the te support instance
        :rtype: str
        """
        return self.string_rep('|')

    def __repr__(self)->str:
        """
        Representation of the te support instance

        :return: string representation of the te support instance
        :rtype: str
        """
        return self.string_rep('\n')


    def __format__(self, spec:str)->str:
        """
        Formatted the te support instance

        :param str spec: format specification
        :return: formatted te support instance
        :rtype: str
        """
        return self.string_rep('|')


