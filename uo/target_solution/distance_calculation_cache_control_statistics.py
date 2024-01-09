""" 
The :mod:`~uo.target_solution.distance_calculation_cache_control_statistics` module describes the class :class:`~uo.target_solution.distance_calculation_cache_control_statistics.DistanceCalculationCacheControlStatistics`.
"""

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)


from abc import ABCMeta, abstractmethod
from typing import NamedTuple
from typing import TypeVar, Generic
from typing import Generic
from typing import Optional

E_co = TypeVar("E_co", covariant=True) 

class DistanceCalculationCacheControlStatistics(Generic[E_co]):
    """
    Class that represents control statistics for solution code distance calculation cache.
    """

    def __init__(self, is_caching:bool, max_cache_size:Optional[int]=0)->None:
        """
        Create new `DistanceCalculationCacheControlStatistics` instance
        
        :param bool is_caching: is cashing enabled during calculation of distances among solution representations
        :param Optional[int] max_cache_size: maximum size of the cache - if 0 cache is with unlimited size
        """
        if not isinstance(is_caching, bool):
                raise TypeError('Parameter \'is_caching\' must be \'bool\'.')        
        if not isinstance(max_cache_size, int) and max_cache_size is not None:
                raise TypeError('Parameter \'is_caching\' must be \'int\' or \'None\'.')        
        self.__is_caching:bool = is_caching
        self.__max_cache_size:int = max_cache_size
        self.__cache:dict[(E_co,E_co)] = {}
        self.__cache_hit_count:int = 0
        self.__cache_request_count:int = 0

    @property
    def is_caching(self)->bool:
        """
        Property getter for `is_caching` 

        :return: if caching is used during calculation of the solution code distances, or not 
        :rtype: bool
        """
        return self.__is_caching

    @is_caching.setter
    def is_caching(self, value:bool)->None:
        """
        Property setter for `is_caching`
        
        :param bool value: value that is set for `is_caching`
        """
        if not isinstance(value, bool):
            raise TypeError('Parameter \'is_caching\' must have type \'bool\'.')
        self.__is_caching = value

    @property
    def max_cache_size(self)->int:
        """
        Property getter for `max_cache_size` 

        :return: maximum size of the cache - if 0 cache is with unlimited size 
        :rtype: int
        """
        return self.__max_cache_size

    @property
    def cache(self)->dict[(E_co,E_co)]:
        """
        Property getter for cache 

        :return:  cache that is used during calculation for previously obtained solution code distances
        :rtype: dict[(E_co,E_co)]
        """
        return self.__cache

    @cache.setter
    def cache(self, value:dict[(E_co,E_co)])->None:
        """
        Property setter for cache

        :param dict[(E_co,E_co)] value: value that is set for `cache`
        """
        if not isinstance(value, dict):
            raise TypeError('Parameter \'cache\' must be a dictionary.')
        self.__cache = value

    @property
    def cache_hit_count(self)->int:
        """
        Property getter for cache_hit_count 

        :return: number of cache hits during calculation of the solution code distances 
        :rtype: int
        """
        return self.__cache_hit_count

    def increment_cache_hit_count(self)->None:
        """
        Increments number of cache hits during calculation of the solution code distances 
        """
        self.__cache_hit_count += 1

    @property
    def cache_request_count(self)->int:
        """
        Property getter for cache_request_count 

        :return: overall number of calculation of the solution code distances 
        :rtype: int
        """
        return self.__cache_request_count

    def increment_cache_request_count(self)->None:
        """
        Increments overall number of calculation of the solution code distances 
        """
        self.__cache_request_count += 1

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of solution distance calculation cache control statistic 

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
        s += '__is_caching=' + str(self.__is_caching) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += '__cache_hit_count=' + str(self.__cache_hit_count) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += '__cache_requests_count=' + str(self.__cache_request_count) + delimiter
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


