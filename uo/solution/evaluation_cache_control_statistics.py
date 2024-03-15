""" 
The :mod:`~uo.solution.evaluation_cache_control_statistics` module describes the class :class:`~uo.solution.EvaluationCacheControlStatistics`.
"""

from typing import Optional

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

class EvaluationCacheControlStatistics:
    """
    Class that represents control statistics for evaluation caching.
    """
    
    def __init__(self, is_caching:bool=False, max_cache_size:Optional[int]=0)->None:
        """
        Create new `EvaluationCacheControlStatistics` instance
        :param Optional[bool] is_caching: determine if caching is activated
        :param Optional[int] max_cache_size: maximum size of the cache - if 0 cache is with unlimited size
        """
        if not isinstance(is_caching, bool):
                raise TypeError('Parameter \'is_caching\' must be \'bool\'.')        
        if not isinstance(max_cache_size, int) and max_cache_size is not None:
                raise TypeError('Parameter \'is_caching\' must be \'int\' or \'None\'.')        
        self.__is_caching:bool = is_caching
        self.__max_cache_size:int = max_cache_size
        self.__cache:dict[str] = {}
        self.__cache_hit_count:int = 0
        self.__cache_request_count:int = 0

    def __copy__(self):
        """
        Internal copy of the `EvaluationCacheControlStatistics` instance

        :return: new `EvaluationCacheControlStatistics` instance with the same properties
        :rtype: `EvaluationCacheControlStatistics`
        """
        pr = deepcopy(self)
        return pr

    def copy(self):
        """
        Copy the `EvaluationCacheControlStatistics` instance

        :return: new `EvaluationCacheControlStatistics` instance with the same properties
        :rtype: `EvaluationCacheControlStatistics`
        """
        return self.__copy__()

    @property
    def is_caching(self)->bool:
        """
        Property getter for is_caching 

        :return: if caching is used during evaluation, or not 
        :rtype: bool
        """
        return self.__is_caching

    @is_caching.setter
    def is_caching(self, value:bool)->None:
        """
        Property setter for is_caching

        :param bool value: value for determining if caching is activated
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
    def cache(self)->dict[str]:
        """
        Property getter for cache 
        
        :return: cache that is used during evaluation 
        :rtype: dict[str]
        """
        return self.__cache

    @cache.setter
    def cache(self, value:dict[str])->None:
        """
        Property setter for cache

        :param dict[str] value: value for cache
        """
        if not isinstance(value, dict):
            raise TypeError('Parameter \'cache\' must be a dictionary.')
        self.__cache = value

    @property
    def cache_hit_count(self)->int:
        """
        Property getter for cache_hit_count 

        :return: number of cache hits during evaluation
        :rtype: int
        """
        return self.__cache_hit_count

    def increment_cache_hit_count(self)->None:
        """
        Increments number of cache hits during evaluation 
        """
        self.__cache_hit_count += 1

    @property
    def cache_request_count(self)->int:
        """
        Property getter for cache_request_count 

        :return: overall number of evaluations 
        :rtype: int
        """
        return self.__cache_request_count

    def increment_cache_request_count(self)->None:
        """
        Increments overall number of evaluations 
        """
        self.__cache_request_count += 1

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the `EvaluationCacheControlStatistics` instance

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
        s += '__cache_request_count=' + str(self.__cache_request_count) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the `EvaluationCacheControlStatistics` instance

        :return: string representation of the `EvaluationCacheControlStatistics` instance
        :rtype: str
        """
        return self.string_rep('|', 0, '', '{', '}')


    def __repr__(self)->str:
        """
        Representation of the `EvaluationCacheControlStatistics` instance
        :return: str -- string representation of the `EvaluationCacheControlStatistics` instance
        """
        return self.string_rep('\n', 0, '   ', '{', '}')

    def __format__(self, spec:str)->str:
        """
        Formatted the `EvaluationCacheControlStatistics` instance
        :param spec: str -- format specification
        :return: str -- formatted `EvaluationCacheControlStatistics` instance
        """
        return self.string_rep('|')

