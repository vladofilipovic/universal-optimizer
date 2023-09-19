""" 
..  _py_max_ones_problem_bit_array_solution_vns_support:

The :mod:`~opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_bit_array_solution_vns_support` contains class :class:`~opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_bit_array_solution_vns_support.MaxOnesProblemBinaryBitArraySolutionVnsSupport`, that represents supporting parts of the `VNS` algorithm, where solution of the :ref:`Problem_Max_Ones` have `BitArray` representation.
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
from bitstring import BitArray

from uo.utils.logger import logger
from uo.target_solution.target_solution import ObjectiveFitnessFeasibility
from uo.algorithm.metaheuristic.variable_neighborhood_search.problem_solution_vns_support import ProblemSolutionVnsSupport

from opt.single_objective.trivial.max_ones_problem.max_ones_problem import MaxOnesProblem
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_bit_array_solution import MaxOnesProblemBinaryBitArraySolution

class MaxOnesProblemBinaryBitArraySolutionVnsSupport(ProblemSolutionVnsSupport):
    
    def __init__(self)->None:
        """
        Create new `MaxOnesProblemBinaryBitArraySolutionVnsSupport` instance
        """
        return

    def __copy__(self):
        """
        Internal copy of the `MaxOnesProblemBinaryBitArraySolutionVnsSupport`

        :return: new `MaxOnesProblemBinaryBitArraySolutionVnsSupport` instance with the same properties
        :rtype: `MaxOnesProblemBinaryBitArraySolutionVnsSupport`
        """
        sol = deepcopy(self)
        return sol

    def copy(self):
        """
        Copy the `MaxOnesProblemBinaryBitArraySolutionVnsSupport` instance

        :return: new `MaxOnesProblemBinaryBitArraySolutionVnsSupport` instance with the same properties
        :rtype: `MaxOnesProblemBinaryBitArraySolutionVnsSupport`
        """
        return self.__copy__()

    def shaking(self, k:int, problem:MaxOnesProblem, solution:MaxOnesProblemBinaryBitArraySolution, optimizer:Algorithm)->bool:
        """
        Random shaking of k parts such that new solution code does not differ more than k from all solution codes 
        inside shakingPoints 

        :param int k: int parameter for VNS
        :param `MaxOnesProblem` problem: problem that is solved
        :param `MaxOnesProblemBinaryBitArraySolution` solution: solution used for the problem that is solved
        :param `Algorithm` optimizer: optimizer that is executed
        :return: if randomization is successful
        :rtype: bool
        """    
        tries:int = 0
        limit:int = 10000
        while tries < limit:
            positions:list[int] = []
            for i in range(0,k):
                positions.append(choice(range(k)))
            new_representation:BitArray = deepcopy(solution.representation)
            new_representation.invert(positions)
            all_ok:bool = True
            #logger.debug(solution_codes)
            for sc in solution_codes:
                sc_representation = solution.native_representation_from_solution_code(sc)
                if sc_representation is not None and sc_representation != '':
                    comp_result:int = (sc_representation ^ new_representation).count(value=1)
                    if comp_result > k:
                        all_ok = False
            if all_ok:
                break
        if tries < limit:
            solution.representation = new_representation
            solution.evaluate(problem)
            return True
        else:
            return False 

    def __change_bit_find_best_helper__(self, problem:MaxOnesProblem, solution:MaxOnesProblemBinaryBitArraySolution, 
            optimizer: Algorithm)->bool:
        """
        Improving the best solution by inverting one bit of the representation, e.g. with "best improvement" approach 

        :param `MaxOnesProblem` problem: problem that is solved
        :param `MaxOnesProblemBinaryBitArraySolution` solution: solution that is potentially improved
        :param `Algorithm` optimizer: optimizer that is executed
        :return: if the best one is changed, or not
        :rtype: bool
        """        
        best_ind:int = None
        best_fv:float = solution.fitness_value
        for i in range(0, len(solution.representation)):
            solution.representation.invert(i) 
            optimizer.evaluation += 1
            new_fv = solution.calculate_objective_fitness_feasibility(problem).fitness_value
            if new_fv > best_fv:
                best_ind = i
                best_fv = new_fv
            solution.representation.invert(i)
        if best_ind is not None:
            solution.representation.invert(best_ind)
            optimizer.evaluation += 1
            solution.evaluate(problem)
            if solution.fitness_value != best_fv:
                raise ValueError('Fitness calculation within function `change_bit_find_best_helper` is not correct.')
            return True
        return False

    def local_search_best_improvement(self, k:int, problem:MaxOnesProblem, solution:MaxOnesProblemBinaryBitArraySolution, 
            optimizer: Algorithm)->MaxOnesProblemBinaryBitArraySolution:
        """
        Executes "best improvement" variant of the local search procedure 
        
        :param int k: int parameter for VNS
        :param `MaxOnesProblem` problem: problem that is solved
        :param `MaxOnesProblemBinaryBitArraySolution` solution: solution used for the problem that is solved
        :param `Algorithm` optimizer: optimizer that is executed
        :return: result of the local search procedure 
        :rtype: MaxOnesProblemBinaryBitArraySolution
        """
        while True:
            if not self.__change_bit_find_best_helper__(problem, solution, optimizer):
                break
        return solution

    def __change_bit_find_better_helper__(self, problem:MaxOnesProblem, solution:MaxOnesProblemBinaryBitArraySolution, 
            optimizer: VnsOptimizer)->bool:
        """
        Improving the best solution by inverting one bit of the representation, e.g. with "first improvement" approach 

        :param `MaxOnesProblem` problem: problem that is solved
        :param `MaxOnesProblemBinaryBitArraySolution` solution: solution that is potentially improved
        :param `Algorithm` optimizer: optimizer that is executed
        :return: if the best one is changed, or not
        :rtype: bool
        """        
        best_ind:int = None
        best_fv:float = solution.fitness_value
        for i in range(0, len(solution.representation)):
            solution.representation.invert(i) 
            optimizer.evaluation += 1
            new_fv = solution.calculate_objective_fitness_feasibility(problem).fitness_value
            if new_fv > best_fv:
                best_ind = i
                best_fv = new_fv
                solution.representation.invert(best_ind) 
                optimizer.evaluation += 1 
                solution.evaluate(problem)
                if solution.fitness_value != best_fv:
                    raise Exception('Fitness calculation within `change_bit_find_better_helper` function is not correct.')
                return True
        return False

    def local_search_first_improvement(self, k:int, problem:MaxOnesProblem, solution:MaxOnesProblemBinaryBitArraySolution, 
            optimizer: Algorithm)->MaxOnesProblemBinaryBitArraySolution:
        """
        Executes "first improvement" variant of the local search procedure 
        
        :param int k: int parameter for VNS
        :param `MaxOnesProblem` problem: problem that is solved
        :param `MaxOnesProblemBinaryBitArraySolution` solution: solution used for the problem that is solved
        :param `Algorithm` optimizer: optimizer that is executed
        :return: result of the local search procedure 
        :rtype: MaxOnesProblemBinaryBitArraySolution
        """
        while True:
            if not self.__change_bit_find_better_helper__(problem, solution, optimizer):
                break
        return solution

    def string_representation(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the vns support structure

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
        return 'MaxOnesProblemBinaryBitArraySolutionVnsSupport'

    def __str__(self)->str:
        """
        String representation of the vns support instance

        :return: string representation of the vns support instance
        :rtype: str
        """
        return self.string_representation('|')

    def __repr__(self)->str:
        """
        Representation of the vns support instance

        :return: string representation of the vns support instance
        :rtype: str
        """
        return self.string_representation('\n')


    def __format__(self, spec:str)->str:
        """
        Formatted the vns support instance

        :param str spec: format specification
        :return: formatted vns support instance
        :rtype: str
        """
        return self.string_representation('|')


