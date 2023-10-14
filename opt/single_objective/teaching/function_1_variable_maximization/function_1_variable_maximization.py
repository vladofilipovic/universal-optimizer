
import sys
from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent)

from copy import deepcopy

from typing import NamedTuple

from uo.utils.logger import logger

from uo.target_problem.target_problem import TargetProblem

Function1VariableMaximizationElements = NamedTuple('Function1VariableMaximizationElements', 
            [('expression',str), 
            ('domain_low',float), 
            ('domain_up',float)]
        )

class Function1VariableMaximization(TargetProblem):
    
    def __init__(self, expression:str, domain_low:float, domain_up:float)->None:
        super().__init__(name="Function1VariableMaximization", is_minimization=False)
        self.__expression:str = expression
        self.__domain_low:float = domain_low
        self.__domain_up:float = domain_up

    @classmethod
    def __load_from_file__(cls, file_path:str, data_format:str)->int:
        logger.debug("Load parameters: file path=" + str(file_path) 
                +  ", data format representation=" + data_format)
        if data_format=='txt':
                input_file = open(file_path, 'r')
                text_line = input_file.readline().strip()
                # skip comments
                while text_line.startswith("//") or text_line.startswith(";"):
                    text_line = input_file.readline()
                data:list[str] = text_line.split()
                if len(data)>=3:
                    return Function1VariableMaximizationElements(data[0], float(data[1]), float(data[2]))
                else:
                    raise ValueError('Invalid line \'{}\' - not enough data'.format(data))        
        else:
            raise ValueError('Value for data format \'{} \' is not supported'.format(data_format))

    @classmethod
    def from_input_file(cls, input_file_path:str, input_format:str):
        """
        Additional constructor. Create new `Function1VariableMaximization` instance when input file and input format are specified

        :param str input_file_path: path of the input file with problem data
        :param str input_format: format of the input
        """
        params:Function1VariableMaximizationElements = Function1VariableMaximization.__load_from_file__(input_file_path, 
                input_format)
        return cls(expression=params.expression, domain_low=params.domain_low, domain_up=params.domain_up)

    def __copy__(self):
        pr = deepcopy(self)
        return pr

    def copy(self):
        return self.__copy__()

    @property
    def expression(self)->str:
        return self.__expression

    @property
    def domain_low(self)->float:
        return self.__domain_low

    @property
    def domain_up(self)->float:
        return self.__domain_up

    @property
    def number_of_intervals(self)->int:
        return self.__number_of_intervals

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        s = delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_start
        s+= super().string_rep(delimiter, indentation, indentation_symbol, '', '')
        s+= delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s+= 'expression=' + self.expression
        s+= delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s+= 'domain_low=' + str(self.domain_low)
        s+= delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s+= 'domain_up=' + str(self.domain_up)
        s += group_end 
        return s

    def __str__(self)->str:
        return self.string_rep('|', 0, '', '{', '}')

    def __repr__(self)->str:
        return self.string_rep('\n', 0, '   ', '{', '}')

    def __format__(self, spec:str)->str:
        return self.string_rep('|')


