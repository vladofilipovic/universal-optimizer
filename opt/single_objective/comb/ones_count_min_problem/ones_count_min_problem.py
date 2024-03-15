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

from uo.problem.problem import Problem
from uo.utils.logger import logger


class OnesCountMinProblem(Problem):
    
    def __init__(self, dim:int)->None:
        """
        Create new `OnesCountMinProblem` instance

        :param int dim: dimension of the problem
        """
        if not isinstance(dim, int):
            raise TypeError('Parameter \'dimension\' for  OnesCountMinProblem should be \'int\'.')
        if dim <= 0:
            raise ValueError('Parameter \'dimension\' for  OnesCountMinProblem should be greater than zero.')
        super().__init__(name="OnesCountMinProblem", is_minimization=True, is_multi_objective=False)
        self.__dimension = dim
        
        
    @classmethod
    def from_dimension(cls, dimension:int):
        """
        Additional constructor. Create new `OnesCountMinProblem` instance when dimension is specified

        :param int dimension: dimension of the problem
        """
        return cls(dim=dimension)


    @classmethod
    def __load_from_file__(cls, file_path:str, data_format:str)->int:
        """
        Static function that read problem data from file

        :param str file_path: path of the file with problem data
        :param str data_format: data format of the file

        :return: all data that describe problem
        :rtype: int
        """
        logger.debug("Load parameters: file path=" + str(file_path) 
                +  ", data format representation=" + data_format)
        if data_format=='txt':
                input_file = open(file_path, 'r')
                text_line = input_file.readline().strip()
                # skip comments
                while text_line.startswith("//") or text_line.startswith(";"):
                    text_line = input_file.readline()
                dimension = int( text_line.split()[0] )
                return dimension
        else:
            raise ValueError('Value for data format \'{} \' is not supported'.format(data_format))

    @classmethod
    def from_input_file(cls, input_file_path:str, input_format:str):
        """
        Additional constructor. Create new `OnesCountMinProblem` instance when input file and input format are specified

        :param str input_file_path: path of the input file with problem data
        :param str input_format: format of the input
        """
        dimension:int = OnesCountMinProblem.__load_from_file__(input_file_path, input_format)
        if dimension is None or str(dimension).strip() == '':
            raise ValueError('Loading from file \'{}\' produces invalid dimension'.format(input_file_path))
        return cls(dim=dimension)

    def __copy__(self):
        """
        Internal copy of the `OnesCountMinProblem` problem

        :return: new `OnesCountMinProblem` instance with the same properties
        :rtype: `OnesCountMinProblem`
        """
        pr = deepcopy(self)
        return pr

    def copy(self):
        """
        Copy the `OnesCountMinProblem` problem

        :return: new `OnesCountMinProblem` instance with the same properties
        :rtype: OnesCountMinProblem
        """
        return self.__copy__()

    @property
    def dimension(self)->int:
        """
        Property getter for dimension of the ones count min problem.

        :return: dimension of the target problem instance 
        :rtype: int
        """
        return self.__dimension

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
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
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_start
        s+= super().string_rep(delimiter, indentation, indentation_symbol, '', '')
        s+= delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'dimension=' + str(self.dimension) + delimiter
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the max ones problem structure

        :return: string representation of the max ones problem structure
        :rtype: str
        """
        return self.string_rep('|', 0, '', '{', '}')


    def __repr__(self)->str:
        """
        Representation of the max ones problem instance
        :return: str -- string representation of the max ones problem instance
        """
        return self.string_rep('\n', 0, '   ', '{', '}')

    def __format__(self, spec:str)->str:
        """
        Formatted the max ones problem instance
        :param spec: str -- format specification
        :return: str -- formatted max ones problem instance
        """
        return self.string_rep('|')
