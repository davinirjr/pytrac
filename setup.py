#!/usr/bin/env python

from setuptools import setup, Command

class PyPandoc(Command):
    description = 'Generates the documentation in reStructuredText format.'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def convert(self, infile, outfile):
        import pypandoc
        with open(outfile, 'w+') as f:
            f.write(pypandoc.convert(infile, 'rst'))

    def run(self):
        self.convert('README.md', 'rst/README.rst')
        self.convert('HISTORY.md', 'rst/HISTORY.rst')


setup(name='pytrac',
      version='0.0.1',
      author='Daniel Bonkowski',
      author_email='bonko@jimdo.com',
      url='https://github.com/Jimdo/pytrac',
      license='Apache',
      description='Library for managing TRAC tickets with Python',
      long_description=open('rst/README.rst').read() + '\n\n' +
                       open('rst/HISTORY.rst').read(),
      packages=['pytrac'],
      tests_require=['mock'],
      test_suite='test',
      cmdclass={'doc': PyPandoc},
      )
