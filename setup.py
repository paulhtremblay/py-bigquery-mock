from setuptools import setup

setup(
    name='py-bigquery-mock',
    version='0.2.4',    
    scripts=['data_mock/scripts/mkmock.py'],
    description='Mock BigQuery',
    url='https://github.com/paulhtremblay/py-bigquery-mock',
    author='Henry Tremblay',
    author_email='paulhtremblay@gmail.com',

    license='GNU GENERAL PUBLIC LICENSE',
    packages=['data_mock/google/cloud/'],
     classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
