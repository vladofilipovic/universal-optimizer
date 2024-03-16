""" 
The :mod:`~uo.algorithm.metaheuristic.metaheuristic` module describes the class :class:`~uo.algorithm.metaheuristic.metaheuristic.Metaheuristic`.
"""

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)

from random import random
from random import randrange
from copy import deepcopy
from datetime import datetime
from io import TextIOWrapper 

from bitstring import BitArray

from abc import ABCMeta, abstractmethod
from typing import Optional, TypeVar, Generic
from typing import Generic


from uo.utils.logger import logger

from uo.problem.problem import Problem
from uo.solution.solution import Solution

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl

from uo.algorithm.algorithm import Algorithm
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

class Metaheuristic(Algorithm, metaclass=ABCMeta):
    """
    This class represent metaheuristic
    """

    @abstractmethod
    def __init__(self, 
            name:str, 
            finish_control:FinishControl,
            random_seed:Optional[int], 
            additional_statistics_control:AdditionalStatisticsControl,
            output_control:OutputControl, 
            problem:Problem,
            solution_template:Solution
    )->None:
        """
        Create new Metaheuristic instance

        :param str name: name of the metaheuristic
        :param `FinishControl` finish_control: structure that control finish criteria for metaheuristic execution
        :param int random_seed: random seed for metaheuristic execution
        :param `AdditionalStatisticsControl` additional_statistics_control: structure that controls additional 
        statistic to be kept during metaheuristic evaluation        
        :param `OutputControl` output_control: structure that controls output
        :param `Problem` problem: problem to be solved
        :param `Solution` solution_template: solution template for the problem to be solved
        """
        if not isinstance(name, str):
                raise TypeError('Parameter \'name\' must be \'str\'.')
        if not isinstance(finish_control, FinishControl):
                raise TypeError('Parameter \'finish_control\' must be \'FinishControl\'.')
        if not isinstance(random_seed, Optional[int]):
                raise TypeError('Parameter \'random_seed\' must be \'int\' or \'None\'.')
        if not isinstance(additional_statistics_control, AdditionalStatisticsControl):
                raise TypeError('Parameter \'additional_statistics_control\' must be \'AdditionalStatisticsControl\'.')
        if not isinstance(output_control, OutputControl):
                raise TypeError('Parameter \'output_control\' must be \'OutputControl\'.')
        if not isinstance(problem, Problem):
                raise TypeError('Parameter \'problem\' must be \'Problem\'.')
        super().__init__(name=name, 
                output_control=output_control, 
                problem=problem,
                solution_template=solution_template)
        self.__finish_control = finish_control.copy()
        if random_seed is not None and isinstance(random_seed, int) and random_seed != 0:
            self.__random_seed:int = random_seed
        else:
            self.__random_seed:int = randrange(sys.maxsize)
        self.__additional_statistics_control:AdditionalStatisticsControl = additional_statistics_control

    @abstractmethod
    def __copy__(self):
        """
        Internal copy of the current metaheuristic

        :return: new `Metaheuristic` instance with the same properties
        :rtype: `Metaheuristic`
        """
        met = deepcopy(self)
        return met

    @abstractmethod
    def copy(self):
        """
        Copy the current metaheuristic
        
        :return: new `Metaheuristic` instance with the same properties
        :rtype: `Metaheuristic`
        """
        return self.__copy__()

    @property
    def finish_control(self)->FinishControl:
        """
        Property getter for the structure that controls finish criteria for metaheuristic execution
        
        :return: structure that controls finish criteria for metaheuristic execution 
        :rtype: `FinishControl`
        """
        return self.__finish_control

    @property
    def random_seed(self)->int:
        """
        Property getter for the random seed used during metaheuristic execution
        
        :return: random seed 
        :rtype: int
        """
        return self.__random_seed

    @property
    def additional_statistics_control(self)->AdditionalStatisticsControl:
        """
        Property getter for the structure that controls keeping of the statistic during metaheuristic execution
        
        :return: structure that controls that controls keeping of the statistic during metaheuristic execution 
        :rtype: `AdditionalStatisticsControl`
        """
        return self.__additional_statistics_control

    def elapsed_seconds(self)->float:
        """
        Calculate time elapsed during execution of the metaheuristic algorithm 
        
        :return: elapsed time (in seconds)
        :rtype: float
        """
        delta = datetime.now() - self.execution_started
        return delta.total_seconds()

    def update_additional_statistics_if_required(self, solution:Solution)->None:
        """
        Updates the additional statistics, if required.
        """
        if not isinstance(self.additional_statistics_control, AdditionalStatisticsControl):
            raise ValueError('Field \'additional_statistics_control\' must have type \'AdditionalStatisticsControl\'.')
        asc:AdditionalStatisticsControl = self.additional_statistics_control
        if not asc.is_active:
            return
        if asc.keep_all_solution_codes:
            asc.add_to_all_solution_codes(solution.string_representation())
        if asc.keep_more_local_optima:
            asc.add_to_more_local_optima(solution.string_representation(), self.best_solution.fitness_value, self.best_solution.string_representation())

    @abstractmethod
    def main_loop_iteration(self)->None:
        """
        One iteration within main loop of the metaheuristic algorithm
        """
        raise NotImplementedError

    def main_loop(self)->None:
        """
        Main loop of the metaheuristic algorithm
        """
        while (not self.finish_control.is_finished(self.evaluation, self.iteration, self.elapsed_seconds())):
            self.write_output_values_if_needed("before_iteration", "b_i")
            self.main_loop_iteration()
            self.write_output_values_if_needed("after_iteration", "a_i")
            logger.debug('Iteration: ' + str(self.iteration) 
                    + ', Evaluations: ' + str(self.evaluation) 
                    + ', Best solution objective: ' + str(self.best_solution.objective_value) 
                    + ', Best solution fitness: ' + str(self.best_solution.fitness_value) 
                    + ', Best solution: ' + str(self.best_solution.string_representation()))

    def optimize(self)->Solution:
        """
        Executing optimization by the metaheuristic algorithm
        """
        self.execution_started = datetime.now()
        self.init()
        self.write_output_headers_if_needed()
        self.write_output_values_if_needed("before_algorithm", "b_a")
        self.main_loop()
        self.execution_ended = datetime.now()
        self.write_output_values_if_needed("after_algorithm", "a_a")
        return self.best_solution

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
            group_end:str ='}')->str:
        """
        String representation of the Metaheuristic instance
        
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
        s = super().string_rep(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'random_seed=' + str(self.random_seed) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'finish_control=' + str(self.finish_control) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'additional_statistics_control=' + str(self.additional_statistics_control) + delimiter
        if self.execution_ended is not None and self.execution_started is not None:
            for _ in range(0, indentation):
                s += indentation_symbol  
            s += 'execution time=' + str( (self.execution_ended - self.execution_started).total_seconds() ) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the `Metaheuristic` instance
        
        :return: string representation of the `Metaheuristic` instance
        :rtype: str
        """
        s = self.string_rep('|')
        return s

    @abstractmethod
    def __repr__(self)->str:
        """
        String representation of the `Metaheuristic` instance
        
        :return: string representation of the `Metaheuristic` instance
        :rtype: str
        """
        s = self.string_rep('\n')
        return s

    @abstractmethod
    def __format__(self, spec:str)->str:
        """
        Formatted the `Metaheuristic` instance
        
        :param str spec: format specification
        :return: formatted `Metaheuristic` instance
        :rtype: str
        """
        return self.string_rep('|')
