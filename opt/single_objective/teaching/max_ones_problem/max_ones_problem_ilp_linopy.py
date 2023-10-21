import sys
from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory)
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from copy import deepcopy
from datetime import datetime

import xarray as xr
from linopy import Model

from uo.utils.logger import logger

from uo.algorithm.algorithm import Algorithm

from opt.single_objective.teaching.max_ones_problem.max_ones_problem import MaxOnesProblem

class MaxOnesProblemIntegerLinearProgrammingSolver(Algorithm):

    def __init__(self, problem:MaxOnesProblem)->None:
        """
        Create new MaxOnesProblemIntegerLinearProgrammingSolver instance

        :param MaxOnesProblem problem: problem to be solved
        """
        super().__init__("MaxOnesProblemIntegerLinearProgrammingSolver", output_control=None, target_problem=problem)

    def __copy__(self):
        """
        Internal copy of the current algorithm

        :return:  new `MaxOnesProblemIntegerLinearProgrammingSolver` instance with the same properties
        :rtype: :class:`MaxOnesProblemIntegerLinearProgrammingSolver`
        """
        alg = deepcopy(self)
        return alg

    def copy(self):
        """
        Copy the current algorithm

        :return:  new `MaxOnesProblemIntegerLinearProgrammingSolver` instance with the same properties
        :rtype: :class:``MaxOnesProblemIntegerLinearProgrammingSolver``
        """
        return self.__copy__()

    def init(self)->None:
        """
        Initialization of the algorithm
        """
        return


    def solve(self):
        """
        Uses ILP model in order to solve MaxOnesProblem
        """
        self.execution_started = datetime.now
        m = Model()
        l = []
        for i in range(self.target_problem.dimension):
            l.append(0)
        coords = xr.DataArray(l)
        x = m.add_variables(binary=True, coords=[coords], name='x')
        logger.debug(m.variables)
        if self.target_problem.is_minimization:
            m.add_objective((x).sum())
        else:
            m.add_objective(-(x).sum())
        m.solve()
        self.execution_ended = datetime.now
        logger.debug(m.solution)

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the 'MaxOnesProblemIntegerLinearProgrammingSolver' instance
        
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
        s = super().string_rep(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the 'MaxOnesProblemIntegerLinearProgrammingSolver' instance
        
        :return: string representation of the 'MaxOnesProblemIntegerLinearProgrammingSolver' instance
        :rtype: str
        """
        return self.string_rep('|')

    def __repr__(self)->str:
        """
        Representation of the 'MaxOnesProblemIntegerLinearProgrammingSolver' instance
        
        :return: string representation of the 'MaxOnesProblemIntegerLinearProgrammingSolver' instance
        :rtype: str
        """
        return self.string_rep('\n')

    def __format__(self, spec:str)->str:
        """
        Formatted 'MaxOnesProblemIntegerLinearProgrammingSolver' instance
        
        :param str spec: format specification
        :return: formatted 'MaxOnesProblemIntegerLinearProgrammingSolver' instance
        :rtype: str
        """
        return self.string_rep('|')
