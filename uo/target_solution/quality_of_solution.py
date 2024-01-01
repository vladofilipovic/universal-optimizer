""" 
The :mod:`~uo.target_solution.quality_of_solution` module describes the class :class:`~uo.target_solution.QualityOfSolution`.
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
    
    @classmethod
    def is_first_fitness_better(cls, qos1:'QualityOfSolution', qos2:'QualityOfSolution', is_minimization: bool)->Optional[bool]:
        """
        Checks if first solution is better than the second one

        :param QualityOfSolution qos1: first quality of solution
        :param QualityOfSolution qos2: second quality of solution
        :return: `True` if first is better, `False` if first is worse, `None` if fitnesses of both 
                solutions are equal
        :rtype: bool
        """
        fit1:Optional[float] = qos1.fitness_value;
        fit2:Optional[float] = qos2.fitness_value;
        # with fitness is better than without fitness
        if fit1 is None:
            if fit2 is not None:
                return False
            else:
                return None
        elif fit2 is None:
            return True
        # if better, return true
        if (is_minimization and fit1 < fit2) or (not is_minimization and fit1 > fit2):
            return True
        # if same fitness, return None
        if fit1 == fit2:
            return None
        # otherwise, return false
        return False

