from setuptools import setup, find_packages


with open('../README.md') as f:
    readme = f.read()

with open('../LICENSE') as f:
    license = f.read()

setup(
    name='app-sender',
    version='0.1.0',
    description='''Application that fetches json files, convert to xml, encrypt and upload to a remote server 
                   via rest interface.''',
    long_description=readme,
    author='David',
    author_email='',
    url='',
    packages=find_packages(exclude=('tests', 'docs'))
)