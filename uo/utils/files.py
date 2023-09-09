""" 
The :mod:`~uo.utils.files` module contains utility functions that deals with files.
"""

from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)

import os

def ensure_dir(path_to_dir:str)->None:
        """
        Ensure existence of the specific directory in the file system
        
        :param path_to_dir:str -- path of the directory whose existence should be ensured
        """    
        if not os.path.exists(path_to_dir):
            os.mkdir(path_to_dir)