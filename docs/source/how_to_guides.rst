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
        :caption: Install dependencies (and docs dependencies) with `poetry`

            > poetry install --with docs

- **Execution of the developed applications**

    - Execute *stripped* illustrative example (executes VNS on Max-Ones problem with binary representation within `int`, uses classes only from`uo`) 

    .. code-block::
        :caption: Execute illustrative example

            > python example_vns_maxones_int_uo

    - Execute *enhanced* illustrative example (executes VNS on Max-Ones problem with binary representation within `int`, uses classes from both `uo` and `app`) 

    .. code-block::
        :caption: Execute illustrative example

            > python example_vns_maxones_int_app

- **Running of all the unit tests within developed applications**

    - Execute command for running tests from directory `/` 

    .. code-block::
        :caption: Run all unit tests within project

            > python -m unittest

- **Building documentation for the library**

    1. Build documentation sources into `/docs/source` folder from `python` source files 

    .. code-block::
        :caption: Build documentation sources

            > sphinx-apidoc -o /docs/source/ uo
            > sphinx-apidoc -o /docs/source/ app


    2. Change current directory to `/docs` 

    .. code-block::
        :caption: Change directory

            > cd docs

    3. Clean previously builded HTML documentation 

    .. code-block::
        :caption: Clean HTML documentation 

            /docs> ./make clean html

    4. Build HTML documentation from `/docs/source` directory. Created documentation is within `/docs/build/html` directory. 

    .. code-block::
        :caption: Clean HTML documentation 

            /docs> ./make html




