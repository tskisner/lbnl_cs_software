lbnl_cs_software
================

Overview of LBNL Software Resources.  This uses sphinx to generate the catalog of software packages which can be viewed here:

http://tskisner.github.io/lbnl_cs_software/


Generating source files
-------------------------

Before running sphinx, you should use the included script to parse the text files in the "entries" directory into rst files read by sphinx::

	$> ./update_docs.py


Building
----------

You will need to have sphinx and dependencies installed.  Under most Linux installations, the executable is called "sphinx-build".  If you install with macports, then it will be called "sphinx-build-2.7".  In order to build the HTML pages, just do::

	$> make clean; make html

If you are using macports to get sphinx::

	$> make clean; make -f Makefile.macports html


Viewing
-----------

Copy the build/html directory to a webserver, or point your browser to build/html/index.html


