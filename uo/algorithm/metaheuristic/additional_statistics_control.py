""" 
The :mod:`~uo.algorithm.metaheuristic.additional_statistics_control` module describes the class :class:`~uo.algorithm.metaheuristic.AdditionalStatisticsControl`.
"""

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

from uo.algorithm.metaheuristic.solution_code_distance_cache_control_statistics import \
        DistanceCalculationCacheControlStatistics

class AdditionalStatisticsControl:

    """
    This class determine additional statistics that should be kept during execution of the 
    :class:`uo.algorithm.metaheuristic.Metaheuristic` 
    """

    def __init__(self, 
            keep:str='', 
            use_cache_for_distance_calculation:bool = False,
        ) -> None:
        """
        Creates new :class:`uo.algorithm.metaheuristic.AdditionalStatisticsControl` instance

        :param str keep: list of comma-separated strings that describes what to be kept during metaheuristic execution 
        (currently it contains strings `all_solution_code`, `distance_among_solutions`) 
        :param bool use_cache_for_distance_calculation: should cache be used for calculating distances among solutions
        """
        self.__can_be_kept:list[str] = ['all_solution_code',
                'distance_among_solutions']
        self.__use_cache_for_distance_calculation = use_cache_for_distance_calculation
        self.__determine_keep_helper__(keep)

    def __determine_keep_helper__(self, keep:str):
        """
        Helper function that determines which criteria should be checked during

        :param str keep: comma-separated list of values that should be kept 
        (currently keep contains strings `all_solution_code`, `distance_among_solutions`) 
        """
        self.__keep_all_solution_codes = False
        self.__keep_distance_among_solutions = False
        kep:list[str] = keep.split('&')
        for ke in kep: 
            k:str = ke.strip()
            if k=='':
                continue
            if k == 'all_solution_code':
                self.__keep_all_solution_codes = True
            elif k == 'distance_among_solutions':
                self.__keep_distance_among_solutions = True
            else:
                raise ValueError("Invalid value for keep '{}'. Should be one of:{}.".format( k, 
                    "all_solution_code, distance_among_solutions"))
        if self.__keep_all_solution_codes:
            #class/static variable all_solution_codes
            if not hasattr(AdditionalStatisticsControl, 'all_solution_codes'):
                AdditionalStatisticsControl.all_solution_codes:set[str] = set()
        if self.__keep_distance_among_solutions:
            #class/static variable representation_distance_cache_cs
            if not hasattr(AdditionalStatisticsControl, 'representation_distance_cache_cs'):
                AdditionalStatisticsControl.representation_distance_cache_cs: \
                        DistanceCalculationCacheControlStatistics = DistanceCalculationCacheControlStatistics(
                        self.__use_cache_for_distance_calculation)

    @property
    def use_cache_for_distance_calculation(self)->bool:
        """
        Property getter for using cache during distance calculation 

        :return: if cache is used during distance calculation 
        :rtype: bool
        """
        return self.__use_cache_for_distance_calculation

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
        if self.__keep_distance_among_solutions:
            ret += 'distance_among_solutions, '
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
    def keep_distance_among_solutions(self)->bool:
        """
        Property getter for decision if distance among solutions to be calculated and kept

        :return: if distance among solutions to be calculated and kept
        :rtype: bool
        """
        return self.__keep_distance_among_solutions

    def keep_all_solution_codes_if_necessary(self, representation:str)->None:
        """
        Filling all solution code, if necessary 

        :param representation: solution representation to be inserted into all solution code
        :type representation: str
        :rtype: None
        """        
        if self.keep_all_solution_codes:
            AdditionalStatisticsControl.all_solution_codes.add(representation)

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
        s += 'keep=' + str(self.keep) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'use_cache_for_distance_calculation=' + str(self.use_cache_for_distance_calculation) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        if self.keep_all_solution_codes:
            for i in range(0, indentation):
                s += indentation_symbol  
            s += 'all solution codes=' + str(len(AdditionalStatisticsControl.all_solution_codes)) + delimiter
        if self.keep_distance_among_solutions and self.use_cache_for_distance_calculation:
            for i in range(0, indentation):
                s += indentation_symbol  
            s += '__representation_distance_cache_cs(static)=' + AdditionalStatisticsControl. \
                    representation_distance_cache_cs.string_rep(
                    delimiter, indentation + 1, indentation_symbol, '{', '}') + delimiter
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

