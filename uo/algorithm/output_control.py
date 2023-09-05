from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

class OutputControl:

    """
    This class determine where the output generated during execution of the 
    :class:`optimization_algorithms.algorithm.Algorithm` instance will be written 
    """

    def __init__(self, write_to_output:bool=False, output_file=None) -> None:
        """
        Creates new :class:`optimization_algorithms.algorithm.OutputControl` instance

        :param bool write_to_output: if algorithm will write to output, or not
        :param output_file: output file to which algorithm will write
        :type output_file: File, optional
        """
        self.__write_to_output:bool = write_to_output
        self.__output_file = output_file

    @property
    def write_to_output(self)->bool:
        """
        Property getter for determining if write to output 

        :return: if write_to_output, or not 
        :rtype: bool
        """
        return self.__write_to_output

    @property
    def output_file(self):
        """
        Property getter for output file 

        :return: output file to which algorithm will write
        :rtype: File
        """
        return self.__write_to_output

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


