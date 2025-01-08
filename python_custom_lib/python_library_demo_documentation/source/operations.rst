operations module
=================
Introduction
------------

Normal text can also be added in the `.rst` file to give more context 
to the automatically added documentation from the python files.

Some useful images can be added in the `.rst` file using the `image` command as shown below::

   .. figure:: images/image.png
      :alt: some useful image
      :width: 300px
      :class: with-shadow
      :align: center

      Image caption here.

The above code block produces the following figure. 

.. figure:: images/image.png
   :alt: some useful image
   :width: 300px
   :class: with-shadow
   :align: center

   Image caption here.

Operations
----------

The documentation of the functions in the `utils/operations.py` file that
was automatically generated using `sphinx-apidoc` command.

.. automodule:: operations
   :members:
   :undoc-members:
   :show-inheritance:
