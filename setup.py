from setuptools import setup, find_packages
import os

version = '1.0'

long_description = (
    open('README.txt').read()
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='cirb.leaflet',
      version=version,
      description="Plone Leafleat integration for CIRB",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Framework :: Zope2",
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='',
      author='Benoit Suttor',
      author_email='bsuttor@cirb.irisnet.be',
      url='https://github.com/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['cirb', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*- 
      [z3c.autoinclude.plugin]
      target = plone
      """
      )
