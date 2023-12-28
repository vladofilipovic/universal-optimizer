""" 
The :mod:`~uo.target_problem.target_problem` module describes the class :class:`~uo.target_problem.TargetProblem`.
"""

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

from copy import deepcopy


from uo.target_problem.target_problem import TargetProblem 

class TargetProblemVoid(TargetProblem):
    
    def __init__(self, name:str, is_minimization:bool)->None:
        super().__init__(name, is_minimization)

    def __copy__(self):
        pr = deepcopy(self)
        return pr

    def copy(self):
        return self.__copy__()

    def load_from_file(data_representation: str)->None:
        return

    def __str__(self)->str:
        return ''

    def __repr__(self)->str:
        return ''

    def __format__(self, spec:str)->str:
        return ''
    
