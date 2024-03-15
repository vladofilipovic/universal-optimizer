""" 
The :mod:`~uo.problem.problem` module describes the class :class:`~uo.problem.Problem`.
"""

from pathlib import Path
from typing import Optional
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

from copy import deepcopy
from abc import ABCMeta, abstractmethod

class Problem(metaclass=ABCMeta):
    """
    The `Problem` class represents a target problem for optimization. It is an abstract base class that provides a common interface for defining and manipulating target problems.

    Attributes:
        name (str): The name of the target problem.
        is_minimization (bool): Indicates whether the problem is a minimization problem.
        is_multi_objective (bool): Indicates whether the problem is a multi-objective optimization problem.

    Methods:
        __init__(name: str = "", is_minimization: Optional[bool] = None, is_multi_objective: Optional[bool] = None) -> None:
            Initializes a new `Problem` instance with the specified name, minimization flag, and multi-objective flag.
        
        __copy__() -> Problem:
            Creates a deep copy of the current target problem instance.
        
        copy() -> Problem:
            Creates a copy of the current target problem instance.
        
        name() -> str:
            Returns the name of the target problem.
        
        is_minimization() -> bool:
            Returns whether the problem is a minimization problem.
        
        is_multi_objective() -> bool:
            Returns whether the problem is a multi-objective optimization problem.
        
        string_rep(delimiter: str, indentation: int = 0, indentation_symbol: str = '', group_start: str = '{', group_end: str = '}') -> str:
            Returns a string representation of the target problem instance.
        
        __str__() -> str:
            Returns a string representation of the target problem instance.
        
        __repr__() -> str:
            Returns a string representation of the target problem instance.
        
        __format__(spec: str) -> str:
            Returns a formatted string representation of the target problem instance.
    """

    @abstractmethod
    def __init__(self, name:str = "", 
                is_minimization:Optional[bool]=None, 
                is_multi_objective:Optional[bool]=None)->None:
        """
        Create a new Problem instance.

        Parameters:
            name (str): The name of the target problem.
            is_minimization (bool, optional): Indicates whether the problem is a minimization problem. Defaults to None.
            is_multi_objective (bool, optional): Indicates whether the problem is a multi-objective optimization problem. Defaults to None.

        Raises:
            TypeError: If the 'name' parameter is not of type 'str'.
            TypeError: If the 'is_minimization' parameter is not of type 'bool' or None.
            TypeError: If the 'is_multi_objective' parameter is not of type 'bool' or None.
        """
        if not isinstance(name, str):
                raise TypeError('Parameter \'name\' must be \'str\'.')
        if not isinstance(is_minimization, bool) and is_minimization is not None:
                raise TypeError('Parameter \'is_minimization\' must be \'bool\' or have value None.')        
        if not isinstance(is_multi_objective, bool) and is_multi_objective is not None:
                raise TypeError('Parameter \'is_multi_objective\' must be \'bool\' or have value None.')        
        self.__name:str = name
        self.__is_minimization:Optional[bool] = is_minimization
        self.__is_multi_objective:Optional[bool] = is_multi_objective

    @abstractmethod
    def __copy__(self):
        """
        Internal copy of the current target problem

        :return:  new `Problem` instance with the same properties
        :rtype: Problem
        """
        pr = deepcopy(self)
        return pr
    @abstractmethod
    def copy(self):
        """
        Copy the current target problem

        :return: new `Problem` instance with the same properties
        :rtype: Problem
        """
        return self.__copy__()

    @property
    def name(self)->str:
        """
        Property getter for the name of the target problem
        
        :return: name of the target problem instance 
        :rtype: str
        """
        return self.__name

    @property
    def is_minimization(self)->bool:
        """
        Property getter for the info if problem optimization is minimization

        :return: bool -- if minimization takes place 
        """
        return self.__is_minimization


    @property
    def is_multi_objective(self)->bool:
        """
        Property getter for the info if problem optimization is multi objective

        :return: bool -- if optimization is multi objective
        """
        return self.__is_multi_objective

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
            group_end:str ='}')->str:
        """
        String representation of the target problem instance

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
        s =  delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_start + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'name=' + self.name + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'is_minimization=' + str(self.is_minimization) 
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the target problem instance

        :return: string representation of the target problem instance
        :rtype: str
        """
        return self.string_rep('|')

    @abstractmethod
    def __repr__(self)->str:
        """
        Representation of the target problem instance

        :return: string representation of the problem instance
        :rtype: str
        """
        return self.string_rep('\n')

    @abstractmethod
    def __format__(self, spec:str)->str:
        """
        Formatted the target problem instance

        :param str spec: format specification
        :return: formatted target problem instance
        :rtype: str
        """
        return self.string_rep('|')

