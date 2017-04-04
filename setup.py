from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))


setup(
    name="pyti",

    version='0.1.1',

    description='Technical Indicator Library',
    long_description="This library contains various financial technical "
                     "indicators that can be used to analyze financial data.",

    url='https://github.com/kylejusticemagnuson/pyti',

    author='Kyle Justice Magnuson',
    author_email='kyle@collectiveidea.com',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
    ],

    keywords='financial technical indicator functions',

    packages=find_packages(exclude=['tests']),

    install_requires=['numpy'],

)
