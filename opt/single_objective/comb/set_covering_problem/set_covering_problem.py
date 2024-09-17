""" 
..  _py_set_covering_problem:
"""

import sys
from pathlib import Path
from typing import Optional
from typing import Set
directory = Path(__file__).resolve()
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent)

from copy import deepcopy

from linopy import Model
import json

from uo.problem.problem import Problem
from uo.utils.logger import logger

class SetCoveringProblem(Problem):
    """
    Class representing the Minimum Set Covering Problem.

    This class inherits from the TargetProblem class and is used to define and solve the Set Covering Problem Problem. The problem is defined by a set U and a list of subsets of U named S.
    
    Attributes:
        universe (Set[int]): set of elements U that should be covered.
        subsets (list[Set[int]]): list of subsets. Each subset covers some of the elements form U.
    
    Methods:
        __init__(universe: Set[int], subsets: list[Set[int]]): Initializes a new instance of the SetCoveringProblem class.
        
        __load_from_files__(universe_file_path: str, subsets_file_path: str) -> tuple: Static function that reads problem data from files.
        from_input_files(universe_file_path: str, subsets_file_path: str): Creates a new SetCoveringProblem instance when the input file and input format are specified.
        __copy__() -> SetCoveringProblem: Internal copy of the SetCoveringProblem problem.
        copy() -> SetCoveringProblem: Copy the SetCoveringProblem problem.
        universe() -> Set[int]: Property getter for the set that should be covered in the target problem.
        subsets() -> list[Set[int]]: Property getter for the list of subsets S of the target problem.
        dimension() -> int: Property getter for the dimension of the target problem.
        string_rep(delimiter: str, indentation: int = 0, indentation_symbol: str = '', group_start: str = '{', group_end: str = '}') -> str: String representation of the SetCoveringProblem instance.
        __str__() -> str: String representation of the SetCoveringProblem structure.
        __repr__() -> str: Representation of the SetCoveringProblem instance.
        __format__() -> str: Formatted SetCoveringProblem instance.
    """

    def __init__(self, universe:Set[int], subsets:list[Set[int]])->None:
        """
        Create new `SetCoveringProblem` instance

        :param Set[int] universe: initial set U that should be covered in the problem
        :param list[Set[int]] subsets: list of subsets S that should cover U in the problem
        """
        if not isinstance(universe, set):
            raise TypeError('Parameter \'universe\' for  SetCoveringProblem should be a \'set\'.')
        if not isinstance(subsets, list):
            raise TypeError('Parameter \'subsets\' for  SetCoveringProblem should be \'list\'.')
        super().__init__(name="SetCoveringProblem", is_minimization=True, is_multi_objective=False)
        self.__universe = universe
        self.__subsets = subsets
        self.__dimension = len(subsets)

    @classmethod
    def from_universe_and_subset_files(cls, universe:Set[int], subsets:list):
        """
        Additional constructor. Create new `SetCoveringProblem` instance where the universe and subsets are specified.
        
        :param Set[int] universe: initial set U that should be covered in the problem
        :param list[Set[int]] subsets: list of subsets S that should cover U in the problem
        """
        return cls(universe, subsets)

    @classmethod
    def __load_from_files__(cls,universe_file_path: str, subsets_file_path: str)->tuple:
        """
        Static function that reads problem data from specified files
        
        :param str universe_file_path: path to the file that contains elements of the set U
        :param str subsets_file_path: path to the file that contains list of subsets and their elements
        :return: all data that describe problem
        :rtype: tuple
        """
        logger.debug("Load parameters: universe file path=" + str(universe_file_path) + ",  subsets file path=" + str(subsets_file_path))
        with open(universe_file_path, 'r') as universe_file:
            universe = set(universe_file.read().splitlines())
        with open(subsets_file_path, 'r') as subset_file:
            subsets = json.load(subset_file)

        return universe, subsets

    @classmethod
    def from_input_files(cls, universe_file_path: str, subsets_file_path: str)->'SetCoveringProblem':
        """
        Additional constructor. Create new `SetCoveringProblem` instance when input file and input format are specified
        
        :param str universe_file_path: path to the file that contains elements of the set U
        :param str subsets_file_path: path to the file that contains list of subsets and their elements
        :return: class instance
        :rtype: MinimumMultiCutProblem
        """
        result:tuple = SetCoveringProblem.__load_from_file__(universe_file_path, subsets_file_path)
        universe:Set[int] = result[0]
        subsets:list[Set[int]] = result[1]

        return cls(universe = universe,subsets = subsets)

    def __copy__(self)->'SetCoveringProblem':
        """
        Internal copy of the `SetCoveringProblem` problem
        
        :return: new `SetCoveringProblem` instance with the same properties
        :rtype: `SetCoveringProblem`
        """
        pr = deepcopy(self)
        return pr

    def copy(self)->'SetCoveringProblem':
        """
        Copy the `SetCoveringProblem` problem
        
        :return: new `SetCoveringProblem` instance with the same properties
        :rtype: SetCoveringProblem
        """
        return self.__copy__()

    @property
    def universe(self)->Set[int]:
        """
        Property getter for the initial set U of the target problem
        
        :return: set U of the target problem instance 
        :rtype: Set[int]
        """
        return self.__universe

    @property
    def subsets(self)->list[Set[int]]:
        """
        Property getter for the list of subsets S of the target problem
        
        :return: list of subsets S of the target problem instance 
        :rtype: list
        """
        return self.__subsets

    @property
    def dimension(self)->int:
        """
        Property getter for dimension of the target problem

        :return: dimension of the target problem instance 
        :rtype: int
        """
        return self.__dimension

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the `SetCoveringProblem` instance
        
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
        s+= super().string_rep(delimiter, indentation, indentation_symbol, '', '')
        s+= delimiter
        s += 'universe = ' + str(self.__universe)
        s += delimiter
        s += 'subsets=' + str(self.__subsets)
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the set covering problem structure
        
        :return: string representation of the set covering problem structure
        :rtype: str
        """
        return self.string_rep('|', 0, '', '{', '}')


    def __repr__(self)->str:
        """
        Representation of the set covering problem instance
        
        :return: str -- string representation of the set covering problem instance
        """
        return self.string_rep('\n', 0, '   ', '{', '}')

    def __format__(self)->str:
        """
        Formatted the set covering problem instance
        
        :return: str -- formatted set covering problem instance
        """
        return self.string_rep('|')