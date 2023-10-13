
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

class Function1VariableMaximization(TargetProblem):
    
    def __init__(self, file_path:str=None, dim:int=None)->None:
        super().__init__(name="Function1VariableMaximization", is_minimization=False, file_path=file_path, 
                dimension=dim)
        self.__expression:str = None
        self.__domain_low:float = None
        self.__domain_up:float = None
        self.__number_of_intervals:int = None

    @classmethod
    def from_string(cls, construction_string:str):
        return cls( 
            construction_tuple.finish_control,
            construction_tuple.random_seed, 
            construction_tuple.additional_statistics_control,
            construction_tuple.output_control, 
            construction_tuple.target_problem, 
            construction_tuple.initial_solution,
            construction_tuple.problem_solution_vns_support, 
            construction_tuple.k_min, 
            construction_tuple.k_max, 
            construction_tuple.local_search_type)

    @classmethod
    def from_file(cls, file_path:str):
        return cls( 
            construction_tuple.finish_control,
            construction_tuple.random_seed, 
            construction_tuple.additional_statistics_control,
            construction_tuple.output_control, 
            construction_tuple.target_problem, 
            construction_tuple.initial_solution,
            construction_tuple.problem_solution_vns_support, 
            construction_tuple.k_min, 
            construction_tuple.k_max, 
            construction_tuple.local_search_type)

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

    def load_from_file(self, data_format:str='txt')->None:
        logger.debug("Load parameters: file path=" + str(self.file_path) 
                +  ", data format representation=" + data_format)
        if data_format=='txt':
                input_file = open(self.file_path, 'r')
                text_line = input_file.readline().strip()
                # skip comments
                while text_line.startswith("//") or text_line.startswith(";"):
                    text_line = input_file.readline()
                data:list[str] = text_line.split()
                if len(data)>=4:
                    self.__expression = data[0]
                    self.__domain_low = float(data[1])
                    self.__domain_up = float(data[2])
                    self.number_of_intervals = int(data[3])
                else:
                    raise ValueError('Invalid line \'{}\' - not enough data'.format(data))        
        else:
            raise ValueError('Value for data format \'{} \' is not supported'.format(data_format))

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
        s+= 'domain_low=' + self.domain_low
        s+= delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s+= 'domain_up=' + self.domain_up
        s+= delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s+= 'number_of_intervals=' + self.number_of_intervals
        s += group_end 
        return s

    def __str__(self)->str:
        return self.string_rep('|', 0, '', '{', '}')

    def __repr__(self)->str:
        return self.string_rep('\n', 0, '   ', '{', '}')

    def __format__(self, spec:str)->str:
        return self.string_rep('|')


