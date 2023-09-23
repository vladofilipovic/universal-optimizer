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
        if self.__counters.all(True):
            return False
        ind_not_max:int = self.__number_of_counters-1
        for i in range(ind_not_max, -1, -1):
            if self.__counters[i] == False:
                ind_not_max = i
                break
        self.__counters[ind_not_max] += True
        for i in range(ind_not_max+1, self.__number_of_counters):
            self.__counters[i]=False
        return True

# testing the developed class
def main():
    cc:ComplexCounterBitArrayFull = ComplexCounterBitArrayFull(6)
    can_progress:bool = cc.reset()
    for i in range(1, 100):
        print(cc.current_state().bin)
        can_progress = cc.progress()

if __name__ == '__main__':
    main()
