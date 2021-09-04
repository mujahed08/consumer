# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


""" with open('README.MD') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()
"""

setup(
    name='consumer',
    version='0.1.0',
    description='consumer - a websocket based consumer',
    long_description='readme',
    author='Mohammed Mujahed Khan',
    author_email='mohammed.khanejd@gmail.com',
    url='https://github.com/mujahed08/consumer',
    license='license',
    packages=find_packages(exclude=('tests'))
)