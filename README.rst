========
py-llll
========

LINQ-like list processing library in Python and supports lazy evaluation.

forked by `kana/py-llll <https://github.com/kana/py-llll>`_


What is LINQ
==============

LINQ is .NET's library.


notice
---------

You may want to know about LINQ or other list processing library.

Function name is same as original in most cases, But some of that has a littele defference.

　　

You can read kana's article from http://labs.timedia.co.jp/2011/07/linq-like-list-library-in-python.html ,
if you can read japanese.


Support
=========

You can run pynk on 2.6 and 2.7.


Installation
=============

You clould clone this repository and use setup.py:

    ``python setup.py install``


If you want to install by pip:

    ``pip install https://github.com/hachibeeDI/py-llll/archive/master.zip``


Usage
-------

.. code:: python

    from operator import add
    from functools import partial

    from pynk.llll import select, to_tuple

    add_two = partial(add, 2)
    range(10) | select(add_two) | to_tuple()
    # => (2,  3,  4,  5,  6,  7,  8,  9,  10,  11)



Documentation
==============



Testing
========

There is only doctest as yet.


