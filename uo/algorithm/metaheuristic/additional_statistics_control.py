""" 
The :mod:`~uo.algorithm.metaheuristic.additional_statistics_control` module describes the class :class:`~uo.algorithm.metaheuristic.AdditionalStatisticsControl`.
"""

from pathlib import Path
from random import random
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

class AdditionalStatisticsControl:

    """
    This class determine additional statistics that should be kept during execution of the 
    :class:`uo.algorithm.metaheuristic.Metaheuristic` 
    """

    def __init__(self, 
            keep:str='', 
            max_local_optima:int = 10,
        ) -> None:
        """
        Creates new :class:`uo.algorithm.metaheuristic.AdditionalStatisticsControl` instance

        :param str keep: list of comma-separated strings that describes what to be kept during metaheuristic execution 
        (currently it contains strings `all_solution_code`, `more_local_optima`) 
        :param int max_local_optima: number of local optima to be kept
        """
        if not isinstance(keep, str):
                raise TypeError('Parameter \'keep\' must be \'str\'.')
        if not isinstance(max_local_optima, int):
                raise TypeError('Parameter \'max_local_optima\' must be \'int\'.')
        self.__can_be_kept:list[str] = ['all_solution_code',
                'more_local_optima']
        self.__max_local_optima:int = max_local_optima
        self.__determine_keep_helper__(keep)

    def __determine_keep_helper__(self, keep:str):
        """
        Helper function that determines which criteria should be checked during

        :param str keep: comma-separated list of values that should be kept 
        (currently keep contains strings `all_solution_code`, `more_local_optima`) 
        """
        if not isinstance(keep, str):
            raise TypeError('Parameter \'keep\' must be string.')
        self.__keep_all_solution_codes = False
        self.__keep_more_local_optima = False
        kep:list[str] = keep.split(',')
        for ke in kep: 
            k:str = ke.strip()
            if k=='' or k=='None':
                continue
            if k == 'all_solution_code':
                self.__keep_all_solution_codes = True
            elif k == 'more_local_optima':
                self.__keep_more_local_optima = True
            else:
                raise ValueError("Invalid value for keep '{}'. Should be one of:{}.".format( k, 
                    "all_solution_code, more_local_optima"))
        #class/static variable all_solution_codes
        if not hasattr(AdditionalStatisticsControl, 'all_solution_code'):
            AdditionalStatisticsControl.all_solution_codes:set[str] = set()
        # values of the local optima foreach element calculated 
        if not hasattr(AdditionalStatisticsControl, 'more_local_optima'):                
            AdditionalStatisticsControl.more_local_optima:dict[str, float] = {}

    @property
    def max_local_optima(self)->int:
        """
        Property getter for maximum number of local optima that will be kept

        :return: maximum number of local optima that will be kept
        :rtype: int
        """
        return self.__max_local_optima

    @property
    def keep(self)->str:
        """
        Property getter for keep property 

        :return: comma-separated list of values vo be kept
        :rtype: str
        """
        ret:str = ''
        if self.__keep_all_solution_codes:
            ret += 'all_solution_code, '
        if self.__keep_more_local_optima:
            ret += 'more_local_optima, '
        ret = ret[0:-2]
        return ret

    @keep.setter
    def keep(self, value:str)->None:
        """
        Property setter for the keep property 
        """
        self.__determine_keep_helper__(value)

    @property
    def keep_all_solution_codes(self)->bool:
        """
        Property getter for property if all solution codes to be kept

        :return: if all solution codes to be kept
        :rtype: bool
        """
        return self.__keep_all_solution_codes

    @property
    def keep_more_local_optima(self)->bool:
        """
        Property getter for decision if more local optima should be kept

        :return: if more local optima should be kept
        :rtype: bool
        """
        return self.__keep_more_local_optima

    def add_to_all_solution_codes_if_required(self, representation:str)->None:
        """
        Filling all solution code, if necessary 

        :param representation: solution representation to be inserted into all solution code
        :type representation: str
        :rtype: None
        """        
        if not isinstance(representation, str):
            raise TypeError('Parameter \'representation\' must be string.')
        if self.keep_all_solution_codes:
            AdditionalStatisticsControl.all_solution_codes.add(representation)

    def add_to_more_local_optima_if_required(self, solution_to_add_rep:str, solution_to_add_fitness:float|list[float], 
            best_solution_rep:str)->bool:
        """
        Add solution to the local optima structure 

        :param str solution_to_add_rep: string representation of the solution to be added to local optima structure
        :param float solution_to_add_fitness: fitness value of the solution to be added to local optima structure
        :param str best_solution_rep: string representation of the best solution so far
        :return:  if adding is successful e.g. current_solution is new element in the structure
        :rtype: bool
        """       
        if not isinstance(solution_to_add_rep, str):
            raise TypeError('Parameter \'solution_to_add_rep\' must be string.')
        if not self.keep_more_local_optima:
            return False
        if solution_to_add_rep in AdditionalStatisticsControl.more_local_optima:
            return False
        if len(AdditionalStatisticsControl.more_local_optima) >= self.__max_local_optima:
            # removing random, just taking care not to remove the best ones
            while True:
                code:str = random.choice(AdditionalStatisticsControl.more_local_optima.keys())
                if code != best_solution_rep:
                    del AdditionalStatisticsControl.more_local_optima[code]
                    break
        AdditionalStatisticsControl.more_local_optima[solution_to_add_rep]=solution_to_add_fitness
        return True


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
        s += 'keep=' + str(self.keep) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'use_cache_for_distance_calculation=' + str(self.use_cache_for_distance_calculation) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        if self.keep_all_solution_codes:
            for _ in range(0, indentation):
                s += indentation_symbol  
            s += 'all solution codes=' + str(len(AdditionalStatisticsControl.all_solution_codes)) + delimiter
        for _ in range(0, indentation):
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

