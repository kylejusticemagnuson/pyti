from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_discription = f.read()

setup(
    name="py-technical-indicators",

    version='0.1.0',

    description='Library containing various technical indicator functions',
    long_discription=long_discription,

    url='https://github.com/kylejusticemagnuson/py-technical-indicators',

    author='Kyle Justice Magnuson',
    author_email='kyle@collectiveidea.com',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Financial Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
    ],

    keywords='financial technical indicator functions',

    packages=find_packages(exclude=['tests']),

    install_requires=['numpy'],

)
