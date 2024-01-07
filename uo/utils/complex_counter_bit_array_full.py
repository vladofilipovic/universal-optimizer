from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

from copy import deepcopy
from datetime import datetime

from bitstring import BitArray

from uo.utils.logger import logger

class ComplexCounterBitArrayFull:
    """
    This class describes complex counter with uniform values, that counts full 
    """

    def __init__(self, number_of_counters:int)->None:
        """
        Create new ComplexCounterBitArrayFull instance

        :param int number_of_counters: number of counters within complex counter
        :param int counter_size: size of each counter within complex counter
        """
        if not isinstance(number_of_counters, int):
                raise TypeError('Parameter \'number_of_counters\' must be \'int\'.')        
        if number_of_counters <= 0:
                raise ValueError('Parameter \'number_of_counters\' must be greater than zero.')                    
        self.__number_of_counters:int = number_of_counters
        self.__counters:BitArray = BitArray(number_of_counters)

    def __copy__(self):
        """
        Internal copy of the current complex counter

        :return:  new `ComplexCounterBitArrayFull` instance with the same properties
        :rtype: :class:`uo.utils.ComplexCounterBitArrayFull`
        """
        cc = ComplexCounterBitArrayFull(self.__number_of_counters)
        cc.__counters = BitArray(bin=self.__counters.bin)
        return cc

    def copy(self):
        """
        Copy the current complex counter

        :return:  new `ComplexCounterBitArrayFull` instance with the same properties
        :rtype: :class:`uo.utils.ComplexCounterBitArrayFull`
        """
        return self.__copy__()

    def current_state(self)->BitArray:
        """
        Returns current state of the complex counter

        :return: current state of the complex counter
        :rtype: BitArray
        """
        return self.__counters

    def reset(self)->bool:
        """
        Resets the complex counter to its initial position.

        :return: if progress is possible after resetting
        :rtype: bool
        """
        self.__counters.set(False)
        return self.__number_of_counters > 0

    def progress(self)->bool:
        """
        Make the progress to the complex counter. At the same time, determine if complex counter can progress.

        :return: if progress is successful
        :rtype: bool
        """
        if self.__counters.all(True, range(self.__number_of_counters)):
            return False
        ind_not_max:int = self.__counters.find('0b0')[0]
        self.__counters[ind_not_max] = True
        self.__counters.set(False, range(0,ind_not_max))
        return True

    def can_progress(self)->bool:
        return not self.__counters.all(True)


# testing the developed class
def main():
    cc:ComplexCounterBitArrayFull = ComplexCounterBitArrayFull(6)
    can_progress:bool = cc.reset()
    for i in range(1, 100):
        print(cc.current_state().bin)
        can_progress = cc.progress()

if __name__ == '__main__':
    main()
