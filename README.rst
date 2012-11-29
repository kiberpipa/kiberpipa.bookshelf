SETUP DEVELOPMENT ENVIRONMENT
=============================

::

    $ sudo apt-get install python26 python26-dev python26-setuptools
    $ python2.6 bootstrap.py -d
    $ bin/buildout
    $ bin/pserve --reload development.ini


DEPLOY
======

::

    $ git clone https://github.com/kiberpipa/kiberpipa.bookshelf production && cd production
    $ vim buildout.d/secrets.cfg
    $ echo -e "[buildout]\nextends = buildout.d/production.cfg" > buildout.cfg
    $ python bootstrap.py -d
    $ bin/buildout
    # deploy solr to solr/ folder
    $ bin/supervisord
