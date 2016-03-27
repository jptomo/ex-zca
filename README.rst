=========================================
An example of Zope Component Architecture
=========================================

This project aim to implement DIP (the Dependency Inversion Principle).

.. code-block:: console

   $ cd /path/to/ex-zca
   $ python3.5 -m venv --clear venv
   $ ./venv/bin/python3.5 -m pip install -U setuptools pip wheel
   $ ./venv/bin/python3.5 -m pip install -U zope.interface zope.component
   $ ./venv/bin/python3.5 demo.py
