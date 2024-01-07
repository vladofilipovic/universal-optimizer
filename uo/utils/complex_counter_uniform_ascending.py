from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

from copy import deepcopy
from datetime import datetime

from uo.utils.logger import logger

class ComplexCounterUniformAscending:
    """
    This class describes complex counter with uniform values, that counts only ascending data 
    """

    def __init__(self, number_of_counters:int, counter_size:int)->None:
        """
        Create new ComplexCounterUniformAscending instance

        :param int number_of_counters: number of counters within complex counter
        :param int counter_size: size of each counter within complex counter
        """
        if not isinstance(number_of_counters, int):
                raise TypeError('Parameter \'number_of_counters\' must be \'int\'.')    
        if number_of_counters <= 0:    
                raise ValueError('Parameter \'number_of_counters\' must be greater than zero.')    
        if not isinstance(counter_size, int):
                raise TypeError('Parameter \'counter_size\' must be \'int\'.')        
        if counter_size <= 0:    
                raise ValueError('Parameter \'counter_size\' must be greater than zero.')    
        if counter_size < number_of_counters:    
                raise ValueError('Parameter \'counter_size\' must be greater or equal to parameter \'number_of_counters\'.')    
        self.__number_of_counters:int = number_of_counters
        self.__counter_size:int = counter_size
        self.__counters:list[int] = [0] * number_of_counters
        self.reset()

    def __copy__(self):
        """
        Internal copy of the current complex counter

        :return:  new `ComplexCounterUniformAscending` instance with the same properties
        :rtype: :class:`uo.utils.ComplexCounterUniformAscending`
        """
        ccud = deepcopy(self)
        return ccud

    def copy(self):
        """
        Copy the current complex counter

        :return:  new `ComplexCounterUniformAscending` instance with the same properties
        :rtype: :class:`uo.utils.ComplexCounterUniformAscending`
        """
        return self.__copy__()

    def current_state(self)->list[int]:
        """
        Returns current state of the complex counter

        :return: current state of the complex counter
        :rtype: list[int]
        """
        return self.__counters

    def reset(self)->bool:
        """
        Resets the complex counter to its initial position.

        :return: if progress is possible after resetting
        :rtype: bool
        """
        for i in range(self.__number_of_counters):
            self.__counters[i]=i
        return self.__number_of_counters * self.__counter_size > 0

    def progress(self)->bool:
        """
        Make the progress to the complex counter. At the same time, determine if complex counter can progress.

        :return: if progress is successful
        :rtype: bool
        """
        finish:bool = True
        for i in range(0, self.__number_of_counters):
            if self.__counters[i] < self.__counter_size -1:
                finish = False
        if finish:
            return False
        ind_not_max:int = self.__number_of_counters-1
        for i in range(ind_not_max, -1, -1):
            if self.__counters[i] < self.__counter_size -1:
                ind_not_max = i
                break
        self.__counters[ind_not_max] += 1
        for i in range(ind_not_max+1, self.__number_of_counters):
            self.__counters[i]=0
        return True

# testing the developed class
def main():
    cc:ComplexCounterUniformAscending = ComplexCounterUniformAscending(4,6)
    can_progress:bool = cc.reset()
    for i in range(1, 1400):
        print(cc.current_state())
        can_progress = cc.progress()

if __name__ == '__main__':
    main()
