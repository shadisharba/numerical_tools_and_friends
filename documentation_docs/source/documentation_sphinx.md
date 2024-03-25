# Instructions to build documentation from this repository
0. check [Carol Willing - Practical Sphinx - PyCon 2018] (https://www.youtube.com/watch?v=0ROZRNZkPS8)
1. modified from [sphinx-doc-tutorial](https://git.opendfki.de/dinesh_krishna.natarajan/sphinx-doc-tutorial)
2. Install the following packages using `pip`.
   ```
   pip install sphinx
   pip install sphinx_rtd_theme
   pip install recommonmark
   pip install nbsphinx
   ```
   or use the `requirements.txt` file to install all the required packages.
   ```
   pip install -r requirements.txt
   ```
3. `pandoc` is needed to generate documentation from Jupyter Notebooks using Sphinx. Installation instructions can be found [here](https://pandoc.org/installing.html).  
4. Use `documentation_build.bat` to generate HTML documentation.
5. The generated documentation can be found in the `documentation_docs/build/html/` directory. 
6. An online demo of the generated [HTML docs](https://www.dfki.uni-kl.de/~natarajan/sphinx-doc-tutorial/index.html). 

# Instructions to generate Python documentation using Sphinx
To create your own documentation from scratch, follow the instructions below.
## Step 1: Create documented code
 * Create scripts and modules in Python.
 * For automatic docstring generation in VSCode, use [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) plugin with appropriate convention. 
 * Example docstrings following the sphinx convention is shown below:
    ```python
    def add( a, b ):
        """
        This function computes the sum of the two arguments.

        :param num1: first argument
        :type num1: float
        :param num2: second argument
        :type num2: float
        :return: sum of the two arguments 
        :rtype: int or float

        .. note:: This function can accept :class:`int` parameters too.

        Example::
            result = add(a,b)
        """
        assert type(a) == type(b)
        return a + b
    ```
 * **Note**: For other docstring conventions such as the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html), additional extensions such as [`sphinx.ext.napoleon`](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html) are necessary.
 * Different docstring conventions can be used in the same project and [Sphinx](https://www.sphinx-doc.org/en/master/) (and its extensions) will parse them to generate documentation with a uniform convention. 

## Step 2: Setup sphinx project
* Install `sphinx` package using pip, if not already installed.
* From your code's parent directory, create a `docs/` sub-directory to build the documentation files.  
* In the `docs/` directory, initiate the sphinx project using `sphinx-quickstart` with the default options for the prompts as shown below.  
* Separating source and build directories keeps the `docs/` directory structured.   

    ```
    $ sphinx-quickstart
    Welcome to the Sphinx 4.0.3 quickstart utility.

    Selected root path: .

    > Separate source and build directories (y/n) [n]: y

    Creating file docs/source/conf.py.
    Creating file docs/source/index.rst.
    Creating file docs/Makefile.
    Creating file docs/make.bat.

    Finished: An initial directory structure has been created.

    You should now populate your master file docs/source/index.rst and create other documentation

    ```
## Step 3: Configure sphinx documentation builder
 * In the `docs/source/conf.py` file, uncomment the path setup comments shown below and edit the absolute path to the modules directory of the project.

    ```python
    # -- Path setup --------------------------------------------------------------

    # If extensions (or modules to document with autodoc) are in another directory,
    # add these directories to sys.path here. If the directory is relative to the
    # documentation root, use os.path.abspath to make it absolute, like shown here.
    import os
    import sys
    sys.path.insert(0, os.path.abspath('../../documentation_utils'))
    ```
 * In the `docs/source/conf.py` file, add 'sphinx.ext.autodoc' and other necessary extensions to the extensions list.

    ```python
    extensions = [ 'sphinx.ext.autodoc',  # to autogenerate .rst files
   'sphinx.ext.napoleon', # to parse google stye python docstrings
   'sphinx.ext.mathjax', # to include math expressions in the .rst files
   'recommonmark', # to include markdown files in sphinx documentation
   ]
    ```
 * In the same file, change the html theme if necessary. Note: The default installed theme is 'alabaster'. Any other theme might have to be installed via `pip install theme_name`. Available sphinx themes can be found [here](https://sphinx-themes.org/#themes).
    ```python
    html_theme = 'sphinx_rtd_theme'
    ```
## Step 4: Configure the `.rst` files
 * The 'reStructured Text' files indicate the contents of the documentation. [Here](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) is a primer for the *reStructuredText* markup language. 
 * The `index.rst` acts as the main file (equivalent to a Latex main file). The contents of the documentation can be added directly to the `index.rst` file or individual `.rst` files can be created and then referenced in the `index.rst` file. Each `.rst` file gets its own webpage.
 * Documentation for the modules present in the `documentation_utils/arithmetic.py` and `documentation_utils/operations.py` can be automatically generated using the [`sphinx-apidoc`](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html) command. From the `docs/` directory, the following command can be used to automatically generate the `.rst` files for the modules in `documentation_utils/` directory. To recursively generate the `.rst` files for the submodules inside the `documentation_utils/` folder, simply create an `__init__.py` file inside the submodule directories.
  
 `sphinx-apidoc -M -o docs/source/ utils/`
   *  The `-o` argument points to the output directory `source/`. 
   *  The `-M` option lists the modules before the submodules. 
   ```
   $ sphinx-apidoc -M -o docs/source/ utils/
   Creating file docs/source/arithmetic.rst.
   Creating file docs/source/operations.rst.
   Creating file docs/source/submodule.rst.
   Creating file docs/source/modules.rst.
   ```
 * The `modules.rst` file includes a Table of Contents which lists all the python scripts in the `documentation_utils/` directory. Each python script leads to an individual `.rst` file for that script. 
   ```
   utils
   =====

   .. toctree::
      :maxdepth: 4

      arithmetic
      operations
      submodule

   ```
 * The generated `arithmetic.rst` file contains: 
    ```
    .. automodule:: arithmetic
       :members:
       :undoc-members:
       :show-inheritance:
    ```
    For customization of the various `autodoc` commands, refer to its [documentation](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html). The `__init__` function is excluded by default, but can be added using the automodule option: 
    ```
      :special-members: __init__
   ```
 * In the `.rst` files, additional descriptive text can be directly added without any commands to give more context to the documentation. Images can also be added using the `image` command. Additional options for the command can be found [here](https://docutils.sourceforge.io/0.4/docs/ref/rst/directives.html#image).
    ```
    .. image:: images/image.png
       :alt: some useful image
       :width: 300px
    ```
 * The `modules.rst` is then included in the parent `index.rst` using the `include` command.
    ```
    .. include modules.rst
    ```
 * An alternative to using the `include` command is to add the names
 of the `.rst` files (without extension) to the toctree in `index.rst`. This method also has the benefit that each `.rst` file has an entry (with the title mentioned in its `.rst` file) in the Table of Contents with a hyperlink to the module's individual webpage.
    ```
    .. toctree::
        modules
       :maxdepth: 2
       :caption: Contents
    ```
 * Including math expressions in the `.rst` files is handled by the extension `sphinx.ext.mathjax`. It has to be added to the extensions list in `conf.py`.
    * Syntax for inline math:
        ```
        :math:`x^2 + y^2 = z^2`
        ```
    * Symntax for math equations:
        ```
        .. math::
                x^2 + y^2 = z^2 \\
                x^2 + y^2 = z^2
        ```
* In order to include markdown files into the documentation, an extension named [`recommonmark`](https://recommonmark.readthedocs.io/en/latest/) is required. It has to be added to the extensions list in `conf.py`.
    ```
    pip install recommonmark
    ```
    Now, any markdown files from the `source/` directory can be added to the documentation by including the file in the toctree of `index.rst`.
    ```
    .. toctree::
       Instructions <../README.md>
       modules
       :maxdepth: 2
       :caption: Contents
    ```
 * Jupyter Notebooks can be added using a Sphinx extension called [`nbsphinx`](https://nbsphinx.readthedocs.io/en/0.8.6/). An `.rst` file for the notebook can be created to import the contents and also add any descriptive text. 

   Notebooks from the project directory / module directory could not be added using relative path. The easiest solution was to place the notebooks were placed inside the `docs/source/` directory. 
  
   In the `.rst` file for the notebook, add the following to create a table of contents linking to the contents of the Jupyter notebook.

   ```
   .. toctree::
      :caption: Contents
      :maxdepth: 1 

      notebooks/demo
   ```

## Step 5: Build the documentation in HTML and/or Latex
 * From the `docs/` directory, the documentation can be built using the `make builder` command where the builder is either `html` or `latex` or `latexpdf`.
 * For HTML, the options are automatically generated in `docs/source/conf.py` by the  `sphinx-quickstart` command.
    ```
    make html
    ```
 * LaTeX documentation can be automatically generated without any additions to the `conf.py` file. If customization is necessary, the Latex options can be added to the `conf.py` file. Example for LaTeX options for customizations can be found [here](https://www.sphinx-doc.org/en/master/latex.html). 
    ```
    make latexpdf
    ```
 * The generated HTML or Latex files can be found in `docs/build/html` or `docs/build/latex` respectively.
 * The HTML documentation can be viewed locally via the `docs/build/html/index.html` file. The individual webpage can also be found as `.html` files.
 * The Latex documentation can be viewed via the `docs/build/latex/[project_name].pdf` file.