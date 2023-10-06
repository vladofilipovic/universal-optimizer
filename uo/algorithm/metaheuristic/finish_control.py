""" 
The :mod:`~uo.algorithm.metaheuristic.finish_control` module describes the class :class:`~uo.algorithm.metaheuristic.FinishControl`.
"""

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
            seconds_max:float = 0  
        ) -> None:
        """
        Creates new :class:`uo.algorithm.FinishControl` instance

        :param str criteria: list of finish criteria, separated with sign `&` 
        (currently finish criteria contains strings `evaluations_max`, `iterations_max`, `seconds_max`) 
        :param int evaluations_max: maximum number of evaluations for metaheuristic execution
        :param int iterations_max: maximum number of iterations for metaheuristic execution
        :param int seconds_max: maximum number of seconds for metaheuristic execution
        """
        self.__implemented_criteria:list[str] = ['evaluations_max',
                'iterations_max',
                'seconds_max']
        self.__evaluations_max = evaluations_max
        self.__iterations_max = iterations_max
        self.__seconds_max = seconds_max
        self.__check_evaluations = False
        self.__check_iterations = False
        self.__check_seconds = False
        self.__determine_criteria_helper__(criteria)

    def __determine_criteria_helper__(self, criteria:str):
        """
        Helper function that determines which criteria should be checked during

        :param str criteria: list of finish criteria, separated with sign `&` 
        (currently finish criteria contains strings `evaluations`, `iterations`, `seconds`) 
        """
        crit:list[str] = criteria.split('&')
        for cr in crit: 
            c:str = cr.strip()
            if c == 'evaluations':
                if self.__evaluations_max > 0:
                    self.__check_evaluations = True
            elif c == 'iterations':
                if self.__iterations_max > 0:
                    self.__check_iterations = True
            elif m == 'seconds':
                if self.__seconds_max > 0:
                    self.__check_seconds = True
            else:
                raise ValueError("Invalid value for criteria {}. Should be one of:{}.".format( c, 
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
        return ret

    @criteria.setter
    def criteria(self, value:str)->None:
        """
        Property setter for the finish criteria property
        """
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
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_start + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'criteria=' + str(self.criteria) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'evaluations_max=' + str(self.evaluations_max) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'iterations_max=' + str(self.iterations_max) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'seconds_max=' + str(self.seconds_max) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the cache control and statistics structure

        :return: string representation of the cache control and statistics structure
        :rtype: str
        """
        return self.string_rep('|')

    def __repr__(self)->str:
        """
        Representation of the cache control and statistics structure

        :return: string representation of cache control and statistics structure
        :rtype: str
        """
        return self.string_rep('\n')


    def __format__(self, spec:str)->str:
        """
        Formatted the cache control and statistics structure

        :param str spec: format specification
        :return: formatted cache control and statistics structure
        :rtype: str
        """
        return self.string_rep('|')

