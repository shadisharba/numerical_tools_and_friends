arithmetic module
=================
Introduction
------------

The documentation of the class Arithmetic and its members from 
the `utils/arithmetic.py` file that was automatically generated 
using `sphinx-apidoc` command.

Here are some equations with variables :math:`a,b` which can be added in an `.rst` file as::

   .. math::
         c = a + b \\
         d = a \div b \\
         e = a \times b \\
         f = a - b \\
      
Mathjax now renders the above math expressions as:

.. math::
      c = a + b \\
      d = a \div b \\
      e = a \times b \\
      f = a - b \\
      
Arithmetic Class
----------------

.. automodule:: arithmetic
   :members:
   :special-members: __init__
   :undoc-members:
   :show-inheritance:

Attention
---------

The following methods can be used to call attention to text.

.. warning:: You have been **warned**!
.. seealso:: Some external/internal links.

Version information can be added using::
   
   .. versionadded:: 0.0.1
   .. versionchanged:: 0.0.1

These print the following: 

.. versionadded:: 0.0.1
.. versionchanged:: 0.0.1

Tables
------
Here is the code to add a table:: 

   +------------+------------+-----------+
   | Column 1   | Column 2   | Column 3  |
   +============+============+===========+
   |     A1     |     A2     |    A3     |
   +------------+------------+-----------+
   |     B1     |    B2      |    B3     |
   +------------+------------+-----------+

It produces the following table: 

+------------+------------+-----------+
| Column 1   | Column 2   | Column 3  |
+============+============+===========+
|     A1     |     A2     |    A3     |
+------------+------------+-----------+
|     B1     |    B2      |    B3     |
+------------+------------+-----------+
