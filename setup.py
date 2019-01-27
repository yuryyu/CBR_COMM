from setuptools import setup, find_packages

setup(
    name='intelici-cyber',
    version='0.1',
    description='Repository containing all the Cyber stuff',
    author='Intelici',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=["numpy", 'networkx', 'python-igraph'],
    extras_require={
        'test': ['pytest'],
    },
)

