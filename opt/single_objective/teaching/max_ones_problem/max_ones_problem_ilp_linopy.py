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
from uo.target_solution.target_solution import QualityOfSolution


from uo.algorithm.optimizer import Optimizer
from uo.algorithm.output_control import OutputControl

from opt.single_objective.teaching.max_ones_problem.max_ones_problem import MaxOnesProblem

@dataclass
class MaxOnesProblemIntegerLinearProgrammingSolverConstructionParameters:
        """
        Instance of the class :class:`MaxOnesProblemIntegerLinearProgrammingSolverConstructionParameters` represents constructor parameters for max ones problem ILP solver.
        """
        output_control: OutputControl = None
        target_problem: TargetProblem = None

class MaxOnesProblemIntegerLinearProgrammingSolution(TargetSolution[object, str]):
    def __init__(self, sol:'Solution')->None:
        super().__init__("MaxOnesProblemIntegerLinearProgrammingSolution",
        random_seed=None, fitness_value=0, objective_value=0, is_feasible=True,
        evaluation_cache_is_used=False, evaluation_cache_max_size=0, 
        distance_calculation_cache_is_used=False, distance_calculation_cache_max_size=0)
        self.__sol = sol

    def string_representation(self):
        return str(self.__sol)    

    def __copy__(self):
        pr = deepcopy(self)
        return pr

    def copy(self):
        return self.__copy__()

    def copy_to(self, destination)->None:
        destination = copy(self)

    def argument(self, representation:object)->str:
        return str(representation)

    def init_random(self, problem:TargetProblem)->None:
        self.representation = None
        return

    def init_from(self, representation:object, problem:TargetProblem)->None:
        self.representation = representation

    def native_representation(self, representation_str:str)->object:
        return representation_str

    def calculate_quality_directly(self, representation:object, 
            problem:TargetProblem)->QualityOfSolution:
        return QualityOfSolution(0, 0, True)

    def representation_distance_directly(solution_code_1:str, solution_code_2:str)->float:
        return 0

    def __str__(self)->str:
        return str(self.__sol)

    def __repr__(self)->str:
        return self.__repr__()

    def __format__(self, spec:str)->str:
        return self.__format__()    


class MaxOnesProblemIntegerLinearProgrammingSolver(Optimizer):

    def __init__(self, output_control:OutputControl,  problem:MaxOnesProblem)->None:
        """
        Create new `MaxOnesProblemIntegerLinearProgrammingSolver` instance

        :param `OutputControls` output_control: object that control output
        :param `MaxOnesProblem` problem: problem to be solved
        """
        super().__init__("MaxOnesProblemIntegerLinearProgrammingSolver", output_control=output_control, 
                target_problem=problem)
        self.__model = Model()

    @classmethod
    def from_construction_tuple(cls, 
            construction_params:MaxOnesProblemIntegerLinearProgrammingSolverConstructionParameters=None):
        """
        Additional constructor. Create new `MaxOnesProblemIntegerLinearProgrammingSolver` instance from construction parameters

        :param `MaxOnesProblemIntegerLinearProgrammingSolverConstructionParameters` construction_params: parameters for construction 
        """
        return cls(
            construction_tuple.output_control, 
            construction_tuple.target_problem)

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
        Uses ILP model in order to solve MaxOnesProblem
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
        self.best_solution = MaxOnesProblemIntegerLinearProgrammingSolution( self.model.solution.x )
        #logger.debug(self.model.solution.x)

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
