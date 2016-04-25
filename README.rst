==============
python-utilkit
==============

Some useful functions and usability that should be shared between your apps.

|PyPI version| |PyPI downloads| |PyPI license| |pyversions|

Repo: `<https://github.com/aquatix/python-utilkit/>`_

Installation
------------

From PyPI
~~~~~~~~~

Assuming you already are inside a virtualenv:

.. code-block:: bash

    pip install utilkit

From Git
~~~~~~~~

Create a new virtualenv (if you are not already in one) and install the
necessary packages:

.. code-block:: bash

    git clone https://github.com/aquatix/python-utilkit.git
    cd utilkit
    mkvirtualenv utilkit # or whatever project you are working on
    pip install -r requirements.txt


datetime utils
--------------


file utils
----------


print utils
-----------

Pretty printing of data, for example the formatting of two-dimensional lists into
a table which finds out the correct width of its columns by itself (to_smart_columns).


string utils
------------


What's new?
-----------

See the `Changelog`_.


.. _python-utilkit: https://pypi.python.org/pypi/python-utilkit
.. |PyPI version| image:: https://img.shields.io/pypi/v/utilkit.svg
   :target: https://pypi.python.org/pypi/utilkit/
.. |PyPI downloads| image:: https://img.shields.io/pypi/dm/utilkit.svg
   :target: https://pypi.python.org/pypi/utilkit/
.. |PyPI license| image:: https://img.shields.io/github/license/aquatix/python-utilkit.svg
   :target: https://pypi.python.org/pypi/utilkit/
.. _Changelog: https://github.com/aquatix/python-utilkit/blob/master/CHANGELOG.md
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/python-utilkit.svg
.. |version| image:: https://img.shields.io/pypi/v/python-utilkit.svg
   :target: `python-utilkit`_
