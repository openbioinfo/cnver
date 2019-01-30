.. ctCNV documentation master file, created by
   sphinx-quickstart on Thu Oct 25 11:10:32 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ctCNV's documentation!
=================================

========
ctCNV
========


Introduction
============

ctCNV is used to run cfDNA bam data to make CNV baseline or get copy number variantion. The input file should be ``sorted bam and indexed``. Toos ``sambamba`` is needed.


Authors
=======

.. _authors:

    - lsx <lsx@vienomics.com>


Status
======

.. note::

    **not reviewed**



Installation::
==============
use git to clone code::

    git clone git@192.168.1.251:/home/git/ctCNV.git

..  attention::

    if you want to run ``ctCNV`` on local server without docker , try to install ``sambamba``.


Usage
=====


just type commond::
    
    /path/to/ctCNV.py -h


must_args
---------

- --i
    input bam

- --b
    bed file

- --l
    basline file

- --o 
    output directory


RUN
===

something ...



Tests
======

check test report `here <http://192.168.1.251:4700/dev-tests/ctCNV/>`_

Report
======

check sample repot `here <http://192.168.1.251:4700/dev-report/cnv_report/>`_



.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
