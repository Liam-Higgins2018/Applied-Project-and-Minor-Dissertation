from setuptools import setup

##from docopt import docopt
def readme_file_contents():
    with open('README.rst') as readme_file:
        data = readme_file.read()
    return data

setup(
    name= 'HoneyPot',
    version= '1.0.0',
    description = 'Badic TCP honeypot',
    long_description = readme_file_contents(),
    author = 'Liam Higgins',
    licence = 'MIT',
    package = ['nanopot'],
    # scripts = ['bin/nanopot', 'bin/nanopot.bat'],
    zip_safe = False,
    install_requires = ['docopt']

)