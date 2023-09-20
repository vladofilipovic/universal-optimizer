""" 
The :mod:`~uo.algorithm.output_control` module describes the class :class:`~uo.algorithm.OutputControl`.
"""

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

from copy import deepcopy
from io import TextIOWrapper 

class OutputControl:

    """
    This class determine where the output generated during execution of the 
    :class:`uo.algorithm.Algorithm` instance will be written 
    """

    def __init__(self, write_to_output:bool=False, output_file:TextIOWrapper=None, fields:str=None, 
            moments:str=None) -> None:
        """
        Creates new :class:`uo.algorithm.OutputControl` instance

        :param bool write_to_output: if algorithm will write to output, or not
        :param output_file: output file to which algorithm will write
        :type output_file: TextIOWrapper
        :param str fields: comma-separated list of fields for output - basically fields of the optimizer object 
        (e.g. `best_solution.fitness_value`, `iteration`, `evaluation`, `seconds_max` etc.) and last word in specific 
        field should he header od the csv column
        :param str moments: comma-separated list of moments for output - contains `on-algorithm`, `on-iteration`,
        `on-step` 
        """
        self.__write_to_output:bool = write_to_output
        self.__output_file:TextIOWrapper = output_file
        self.__fields:str = fields
        self.__moments:str = moments
        self.__report_on_algorithm:bool = True
        self.__report_on_iteration:bool = False
        self.__report_on_step:bool = False

    def __copy__(self):
        """
        Internal copy of the output control

        :return:  new `OutputControl` instance with the same properties
        :rtype: :class:`uo.algorithm.OutputControl`
        """
        oc = deepcopy(self)
        return oc

    def copy(self):
        """
        Copy the current output control

        :return:  new `OutputControl` instance with the same properties
        :rtype: :class:`uo.algorithm.OutputControl`
        """
        return self.__copy__()


    @property
    def write_to_output(self)->bool:
        """
        Property getter for determining if write to output 

        :return: if write to output during algorithm execution, or not 
        :rtype: bool
        """
        return self.__write_to_output

    @property
    def output_file(self)->TextIOWrapper:
        """
        Property getter for output file 

        :return: output file to which algorithm will write
        :rtype: `TextIOWrapper`
        """
        return self.__output_file

    @output_file.setter
    def output_file(self, value)->None:
        """
        Property setter for the output file
        """
        self.__output_file = value

    @property
    def fields(self)->str:
        """
        Property getter for fields property 

        :return: comma-separated list of fields for output
        :rtype: str
        """
        return self.__fields

    @fields.setter
    def fields(self, value:str)->None:
        """
        Property setter for the fields property
        """
        self.__fields = value

    @property
    def moments(self)->str:
        """
        Property getter for moments property 

        :return: comma-separated list of moments for output
        :rtype: str
        """
        return self.__moments

    @moments.setter
    def moments(self, value:str)->None:
        """
        Property setter for the moments property
        """
        self.__moments = value
        if 'on_algorithm' in self.__moments:
            self.__report_on_algorithm = True
        else:
            self.__report_on_algorithm = False
        if 'on_iteration' in self.__moments:
            self.__report_on_iteration = True
        else:
            self.__report_on_iteration = False
        if 'on_iteration' in self.__moments:
            self.__report_on_step = True
        else:
            self.__report_on_step = False

    @property
    def report_on_algorithm(self)->bool:
        """
        Property getter for property `report_on_algorithm`

        :return: should report to the output on algorithm
        :rtype: str
        """
        return self.__report_on_algorithm

    @property
    def report_on_iteration(self)->bool:
        """
        Property getter for property `report_on_iteration`

        :return: should report to the output on each iteration
        :rtype: str
        """
        return self.__report_on_iteration

    @property
    def report_on_step(self)->bool:
        """
        Property getter for property `report_on_step`

        :return: should report to the output on each step within iteration
        :rtype: str
        """
        return self.__report_on_step

    def string_representation(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
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
        s += 'write_to_output=' + str(self.write_to_output) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'output_file=' + str(self.output_file) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'fields=' + str(self.fields) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'moments=' + str(self.moments) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'report_on_algorithm=' + str(self.report_on_algorithm) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'report_on_iteration=' + str(self.report_on_iteration) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'report_on_step=' + str(self.report_on_step) + delimiter
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
        return self.string_representation('|')

    def __repr__(self)->str:
        """
        Representation of the cache control and statistics structure

        :return: string representation of cache control and statistics structure
        :rtype: str
        """
        return self.string_representation('\n')


    def __format__(self, spec:str)->str:
        """
        Formatted the cache control and statistics structure

        :param str spec: format specification
        :return: formatted cache control and statistics structure
        :rtype: str
        """
        return self.string_representation('|')


