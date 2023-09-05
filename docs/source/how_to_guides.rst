How-to Guides
=============

- Installation the library from provided source code

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


- Building documentation of the library

    1. Change current directory to `/docs` 

    .. code-block::
        :caption: Change directory

            > cd docs

    2. Clean previous HTML documentation 

    .. code-block::
        :caption: Clean HTML documentation 

            /docs> ./make clean html

    3. Build HTML documentation from `/docs/source` directory. Created documentation is within `/docs/build/html` directory. 

    .. code-block::
        :caption: Clean HTML documentation 

            /docs> ./make html




