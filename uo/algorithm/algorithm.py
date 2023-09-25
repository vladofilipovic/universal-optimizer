""" 
The :mod:`~uo.algorithm.algorithm` module describes the class :class:`~uo.algorithm.Algorithm`.
"""

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

from copy import deepcopy
from datetime import datetime
from abc import ABCMeta, abstractmethod

from uo.utils.logger import logger
from uo.algorithm.output_control import OutputControl
from uo.target_problem.target_problem import TargetProblem
from uo.target_solution.target_solution import TargetSolution

    
class Algorithm(metaclass=ABCMeta):
    """
    This class describes Algorithm
    """

    @abstractmethod
    def __init__(self, name:str, output_control:OutputControl,  target_problem:TargetProblem)->None:
        """
        Create new Algorithm instance

        :param str name: name of the algorithm
        :param int evaluations_max: maximum number of evaluations for algorithm execution
        :param int seconds_max: maximum number of seconds for algorithm execution
        :param `OutputControl` output_control: structure that controls output
        :param `TargetProblem` target_problem: problem to be solved
        """
        self.__name:str = name
        self.__output_control:OutputControl = output_control
        if isinstance(target_problem, TargetProblem):
            self.__target_problem:TargetProblem = target_problem.copy()
        else:
            self.__target_problem:TargetProblem = target_problem
        self.__best_solution:TargetSolution = None
        self.__evaluation:int = 0
        self.__execution_started:datetime = None
        self.__execution_ended:datetime = None
        self.__iteration:int = 0
        self.__iteration_best_found:int = 0
        self.__second_when_best_obtained:float = 0.0

    @abstractmethod
    def __copy__(self):
        """
        Internal copy of the current algorithm

        :return:  new `Algorithm` instance with the same properties
        :rtype: :class:`uo.algorithm.Algorithm`
        """
        alg = deepcopy(self)
        return alg

    @abstractmethod
    def copy(self):
        """
        Copy the current algorithm

        :return:  new `Algorithm` instance with the same properties
        :rtype: :class:`uo.algorithm.Algorithm`
        """
        return self.__copy__()

    @property
    def name(self)->str:
        """
        Property getter for the name of the algorithm
        
        :return: name of the algorithm instance 
        :rtype: str
        """
        return self.__name

    @property
    def target_problem(self)->TargetProblem:
        """
        Property getter for the target problem to be solved
        
        :return TargetProblem: target problem to be solved 
        """
        return self.__target_problem

    @property
    def evaluation(self)->int:
        """
        Property getter for current number of evaluations during algorithm execution
        
        :return: current number of evaluations 
        :rtype: int
        """
        return self.__evaluation

    @evaluation.setter
    def evaluation(self, value:int)->None:
        """
        Property setter for current number of evaluations
        """
        self.__evaluation = value

    @property
    def execution_started(self)->datetime:
        """
        Property getter for time when execution started
        
        :return datetime: time when execution started 
        """
        return self.__execution_started

    @execution_started.setter
    def execution_started(self, value:datetime)->None:
        """
        Property setter for time when execution started

        :param datetime value: time when execution started
        """
        self.__execution_started = value

    @property
    def execution_ended(self)->datetime:
        """
        Property getter for time when execution ended
        
        :return datetime: time when execution ended 
        """
        return self.__execution_ended

    @execution_ended.setter
    def execution_ended(self, value:datetime)->None:
        """
        Property setter for time when execution ended
        
        :param datetime value: time when execution ended
        """
        self.__execution_ended = value

    @property
    def output_control(self)->OutputControl:
        """
        Property getter for the output control of the executing algorithm
        
        :return: output control of the executing algorithm
        :rtype: `OutputControl`
        """
        return self.__output_control

    @output_control.setter
    def output_control(self, value:OutputControl)->None:
        """
        Property setter for the output control of the executing algorithm
        
        :param int value: `OutputControl`
        """
        self.__output_control = value

    @property
    def best_solution(self)->TargetSolution:
        """
        Property getter for the best solution obtained during metaheuristic execution
        
        :return: best solution so far 
        :rtype: TargetSolution
        """
        return self.__best_solution

    @property
    def iteration(self)->int:
        """
        Property getter for the iteration of metaheuristic execution
        
        :return: iteration
        :rtype: int
        """
        return self.__iteration

    @iteration.setter
    def iteration(self, value:int)->None:
        """
        Property setter the iteration of metaheuristic execution
        
        :param int value: iteration
        """
        self.__iteration = value

    @abstractmethod
    def init(self)->None:
        """
        Initialization of the algorithm
        """
        raise NotImplementedError

    def is_first_solution_better(self, sol1:TargetSolution, sol2:TargetSolution)->bool:
        """
        Checks if first solution is better than the second one

        :param TargetSolution sol1: first solution
        :param TargetSolution sol2: second solution
        :return: `True` if first solution is better, `False` if first solution is worse, `None` if fitnesses of both 
                solutions are equal
        :rtype: bool
        """
        if self.target_problem is None:
            raise ValueError('Target problem have to be defined within metaheuristic.')
        if self.target_problem.is_minimization is None:
            raise ValueError('Information if minimization or maximization is set within metaheuristic target problem'
                    'have to be defined.')
        is_minimization:bool = self.target_problem.is_minimization
        if sol1 is None:
            fit1:float = None
        else:
            fit1:float = sol1.calculate_objective_fitness_feasibility(self.target_problem).fitness_value;
        if sol2 is None:
            fit2:float = None
        else:
            fit2:float = sol2.calculate_objective_fitness_feasibility(self.target_problem).fitness_value;
        # with fitness is better than without fitness
        if fit1 is None:
            if fit2 is not None:
                return False
            else:
                return None
        elif fit2 is None:
            return True
        # if better, return true
        if (is_minimization and fit1 < fit2) or (not is_minimization and fit1 > fit2):
            return True
        # if same fitness, return None
        if fit1 == fit2:
            return None
        # otherwise, return false
        return False

    def copy_to_best_solution(self, solution:TargetSolution)->None:
        """
        Copies function argument to become the best solution within metaheuristic instance and update info about time 
        and iteration when the best solution is updated 

        :param TargetSolution solution: solution that is source for coping operation
        """
        self.__best_solution = solution.copy()
        self.__second_when_best_obtained = (datetime.now() - self.execution_started).total_seconds()
        self.__iteration_best_found = self.iteration

    def write_output_headers_if_needed(self):
        """
        Write headers(with field names) to output file, if necessary 
        """            
        if self.output_control.write_to_output:
            output:TextIOWrapper = self.output_control.output_file
            f_hs:list[str] = self.output_control.fields_headings
            for f_h in f_hs:
                output.write(f_h)
                output.write('\t')
            output.write('\n')

    def write_output_values_if_needed(self, step_name:str, step_name_value:str):
        """
        Write data(with field values) to output file, if necessary 

        :param str step_name: name of the step when data should be written to output - have to be one of the following values: 'after_algorithm', 'before_algorithm', 'after_iteration', 'before_iteration', 'after_evaluation', 'before_evaluation', 'after_step_in_iteration', 'before_step_in_iteration'
        :param str step_name_value: what should be written to the output instead of step_name
        """            
        if self.output_control.write_to_output:
            output:TextIOWrapper = self.output_control.output_file
            should_write:bool = False
            if step_name == 'after_algorithm':
                should_write = True
            elif step_name == 'before_algorithm':
                should_write = self.output_control.write_before_algorithm
            elif step_name == 'after_iteration':
                should_write = self.output_control.write_after_iteration
            elif step_name == 'before_iteration':
                should_write = self.output_control.write_before_iteration
            elif step_name == 'after_evaluation':
                should_write = self.output_control.write_after_evaluation
            elif step_name == 'before_evaluation':
                should_write = self.output_control.write_before_evaluation
            elif step_name == 'after_step_in_iteration':
                should_write = self.output_control.write_after_step_in_iteration
            elif step_name == 'before_step_in_iteration':
                should_write = self.output_control.write_before_step_in_iteration
            else:
                raise ValueError("Supplied step name '" + step_name + "' is not valid.")
            if should_write:
                fields_def:list[str] = self.output_control.fields_definitions 
                for f_def in fields_def:
                    if f_def != "":
                        try:
                            data = eval(f_def)
                            s_data:str = str(data)
                            if s_data == "step_name":
                                s_data = step_name_value
                        except:
                            s_data:str = 'XXX'
                        output.write( s_data + '\t')
                output.write('\n')

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the 'Algorithm' instance
        
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
        s = group_start
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'name=' + self.name + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'target_problem=' + self.target_problem.string_rep(delimiter, indentation + 1, 
                indentation_symbol, '{', '}')  + delimiter 
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'best_solution=' + self.best_solution.string_rep(delimiter, indentation + 1, 
                indentation_symbol, group_start, group_end) + delimiter 
        for i in range(0, indentation):
            s += indentation_symbol  
        s += '__output_control=' + self.__output_control.string_rep(
                delimiter, indentation + 1, indentation_symbol, '{', '}') + delimiter
        s += '__evaluation=' + str(self.__evaluation) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'execution_started=' + str(self.execution_started) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'execution_ended=' + str(self.execution_ended) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    @abstractmethod
    def __str__(self)->str:
        """
        String representation of the 'Algorithm' instance
        
        :return: string representation of the 'Algorithm' instance
        :rtype: str
        """
        return self.string_rep('|')

    @abstractmethod
    def __repr__(self)->str:
        """
        Representation of the 'Algorithm' instance
        
        :return: string representation of the 'Algorithm' instance
        :rtype: str
        """
        return self.string_rep('\n')

    @abstractmethod
    def __format__(self, spec:str)->str:
        """
        Formatted 'Algorithm' instance
        
        :param str spec: format specification
        :return: formatted 'Algorithm' instance
        :rtype: str
        """
        return self.string_rep('|')
