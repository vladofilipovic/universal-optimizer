""" 
The :mod:`~uo.algorithm.output_control` module describes the class :class:`~uo.algorithm.OutputControl`.
"""

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

from io import TextIOWrapper 

class OutputControl:

    """
    This class determine where the output generated during execution of the 
    :class:`uo.algorithm.Algorithm` instance will be written 
    """

    def __init__(self, write_to_output:bool=False, output_file:TextIOWrapper=None, fields:str='', 
            moments:str='') -> None:
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
        self.__fields_headings:list[str] = ['iteration',
                'evaluation',
                'step_name',
                'best_solution_representation',
                'best_solution_fitness_value',
                'best_solution_objective_value',
                'best_solution_is_feasible']
        self.__fields_definitions:list[str] = ['self.iteration',
                'self.evaluation',
                '"step_name"',
                'self.best_solution.representation',
                'self.best_solution.fitness_value',
                'self.best_solution.objective_value',
                'self.best_solution.is_feasible']
        self.__determine_fields_helper__(fields)
        self.__write_before_algorithm:bool = False
        self.__write_after_algorithm:bool = False
        self.__write_before_iteration:bool = False
        self.__write_after_iteration:bool = False
        self.__write_before_evaluation:bool = False
        self.__write_after_evaluation:bool = False
        self.__write_before_step_in_iteration:bool = False
        self.__write_after_step_in_iteration:bool = False
        self.__determine_moments_helper__(moments)

    def __determine_fields_helper__(self, fields:str):
        fields_head:list[str] = fields.replace('.','_').replace(' ', '').split(',')
        for f_h in fields_head:
            if f_h != '':
                if f_h not in self.fields_headings:
                    self.fields_headings.append(f_h)
        fields_def:list[str] = fields.split(',') 
        for f_def in fields_def:
            if f_def != '':
                if f_def[0] != "'" and f_def[0] != '"':
                    f_def = 'self.' + f_def
                if f_def not in self.fields_definitions:
                    self.fields_definitions.append(f_def)

    def __determine_moments_helper__(self, moments:str):
        self.__write_after_algorithm = True
        if 'before_algorithm' in moments:
            self.__write_before_algorithm = True
        else:
            self.__write_before_algorithm = False
        if 'before_iteration' in moments:
            self.__write_before_iteration = True
        else:
            self.__write_before_iteration = False
        if 'after_iteration' in moments:
            self.__write_after_iteration = True
        else:
            self.__write_after_iteration = False
        if 'before_evaluation' in moments:
            self.__write_before_evaluation = True
        else:
            self.__write_before_evaluation = False
        if 'after_evaluation' in moments:
            self.__write_after_evaluation = True
        else:
            self.__write_after_evaluation = False
        if 'before_step_in_iteration' in moments:
            self.__write_before_step_in_iteration = True
        else:
            self.__write_before_step_in_iteration = False
        if 'after_step_in_iteration' in moments:
            self.__write_after_step_in_iteration = True
        else:
            self.__write_after_step_in_iteration = False

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
        return self.__fields_definitions.join(', ').replace('self.','')

    @fields.setter
    def fields(self, value:str)->None:
        """
        Property setter for the fields property
        """
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
        s += 'fields_headings=' + str(self.fields_headings) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'fields_definitions=' + str(self.fields_definitions) + delimiter
        for i in range(0, indentation):
            s += indentation_symbol  
        s += 'moments=' + str(self.moments) + delimiter
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


