""" 
..  _py_max_ones_problem:

The :mod:`~opt.single_objective.trivial.max_ones_problem.max_ones_problem` contains class :class:`~opt.single_objective.trivial.max_ones_problem.max_ones_problem.MaxOnesProblem`, that represents :ref:`Problem_Max_Ones`.
"""
import sys
from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent)

from copy import deepcopy

from uo.target_problem.target_problem import TargetProblem

from uo.utils.logger import logger

class MaxOnesProblem(TargetProblem):
    
    def __init__(self, file_path:str=None, dim:int=None)->None:
        """
        Create new `MaxOnesProblem` instance

        :param str file_path: path of the file with data for the parget problem instance 
        :param int dim: dimension of the problem
        """
        super().__init__(name="MaxOnesProblem", is_minimization=False, file_path=file_path, dimension=dim)


    def __copy__(self):
        """
        Internal copy of the `MaxOnesProblem` problem

        :return: new `MaxOnesProblem` instance with the same properties
        :rtype: `MaxOnesProblem`
        """
        pr = deepcopy(self)
        return pr

    def copy(self):
        """
        Copy the `MaxOnesProblem` problem

        :return: new `MaxOnesProblem` instance with the same properties
        :rtype: MaxOnesProblem
        """
        return self.__copy__()

    def load_from_file(self, data_format:str='txt')->None:
        """
        Read target problem data from file

        :param str data_format: data format of the file
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
        String representation of the `MaxOneProblem` instance

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
        String representation of the max ones problem structure

        :return: string representation of the max ones problem structure
        :rtype: str
        """
        return self.string_representation('|', 0, '', '{', '}')


    def __repr__(self)->str:
        """
        Representation of the max ones problem instance
        :return: str -- string representation of the max ones problem instance
        """
        return self.string_representation('\n', 0, '   ', '{', '}')

    def __format__(self, spec:str)->str:
        """
        Formatted the max ones problem instance
        :param spec: str -- format specification
        :return: str -- formatted max ones problem instance
        """
        return self.string_representation('|')


