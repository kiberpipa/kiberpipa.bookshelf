SETUP DEVELOPMENT ENVIRONMENT
=============================

::

    $ python bootstrap.py -d
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
    $ bin/pserve --reload development.ini
    # deploy solr to solr/ folder
    $ bin/supervisord
