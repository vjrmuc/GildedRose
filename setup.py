from setuptools import setup, find_packages

setup(
    name='HomeWorkTask',
    version='0.1',
    author='Aleksandar Angelov',
    packages=find_packages(include=['main.*']),
    long_description=open('README.md').read(),
    test_suite='test'
)