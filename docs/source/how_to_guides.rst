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

- **Unit testing of the developed applications**

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




