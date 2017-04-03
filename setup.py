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

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Financial Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
    ],

    keywords='financial technical indicator functions',

    packages=find_packages(exclude=['docs', 'tests']),

    install_requires=['numpy'],

)
