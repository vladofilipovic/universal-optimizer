""" 
.. _py_ones_count_max_problem_int_solution_vns_support:

The :mod:`~opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_binary_int_solution_vns_support` contains 
class :class:`~opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_binary_int_solution_vns_support.OnesCountMaxProblemBinaryIntSolutionVnsSupport`, 
that represents solution of the :ref:`Problem_Ones_Count_Max`, where `int` representation of the problem has been used.
"""

import sys
from pathlib import Path
from typing import Optional
directory = Path(__file__).resolve()
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent)

from copy import deepcopy
from random import choice
from random import randint

from uo.utils.logger import logger
from uo.utils.complex_counter_uniform_ascending import ComplexCounterUniformAscending

from uo.solution.quality_of_solution import QualityOfSolution
from uo.algorithm.algorithm import Algorithm
from uo.algorithm.metaheuristic.variable_neighborhood_search.problem_solution_vns_support import ProblemSolutionVnsSupport

from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem import OnesCountMaxProblem
from opt.single_objective.comb.ones_count_max_problem.ones_count_max_problem_binary_int_solution import OnesCountMaxProblemBinaryIntSolution

class OnesCountMaxProblemBinaryIntSolutionVnsSupport(ProblemSolutionVnsSupport[int,str]):
    
    def __init__(self)->None:
        """
        Create new `OnesCountMaxProblemBinaryIntSolutionVnsSupport` instance
        """
        return

    def __copy__(self):
        """
        Internal copy of the `OnesCountMaxProblemBinaryIntSolutionVnsSupport`

        :return: new `OnesCountMaxProblemBinaryIntSolutionVnsSupport` instance with the same properties
        :rtype: OnesCountMaxProblemBinaryIntSolutionVnsSupport
        """
        sup = deepcopy(self)
        return sup

    def copy(self):
        """
        Copy the `OnesCountMaxProblemBinaryIntSolutionVnsSupport`
        
        :return: new `OnesCountMaxProblemBinaryIntSolutionVnsSupport` instance with the same properties
        :rtype: `OnesCountMaxProblemBinaryIntSolutionVnsSupport`
        """        
        return self.__copy__()
        
    def shaking(self, k:int, problem:OnesCountMaxProblem, solution:OnesCountMaxProblemBinaryIntSolution, 
            optimizer:Algorithm)->bool:
        """
        Random VNS shaking of k parts such that new solution code does not differ more than k from all solution codes 
        inside shakingPoints 

        :param int k: int parameter for VNS
        :param `OnesCountMaxProblem` problem: problem that is solved
        :param `OnesCountMaxProblemBinaryIntSolution` solution: solution used for the problem that is solved
        :param `Algorithm` optimizer: optimizer that is executed
        :return: if shaking is successful
        :rtype: bool
        """    
        if optimizer.finish_control.is_finished(optimizer.evaluation, optimizer.iteration, optimizer.elapsed_seconds()):
            return False
        tries:int = 0
        limit:int = 10000
        while tries < limit:
            positions:list[int] = []
            for i in range(0,k):
                positions.append(choice(range(problem.dimension)))
            mask:int = 0
            for p in positions:
                mask |= 1 << p
            solution.representation ^= mask
            all_ok:bool = True
            if solution.representation.bit_count() > problem.dimension:
                all_ok = False
            if all_ok:
                break
        if tries < limit:
            if optimizer.finish_control.is_finished(optimizer.evaluation, optimizer.iteration, optimizer.elapsed_seconds()):
                return solution
            optimizer.write_output_values_if_needed("before_evaluation", "b_e")
            optimizer.evaluation += 1
            solution.evaluate(problem)
            optimizer.write_output_values_if_needed("after_evaluation", "a_e")
            return True
        else:
            return False 

    def local_search_best_improvement(self, k:int, problem:OnesCountMaxProblem, solution:OnesCountMaxProblemBinaryIntSolution, 
            optimizer: Algorithm)->bool:
        """
        Executes "best improvement" variant of the local search procedure 
        
        :param int k: int parameter for VNS
        :param `OnesCountMaxProblem` problem: problem that is solved
        :param `OnesCountMaxProblemBinaryIntSolution` solution: solution used for the problem that is solved
        :param `Algorithm` optimizer: optimizer that is executed
        :return: result of the local search procedure 
        :rtype: if local search is successful
        """
        if optimizer.finish_control.is_finished(optimizer.evaluation, optimizer.iteration, optimizer.elapsed_seconds()):
            return False
        if k < 1 or k > problem.dimension:
            return False
        start_sol:OnesCountMaxProblemBinaryIntSolution = solution.copy()
        best_sol:OnesCountMaxProblemBinaryIntSolution = solution.copy()
        better_sol_found:bool = False
        # initialize indexes
        indexes:ComplexCounterUniformAscending = ComplexCounterUniformAscending(k,problem.dimension)
        in_loop:bool = indexes.reset()
        while in_loop:
            # collect positions for inversion from indexes
            positions:list[int] = indexes.current_state()
            # invert and compare, switch of new is better
            mask:int = 0
            for i in positions:
                mask |= 1 << i
            solution.representation ^= mask 
            if optimizer.finish_control.is_finished(optimizer.evaluation, optimizer.iteration, optimizer.elapsed_seconds()):
                solution.copy_from(start_sol)
                return False
            optimizer.write_output_values_if_needed("before_evaluation", "b_e")
            optimizer.evaluation += 1
            solution.evaluate(problem)
            optimizer.write_output_values_if_needed("after_evaluation", "a_e")
            if optimizer.is_first_better(solution, best_sol, problem):
                better_sol_found = True
                best_sol.copy_from(solution)
            solution.representation ^= mask 
            # increment indexes and set in_loop accordingly
            in_loop = indexes.progress()
        if better_sol_found:
            solution.copy_from(best_sol)
            return True
        solution.copy_from(start_sol)
        return False

    def local_search_first_improvement(self, k:int, problem:OnesCountMaxProblem, solution:OnesCountMaxProblemBinaryIntSolution, 
            optimizer: Algorithm)->bool:
        """
        Executes "first improvement" variant of the local search procedure 
        
        :param int k: int parameter for VNS
        :param `OnesCountMaxProblem` problem: problem that is solved
        :param `OnesCountMaxProblemBinaryIntSolution` solution: solution used for the problem that is solved
        :param `Algorithm` optimizer: optimizer that is executed
        :return: result of the local search procedure 
        :rtype: if local search is successful
        """
        if optimizer.finish_control.is_finished(optimizer.evaluation, optimizer.iteration, optimizer.elapsed_seconds()):
            return False
        if k < 1 or k > problem.dimension:
            return False
        start_sol:OnesCountMaxProblemBinaryIntSolution = solution.copy()
        # initialize indexes
        indexes:ComplexCounterUniformAscending = ComplexCounterUniformAscending(k,problem.dimension)
        in_loop:bool = indexes.reset()
        while in_loop:
            # collect positions for inversion from indexes
            positions:list[int] = indexes.current_state()
            # invert and compare, switch and exit if new is better
            mask:int = 0
            for i in positions:
                mask |= 1 << i
            solution.representation ^= mask 
            if optimizer.finish_control.is_finished(optimizer.evaluation, optimizer.iteration, optimizer.elapsed_seconds()):
                solution.copy_from(start_sol)
                return False
            optimizer.write_output_values_if_needed("before_evaluation", "b_e")
            optimizer.evaluation += 1
            solution.evaluate(problem)
            optimizer.write_output_values_if_needed("after_evaluation", "a_e")
            if optimizer.is_first_better(solution, start_sol, problem):
                return True
            solution.representation ^= mask
            # increment indexes and set in_loop accordingly
            in_loop = indexes.progress()
        solution.copy_from(start_sol)
        return False

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the vns support instance

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
        return 'OnesCountMaxProblemBinaryIntSolutionVnsSupport'

    def __str__(self)->str:
        """
        String representation of the vns support instance

        :return: string representation of the vns support instance
        :rtype: str
        """
        return self.string_rep('|')

    def __repr__(self)->str:
        """
        Representation of the vns support instance

        :return: string representation of the vns support instance
        :rtype: str
        """
        return self.string_rep('\n')


    def __format__(self, spec:str)->str:
        """
        Formatted the vns support instance

        :param str spec: format specification
        :return: formatted vns support instance
        :rtype: str
        """
        return self.string_rep('|')
