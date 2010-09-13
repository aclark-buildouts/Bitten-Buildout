Introduction
============

This buildout demonstrates the use of Bitten for continuous integration and provides a south database migration example.

Prerequisites
-------------

You will need a Python with the Subversion bindings installed. If you do not
have one handy, check out:

    - http://github.com/aclark4life/Subversion-Python-Buildout

You will also need Subversion's ``svn`` and ``svnadmin`` in your PATH.

Install
-------

To install the demo, do this::    

    $ git clone git://github.com/aclark4life/Subversion-Python-Buildout.git
    $ /path/to/python/with/svn/bindings/bin/python bootstrap.py
    $ bin/buildout
    $ bin/supervisord -e debug -n

Then:

    - Create a test configuration in Admin -> Configurations in Trac
    - Cut and paste ``ci-recipe.xml`` into the recipe field.
    - Select ``trunk`` for the path.
    - Create a target platform for localhost (e.g. os =~ Darwin)

Test
----

Everytime you run ``bin/buildout``, a test commit will be made. Watch
http://localhost:8080/project/build for the results.


