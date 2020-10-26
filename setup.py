from setuptools import setup
from setuptools import find_packages

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup( name='toto',
       install_requires=requirements,
       description="Project Description",
       packages=find_packages(),
       scripts=['scripts/toto-run'])
