from setuptools import setup, find_packages


with open('../README.md') as f:
    readme = f.read()

with open('../LICENSE') as f:
    license = f.read()

setup(
    name='app-receiver',
    version='0.1.0',
    description='''Flask application that provides rest interface to upload an encrypted xml file, then decrypts it .
                   and stores in a given location.''',
    long_description=readme,
    author='David',
    author_email='',
    url='',
    packages=find_packages(exclude=('tests', 'docs'))
)