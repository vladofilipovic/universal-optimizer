""" 
..  _py_max_ones_problem:

The :mod:`~app.max_ones_problem.max_ones_problem` contains class :class:`~app.max_ones_problem.max_ones_problem.MaxOnesProblem`, that represents :ref:`Problem_Max_Ones`.
"""
import sys
from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)

from copy import deepcopy

from uo.target_problem.target_problem import TargetProblem

from app.utils.logger import logger

class MaxOnesProblem(TargetProblem):
    
    def __init__(self, file_path:str)->None:
        """
        Create new MaxOnesProblem instance
        :param file_path:str -- path of the file with data for the parget problem instance 
        """
        super().__init__("MaxOnesProblem", False, file_path)

    def __copy__(self):
        """
        Internal copy of the MaxOnesProblem problem
        :return: MaxOnesProblem -- new MaxOnesProblem instance with the same properties
        """
        pr = deepcopy(self)
        return pr

    def copy(self):
        """
        Copy the MaxOnesProblem problem
        :return: MaxOnesProblem -- new MaxOnesProblem instance with the same properties
        """
        return self.__copy__()

    def load_from_file(self, data_format:str='txt')->None:
        """
        Read target problem data from file
        :param data_format: str -- data format of the file
        """
        logger.debug("Load parameters: file path={}, data format representation={}".format(self.file_path, 
                data_format))
        if data_format=='txt':
                input_file = open(self.file_path, 'r')
                text_line = input_file.readline().strip()
                # skip comments
                while text_line.startswith("//") or text_line.startswith(";"):
                    text_line = input_file.readline()
                self.dimension = int( text_line.split()[0] )
        else:
            raise ValueError('Value for data format \'{} \' is not supported'.format(data_format))

    def string_representation(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the target solution instance
        :param delimiter: str -- delimiter between fields
        :param indentation:int -- level of indentation
        :param indentation_symbol:str -- indentation symbol
        :param group_start -- group start string 
        :param group_end -- group end string 
        :return: str -- string representation of target solution instance
        """          
        s = delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_start
        s+= super().string_representation(delimiter, indentation, indentation_symbol, '', '')
        s+= delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the target problem instance
        :return: str -- string representation of the target problem instance
        """
        return self.string_representation('|', 0, '', '{', '}')


    def __repr__(self)->str:
        """
        Representation of the target problem instance
        :return: str -- string representation of the problem instance
        """
        return self.string_representation('\n', 0, '   ', '{', '}')

    def __format__(self, spec:str)->str:
        """
        Formatted the target problem instance
        :param spec: str -- format specification
        :return: str -- formatted target problem instance
        """
        return self.string_representation('|')


