""" 
The :mod:`~uo.solution.quality_of_solution` module describes the class :class:`~uo.solution.QualityOfSolution`.
"""

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

from typing import Optional

class QualityOfSolution:

    def __init__(self, 
                objective_value:Optional[float], 
                objective_values:Optional[list[float]|tuple[float]],
                fitness_value:Optional[float], 
                fitness_values:Optional[list[float]|tuple[float]], 
                is_feasible:bool)->None:
        """
        Initializes the instance variables of the QualityOfSolution class with the provided values.

        Args:
            fitness_value (Optional[float]): The fitness value of the target solution.
            fitness_values (Optional[list[float]|tuple[float]]): The fitness values of the target solution.
            objective_value (Optional[float]): The objective value of the target solution.
            objective_values (Optional[list[float]|tuple[float]]): The objective values of the target solution.
            is_feasible (bool): The feasibility of the target solution.

        Returns:
            None. The method is a constructor and does not return anything.
        """
        if not isinstance(is_feasible, bool):
                raise TypeError('Parameter \'is_feasible\' must be \'bool\'.')        
        self.__objective_value:Optional[float] = objective_value
        self.__objective_values:Optional[list[float]|tuple[float]] = objective_values
        self.__fitness_value:Optional[float] = fitness_value
        self.__fitness_values:Optional[list[float]|tuple[float]] = fitness_values
        self.__is_feasible:bool = is_feasible

    @property
    def fitness_value(self)->Optional[float]:
        """
        Property getter for fitness value of the target solution

        :return: fitness value of the target solution instance 
        :rtype: float
        """
        return self.__fitness_value

    @property
    def fitness_values(self)->Optional[list[float]|tuple[float]]:
        """
        Property getter for fitness values of the target solution

        :return: fitness values of the target solution instance 
        :rtype: list[float]|tuple[float] 
        """
        return self.__fitness_values
    
    @property
    def objective_value(self)->Optional[float]:
        """
        Property getter for objective value of the target solution

        :return: objective value of the target solution instance 
        :rtype: float
        """
        return self.__objective_value

    @property
    def objective_values(self)->Optional[list[float]|tuple[float]]:
        """
        Property getter for objective values of the target solution

        :return: objective values of the target solution instance 
        :rtype: list[float]|tuple[float] 
        """
        return self.__objective_values

    @property
    def is_feasible(self)->bool:
        """
        Property getter for feasibility of the target solution

        :return: feasibility of the target solution instance 
        :rtype: bool
        """
        return self.__is_feasible


