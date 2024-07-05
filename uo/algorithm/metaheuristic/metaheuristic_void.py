from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)

from random import random
from random import randrange
from copy import deepcopy
from datetime import datetime
from io import TextIOWrapper 

from uo.utils.logger import logger

from typing import Optional

from uo.problem.problem import Problem
from uo.solution.solution import Solution

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl

from uo.algorithm.algorithm import Algorithm
from uo.algorithm.metaheuristic.metaheuristic import Metaheuristic
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl
class MetaheuristicVoid(Metaheuristic):
    def __init__(self, 
            finish_control:FinishControl,
            problem:Problem,
            solution_template:Optional[Solution]=None,
            name:str='metaheuristic-void', 
            output_control:Optional[OutputControl]=None,
            random_seed:Optional[int]=None, 
            additional_statistics_control:Optional[AdditionalStatisticsControl]=None
    )->None:
        super().__init__(
                name=name, 
                finish_control=finish_control,
                random_seed=random_seed,
                additional_statistics_control=additional_statistics_control,
                output_control=output_control, 
                problem=problem,
                solution_template=solution_template
        )

    def __copy__(self):
        return super().__copy__()

    def copy(self):
        return self.__copy__()

    def init(self):
        return
    
    def main_loop_iteration(self)->None:
        return


    def __str__(self)->str:
        return super().__str__()

    def __repr__(self)->str:
        return super().__repr__()

    def __format__(self, spec:str)->str:
        return super().__format__(spec)

