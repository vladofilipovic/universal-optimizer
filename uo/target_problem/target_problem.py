""" 
The :mod:`~uo.target_problem.target_problem` module describes the class :class:`~uo.target_problem.TargetProblem`.
"""

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

from copy import deepcopy
from abc import ABCMeta, abstractmethod

class TargetProblem(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, name:str, is_minimization:bool, file_path:str, dimension:int=None)->None:
        """
        Create new TargetProblem instance

        :param str name: name of the target problem
        :param bool is_minimization: should minimum or maximum be determined
        :param str file_path: path of the file with data for the target problem instance 
        :param int dimension: dimension the target problem instance 
        """
        self.__name:str = name
        self.__is_minimization = is_minimization
        self.__file_path:str = file_path
        self.__dimension:int = dimension

    @abstractmethod
    def __copy__(self):
        """
        Internal copy of the current target problem

        :return:  new `TargetProblem` instance with the same properties
        :rtype: TargetProblem
        """
        pr = deepcopy(self)
        return pr

    @abstractmethod
    def copy(self):
        """
        Copy the current target problem

        :return: new `TargetProblem` instance with the same properties
        :rtype: TargetProblem
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
        Property getter for the name of the algorithm

        :return: bool -- if minimization takes place 
        """
        return self.__is_minimization

    @property
    def file_path(self)->str:
        """
        Property getter for the file path of the target problem

        :return: file path of the target problem instance 
        :rtype: str
        """
        return self.__file_path

    @property
    def dimension(self)->int:
        """
        Property getter for dimension of the target problem

        :return: dimension of the target problem instance 
        :rtype: int
        """
        return self.__dimension

    @dimension.setter
    def dimension(self, value:int)->None:
        """
        Property setter for dimension of the target problem
        """
        if value < 0:
            raise ValueError("Dimension less than 0 is not possible.")
        self.__dimension = value

    @abstractmethod
    def load_from_file(data_representation: str)->None:
        """
        Read target problem data from file and set intrinsic data

        :param str data_representation: data representation within file
        """
        raise NotImplementedError

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', group_end:str ='}')->str:
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
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_start + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'name=' + self.name + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'is_minimization=' + str(self.is_minimization) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'file path=' + str(self.file_path) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol 
        s += 'dimension=' + str(self.dimension) + delimiter
        for i in range(0, indentation):
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

