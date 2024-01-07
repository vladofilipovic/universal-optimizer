How-to Guides
=============

- **Installation the library from provided source code**

    1. Installing  and initializing `poetry`

    .. code-block::
        :caption: Installing poetry

            > pip install poetry

    2. Check if `poetry` is successfully installed

    .. code-block::
        :caption: Check poetry version

            > poetry --version

    3. Create virtual environment with `poetry` (if environment is already created, same command activate it, and command `deactivate` is used for deactivation) 

    .. code-block::
        :caption: Create/activate virtual environment

            > poetry shell

    4. Install project's packets and documentation builder packets with `poetry` 

    .. code-block::
        :caption: Install dependencies (and documentation dependencies) with `poetry`

            > poetry install --with docs

- **Running of all the unit tests within developed applications**

    - Execute command for running tests from directory `/` 

    .. code-block::
        :caption: Run all unit tests within project

            > python -m unittest


    - Execute command for obtaining coverage analysis from directory `/` 

    .. code-block::
        :caption: Obtain coverage analysis of tests within project

            > python -m coverage run -m unittest
            > python -m coverage report


- **Building documentation for the library**

    1. Build documentation sources into `/documentation/source` folder from `python` source files 

    .. code-block::
        :caption: Build documentation sources

            > sphinx-apidoc -o documentation/source/ uo
            > sphinx-apidoc -o documentation/source/ opt


    2. Change current directory to `/documentation` 

    .. code-block::
        :caption: Change directory

            > cd documentation

    3. Clean previously builded HTML documentation 

    .. code-block::
        :caption: Clean HTML documentation 

            /documentation> ./make clean html

    4. Build HTML documentation from `/documentation/source` directory. Created documentation is within `/documentation/build/html` directory. 

    .. code-block::
        :caption: Build HTML documentation 

            /documentation> ./make html




