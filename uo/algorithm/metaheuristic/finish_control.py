""" 
The :mod:`~uo.algorithm.metaheuristic.finish_control` module describes the class :class:`~uo.algorithm.metaheuristic.FinishControl`.
"""

from copy import deepcopy
from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

class FinishControl:

    """
    This class determine finishing criteria and status during execution of the 
    :class:`uo.algorithm.metaheuristic.Metaheuristic` 
    """

    def __init__(self, 
            criteria:str='evaluations & seconds & iterations', 
            evaluations_max:int = 0,
            iterations_max:int = 0,
            seconds_max:int|float = 0  
        ) -> None:
        """
        Creates new :class:`uo.algorithm.metaheuristic.FinishControl` instance

        :param str criteria: list of finish criteria, separated with sign `&` 
        (currently finish criteria contains strings `evaluations_max`, `iterations_max`, `seconds_max`) 
        :param int evaluations_max: maximum number of evaluations for metaheuristic execution
        :param int iterations_max: maximum number of iterations for metaheuristic execution
        :param float seconds_max: maximum number of seconds for metaheuristic execution
        """
        if not isinstance(criteria, str):
                raise TypeError('Parameter \'criteria\' must be \'str\'.')
        if not isinstance(evaluations_max, int):
                raise TypeError('Parameter \'evaluations_max\' must be \'int\'.')
        if not isinstance(iterations_max, int):
                raise TypeError('Parameter \'iterations_max\' must be \'int\'.')
        if not isinstance(seconds_max, int|float):
                raise TypeError('Parameter \'seconds_max\' must be \'float\' or \'int\'.')
        self.__implemented_criteria:list[str] = ['evaluations_max',
                'iterations_max',
                'seconds_max']
        self.__evaluations_max = evaluations_max
        self.__iterations_max = iterations_max
        self.__seconds_max = seconds_max
        self.__determine_criteria_helper__(criteria)

    def __copy__(self):
        """
        Internal copy of the current finish control

        :return:  new `FinishControl` instance with the same properties
        :rtype: FinishControl
        """
        oc = deepcopy(self)
        return oc

    def copy(self):
        """
        Copy the current finish control

        :return: new `FinishControl` instance with the same properties
        :rtype: FinishControl
        """
        return self.__copy__()


    def __determine_criteria_helper__(self, criteria:str):
        """
        Helper function that determines which criteria should be checked during

        :param str criteria: list of finish criteria, separated with sign `&` 
        (currently finish criteria contains strings `evaluations`, `iterations`, `seconds`) 
        """
        if not isinstance( criteria, str):
            raise TypeError('Parameter \'criteria\' must be string.')
        self.__check_evaluations = False
        self.__check_iterations = False
        self.__check_seconds = False
        crit:list[str] = criteria.split('&')
        for cr in crit: 
            c:str = cr.strip()
            if c=='':
                continue
            if c == 'evaluations':
                if self.__evaluations_max > 0:
                    self.__check_evaluations = True
            elif c == 'iterations':
                if self.__iterations_max > 0:
                    self.__check_iterations = True
            elif c == 'seconds':
                if self.__seconds_max > 0:
                    self.__check_seconds = True
            else:
                raise ValueError("Invalid value for criteria '{}'. Should be one of:{}.".format( c, 
                    "evaluations, iterations, seconds"))

    @property
    def evaluations_max(self)->int:
        """
        Property getter for maximum number of evaluations 

        :return: maximum number of evaluations 
        :rtype: int
        """
        return self.__evaluations_max

    @property
    def iterations_max(self)->int:
        """
        Property getter for maximum number of iterations 

        :return: maximum number of iterations 
        :rtype: int
        """
        return self.__iterations_max

    @property
    def seconds_max(self)->float:
        """
        Property getter for maximum number of seconds for metaheuristic execution 

        :return: maximum number of seconds 
        :rtype: float
        """
        return self.__seconds_max

    @property
    def criteria(self)->str:
        """
        Property getter for finish criteria property 

        :return: list of finish criteria separated with `&`
        :rtype: str
        """
        ret:str = ''
        if self.__check_evaluations:
            ret += 'evaluations & '
        if self.__check_iterations:
            ret += 'iterations & '
        if self.__check_seconds:
            ret += 'seconds & '
        ret = ret[0:-2]
        return ret.strip()

    @criteria.setter
    def criteria(self, value:str)->None:
        """
        Property setter for the finish criteria property
        """
        if not isinstance(value, str):
            raise TypeError('Parameter \'criteria\' must have type \'str\'.')
        self.__determine_criteria_helper__(value)

    @property
    def check_evaluations(self)->bool:
        """
        Property getter for property `check_evaluations`

        :return: if number of evaluations is within finish criteria
        :rtype: bool
        """
        return self.__check_evaluations

    @property
    def check_iterations(self)->bool:
        """
        Property getter for property `check_iterations`

        :return: if number of iterations is within finish criteria
        :rtype: bool
        """
        return self.__check_iterations

    @property
    def check_seconds(self)->bool:
        """
        Property getter for property `check_seconds`

        :return: if elapsed time (in seconds) is within finish criteria
        :rtype: bool
        """
        return self.__check_seconds

    def is_finished(self, evaluation:int, iteration:int, elapsed_seconds:float):
        """
        Check if execution of metaheuristic is finished, according to specified criteria

        :param int evaluation: number of evaluations for metaheuristic execution
        :param int iteration: number of iterations for metaheuristic execution
        :param float elapsed_seconds: elapsed time (in seconds) for metaheuristic execution
        :return: if execution is finished
        :rtype: bool
        """
        return (self.check_evaluations and evaluation >= self.evaluations_max) \
                or (self.check_iterations and iteration >= self.iterations_max) \
                or (self.check_seconds and elapsed_seconds >= self.seconds_max)

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the target solution instance

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
        s += group_start + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'criteria=' + str(self.criteria) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'evaluations_max=' + str(self.evaluations_max) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'iterations_max=' + str(self.iterations_max) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'seconds_max=' + str(self.seconds_max) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the finish control 

        :return: string representation of the finish control 
        :rtype: str
        """
        return self.string_rep('|')

    def __repr__(self)->str:
        """
        Representation of the finish control 

        :return: string representation of finish control 
        :rtype: str
        """
        return self.string_rep('\n')


    def __format__(self, spec:str)->str:
        """
        Formatted the finish control 

        :param str spec: format specification
        :return: formatted finish control structure
        :rtype: str
        """
        return self.string_rep('|')

