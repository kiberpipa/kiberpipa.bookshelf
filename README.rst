SETUP DEVELOPMENT ENVIRONMENT
=============================

::

    $ git clone https://github.com/kiberpipa/kiberpipa.bookshelf && cd kiberpipa.bookshelf
    $ sudo apt-get install python26 python26-dev python26-setuptools
    $ echo -e "[buildout]\nextends = buildout.d/development.cfg" > buildout.cfg
    $ cp buildout.d/secrets.cfg.sample buildout.d/secrets.cfg
    $ vim buildout.d/secrets.cfg
    $ python2.6 bootstrap.py -d
    $ bin/buildout
    # deploy solr to solr/ folder
    $ java -jar solr/start.jar
    $ bin/pserve --reload development.ini


DEPLOY
======

::

    $ sudo apt-get install python26 python26-dev python26-setuptools
    $ git clone https://github.com/kiberpipa/kiberpipa.bookshelf production && cd production
    $ echo -e "[buildout]\nextends = buildout.d/production.cfg" > buildout.cfg
    $ cp buildout.d/secrets.cfg.sample buildout.d/secrets.cfg
    $ vim buildout.d/secrets.cfg
    $ python bootstrap.py -d
    $ bin/buildout
    # deploy solr to solr/ folder
    $ bin/supervisord
