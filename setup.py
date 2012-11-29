# -*- coding: utf-8 -*-

import os

from setuptools import setup
from setuptools import find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name='kiberpipa.bookshelf',
    version='0.1.dev0',
    description='Simple interface talking to solr storage full of scanned books',
    long_description=read('README.rst') +
                     read('HISTORY.rst'),
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    keywords='web wsgi pylons pyramid',
    author='Domen Kožar',
    author_email='domen@dev.si',
    url='',
    license='BSD',
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'pyramid>=1.4a4',
        'pyramid_tm',
        'raven',
        'pyramid_jinja2',
        'pysolr',
        'dogpile.cache',
        'unittest2',
        'mock',
        'ordereddict',
        'simplejson',
        'webhelpers',
        'iptools'
#        'pyramid_webassets',
#        'pyramid_marrowmailer',
    ],
    extras_require={
        'test': [
            'nose',
            'nose-selecttests',
            'coverage',
            'flake8',
        ],
        'development': [
            'zest.releaser',
            'Sphinx',
            'pyramid_debugtoolbar',
            'waitress',
        ],
        'production': [
            'gunicorn',
            'supervisor',
        ],
    },
    entry_points="""
    [paste.app_factory]
    main = kiberpipa.bookshelf:main

    [console_scripts]
    """,
    paster_plugins=['pyramid'],
    include_package_data=True,
    zip_safe=False,
)
