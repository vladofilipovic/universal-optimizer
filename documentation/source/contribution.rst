How to Contribute
=================


This system is developed in `Python <https://www.python.org>`_ programming language, using `poetry <https://python-poetry.org>`_ as project and package manager, `unittest <https://docs.python.org/3/library/unitest.html>`_  library for unit testing and `Sphinx <https://www.sphinx-doc.org/en/master>`_ system for documentation generation. Same tool set should be use for contribution to the project.

Contribution is encouraged in following four domains:

1. Designing novel optimization methods. Requirements:

    1. Algorithms should be derived from the specified class.

        - Class that implements metaheuristic optimization should be derived either from the :class:`uo.algorithm.metaheuristic.single_solution_metaheuristic.SingleSolutionMetaheuristic` class, or from the :class:`uo.algorithm.metaheuristic.population_based_metaheuristic.PopulationBasedMetaheuristic`. It should be placed into separate directory within `uo/algorithm/metaheuristic/` directory.

        - Class that implements exact optimization should be derived from the :class:`uo.algorithm.Algorithm` class. That class should be placed into separate directory within `/uo/algorithm/` directory.

    2. Type hints and documentation.

        - All programming objects (classes, functions, variables, parameters, optional parameters etc.) should be `type-hinted <https://www.infoworld.com/article/3630372/get-started-with-python-type-hints.html>`_
        
        - All programming objects (classes, functions, etc.) should be properly documented using the system `Sphinx`, reStructuredText and doc comments within the code.

        - Each of the implemented algorithm should have separate documentation web page, where that algorithm is described and documented. There should be the link from doc comments within implemented functionality toward the web page that explains algorithm and vice versa.  

    3. Unit testing coverage.
    
        - Implemented programming code should be fully covered with unit tests.  
    
        - Here, `unittest` framework  used. 
        
        - Test should be placed into separate directory under directory `/tests/uo/`. 

        - All developed code should be covered with unit test, and test coverage rate should be not less than 80%. 


2. Building application for solving optimization problems. Requirements:

    1. All parameters that should be set in order to tune application should be accessible to user through command-line parameters. Command-line parameters should have sufficient and adequate help system.

    2. Implemented applications should have examples of use for every approach contained within application. 
    
        - Those examples should be placed in root folder, with file name `example-<algorithm>-<problem>.py`.

3. Designing and executing comparison experiments, using previously builded applications. Requirements: 

    1. Experiments should use only previously developed applications, not Python programming constructs. It should be invoked by batch/command file.

4. Visualizing experimentally obtained data (either data about comparison, either data about algorithm execution). Requirements:

    1. Experiments should use only previously developed applications, not Python programming constructs.

Contributors
============

Contribution domains
--------------------

1. Contribution in the designing novel optimization methods:

    1. Library structure and organization - [VladimirFilipovic]_

    2. Total Enumeration exact algorithm (using binary string structure) - [VladimirFilipovic]_
    
    3. Variable Neighborhood Search :ref:`Algorithm_Variable_Neighborhood_Search` metaheuristics - [VladimirFilipovic]_ 

2. Contribution in solving optimization problems:

    1. Ones Count Optimization Problem :ref:`Problem_Ones_Count_Max`:

        - Integer Linear programming method (using `linopy` library) - [VladimirFilipovic]_  

        - Total Enumeration method, with solution that has binary representation (using `BitArray` object) - [VladimirFilipovic]_  

        - Variable Neighborhood Search method, with solution that has binary representation (using `BitArray` object) - [VladimirFilipovic]_  

        - Variable Neighborhood Search method, with solution that has binary representation (using `int`) - [VladimirFilipovic]_  

    2. Max Function One Variable Problem:

        - Total Enumeration method, with solution that has binary representation (using `int` object) - [VladimirFilipovic]_  

Contributor List
----------------

.. [VladimirFilipovic] Vladimir Filipović, github: https://github.com/vladofilipovic, www: https://vladofilipovic.github.io e-mail: vladofilipovic@hotmail.com

