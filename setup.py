from setuptools import setup

with open('README') as f:
    long_description = f.read()

with open('VERSION') as f:
    version = f.readline().strip()

setup(
    name='ase-game',
    description=long_description,
    license='MIT',
    version=version,
    packages=[
        'ase_game',
    ],
    scripts=[
        'scripts/eins.py',
    ],
    zip_safe=False,
    install_requires=['pytest'],
)
