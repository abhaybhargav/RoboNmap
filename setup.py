from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


install_dependencies = (
    'python-libnmap==0.7.0',
    'robotframework==3.0.4'
)

setup(
    name='RoboNmap',
    version='1.1',
    packages=[''],
    package_dir={'': 'robonmap'},
    url='',
    license='MIT License',
    author='Abhay Bhargav',
    install_requires = [
    'python-libnmap==0.7.0',
    'robotframework==3.0.4'
    ],
    description='RoboNmap - Robot Framework Library for the Nmap Port and Vulnerability Scanner',
    long_description = long_description,
    long_description_content_type='text/markdown'
)
