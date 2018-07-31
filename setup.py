import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='AutoFwParser',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='Apache License 2.0',
    description='A simple Library to Parser Firewall Configuration.',
    long_description=README,
    url='https://github.com/adahya/AutoFwParser',
    author='Ahmed Dahya',
    author_email='a.dahya@live.com',
    classifiers=[
        'Environment :: Python Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License 2.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)