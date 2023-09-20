How to Contribute
=================

1. Algorithms should be derived from the specified class.

    - Class that implements metaheuristic optimization should be derived from the :class:`uo.algorithm.metaheuristic.Metaheuristic` class, and it should be placed into separate directory within `uo/algorithm/metaheuristic/` directory.

    - Class that implements exact optimization should be derived from the :class:`uo.algorithm.Algorithm` class, and it should be placed into separate directory within `/uo/algorithm/` directory.

2. All programming objects (classes, functions, etc.) should be properly documented using the system `Sphinx`, reStructuredText and doc comments within the code.

3. Implemented algorithm should have separate documentation web page, where that algorithm is described and documented. There should be the link from doc comments within implemented functionality toward the web page that explains algorithm.  

4. Implemented programming code should be covered with unit tests. Test should be placed into separate directory under directory `/tests/`.  In order to do so, `unittest` is used. 

5. Implemented algorithm should have examples of use for at least one problem. Those examples should be placed in root folder, with file name `example-<algorithm>-<problem>.py`.


Contributors
============

- Vladimir Filipović vladofilipovic@hotmail.com 
    - initial library structure 
    - initial implementation of Variable Neighborhood Search metaheuristic  
