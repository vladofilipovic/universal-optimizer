""" 
..  _py_minimum_multi_cut_problem_bit_array_solution:

The :mod:`~opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem_binary_bit_array_solution` contains class :class:`~opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem_binary_bit_array_solution.MinimumMultiCutProblemBinaryBitArraySolution`, that represents solution of the :ref:`Problem_Minimum_Multi_Cut`, where `BitArray` representation of the problem has been used.
"""
import sys
from pathlib import Path
from typing import Optional
directory = Path(__file__).resolve()
sys.path.append(directory)
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent)

from copy import deepcopy
from random import choice
from random import random
import random as rnd
import networkx as nx

from bitstring import Bits, BitArray, BitStream, pack

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.quality_of_solution import QualityOfSolution
from uo.target_solution.target_solution import TargetSolution

from opt.single_objective.comb.minimum_multi_cut_problem.minimum_multi_cut_problem import MinimumMultiCutProblem

from uo.utils.logger import logger

class MinimumMultiCutProblemBinaryBitArraySolution(TargetSolution[BitArray,str]):
    
    def __init__(self, random_seed:Optional[int]=None, 
            evaluation_cache_is_used:bool=False, 
            evaluation_cache_max_size:int=0,
            distance_calculation_cache_is_used:bool=False,
            distance_calculation_cache_max_size:int=0)->None:
        """
        Create new `MinimumMultiCutProblemBinaryBitArraySolution` instance
        """
        if not isinstance(random_seed, int) and random_seed is not None:
            raise TypeError('Parameter \'random_seed\' must be \'int\' or \'None\'.')
        super().__init__(random_seed=random_seed, fitness_value=None, fitness_values=None,
                objective_value=None, objective_values=None, is_feasible=False, evaluation_cache_is_used=evaluation_cache_is_used,
                evaluation_cache_max_size=evaluation_cache_max_size,
                distance_calculation_cache_is_used=distance_calculation_cache_is_used,
                distance_calculation_cache_max_size=distance_calculation_cache_max_size)

    def __copy__(self)->'MinimumMultiCutProblemBinaryBitArraySolution':
        """
        Internal copy of the `MinimumMultiCutProblemBinaryBitArraySolution`

        :return: new `MinimumMultiCutProblemBinaryBitArraySolution` instance with the same properties
        :rtype: MinimumMultiCutProblemBinaryBitArraySolution
        """
        sol = super().__copy__()
        if self.representation is not None:
            sol.representation = BitArray(bin=self.representation.bin)
        else:
            sol.representation = None
        return sol

    def copy(self)->'MinimumMultiCutProblemBinaryBitArraySolution':
        """
        Copy the `MinimumMultiCutProblemBinaryBitArraySolution`
        
        :return: new `MinimumMultiCutProblemBinaryBitArraySolution` instance with the same properties
        :rtype: `MinimumMultiCutProblemBinaryBitArraySolution`
        """
        return self.__copy__()

    def copy_from(self, original)->None:
        """
        Copy all data from the original target solution
        """
        super().copy_from(original)
        if original.representation is not None:
            self.representation = BitArray(bin=self.representation.bin)
        else:
            self.representation = None
        
    def argument(self, representation:BitArray)->str:
        """
        Argument of the target solution

        :param representation: internal representation of the solution
        :type representation: `BitArray`
        :return: solution code
        :rtype: str 
        """
        return representation.bin

    def init_random(self, problem:TargetProblem)->None:
        """
        Random initialization of the solution

        :param `TargetProblem` problem: problem which is solved by solution
        """
        #logger.debug('Solution: ' + str(self))
        if problem.graph is None:
            raise ValueError('Can not randomly initialize solution without its graph.')
        if problem.source_terminal_pairs is None:
            raise ValueError('Can not randomly initialize solution with its source_terminal_pairs.')
        self.representation = BitArray(len(problem.graph.edges()))
        for i in range(len(self.representation)):
            if random() > 0.5:
                self.representation[i] = True

    def init_from(self, representation:BitArray, problem:TargetProblem)->None:
        """
        Initialization of the solution, by setting its native representation 

        :param BitArray representation: representation that will be ste to solution
        :param `TargetProblem` problem: problem which is solved by solution
        """
        if not isinstance(representation, BitArray):
            raise TypeError('Parameter \'representation\' must have type \'BitArray\'.')
        if len(representation) == 0:
            raise ValueError('Representation must have positive length.')
        self.representation = BitArray(bin=representation.bin)

    def is_feasable(self, representation:BitArray, graph: nx.Graph, source_terminal_pairs:list[tuple[int,int]]) -> bool:
        edges = list(graph.edges())
        new_graph = nx.Graph()
        nodes_to_insert = graph.nodes()
        new_graph.add_nodes_from(nodes_to_insert)  # to check

        for i in range(representation.len):
            if representation[i]:
                x,y = edges[i]
                new_graph.add_edge(x,y,weight = graph[x][y]['weight'])

        for x,y in source_terminal_pairs:
            if nx.has_path(new_graph,x,y):
                return False

        return True

    def calc_fitness(self, representation:BitArray, graph: nx.Graph, source_terminal_pairs:list[tuple[int,int]]) -> tuple[int,float]:
        if not self.is_feasable(representation, graph, source_terminal_pairs):
            return (float('inf'), float('-inf'))
            
        edges = list(graph.edges())
        value = 0
        for i in range(representation.len):
            if not representation[i]:
                x,y = edges[i]
                value += graph[x][y]['weight']

        if value == 0:
            return (0, float('inf'))
        return (value, 1/value)

    def calculate_quality_directly(self, representation:BitArray, 
            problem:MinimumMultiCutProblem)->QualityOfSolution:
        """
        Fitness calculation of the minimum multi cut binary BitArray solution

        :param BitArray representation: native representation of solution whose fitness is calculated
        :param TargetProblem problem: problem that is solved
        :return: objective value, fitness value and feasibility of the solution instance
        :rtype: `QualityOfSolution`
        """
        is_valid = self.is_feasable(representation, problem.graph, problem.source_terminal_pairs)
        objective, fitness = self.calc_fitness(representation, problem.graph, problem.source_terminal_pairs)
        return QualityOfSolution(objective, None, objective, None, is_valid)

    def native_representation(self, representation_str:str)->BitArray:
        """
        Obtain `BitArray` representation from string representation of the BitArray binary solution of the Minimum Multi Cut problem 

        :param str representation_str: solution's representation as string
        :return: solution's representation as BitArray
        :rtype: `BitArray`
        """
        if not isinstance(representation_str, str):
            raise TypeError('Representation argument have to be string.')
        ret:BitArray = BitArray(bin=representation_str)
        return ret

    def representation_distance_directly(self, solution_code_1:str, solution_code_2:str)->float:
        """
        Calculating distance between two solutions determined by its code

        :param str solution_code_1: solution code for the first solution
        :param str solution_code_2: solution code for the second solution
        :return: distance between two solutions represented by its code
        :rtype: float
        """
        rep_1:BitArray = self.native_representation(solution_code_1)
        rep_2:BitArray = self.native_representation(solution_code_2)
        result = (rep_1 ^ rep_2).count(True)
        return result 

    def string_rep(self, delimiter:str='\n', indentation:int=0, indentation_symbol:str='   ', 
            group_start:str='{', group_end:str='}',)->str:
        """
        String representation of the solution instance

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
        :return: string representation of instance that controls output
        :rtype: str
        """        
        s = delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_start
        s += super().string_rep(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        s += delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'string_representation()=' + self.string_representation()
        s += delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the solution instance

        :return: string representation of the solution instance
        :rtype: str
        """
        return self.string_rep('\n', 0, '   ', '{', '}')

    def __repr__(self)->str:
        """
        Representation of the solution instance

        :return: string representation of the solution instance
        :rtype: str
        """
        return self.string_rep('\n', 0, '   ', '{', '}')

    def __format__(self, spec:str)->str:
        """
        Formatted the solution instance

        :param str spec: format specification
        :return: formatted solution instance
        :rtype: str
        """
        return self.string_rep('\n', 0, '   ', '{', '}')

