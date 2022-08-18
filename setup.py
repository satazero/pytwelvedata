from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except IOError:
    long_description = 'Python module for retrieving financial data from TwelveData API endpoints'

setup(
    name='pytwelvedata',
    version='0.1.0',
    author='Andrew Zero',
    author_email='galoisraid@gmail.com',
    license='MIT',
    description='Python module for retrieving financial data from TwelveData API endpoints',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 3 - Alpha Copy',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial :: Investment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    url='https://github.com/satazero/pytwelvedata',
    install_requires=[
        'aiohttp',
        'requests',
        'pandas'
    ],
    test_requires=[
        'aioresponses',
        'nose',
        'requests_mock'
    ],
    extras_requires={
    },
    keywords=['stocks', 'market', 'finance', 'alpha_vantage', 'quotes',
              'shares'],
    packages=find_packages(
        exclude=['helpers', 'test_alpha_vantage', 'images']),
    package_data={
        'pytwelvedata': [],
    }
)