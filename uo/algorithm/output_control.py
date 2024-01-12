""" 
The :mod:`~uo.algorithm.output_control` module describes the class :class:`~uo.algorithm.OutputControl`.
"""

from copy import deepcopy
from pathlib import Path
from typing import Optional
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

from io import TextIOWrapper 

class OutputControl:

    """
    This class determine where the output generated during execution of the 
    :class:`uo.algorithm.Algorithm` instance will be written 
    """

    def __init__(self, write_to_output:bool=False, output_file:Optional[TextIOWrapper]=None, 
            fields:str='iteration, evaluation, "step_name", best_solution.argument(), '
                'best_solution.fitness_value, best_solution.objective_value, best_solution.is_feasible', 
            moments:str='after_algorithm') -> None:
        """
        Creates new :class:`uo.algorithm.OutputControl` instance

        :param bool write_to_output: if algorithm will write to output, or not
        :param output_file: output file to which algorithm will write
        :type output_file: TextIOWrapper
        :param str fields: comma-separated list of fields for output - basically fields of the optimizer object 
        (e.g. `best_solution.fitness_value`, `iteration`, `evaluation`, `seconds_max` etc.) and last word in specific 
        field should he header od the csv column
        :param str moments: comma-separated list of moments for output - contains following elements:
        `before_algorithm`, `after_algorithm`, `before_iteration`, `after_iteration`, 
        `before_evaluation`, `after_evaluation`, `before_step_in_iteration`, `after_step_in_iteration`
        """
        if not isinstance(write_to_output, bool):
            raise TypeError('Parameter \'write_to_output\' must have type \'bool\'.')
        if not isinstance(output_file, Optional[TextIOWrapper]):
            raise TypeError('Parameter \'output_file\' must have type \'TextIOWrapper\' or be \'None\'.')
        if not isinstance(fields, str):
            raise TypeError('Parameter \'fields\' must have type \'str\'.')
        if not isinstance(moments, str):
            raise TypeError('Parameter \'moments\' must have type \'str\'.')
        self.__write_to_output:bool = write_to_output
        self.__output_file:TextIOWrapper = output_file
        self.__fields_headings:list[str] = ['iteration',
                'evaluation',
                'step_name',
                'best_solution_string_representation',
                'best_solution_fitness_value',
                'best_solution_objective_value',
                'best_solution_is_feasible']
        self.__fields_definitions:list[str] = ['self.iteration',
                'self.evaluation',
                '"step_name"',
                'self.best_solution.string_representation()',
                'self.best_solution.fitness_value',
                'self.best_solution.objective_value',
                'self.best_solution.is_feasible']
        self.__determine_fields_helper__(fields)
        self.__determine_moments_helper__(moments)

    def __copy__(self):
        """
        Internal copy of the current output control

        :return:  new `OutputControl` instance with the same properties
        :rtype: OutputControl
        """
        oc = self
        return oc

    def copy(self):
        """
        Copy the current output control

        :return: new `OutputControl` instance with the same properties
        :rtype: OutputControl
        """
        return self.__copy__()

    def __determine_fields_helper__(self, fields:str):
        """
        Helper function that determines fields header list anf field definition lists of the control instance

        :param str fields: comma-separated list of fields for output - basically fields of the optimizer object 
        (e.g. `best_solution.fitness_value`, `iteration`, `evaluation`, `seconds_max` etc.) and last word in specific 
        field should he header od the csv column
        """
        fields_head:list[str] = fields.replace('.','_').replace(' ', '').replace('()','').split(',')
        for f_h in fields_head:
            if f_h != '':
                if f_h not in self.fields_headings:
                    self.fields_headings.append(f_h)
        fields_def:list[str] = fields.replace(' ', '').split(',') 
        for f_def in fields_def:
            if f_def != '':
                if f_def[0] != "'" and f_def[0] != '"':
                    f_def = 'self.' + f_def
                if f_def not in self.fields_definitions:
                    self.fields_definitions.append(f_def)

    def __determine_moments_helper__(self, moments:str):
        """
        Helper function that determines moments when value of fields will be written to output

        :param str moments: comma-separated list of moments for output - contains following elements:
        `before_algorithm`, `after_algorithm`, `before_iteration`, `after_iteration`, 
        `before_evaluation`, `after_evaluation`, `before_step_in_iteration`, `after_step_in_iteration`
        """
        self.__write_before_algorithm:bool = False
        self.__write_before_iteration:bool = False
        self.__write_after_iteration:bool = False
        self.__write_before_evaluation:bool = False
        self.__write_after_evaluation:bool = False
        self.__write_before_step_in_iteration:bool = False
        self.__write_after_step_in_iteration:bool = False
        self.__write_after_algorithm = True
        mom:list[str] = moments.split(',')
        for mo in mom: 
            m:str = mo.strip()
            if m=='':
                continue
            if m == 'before_algorithm':
                self.__write_before_algorithm = True
            elif m == 'after_algorithm':
                self.__write_after_algorithm = True
            elif m == 'before_iteration':
                self.__write_before_iteration = True
            elif m == 'after_iteration':
                self.__write_after_iteration = True
            elif m == 'before_evaluation':
                self.__write_before_evaluation = True
            elif m == 'after_evaluation':
                self.__write_after_evaluation = True
            elif m == 'before_step_in_iteration':
                self.__write_before_step_in_iteration = True
            elif m == 'after_step_in_iteration':
                self.__write_after_step_in_iteration = True
            else:
                raise ValueError("Invalid value for moment {}. Should be one of:{}.".format( m, 
                    "before_algorithm, after_algorithm, before_iteration, after_iteration," + 
                    "before_evaluation`, after_evaluation, before_step_in_iteration, after_step_in_iteration"))

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
    def fields_headings(self)->list[str]:
        """
        Property getter for `fields_headings` property 

        :return: list of fields headings for output
        :rtype: list[str]
        """
        return self.__fields_headings

    @property
    def fields_definitions(self)->list[str]:
        """
        Property getter for `fields_definitions` property 

        :return: list of fields definitions to be evaluated during output
        :rtype: list[str]
        """
        return self.__fields_definitions

    @property
    def fields(self)->str:
        """
        Property getter for `fields_definitions` property 

        :return: comma-separated string with list of fields for output
        :rtype: str
        """
        ret:str = ",".join(self.__fields_definitions)
        return ret

    @fields.setter
    def fields(self, value:str)->None:
        """
        Property setter for the fields property
        """
        if not isinstance(value, str):
            raise TypeError('Parameter \'fields\' must have type \'str\'.')
        self.__determine_fields_helper__(value)

    @property
    def moments(self)->str:
        """
        Property getter for moments property 

        :return: comma-separated list of moments for output
        :rtype: str
        """
        ret:str = 'after_algorithm, '
        if self.__write_before_algorithm:
            ret += 'before_algorithm, '
        if self.__write_before_iteration:
            ret += 'before_iteration, '
        if self.__write_after_iteration:
            ret += 'after_iteration, '
        if self.__write_before_evaluation:
            ret += 'before_evaluation, '
        if self.__write_after_evaluation:
            ret += 'after_evaluation, '
        if self.__write_before_step_in_iteration:
            ret += 'before_step_in_iteration, '
        if self.__write_after_step_in_iteration:
            ret += 'after_step_in_iteration, '
        ret = ret[0:-2]
        return ret

    @moments.setter
    def moments(self, value:str)->None:
        """
        Property setter for the moments property
        """
        if not isinstance(value, str):
            raise TypeError('Parameter \'moments\' must have type \'str\'.')
        self.__determine_moments_helper__(value)

    @property
    def write_before_algorithm(self)->bool:
        """
        Property getter for property `write_before_algorithm`

        :return: should write to the output prior to algorithm execution
        :rtype: bool
        """
        return self.__write_before_algorithm

    @property
    def write_after_algorithm(self)->bool:
        """
        Property getter for property `write_after_algorithm`

        :return: should write to the output after algorithm execution
        :rtype: bool
        """
        return self.__write_after_algorithm

    @property
    def write_before_iteration(self)->bool:
        """
        Property getter for property `write_before_iteration`

        :return: should write to the output prior to algorithm iteration
        :rtype: bool
        """
        return self.__write_before_iteration

    @property
    def write_after_iteration(self)->bool:
        """
        Property getter for property `write_after_iteration`

        :return: should write to the output after algorithm iteration
        :rtype: bool
        """
        return self.__write_after_iteration

    @property
    def write_before_evaluation(self)->bool:
        """
        Property getter for property `write_before_evaluation`

        :return: should write to the output prior to evaluation
        :rtype: bool
        """
        return self.__write_before_evaluation

    @property
    def write_after_evaluation(self)->bool:
        """
        Property getter for property `write_after_evaluation`

        :return: should write to the output after evaluation
        :rtype: bool
        """
        return self.__write_after_evaluation

    @property
    def write_before_step_in_iteration(self)->bool:
        """
        Property getter for property `write_before_step_in_iteration`

        :return: should write to the output prior to step in iteration
        :rtype: bool
        """
        return self.__write_before_step_in_iteration

    @property
    def write_after_step_in_iteration(self)->bool:
        """
        Property getter for property `write_after_step_in_iteration`

        :return: should write to the output after step in iteration
        :rtype: bool
        """
        return self.__write_after_step_in_iteration

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
        s += 'write_to_output=' + str(self.write_to_output) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'output_file=' + str(self.output_file) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'fields_headings=' + str(self.fields_headings) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'fields_definitions=' + str(self.fields_definitions) + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += 'moments=' + str(self.moments) + delimiter
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

