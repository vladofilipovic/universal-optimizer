import sys
from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory)
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from dataclasses import dataclass
from copy import deepcopy
from datetime import datetime

import xarray as xr
from linopy import Model

from uo.utils.logger import logger

from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import TargetSolution
from uo.target_solution.target_solution_void_object_str import TargetSolutionVoidObjectStr
from uo.target_solution.target_solution import QualityOfSolution


from uo.algorithm.optimizer import Optimizer
from uo.algorithm.output_control import OutputControl

from opt.single_objective.teaching.ones_count_problem.ones_count_problem import OnesCountProblem

@dataclass
class OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters:
        """
        Instance of the class :class:`OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters` represents constructor parameters for max ones problem ILP solver.
        """
        output_control: OutputControl = None
        target_problem: TargetProblem = None

class OnesCountProblemIntegerLinearProgrammingSolution(TargetSolutionVoidObjectStr):
    def __init__(self, sol:'Solution')->None:
        super().__init__(name="OnesCountProblemIntegerLinearProgrammingSolution")
        self.__sol = sol

    def string_representation(self):
        return str(self.__sol)    

class OnesCountProblemIntegerLinearProgrammingSolver(Optimizer):

    def __init__(self, output_control:OutputControl,  problem:OnesCountProblem)->None:
        """
        Create new `OnesCountProblemIntegerLinearProgrammingSolver` instance

        :param `OutputControls` output_control: object that control output
        :param `OnesCountProblem` problem: problem to be solved
        """
        super().__init__("OnesCountProblemIntegerLinearProgrammingSolver", output_control=output_control, 
                target_problem=problem)
        self.__model = Model()

    @classmethod
    def from_construction_tuple(cls, 
            construction_params:OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters=None):
        """
        Additional constructor. Create new `OnesCountProblemIntegerLinearProgrammingSolver` instance from construction parameters

        :param `OnesCountProblemIntegerLinearProgrammingSolverConstructionParameters` construction_params: parameters for construction 
        """
        return cls(
            construction_tuple.output_control, 
            construction_tuple.target_problem)

    def __copy__(self):
        """
        Internal copy of the current algorithm

        :return:  new `OnesCountProblemIntegerLinearProgrammingSolver` instance with the same properties
        :rtype: :class:`OnesCountProblemIntegerLinearProgrammingSolver`
        """
        alg = deepcopy(self)
        return alg

    def copy(self):
        """
        Copy the current algorithm

        :return:  new `OnesCountProblemIntegerLinearProgrammingSolver` instance with the same properties
        :rtype: :class:``OnesCountProblemIntegerLinearProgrammingSolver``
        """
        return self.__copy__()

    @property
    def model(self)->Model:
        """
        Property getter for the ILP model
        
        :return: model of the problem 
        :rtype: `Model`
        """
        return self.__model    

    def optimize(self)->None:
        """
        Uses ILP model in order to solve OnesCountProblem
        """
        self.iteration = -1
        self.evaluation = -1
        self.execution_started = datetime.now() 
        l = []
        for i in range(self.target_problem.dimension):
            l.append(0)
        coords = xr.DataArray(l)
        x = self.model.add_variables(binary=True, coords=[coords], name='x')
        #logger.debug(self.model.variables)
        if self.target_problem.is_minimization:
            self.model.add_objective((x).sum())
        else:
            self.model.add_objective(-(x).sum())
        self.model.solve()
        self.execution_ended = datetime.now()
        self.write_output_values_if_needed("after_algorithm", "a_a")
        self.best_solution = OnesCountProblemIntegerLinearProgrammingSolution( self.model.solution.x )
        #logger.debug(self.model.solution.x)

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the 'OnesCountProblemIntegerLinearProgrammingSolver' instance
        
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
        String representation of the 'OnesCountProblemIntegerLinearProgrammingSolver' instance
        
        :return: string representation of the 'OnesCountProblemIntegerLinearProgrammingSolver' instance
        :rtype: str
        """
        return self.string_rep('|')

    def __repr__(self)->str:
        """
        Representation of the 'OnesCountProblemIntegerLinearProgrammingSolver' instance
        
        :return: string representation of the 'OnesCountProblemIntegerLinearProgrammingSolver' instance
        :rtype: str
        """
        return self.string_rep('\n')

    def __format__(self, spec:str)->str:
        """
        Formatted 'OnesCountProblemIntegerLinearProgrammingSolver' instance
        
        :param str spec: format specification
        :return: formatted 'OnesCountProblemIntegerLinearProgrammingSolver' instance
        :rtype: str
        """
        return self.string_rep('|')
