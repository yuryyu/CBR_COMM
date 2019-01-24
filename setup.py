from setuptools import setup, find_packages

setup(
    name='intelici-cyber',
    version='0.1',
    description='Repository containing all the Cyber stuff',
    # This should be your name or the name of the organization which owns the
    # project.
    author='Intelici',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['networkx', 'igraph'],
    extras_require={  # Optional
        'test': ['pytest'],
    },
)

