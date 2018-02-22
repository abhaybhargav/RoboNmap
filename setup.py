from setuptools import setup

install_dependencies = (
    'python-libnmap==0.7.0',
    'robotframework==3.0.2'
)

setup(
    name='RoboNmap',
    version='0.1',
    packages=[''],
    package_dir={'': 'robonmap'},
    url='',
    license='MIT License',
    author='Abhay Bhargav',
    author_email='Twitter: @abhaybhargav',
    install_requires = [
    'python-libnmap==0.7.0',
    'robotframework==3.0.2'
    ],
    description=''
)
