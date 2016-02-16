from setuptools import setup, find_packages
from os import path

# Read version                                                                                    
execfile('puma/version.py')

here = path.abspath(path.dirname(__file__))


setup(
    name='phant',
    version=__version__,
    author='Pablo Manuel Garcia Corzo <pablo.manuel.garcia@blue-tc.com>',
    description='Python Universal Monitoring Agent',
    author_email='pablo.manuel.garcia@blue-tc.com',
    url='http://github.com/ozroc/puma',
    packages=['puma', 'puma.encoders', 'puma.backends'],
    install_requires=['schedule'],
    extras_require = {
        'dweet':  ['dweepy'],
        'phant':  ['python-phant'],
        'paho':   ['paho']
        }
)
