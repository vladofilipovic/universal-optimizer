from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

from copy import deepcopy
from datetime import datetime

from typing import Optional

from uo.utils.logger import logger
from uo.algorithm.output_control import OutputControl
from uo.problem.problem import Problem
from uo.problem.problem_void_min_so import ProblemVoidMinSO
from uo.solution.solution import Solution

from uo.algorithm.optimizer import Optimizer
from uo.algorithm.algorithm import Algorithm

class OptimizerVoid(Optimizer):
    def __init__(self, problem:Problem = ProblemVoidMinSO(),
            name:str="optimizer_void", 
            output_control:Optional[OutputControl] = None,
    )->None:
        super().__init__(problem=problem,
                    name=name,
                    output_control=output_control)

    def __copy__(self):
        return super().__copy__()

    def copy(self):
        return self.__copy__()

    def init(self):
        return

    def optimize(self)->Solution:
        return None
        
    def __str__(self)->str:
        return super().__str__()

    def __repr__(self)->str:
        return super().__repr__()

    def __format__(self, spec:str)->str:
        return super().__format__(spec)

