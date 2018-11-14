README
======

Python Teamcity is a python wrapper for the `Teamcity <https://www.jetbrains.com/teamcity//>`_
REST API which aims to provide a more conventionally pythonic way of controlling
a Teamcity server.  It provides a higher-level API containing a number of
convenience functions.

We like to use python-teamcity to automate our Teamcity servers. Here are some of
the things you can use it for:

* Create new jobs
* Copy existing jobs
* Delete jobs
* Update jobs
* Get a job's build information
* Get Teamcity master version information
* Get Teamcity plugin information
* Start a build on a job
* Create nodes
* Enable/Disable nodes
* Get information on nodes
* Create/delete/reconfig views
* Put server in shutdown mode (quiet down)
* List running builds
* Delete builds
* Wipeout job workspace
* Create/delete/update folders [#f1]_
* Set the next build number [#f2]_
* Install plugins
* and many more..

To install::

    $ sudo python setup.py install

Online documentation:

* http://python-teamcity.readthedocs.org/en/latest/

Developers
----------
Bug report:

* https://github.com/octopi-assembly/python-teamcity/issues

Cloning:

* git clone https://github.com/octopi-assembly/python-teamcity.git

More details on how you can contribute is available at:

* https://github.com/octopi-assembly/python-teamcity/blob/master/CODE_OF_CONDUCT.md

Writing a patch
---------------

Be sure that you lint code before created an code review.
The easiest way to do this is to install `sonarlint` in your editor.

Installing without setup.py
---------------------------

Then install the required python packages using pip_::

    $ sudo pip install python-teamcity
    
Inspiration
---------------

The development of this repository started with inspiration from existing repositories which are as follows:
* `PyTeamcity <https://github.com/SurveyMonkey/pyteamcity>`
* `Teamcity Python Rest Client <https://github.com/yotamoron/teamcity-python-rest-client>`

